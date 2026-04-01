#!/usr/bin/env python3
"""
play.py — The runner for interpretations scores.

Convention: every score is a Python file that exposes a `score` variable.
Like Flask exports `app`, like WSGI exports `application`.

    score = Score("4/4", bpm=140)
    # ... build it ...
    # that's it. no play_score() call.

Usage:
    uv run play.py tracks/acid_reign.py
    uv run play.py tracks/acid_reign.py --from 17
    uv run play.py tracks/acid_reign.py --from 17 --to 32
    uv run play.py tracks/the_temple.py --from-time 3:30 --to-time 5:00
    uv run play.py tracks/acid_reign.py -o out.wav
    uv run play.py tracks/acid_reign.py --midi out.mid
    uv run play.py tracks/acid_reign.py --info
    uv run play.py tracks/acid_reign.py --parts
    uv run play.py tracks/acid_reign.py --solo sitar,tabla
    uv run play.py tracks/acid_reign.py --mute kick
    uv run play.py tracks/acid_reign.py --bpm 100
    uv run play.py tracks/acid_reign.py --volume 0.8
    uv run play.py tracks/the_temple.py --pitch 440
    uv run play.py tracks/acid_reign.py --loop 4
    uv run play.py --list
"""

import argparse
import importlib.util
import sys
from pathlib import Path

from pytheory import play_score


TRACKS_DIR = Path(__file__).parent / "tracks"


# ═══════════════════════════════════════════════════════════════════
#  Score loading
# ═══════════════════════════════════════════════════════════════════

def load_score(path):
    """Import a Python score file and return (score, module).

    Convention: the module must expose a `score` variable (a pytheory Score).
    Optional: `title`, `description` attributes.
    """
    path = Path(path).resolve()
    spec = importlib.util.spec_from_file_location("_score", path)
    mod = importlib.util.module_from_spec(spec)

    # Suppress the track's own play_score calls and print noise during import
    import pytheory
    import io
    import os
    _real_play = pytheory.play_score
    _real_stdout = sys.stdout
    pytheory.play_score = lambda s: None
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        pytheory.play_score = _real_play
        sys.stdout = _real_stdout

    if not hasattr(mod, "score"):
        print(f"Error: {path.name} does not export a `score` variable.")
        sys.exit(1)

    return mod.score, mod


def get_title(mod, path):
    """Get title from module or derive from filename."""
    if hasattr(mod, "title"):
        return mod.title
    # Use the module docstring's first line if available
    if mod.__doc__:
        first_line = mod.__doc__.strip().split("\n")[0].strip()
        if first_line:
            return first_line
    return path.stem.replace("_", " ").title()


def get_description(mod):
    """Get description from module."""
    if hasattr(mod, "description"):
        return mod.description
    if mod.__doc__:
        lines = mod.__doc__.strip().split("\n")
        if len(lines) > 1:
            return " ".join(l.strip() for l in lines[1:] if l.strip())
    return ""


# ═══════════════════════════════════════════════════════════════════
#  Post-build modifications
# ═══════════════════════════════════════════════════════════════════

def apply_solo(score, part_names):
    """Solo: mute everything except the named parts."""
    for name, part in score.parts.items():
        if name not in part_names and name != "drums":
            part.set(volume=0.0)


def apply_mute(score, part_names):
    """Mute the named parts."""
    for name in part_names:
        if name in score.parts:
            score.parts[name].set(volume=0.0)


def apply_volume(score, volume):
    """Scale all part volumes."""
    if volume == 1.0:
        return
    for part in score.parts.values():
        if hasattr(part, "volume") and part.volume is not None:
            part.set(volume=part.volume * volume)


# ═══════════════════════════════════════════════════════════════════
#  Audio rendering & playback
# ═══════════════════════════════════════════════════════════════════

def parse_time(s):
    """Parse a time string like '1:30', '90', '0:45' into seconds."""
    if ":" in s:
        parts = s.split(":")
        return int(parts[0]) * 60 + float(parts[1])
    return float(s)


def render_audio(score, *, from_measure=None, to_measure=None,
                 from_seconds=None, to_seconds=None, loop=1):
    """Render score to a numpy audio buffer, optionally slicing by measure."""
    import inspect
    import threading
    import time
    mod = inspect.getmodule(play_score)
    render_score_fn = mod.render_score
    sample_rate = mod.SAMPLE_RATE

    # Spinner while rendering
    result = [None]
    done = threading.Event()

    def _render():
        result[0] = render_score_fn(score)
        done.set()

    t = threading.Thread(target=_render, daemon=True)
    t.start()

    frames = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    start_time = time.monotonic()
    i = 0
    while not done.wait(timeout=0.1):
        elapsed = time.monotonic() - start_time
        sys.stderr.write(f"\r  {frames[i % len(frames)]} Rendering... {elapsed:.1f}s")
        sys.stderr.flush()
        i += 1
    elapsed = time.monotonic() - start_time
    sys.stderr.write(f"\r  Rendered in {elapsed:.1f}s          \n")
    sys.stderr.flush()

    buf = result[0]

    start = 0
    end = len(buf)

    if from_measure is not None or to_measure is not None:
        beats_per_measure = score.time_signature.beats_per_measure
        samples_per_beat = int(sample_rate * 60.0 / score.bpm)
        samples_per_measure = samples_per_beat * beats_per_measure

        if from_measure is not None:
            start = (from_measure - 1) * samples_per_measure
        if to_measure is not None:
            end = min(to_measure * samples_per_measure, len(buf))

    if from_seconds is not None:
        start = int(from_seconds * sample_rate)
    if to_seconds is not None:
        end = int(to_seconds * sample_rate)

    start = int(max(0, min(start, len(buf))))
    end = int(max(start, min(end, len(buf))))

    if start > 0 or end < len(buf):
        buf = buf[start:end]

    if loop > 1:
        import numpy
        buf = numpy.tile(buf, (loop, 1)) if buf.ndim == 2 else numpy.tile(buf, loop)

    return buf, sample_rate


def play_audio(buf, sample_rate, title="", info_lines=None):
    """Simple terminal playback with progress bar."""
    import sounddevice as sd
    import time

    total_frames = len(buf)
    total_sec = total_frames / sample_rate
    tot_m, tot_s = int(total_sec // 60), int(total_sec % 60)

    if title:
        print(f"\n  {title}")
    if info_lines:
        for line in info_lines:
            print(f"  {line}")
    print()

    start = time.monotonic()
    try:
        sd.play(buf, sample_rate)
        while sd.get_stream().active:
            cur_sec = time.monotonic() - start
            cur_m, cur_s = int(cur_sec // 60), int(cur_sec % 60)
            pct = min(1.0, cur_sec / total_sec) if total_sec > 0 else 0
            bar_w = 40
            filled = int(pct * bar_w)
            bar = "█" * filled + "░" * (bar_w - filled)
            sys.stderr.write(f"\r  ▶ {cur_m}:{cur_s:02d} / {tot_m}:{tot_s:02d}  {bar}")
            sys.stderr.flush()
            time.sleep(0.25)
        sys.stderr.write("\n")
    except KeyboardInterrupt:
        sd.stop()
        sys.stderr.write("\n  Stopped.\n")


def save_wav(buf, sample_rate, path):
    """Save audio buffer to WAV file."""
    import numpy
    import scipy.io.wavfile

    peak = numpy.abs(buf).max()
    if peak > 0:
        buf = buf / peak * 0.95

    pcm = (buf * 32767).astype(numpy.int16)
    scipy.io.wavfile.write(path, sample_rate, pcm)


# ═══════════════════════════════════════════════════════════════════
#  Info & inspection
# ═══════════════════════════════════════════════════════════════════

def show_info(score, mod, path):
    """Print detailed score information."""
    title = get_title(mod, path)
    desc = get_description(mod)

    beats = score.total_beats
    bpm = score.bpm
    bpm_measure = score.time_signature.beats_per_measure
    measures = beats / bpm_measure if bpm_measure else 0
    duration_sec = (beats / bpm) * 60 if bpm else 0
    minutes = int(duration_sec // 60)
    seconds = int(duration_sec % 60)

    print(f"  Title:      {title}")
    if desc:
        print(f"  About:      {desc}")
    print(f"  Time:       {score.time_signature}")
    print(f"  BPM:        {bpm}")
    if score.system != "western":
        print(f"  System:     {score.system}")
    if score.temperament != "equal":
        print(f"  Temper:     {score.temperament}")
    if score.reference_pitch != 440.0:
        print(f"  Reference:  {score.reference_pitch} Hz")
    print(f"  Measures:   {int(measures)}")
    print(f"  Beats:      {int(beats)}")
    print(f"  Duration:   {minutes}:{seconds:02d}")
    print(f"  Parts:      {len(score.parts)}")


def show_parts(score):
    """Print part details."""
    for name, part in score.parts.items():
        notes = len(part.notes) if hasattr(part, "notes") else 0
        inst = getattr(part, "instrument", None) or getattr(part, "synth", "sine") or "sine"
        vol = getattr(part, "volume", 1.0) or 1.0
        print(f"  {name:20s}  {str(inst):16s}  vol={vol:<5.2f}  {notes:>4} notes")


def list_tracks():
    """List all .py score files in the tracks/ directory."""
    if not TRACKS_DIR.exists():
        print("No tracks/ directory found.")
        return

    files = sorted(TRACKS_DIR.glob("*.py"))
    if not files:
        print("No .py files in tracks/.")
        return

    print(f"  {'FILE':30s}  {'TITLE'}")
    print(f"  {'─' * 30}  {'─' * 45}")
    for f in files:
        try:
            score, mod = load_score(f)
            title = get_title(mod, f)
            bpm = score.bpm
            parts = len(score.parts)
            beats = score.total_beats
            bpm_measure = score.time_signature.beats_per_measure
            measures = int(beats / bpm_measure) if bpm_measure else 0
            duration_sec = (beats / bpm) * 60 if bpm else 0
            m = int(duration_sec // 60)
            s = int(duration_sec % 60)
            print(f"  {f.name:30s}  {title:30s}  {bpm:>3}bpm  {measures:>3}m  {m}:{s:02d}  {parts}p")
        except Exception as e:
            print(f"  {f.name:30s}  ERROR: {e}")


# ═══════════════════════════════════════════════════════════════════
#  CLI
# ═══════════════════════════════════════════════════════════════════

def pick_track():
    """Interactive curses track picker."""
    import curses

    if not TRACKS_DIR.exists():
        print("No tracks/ directory found.")
        return None

    files = sorted(TRACKS_DIR.glob("*.py"))
    if not files:
        print("No tracks found.")
        return None

    # Pre-load all track metadata before entering curses mode
    entries = []
    for f in files:
        try:
            score, mod = load_score(f)
            name = f.name
            bpm = score.bpm
            parts = len(score.parts)
            duration_sec = (score.total_beats / bpm) * 60 if bpm else 0
            m = int(duration_sec // 60)
            s = int(duration_sec % 60)
            desc = get_description(mod)
            entries.append((f, name, bpm, m, s, parts, desc))
        except Exception:
            entries.append((f, f.name, 0, 0, 0, 0, ""))

    selected = [0]
    result = [None]

    def _picker(stdscr):
        import time, math
        curses.curs_set(0)
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_CYAN, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)
        curses.init_pair(4, curses.COLOR_MAGENTA, -1)
        curses.init_pair(5, curses.COLOR_GREEN, -1)
        curses.init_pair(6, curses.COLOR_RED, -1)
        header_colors = [2, 4, 5, 3, 6]
        stdscr.nodelay(True)

        while True:
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            t = time.monotonic()

            # Header — each letter waves up/down and shifts color
            header = "INTERPRETATIONS"
            hx = max(0, (w - len(header)) // 2)
            for ci, ch in enumerate(header):
                wave = math.sin(t * 2.5 + ci * 0.4)
                y_off = round(wave * 0.5)
                color = header_colors[int((t * 1.5 + ci * 0.3) % len(header_colors))]
                try:
                    stdscr.addstr(1 + y_off, hx + ci, ch,
                                  curses.A_BOLD | curses.color_pair(color))
                except curses.error:
                    pass
            stdscr.addstr(3, max(0, (w - 15) // 2), "─" * 15,
                          curses.color_pair(2))
            stdscr.addstr(4, max(0, (w - 28) // 2), "↑/↓ navigate  ↵ play  q quit",
                          curses.A_DIM)

            # Track list
            list_start = 6
            for i, (f, title, bpm, m, s, parts, desc) in enumerate(entries):
                y = list_start + i
                if y >= h - 4:
                    break

                name_col = 22
                meta_str = f"{bpm:>3} BPM  {m}:{s:02d}" if bpm else ""
                name_display = title[:name_col - 1].ljust(name_col - 1)

                num = f"{i + 1:>2}."

                if i == selected[0]:
                    full = f" ▸ {num} {name_display}  {meta_str}"
                    stdscr.addstr(y, 1, full[:w - 2],
                                  curses.A_BOLD | curses.color_pair(1))
                else:
                    track_color = header_colors[i % len(header_colors)]
                    stdscr.addstr(y, 1, f"   {num} ",
                                  curses.A_BOLD)
                    stdscr.addstr(y, 8, name_display,
                                  curses.color_pair(track_color))
                    if meta_str:
                        stdscr.addstr(y, 8 + name_col, meta_str,
                                      curses.A_DIM)

            # Description of selected track
            _, _, _, _, _, _, desc = entries[selected[0]]
            if desc:
                desc_y = list_start + len(entries) + 1
                if desc_y < h - 2:
                    # Wrap description to fit width
                    desc = desc[:w - 6]
                    stdscr.addstr(desc_y, 3, desc,
                                  curses.A_DIM | curses.color_pair(3))

            stdscr.refresh()
            curses.napms(50)

            key = stdscr.getch()
            if key == curses.KEY_UP or key == ord("k"):
                selected[0] = max(0, selected[0] - 1)
            elif key == curses.KEY_DOWN or key == ord("j"):
                selected[0] = min(len(entries) - 1, selected[0] + 1)
            elif key in (curses.KEY_ENTER, 10, 13):
                result[0] = entries[selected[0]][0]
                return
            elif key == ord("q") or key == 27:
                return

    try:
        curses.wrapper(_picker)
    except KeyboardInterrupt:
        return None

    return result[0]


def build_parser():
    p = argparse.ArgumentParser(
        prog="play.py",
        description="Play interpretations score files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
convention:
  Every score is a .py file that exposes a `score` variable (pytheory Score).
  Like Flask exports `app`. That's it.

examples:
  uv run play.py tracks/acid_reign.py
  uv run play.py tracks/ghost_protocol.py --from 49 --to 64
  uv run play.py tracks/raga_midnight.py -o raga.wav
  uv run play.py tracks/acid_reign.py --solo 303,kick --bpm 150
  uv run play.py tracks/deep_time.py --mute wind --loop 2
  uv run play.py --list
""",
    )

    p.add_argument("score", nargs="?", help="Path to a .py score file")

    disc = p.add_argument_group("discovery")
    disc.add_argument("--list", action="store_true",
                      help="List all tracks in tracks/")

    insp = p.add_argument_group("inspection")
    insp.add_argument("--info", action="store_true",
                      help="Show score metadata and stats")
    insp.add_argument("--parts", action="store_true",
                      help="List all parts with details")

    play = p.add_argument_group("playback")
    play.add_argument("--from", dest="from_measure", type=int, metavar="N",
                      help="Start playback at measure N")
    play.add_argument("--to", dest="to_measure", type=int, metavar="N",
                      help="Stop playback at measure N")
    play.add_argument("--from-time", dest="from_time", metavar="TIME",
                      help="Start playback at time (e.g. 1:30, 90, 0:45)")
    play.add_argument("--to-time", dest="to_time", metavar="TIME",
                      help="Stop playback at time (e.g. 3:00, 180)")
    play.add_argument("--loop", type=int, default=1, metavar="N",
                      help="Loop playback N times (default: 1)")
    play.add_argument("--solo", metavar="PARTS",
                      help="Solo specific parts (comma-separated)")
    play.add_argument("--mute", metavar="PARTS",
                      help="Mute specific parts (comma-separated)")

    over = p.add_argument_group("overrides")
    over.add_argument("--bpm", type=int, metavar="N",
                      help="Override tempo")
    over.add_argument("--volume", type=float, default=1.0, metavar="V",
                      help="Master volume scale (0.0-1.0, default: 1.0)")
    over.add_argument("--pitch", type=float, metavar="HZ",
                      help="Override reference pitch (e.g. 432, 440)")

    exp = p.add_argument_group("export")
    exp.add_argument("-o", "--output", metavar="FILE",
                     help="Export to WAV file")
    exp.add_argument("--midi", metavar="FILE",
                     help="Export to MIDI file")

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    # ── List ───────────────────────────────────────────────────────
    if args.list:
        list_tracks()
        return

    # ── Track picker when no score given ─────────────────────────
    if not args.score:
        path = pick_track()
        if path is None:
            return
    else:
        path = Path(args.score)
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    # ── Load ───────────────────────────────────────────────────────
    score, mod = load_score(path)
    title = get_title(mod, path)

    # ── Post-build modifications ───────────────────────────────────
    if args.bpm:
        score.bpm = args.bpm

    if args.pitch:
        score.reference_pitch = args.pitch

    if args.solo:
        apply_solo(score, set(args.solo.split(",")))

    if args.mute:
        apply_mute(score, set(args.mute.split(",")))

    apply_volume(score, args.volume)

    # ── Info / parts ───────────────────────────────────────────────
    if args.info:
        show_info(score, mod, path)
        return

    if args.parts:
        show_parts(score)
        return

    # ── Export to MIDI ─────────────────────────────────────────────
    if args.midi:
        score.save_midi(args.midi)
        print(f"Exported MIDI -> {args.midi}")
        return

    # ── Show metadata before rendering ──────────────────────────────
    show_info(score, mod, path)
    print()

    # ── Render ─────────────────────────────────────────────────────
    from_sec = parse_time(args.from_time) if args.from_time else None
    to_sec = parse_time(args.to_time) if args.to_time else None

    buf, sr = render_audio(
        score,
        from_measure=args.from_measure,
        to_measure=args.to_measure,
        from_seconds=from_sec,
        to_seconds=to_sec,
        loop=args.loop,
    )

    # ── Export to WAV ──────────────────────────────────────────────
    if args.output:
        save_wav(buf, sr, args.output)
        duration_sec = len(buf) / sr
        m, s = int(duration_sec // 60), int(duration_sec % 60)
        print(f"Exported WAV -> {args.output} ({m}:{s:02d})")
        return

    # ── Play ───────────────────────────────────────────────────────
    # Build info lines for the player UI
    info = []
    info.append(f"{score.time_signature}  {score.bpm} BPM  {len(score.parts)} parts")
    info.append(f"{score.system}  {score.temperament}  A={score.reference_pitch} Hz")

    play_audio(buf, sr, title=title, info_lines=info)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(0)
