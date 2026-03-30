"""
ACID REIGN — 303 acid bass. Groovy, squelchy, raw.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("A", "minor")
s = key.scale

# Notes in the bass range (octave 2-3)
A  = Tone.from_string("A2")
B  = Tone.from_string("B2")
C  = Tone.from_string("C3")
D  = Tone.from_string("D3")
E  = Tone.from_string("E3")
F  = Tone.from_string("F3")
G  = Tone.from_string("G3")
Ab = Tone.from_string("Ab2")  # chromatic approach
Bb = Tone.from_string("Bb2")

score = Score("4/4", bpm=135)

K  = DrumSound.KICK
CL = DrumSound.CLAP
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

# ── 303 — the groove, hand-written, legato slides ──────────────
acid = score.part("303", synth="saw", volume=0.7,
                  lowpass=800, lowpass_q=4.0,
                  distortion=0.3, distortion_drive=4.0,
                  saturation=0.25, legato=True, glide=0.05,
                  sub_osc=0.4, sidechain=0.3)
acid.lfo("lowpass", rate=0.02, min=500, max=6000, bars=64, shape="triangle")

# Four groove patterns — the rests make the groove
# Pattern A: pumping root — DUM-rest-dum-DUM rest-dum-dum-DUM
pA = [(A, 110), (None, 0), (A, 80), (E, 100),
      (None, 0), (A, 85), (G, 75), (A, 105)]

# Pattern B: climbing — slides up chromatically
pB = [(A, 105), (Bb, 80), (C, 95), (None, 0),
      (C, 85), (D, 90), (E, 100), (None, 0)]

# Pattern C: menacing — big gaps, low hits
pC = [(A, 110), (None, 0), (None, 0), (E, 95),
      (None, 0), (A, 100), (Ab, 85), (A, 108)]

# Pattern D: funky — syncopated, all over the place
pD = [(None, 0), (A, 100), (C, 90), (None, 0),
      (E, 105), (D, 85), (None, 0), (A, 110)]

# Bars 1-8: 303 alone — patterns A and B
for _ in range(2):
    for pat in [pA, pB]:
        for _ in range(2):
            for note, vel in pat:
                if note is None:
                    acid.rest(Duration.EIGHTH)
                else:
                    acid.add(note, Duration.EIGHTH, velocity=vel)

# Bars 9-24: cycling all patterns
for _ in range(2):
    for pat in [pA, pB, pC, pD]:
        for _ in range(2):
            for note, vel in pat:
                if note is None:
                    acid.rest(Duration.EIGHTH)
                else:
                    acid.add(note, Duration.EIGHTH, velocity=vel)

# Bars 25-32: just A and C patterns, harder
for _ in range(2):
    for pat in [pA, pC]:
        for _ in range(2):
            for note, vel in pat:
                if note is None:
                    acid.rest(Duration.EIGHTH)
                else:
                    acid.add(note, Duration.EIGHTH, velocity=min(127, vel + 10))

# Bars 33-40: breakdown — sustained notes, filter wide open
for _ in range(2):
    acid.add(A, Duration.WHOLE, velocity=90)
    acid.add(E, Duration.WHOLE, velocity=85)
    acid.add(C, Duration.WHOLE, velocity=88)
    acid.add(A, Duration.WHOLE, velocity=92)

# Bars 41-56: peak — all patterns cycling, max energy
for _ in range(2):
    for pat in [pA, pB, pC, pD]:
        for _ in range(2):
            for note, vel in pat:
                if note is None:
                    acid.rest(Duration.EIGHTH)
                else:
                    acid.add(note, Duration.EIGHTH, velocity=min(127, vel + 12))

# Bars 57-64: patterns A only, filtering down
for _ in range(4):
    for _ in range(2):
        for note, vel in pA:
            if note is None:
                acid.rest(Duration.EIGHTH)
            else:
                acid.add(note, Duration.EIGHTH, velocity=max(40, vel - 15))

# ── KICK — four on the floor, enters bar 9, sidechained ────────
kick = score.part("kick", volume=0.5, humanize=0.03)

for _ in range(8):
    kick.rest(Duration.WHOLE)

for _ in range(48):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=118)

for bar in range(8):
    vel = max(30, 112 - bar * 10)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# ── CLAP — 2 and 4, enters bar 9 ──────────────────────────────
clap = score.part("clap", volume=0.3, reverb=0.15, humanize=0.04)

for _ in range(8):
    clap.rest(Duration.WHOLE)

for _ in range(48):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=100)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=102)

for bar in range(8):
    vel = max(25, 95 - bar * 9)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)

# ── HATS — 16ths with open hat accents, enters bar 17 ──────────
hats = score.part("hats", volume=0.25, humanize=0.04, sidechain=0.15)

for _ in range(16):
    hats.rest(Duration.WHOLE)

for _ in range(40):
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=75)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(OH if beat % 2 == 1 else CH, Duration.SIXTEENTH, velocity=60)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)

for bar in range(8):
    vel = max(20, 68 - bar * 6)
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=vel)
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 28))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 15))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 30))

# ── PAD — dark atmosphere, sidechained ──────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.15,
                 reverb=0.5, chorus=0.3, chorus_rate=0.2,
                 chorus_depth=0.008, lowpass=1200,
                 sidechain=0.4)

prog = key.progression("i", "VII", "VI", "v")

for _ in range(8):
    pad.rest(Duration.WHOLE)

for _ in range(14):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=60)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 135")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing ACID REIGN (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing ACID REIGN...")
    play_score(score)
