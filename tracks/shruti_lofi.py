"""
SHRUTI LOFI — 22-tone microtonal lo-fi hip hop.
The pitch is slightly wrong. That's the point.
Like a tape copied so many times the intervals drifted.
D minor, shruti tuning, 75 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("D", "minor")
s = key.scale  # D E F G A Bb C

D  = s[0]; E  = s[1]; F  = s[2]; G  = s[3]
A  = s[4]; Bb = s[5]; C  = s[6]

score = Score("4/4", bpm=75, system="shruti", temperament="just")

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

prog = key.progression("i", "VII", "VI", "iv")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~3:25):
#   Bars  1-8:   Vinyl + kalimba — warm, wrong, beautiful
#   Bars  9-16:  Rhodes enters — microtonal chords
#   Bars 17-24:  Drums — lazy boom bap
#   Bars 25-32:  Sitar — the sample flip, shruti intervals
#   Bars 33-40:  Mellotron pad — tape on tape
#   Bars 41-48:  Everything together — the lo-fi dream
#   Bars 49-56:  Breakdown — just kalimba + 808
#   Bars 57-64:  Returns soft, fades
# ═══════════════════════════════════════════════════════════════════

# ── VINYL — the crackle, always there ─────────────────────────
vinyl = score.part("vinyl", synth="noise", envelope="pad", volume=0.035,
                   lowpass=1800, highpass=500,
                   distortion=0.35, distortion_drive=2.5,
                   saturation=0.5, pan=0.1)

for _ in range(64):
    vinyl.add(D, Duration.WHOLE, velocity=22)

# ── KALIMBA — the seed, microtonal blips ──────────────────────
kal = score.part("kalimba", instrument="kalimba", volume=0.4,
                 reverb=0.3, reverb_type="taj_mahal",
                 delay=0.15, delay_time=0.4, delay_feedback=0.25,
                 lowpass=3000,
                 pan=-0.2, humanize=0.12)

# Bars 1-8: alone — the shruti intervals are audible, warm
kal_a = [
    (D, Duration.EIGHTH, 68), (None, Duration.EIGHTH, 0),
    (F, Duration.EIGHTH, 60), (A, Duration.EIGHTH, 62),
    (None, Duration.EIGHTH, 0), (F, Duration.EIGHTH, 55),
    (D, Duration.EIGHTH, 65), (None, Duration.EIGHTH, 0),
]
kal_b = [
    (C, Duration.EIGHTH, 62), (None, Duration.EIGHTH, 0),
    (D, Duration.EIGHTH, 58), (F, Duration.EIGHTH, 60),
    (E, Duration.EIGHTH, 55), (None, Duration.EIGHTH, 0),
    (D, Duration.EIGHTH, 62), (None, Duration.EIGHTH, 0),
]
for _ in range(4):
    for note, dur, vel in kal_a:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=vel)
    for note, dur, vel in kal_b:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=vel)

# Bars 9-48: continues — the heartbeat
for _ in range(20):
    for note, dur, vel in kal_a:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=vel)
    for note, dur, vel in kal_b:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=vel)

# Bars 49-56: breakdown — just kalimba, quieter
kal.set(volume=0.35)
for _ in range(4):
    for note, dur, vel in kal_a:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=max(30, vel - 12))
    for note, dur, vel in kal_b:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=max(30, vel - 12))

# Bars 57-64: fading
for rep in range(4):
    off = rep * -10
    for note, dur, vel in kal_a:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=max(18, vel + off - 12))
    for note, dur, vel in kal_b:
        if note is None:
            kal.rest(dur)
        else:
            kal.add(note, dur, velocity=max(18, vel + off - 12))

# ── RHODES — microtonal chords, enters bar 9 ──────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.3,
                    reverb=0.4, reverb_type="taj_mahal",
                    delay=0.1, delay_time=0.4, delay_feedback=0.2,
                    tremolo_depth=0.08, tremolo_rate=2.0,
                    lowpass=3000,
                    pan=0.2, humanize=0.1)

for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# Bars 9-48: sparse chords — the shruti tuning makes them shimmer
for section in range(10):
    p = prog if section % 2 == 0 else key.progression("i", "v", "VI", "iv")
    for chord in p:
        rhodes.add(chord, Duration.EIGHTH, velocity=58)
        rhodes.rest(Duration.DOTTED_QUARTER)
        rhodes.rest(Duration.HALF)

# Bars 49-56: silent
for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# Bars 57-64: returns fading
for vel in [48, 42, 35, 28]:
    for chord in prog:
        rhodes.add(chord, Duration.EIGHTH, velocity=vel)
        rhodes.rest(Duration.DOTTED_QUARTER)
        rhodes.rest(Duration.HALF)

# ── 808 — warm, round, enters bar 9 ──────────────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=0.5,
                 lowpass=180, distortion=0.12, distortion_drive=2.0,
                 sub_osc=0.4, sidechain=0.3)

for _ in range(8):
    sub.rest(Duration.WHOLE)

# Bars 9-48: continuous wave, follows roots
roots = [D.add(-24), C.add(-24), Bb.add(-24), G.add(-24)]
for _ in range(10):
    for root in roots:
        sub.add(root, Duration.WHOLE, velocity=35)

# Bars 49-56: just the root — breakdown
for _ in range(8):
    sub.add(D.add(-24), Duration.WHOLE, velocity=30)

# Bars 57-64: fading
for vel in [28, 25, 22, 18, 14, 10, 5, 0]:
    if vel > 0:
        sub.add(D.add(-24), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# ── DRUMS — lazy boom bap, enters bar 17 ──────────────────────
kick = score.part("kick", volume=0.55, humanize=0.06,
                  reverb=0.1, lowpass=5000)
snare = score.part("snare", volume=0.35, humanize=0.06,
                   reverb=0.2, reverb_decay=1.0,
                   delay=0.06, delay_time=0.4, delay_feedback=0.1,
                   pan=0.05)
hats = score.part("hats", volume=0.2, pan=0.15, humanize=0.06)

for _ in range(16):
    kick.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)
    hats.rest(Duration.WHOLE)

# Bars 17-48: lo-fi beat — lazy, behind the grid
for _ in range(32):
    # Kick on 1 and and-of-2
    kick.hit(K, Duration.QUARTER, velocity=92)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=75)
    kick.rest(Duration.QUARTER)
    kick.rest(Duration.QUARTER)

    # Snare on 2 and 4 with ghost before
    snare.rest(Duration.EIGHTH)
    snare.hit(S, Duration.SIXTEENTH, velocity=35)
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.QUARTER, velocity=85)
    snare.rest(Duration.EIGHTH)
    snare.hit(S, Duration.SIXTEENTH, velocity=32)
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.QUARTER, velocity=88)

    # Hats — lazy 8ths, some louder
    hats.hit(CH, Duration.EIGHTH, velocity=58)
    hats.hit(CH, Duration.EIGHTH, velocity=35)
    hats.hit(CH, Duration.EIGHTH, velocity=52)
    hats.hit(CH, Duration.EIGHTH, velocity=38)
    hats.hit(CH, Duration.EIGHTH, velocity=55)
    hats.hit(CH, Duration.EIGHTH, velocity=32)
    hats.hit(OH, Duration.EIGHTH, velocity=48)
    hats.hit(CH, Duration.EIGHTH, velocity=35)

# Bars 49-56: breakdown — half time
for _ in range(8):
    kick.hit(K, Duration.HALF, velocity=82)
    kick.rest(Duration.HALF)
    snare.rest(Duration.HALF)
    snare.hit(S, Duration.HALF, velocity=72)
    hats.rest(Duration.WHOLE)

# Bars 57-64: returns fading
for vel in [80, 72, 62, 52, 40, 28, 0, 0]:
    if vel > 0:
        kick.hit(K, Duration.QUARTER, velocity=vel)
        kick.rest(Duration.DOTTED_HALF)
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=max(15, vel - 8))
        snare.rest(Duration.HALF)
        hats.hit(CH, Duration.QUARTER, velocity=max(15, vel - 25))
        hats.rest(Duration.DOTTED_HALF)
    else:
        kick.rest(Duration.WHOLE)
        snare.rest(Duration.WHOLE)
        hats.rest(Duration.WHOLE)

# ── SITAR — the sample flip, enters bar 25 ────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.4,
                   reverb=0.2, reverb_type="taj_mahal",
                   delay=0.12, delay_time=0.4, delay_feedback=0.2,
                   lowpass=3500,
                   pan=-0.25, humanize=0.1)

for _ in range(24):
    sitar.rest(Duration.WHOLE)

# Bars 25-32: the hook — shruti intervals make it haunting
sitar_hook = [
    (D, Duration.QUARTER, 72, -0.1), (F, Duration.EIGHTH, 65, 0.0),
    (E, Duration.EIGHTH, 62, 0.0), (D, Duration.HALF, 68, -0.08),
    (None, Duration.QUARTER, 0, 0.0), (A.add(-12), Duration.QUARTER, 60, 0.1),
    (D, Duration.QUARTER, 68, 0.0), (F, Duration.QUARTER, 65, -0.1),
    (G, Duration.HALF, 70, 0.0), (F, Duration.HALF, 65, -0.08),
]
for _ in range(4):
    for note, dur, vel, bend in sitar_hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=vel, bend=bend)

# Bars 33-48: continues under mellotron
for _ in range(8):
    for note, dur, vel, bend in sitar_hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=max(35, vel - 8), bend=bend)

# Bars 49-56: one note — breathing
sitar.add(D, Duration.WHOLE, velocity=55, bend=-0.1)
sitar.rest(Duration.WHOLE)
sitar.add(A.add(-12), Duration.WHOLE, velocity=48, bend=0.08)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 57-64: hook returns fading
for vel in [58, 50, 42, 35]:
    for note, dur, v, bend in sitar_hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=max(20, vel - 10), bend=bend)

# ── MELLOTRON FLUTE — tape pad, enters bar 33 ─────────────────
mello = score.part("mellotron", instrument="mellotron_flute", volume=0.2,
                   reverb=0.35, reverb_type="taj_mahal",
                   lowpass=2500,
                   pan=0.15, humanize=0.08)

for _ in range(32):
    mello.rest(Duration.WHOLE)

# Bars 33-48: warm chords — tape warble + shruti = magic
for _ in range(4):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=48)

# Bars 49-56: silent
for _ in range(8):
    mello.rest(Duration.WHOLE)

# Bars 57-64: returns fading
for vel in [42, 35, 28, 22, 15, 10, 0, 0]:
    if vel > 0:
        mello.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        mello.rest(Duration.WHOLE)

# ── TAMBURA — the shruti drone, enters bar 9 ──────────────────
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.1,
                     reverb=0.35, reverb_type="taj_mahal",
                     chorus=0.3, chorus_rate=0.05, chorus_depth=0.01,
                     lowpass=800, pan=-0.1)

for _ in range(8):
    tambura.rest(Duration.WHOLE)

# Sa-Pa drone — in shruti tuning the fifth is pure, not tempered
for _ in range(48):
    tambura.add(D.add(-24), Duration.HALF, velocity=38)
    tambura.add(A.add(-24), Duration.HALF, velocity=32)

for vel in [30, 25, 20, 15, 10, 5, 0, 0]:
    if vel > 0:
        tambura.add(D.add(-24), Duration.WHOLE, velocity=vel)
    else:
        tambura.rest(Duration.WHOLE)

# ── SINGING BOWL — just two strikes ───────────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.25,
                  reverb=0.5, reverb_type="taj_mahal",
                  delay=0.12, delay_time=0.8, delay_feedback=0.15,
                  pan=0.2)

bowl.add(D.add(-24), Duration.WHOLE, velocity=55)
for _ in range(62):
    bowl.rest(Duration.WHOLE)
bowl.add(D.add(-24), Duration.WHOLE, velocity=42)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"System: shruti / just intonation")
print(f"BPM: 75")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing SHRUTI LOFI (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing SHRUTI LOFI...")
    play_score(score)
