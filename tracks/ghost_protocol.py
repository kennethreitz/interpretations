"""
GHOST PROTOCOL — progressive house in the style of deadmau5.
Dark and driving opening → long build → euphoric release.
Minimal, hypnotic, relentless.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

# ── Key: F minor (dark) → Ab major (euphoric, relative major) ──
key_dark = Key("F", "minor")
key_bright = Key("Ab", "major")

sd = key_dark.scale
sb = key_bright.scale

# F minor: F G Ab Bb C Db Eb
F  = sd[0]; G  = sd[1]; Ab = sd[2]; Bb = sd[3]
C  = sd[4]; Db = sd[5]; Eb = sd[6]

score = Score("4/4", bpm=128)

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (96 bars, ~4.5 min at 128 BPM):
#   Bars  1-8:   Intro — kick + filtered pad, dark
#   Bars  9-24:  Build 1 — bass enters, saw lead, filter opens
#   Bars 25-32:  Breakdown — kick drops, pad swells, tension
#   Bars 33-48:  Drop 1 — everything hits, dark and driving
#   Bars 49-56:  Breakdown 2 — melodic, hopeful, the turn
#   Bars 57-72:  Drop 2 — euphoric, major key, full energy
#   Bars 73-80:  Outro — filtering down, kick rides out
#   Bars 81-96:  Fade — minimal, echoes
# ═══════════════════════════════════════════════════════════════════

K  = DrumSound.KICK
S  = DrumSound.SNARE
CL = DrumSound.CLAP
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

# ── KICK — four on the floor, the heartbeat ────────────────────
kick = score.part("kick", volume=0.5, humanize=0.03)

# Bars 1-24: kick from the start
for _ in range(24):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=115)

# Bars 25-32: breakdown — kick drops out
for _ in range(8):
    kick.rest(Duration.WHOLE)

# Bars 33-72: kick returns for both drops
for _ in range(40):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=118)

# Bars 73-96: outro, fading via velocity
for bar in range(24):
    vel = max(30, 115 - bar * 4)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# ── CLAP — on 2 and 4 ──────────────────────────────────────────
clap = score.part("clap", volume=0.35, reverb=0.2, reverb_decay=0.5,
                  humanize=0.04)

# Bars 1-8: no clap yet
for _ in range(8):
    clap.rest(Duration.WHOLE)

# Bars 9-24: clap enters
for _ in range(16):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=95)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=98)

# Bars 25-32: breakdown — clap out
for _ in range(8):
    clap.rest(Duration.WHOLE)

# Bars 33-72: clap through both drops
for _ in range(40):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=100)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=102)

# Bars 73-96: fading
for bar in range(24):
    vel = max(30, 100 - bar * 3)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)

# ── HATS — offbeat 8ths, deadmau5 style ────────────────────────
hats = score.part("hats", volume=0.3, humanize=0.04)

# Bars 1-8: no hats
for _ in range(8):
    hats.rest(Duration.WHOLE)

# Bars 9-24: offbeat closed hats
for _ in range(16):
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=72)

# Bars 25-32: breakdown — open hat rolls building
for bar in range(8):
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        vel = min(95, 50 + bar * 5 + beat)
        hats.hit(OH if bar > 5 else CH, Duration.EIGHTH, velocity=vel)

# Bars 33-72: hats through drops — offbeat 8ths
for _ in range(40):
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=75)

# Bars 73-96: fading
for bar in range(24):
    vel = max(25, 75 - bar * 2)
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=vel)

# ── BASS — sidechained sub, minimal ────────────────────────────
bass = score.part("bass", synth="saw", envelope="pluck", volume=0.4,
                  lowpass=300, distortion=0.15, distortion_drive=2.5,
                  sub_osc=0.5)

# Bars 1-8: no bass
for _ in range(8):
    bass.rest(Duration.WHOLE)

# Bars 9-32: dark bass line — F minor
bass_dark = [
    (F.add(-24), Duration.EIGHTH), (None, Duration.EIGHTH),
    (F.add(-24), Duration.EIGHTH), (None, Duration.EIGHTH),
    (F.add(-24), Duration.EIGHTH), (None, Duration.QUARTER),
    (Ab.add(-24), Duration.EIGHTH),
]
for _ in range(6):
    for note, dur in bass_dark:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=100)

# Bars 33-48: drop 1 bass — heavier, same pattern
for _ in range(4):
    for note, dur in bass_dark:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=110)

# Bars 49-56: breakdown 2 — bass sustains
for _ in range(4):
    bass.add(F.add(-24), Duration.WHOLE, velocity=85)
for _ in range(4):
    bass.add(Ab.add(-24), Duration.WHOLE, velocity=85)

# Bars 57-72: drop 2 — euphoric bass, Ab major
bass_bright = [
    (Ab.add(-24), Duration.EIGHTH), (None, Duration.EIGHTH),
    (Ab.add(-24), Duration.EIGHTH), (None, Duration.EIGHTH),
    (Ab.add(-24), Duration.EIGHTH), (None, Duration.QUARTER),
    (Eb.add(-24), Duration.EIGHTH),
]
for _ in range(4):
    for note, dur in bass_bright:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=108)

# Bars 73-96: outro bass fading
for _ in range(6):
    for note, dur in bass_dark:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=max(30, 90 - _ * 10))

# ── PAD — filtered supersaw, the atmosphere ─────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.25,
                 reverb=0.5, chorus=0.4, chorus_rate=0.3, chorus_depth=0.008,
                 lowpass=800)
pad.lfo("lowpass", rate=0.02, min=400, max=4000, bars=96, shape="triangle")

# Dark pads — i VI VII throughout, slow chord changes
dark_prog = key_dark.progression("i", "VI", "VII", "i")
bright_prog = key_bright.progression("I", "V", "vi", "IV")

# Bars 1-32: dark pads
for _ in range(8):
    for chord in dark_prog:
        pad.add(chord, Duration.WHOLE)

# Bars 33-48: drop 1 — same chords, filter open
for _ in range(4):
    for chord in dark_prog:
        pad.add(chord, Duration.WHOLE)

# Bars 49-56: breakdown 2 — transition chords
for chord in dark_prog:
    pad.add(chord, Duration.WHOLE)
for chord in bright_prog:
    pad.add(chord, Duration.WHOLE)

# Bars 57-72: drop 2 — euphoric! major key pads
for _ in range(4):
    for chord in bright_prog:
        pad.add(chord, Duration.WHOLE)

# Bars 73-96: outro — back to minor, filtering down
for _ in range(6):
    for chord in dark_prog:
        pad.add(chord, Duration.WHOLE)

# ── LEAD — saw pluck, the hook ──────────────────────────────────
lead = score.part("lead", synth="saw", envelope="pluck", volume=0.3,
                  reverb=0.3, delay=0.35, delay_time=0.234,
                  delay_feedback=0.4, lowpass=3000, humanize=0.05)

# Bars 1-8: silence
for _ in range(8):
    lead.rest(Duration.WHOLE)

# Bars 9-24: dark minimal lead — hypnotic 16th note pattern
lead_dark = [
    F.add(12), None, C.add(12), None,
    Eb.add(12), None, C.add(12), Bb,
    F.add(12), None, C.add(12), None,
    Ab.add(12), None, Eb.add(12), C.add(12),
]
for _ in range(4):
    for note in lead_dark:
        if note is None:
            lead.rest(Duration.SIXTEENTH)
        else:
            lead.add(note, Duration.SIXTEENTH, velocity=85)

# Bars 25-32: breakdown — lead gets melodic
lead_melody = [
    (F.add(12), Duration.HALF, 90),
    (Eb.add(12), Duration.QUARTER, 85),
    (Db.add(12), Duration.QUARTER, 80),
    (C.add(12), Duration.HALF, 88),
    (Bb, Duration.QUARTER, 82),
    (Ab, Duration.QUARTER, 78),
    (Bb, Duration.HALF, 85),
    (C.add(12), Duration.QUARTER, 88),
    (Db.add(12), Duration.QUARTER, 82),
    (C.add(12), Duration.WHOLE, 90),
]
for note, dur, vel in lead_melody:
    lead.add(note, dur, velocity=vel)
for _ in range(4):
    lead.rest(Duration.WHOLE)

# Bars 33-48: drop 1 — lead returns, more intense
for _ in range(4):
    for note in lead_dark:
        if note is None:
            lead.rest(Duration.SIXTEENTH)
        else:
            lead.add(note, Duration.SIXTEENTH, velocity=95)

# Bars 49-56: breakdown 2 — emotional melody, the turn
lead_turn = [
    (Ab.add(12), Duration.HALF, 95),
    (Bb.add(12), Duration.QUARTER, 90),
    (C.add(24), Duration.QUARTER, 100),
    (Bb.add(12), Duration.HALF, 92),
    (Ab.add(12), Duration.QUARTER, 88),
    (Eb.add(12), Duration.QUARTER, 85),
    (Ab.add(12), Duration.HALF, 95),
    (C.add(24), Duration.HALF, 105),
    (Bb.add(12), Duration.WHOLE, 100),
    (Ab.add(12), Duration.WHOLE, 95),
]
for note, dur, vel in lead_turn:
    lead.add(note, dur, velocity=vel)
for _ in range(2):
    lead.rest(Duration.WHOLE)

# Bars 57-72: drop 2 — euphoric lead! Ab major arps
lead_euphoric = [
    Ab.add(12), None, C.add(24), None,
    Eb.add(24), None, C.add(24), Ab.add(12),
    Ab.add(12), None, Bb.add(12), None,
    C.add(24), None, Eb.add(24), C.add(24),
]
for _ in range(4):
    for note in lead_euphoric:
        if note is None:
            lead.rest(Duration.SIXTEENTH)
        else:
            lead.add(note, Duration.SIXTEENTH, velocity=100)

# Bars 73-96: outro — lead dissolves
for _ in range(2):
    for note in lead_dark:
        if note is None:
            lead.rest(Duration.SIXTEENTH)
        else:
            lead.add(note, Duration.SIXTEENTH, velocity=65)
for _ in range(20):
    lead.rest(Duration.WHOLE)

# ── PLUCK — deadmau5 signature stab chord ──────────────────────
pluck = score.part("pluck", synth="saw", envelope="pluck", volume=0.2,
                   reverb=0.25, delay=0.2, delay_time=0.234,
                   delay_feedback=0.35, lowpass=2500, detune=8,
                   humanize=0.04)

# Bars 1-32: silence
for _ in range(32):
    pluck.rest(Duration.WHOLE)

# Bars 33-48: drop 1 — offbeat chord stabs
for _ in range(4):
    for chord in dark_prog:
        pluck.rest(Duration.EIGHTH)
        pluck.add(chord, Duration.EIGHTH, velocity=90)
        pluck.rest(Duration.QUARTER)
        pluck.rest(Duration.EIGHTH)
        pluck.add(chord, Duration.EIGHTH, velocity=85)
        pluck.rest(Duration.QUARTER)

# Bars 49-56: breakdown — silence
for _ in range(8):
    pluck.rest(Duration.WHOLE)

# Bars 57-72: drop 2 — euphoric stabs
for _ in range(4):
    for chord in bright_prog:
        pluck.rest(Duration.EIGHTH)
        pluck.add(chord, Duration.EIGHTH, velocity=95)
        pluck.rest(Duration.QUARTER)
        pluck.rest(Duration.EIGHTH)
        pluck.add(chord, Duration.EIGHTH, velocity=90)
        pluck.rest(Duration.QUARTER)

# Bars 73-96: silence
for _ in range(24):
    pluck.rest(Duration.WHOLE)

# ── RISER — noise sweep for breakdowns ──────────────────────────
riser = score.part("riser", synth="noise", envelope="pad", volume=0.15,
                   lowpass=200)
riser.lfo("lowpass", rate=0.125, min=200, max=8000, bars=8, shape="saw")

# Bars 1-24: silence
for _ in range(24):
    riser.rest(Duration.WHOLE)

# Bars 25-32: first riser
for _ in range(8):
    riser.add(C, Duration.WHOLE, velocity=80)

# Bars 33-48: silence
for _ in range(16):
    riser.rest(Duration.WHOLE)

# Bars 49-56: second riser (bigger)
riser.lfo("lowpass", rate=0.125, min=200, max=10000, bars=8, shape="saw")
for _ in range(8):
    riser.add(C, Duration.WHOLE, velocity=90)

# Bars 57-96: silence
for _ in range(40):
    riser.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key_dark} → {key_bright}")
print(f"BPM: 128")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing GHOST PROTOCOL (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing GHOST PROTOCOL...")
    play_score(score)
