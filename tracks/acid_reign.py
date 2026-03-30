"""
ACID REIGN — 303 acid bass. Simple, raw, relentless.
"""

from pytheory import Key, Duration, Score, play_score
from pytheory.rhythm import DrumSound

key = Key("A", "minor")
s = key.scale
prog = [c.transpose(-24) for c in key.progression("i", "VII", "VI", "v")]

score = Score("4/4", bpm=135)

K  = DrumSound.KICK
CL = DrumSound.CLAP
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

# ── 303 — arpeggiated chords, legato, squelchy ─────────────────
acid = score.part("303", synth="saw", volume=0.7,
                  lowpass=800, lowpass_q=4.0,
                  distortion=0.4, distortion_drive=5.0,
                  saturation=0.3, legato=True, glide=0.04,
                  sub_osc=0.5)
acid.lfo("lowpass", rate=0.015, min=400, max=8000, bars=64, shape="triangle")

# Bars 1-8: 303 alone — arped progression, one octave down
for _ in range(2):
    for chord in prog:
        acid.arpeggio(chord, bars=1, pattern="updown",
                      division=Duration.SIXTEENTH, octaves=2)

# Bars 9-32: same but louder patterns kick in around it
for _ in range(6):
    for chord in prog:
        acid.arpeggio(chord, bars=1, pattern="updown",
                      division=Duration.SIXTEENTH, octaves=2)

# Bars 33-40: breakdown — sustained chords, filter wide
for chord in prog:
    acid.add(chord, Duration.WHOLE)
for chord in prog:
    acid.add(chord, Duration.WHOLE)

# Bars 41-56: back to arps, peak energy
for _ in range(4):
    for chord in prog:
        acid.arpeggio(chord, bars=1, pattern="updown",
                      division=Duration.SIXTEENTH, octaves=2)

# Bars 57-64: fading arps
for _ in range(2):
    for chord in prog:
        acid.arpeggio(chord, bars=1, pattern="up",
                      division=Duration.EIGHTH, octaves=1)

# ── KICK — four on the floor, enters bar 9 ─────────────────────
kick = score.part("kick", volume=0.5, humanize=0.03)

for _ in range(8):
    kick.rest(Duration.WHOLE)

for _ in range(48):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=115)

for bar in range(8):
    vel = max(30, 110 - bar * 10)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# ── CLAP — 2 and 4, enters bar 9 ──────────────────────────────
clap = score.part("clap", volume=0.3, reverb=0.15, humanize=0.04)

for _ in range(8):
    clap.rest(Duration.WHOLE)

for _ in range(48):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=95)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=98)

for bar in range(8):
    vel = max(25, 90 - bar * 8)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)

# ── HATS — 16ths, enters bar 17 ────────────────────────────────
hats = score.part("hats", volume=0.25, humanize=0.04)

for _ in range(16):
    hats.rest(Duration.WHOLE)

for _ in range(40):
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=72)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(OH if beat % 2 == 1 else CH, Duration.SIXTEENTH, velocity=58)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)

for bar in range(8):
    vel = max(20, 65 - bar * 6)
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=vel)
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 25))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 12))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 28))

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
