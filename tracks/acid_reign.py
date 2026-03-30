"""
ACID REIGN — the filthiest 303 bass line in human existence.
Squelchy, resonant, relentless. Filter sweeps that melt faces.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("A", "minor")
s = key.scale

A  = s[0]; B  = s[1]; C  = s[2]; D  = s[3]
E  = s[4]; F  = s[5]; G  = s[6]

score = Score("4/4", bpm=135)

K  = DrumSound.KICK
CL = DrumSound.CLAP
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~3 min):
#   Bars  1-8:   Just the 303, alone. Raw.
#   Bars  9-16:  Kick enters. The groove locks.
#   Bars 17-32:  Full beat, filter opening, acid intensifying
#   Bars 33-40:  Breakdown — 303 goes mental, filter wide
#   Bars 41-56:  Peak — everything, filter sweeping wildly
#   Bars 57-64:  Outro — stripped back, 303 alone again
# ═══════════════════════════════════════════════════════════════════

# ── THE 303 — squelchy saw, high resonance, the whole point ─────
acid = score.part("303", synth="saw", envelope="pluck", volume=0.5,
                  lowpass=800, lowpass_q=4.0,
                  distortion=0.4, distortion_drive=5.0,
                  saturation=0.3, humanize=0.03,
                  legato=True, glide=0.04, sub_osc=0.5)
# The filter sweep — slow open across the whole track
acid.lfo("lowpass", rate=0.015, min=400, max=8000, bars=64, shape="triangle")

# The pattern — classic acid: 16th notes with slides and accents
# Mostly root and fifth with chromatic approach notes
acid_bars = [
    # Pattern A: driving root
    [(A.add(-24), 100), (None, 0), (A.add(-24), 90), (E.add(-24), 85),
     (A.add(-24), 95), (None, 0), (G.add(-36), 80), (A.add(-24), 100),
     (None, 0), (A.add(-24), 88), (None, 0), (E.add(-24), 82),
     (A.add(-24), 95), (G.add(-36), 78), (A.add(-24), 92), (None, 0)],
    # Pattern B: climbing
    [(A.add(-24), 95), (B.add(-24), 85), (C.add(-12), 90), (None, 0),
     (E.add(-12), 100), (None, 0), (C.add(-12), 88), (A.add(-24), 82),
     (None, 0), (G.add(-36), 78), (A.add(-24), 95), (None, 0),
     (C.add(-12), 92), (E.add(-12), 98), (C.add(-12), 85), (A.add(-24), 90)],
    # Pattern C: menacing
    [(A.add(-24), 100), (None, 0), (None, 0), (A.add(-24), 105),
     (Tone.from_string("Ab1"), 90), (A.add(-24), 100), (None, 0), (E.add(-24), 88),
     (None, 0), (None, 0), (A.add(-24), 95), (Tone.from_string("Bb1"), 85),
     (A.add(-24), 100), (None, 0), (G.add(-36), 80), (A.add(-24), 98)],
    # Pattern D: wild — big intervals
    [(A.add(-24), 105), (E.add(-12), 95), (A.add(-24), 100), (None, 0),
     (C.add(-12), 92), (None, 0), (A.add(-24), 98), (E.add(-12), 90),
     (G.add(-36), 85), (A.add(-24), 100), (E.add(-12), 95), (None, 0),
     (C.add(-12), 90), (A.add(-24), 102), (None, 0), (E.add(-12), 95)],
]

# Bars 1-8: just the 303 alone — pattern A and B
for _ in range(2):
    for bar in acid_bars[:2]:
        for note, vel in bar:
            if note is None:
                acid.rest(Duration.SIXTEENTH)
            else:
                acid.add(note, Duration.SIXTEENTH, velocity=vel)

# Bars 9-16: patterns cycle
for bar in acid_bars:
    for note, vel in bar:
        if note is None:
            acid.rest(Duration.SIXTEENTH)
        else:
            acid.add(note, Duration.SIXTEENTH, velocity=vel)
for bar in acid_bars:
    for note, vel in bar:
        if note is None:
            acid.rest(Duration.SIXTEENTH)
        else:
            acid.add(note, Duration.SIXTEENTH, velocity=min(127, vel + 5))

# Bars 17-32: all patterns, louder
for _ in range(4):
    for bar in acid_bars:
        for note, vel in bar:
            if note is None:
                acid.rest(Duration.SIXTEENTH)
            else:
                acid.add(note, Duration.SIXTEENTH, velocity=min(127, vel + 10))

# Bars 33-40: breakdown — 303 goes mental, pattern D repeated
for _ in range(8):
    for note, vel in acid_bars[3]:
        if note is None:
            acid.rest(Duration.SIXTEENTH)
        else:
            acid.add(note, Duration.SIXTEENTH, velocity=min(127, vel + 15))

# Bars 41-56: peak — cycling all patterns at max
for _ in range(4):
    for bar in acid_bars:
        for note, vel in bar:
            if note is None:
                acid.rest(Duration.SIXTEENTH)
            else:
                acid.add(note, Duration.SIXTEENTH, velocity=min(127, vel + 15))

# Bars 57-64: just the 303 again, filtering down
for _ in range(2):
    for bar in acid_bars[:2]:
        for note, vel in bar:
            if note is None:
                acid.rest(Duration.SIXTEENTH)
            else:
                acid.add(note, Duration.SIXTEENTH, velocity=max(40, vel - 20))

# ── KICK — four on the floor, enters bar 9 ─────────────────────
kick = score.part("kick", volume=0.5, humanize=0.03)

for _ in range(8):
    kick.rest(Duration.WHOLE)

for _ in range(48):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=115)

# Bars 57-64: fading
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

# ── HATS — 16th notes, open hat on offbeats, enters bar 17 ─────
hats = score.part("hats", volume=0.25, humanize=0.04)

for _ in range(16):
    hats.rest(Duration.WHOLE)

for _ in range(40):
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=75)
        hats.hit(CH, Duration.SIXTEENTH, velocity=45)
        hats.hit(OH if beat % 2 == 1 else CH, Duration.SIXTEENTH, velocity=60)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)

for bar in range(8):
    vel = max(20, 70 - bar * 6)
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=vel)
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 25))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 15))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(15, vel - 28))

# ── SUB BASS — octave below 303, just the root ─────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.3,
                 lowpass=80)

for _ in range(8):
    sub.rest(Duration.WHOLE)

for _ in range(48):
    sub.add(A.add(-36), Duration.WHOLE, velocity=90)

for bar in range(8):
    sub.add(A.add(-36), Duration.WHOLE, velocity=max(20, 85 - bar * 10))

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
