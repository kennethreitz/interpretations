"""
ACID REIGN — two 303s fighting each other through a wall of resonance.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("A", "minor")

# Bass range notes
A  = Tone.from_string("A2")
Bb = Tone.from_string("Bb2")
C  = Tone.from_string("C3")
D  = Tone.from_string("D3")
E  = Tone.from_string("E3")
F  = Tone.from_string("F3")
G  = Tone.from_string("G2")
A1 = Tone.from_string("A1")  # sub octave

score = Score("4/4", bpm=140)

K  = DrumSound.KICK
CL = DrumSound.CLAP
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

# ── 303 MAIN — the lead voice ──────────────────────────────────
acid = score.part("303", synth="saw", volume=0.6,
                  lowpass=600, lowpass_q=10.0,
                  distortion=0.35, distortion_drive=4.0,
                  saturation=0.8, legato=True, glide=0.05,
                  sub_osc=0.6, sidechain=0.3)
# Filter sweeps UP across the track — the whole point of acid
acid.lfo("lowpass", rate=0.01, min=300, max=10000, bars=64, shape="saw")
# Resonance also sweeps
acid.lfo("lowpass_q", rate=0.02, min=5.0, max=18.0, bars=32, shape="triangle")

# ── 303 SUB — dirty double, octave down, more distortion ───────
acid2 = score.part("303_sub", synth="square", volume=0.35,
                   lowpass=400, lowpass_q=3.0,
                   distortion=0.5, distortion_drive=6.0,
                   saturation=0.8, legato=True, glide=0.08,
                   pan=0.15)
acid2.lfo("lowpass", rate=0.015, min=200, max=4000, bars=64, shape="triangle")

# 16th note patterns — the groove comes from accent + rest placement
# _ = rest, lowercase = soft, UPPERCASE = hard accent
#
# Real acid: every note that ISN'T a rest or accent matters just as much
# The pattern creates tension by where it DOESN'T play

def acid_bar(part, notes, sub_part=None, sub_offset=-12):
    """Write one bar of 16th notes. None = rest."""
    for note, vel in notes:
        if note is None:
            part.rest(Duration.SIXTEENTH)
            if sub_part:
                sub_part.rest(Duration.SIXTEENTH)
        else:
            part.add(note, Duration.SIXTEENTH, velocity=vel)
            if sub_part:
                sub_part.add(note.add(sub_offset), Duration.SIXTEENTH,
                           velocity=max(30, vel - 20))

# ── THE PATTERNS ────────────────────────────────────────────────
# Each is 16 steps (one bar of 16ths at 140 BPM)

# P1: the hook — simple, driving, root-heavy
P1 = [(A, 110), (None, 0), (A, 75), (None, 0),
      (A, 105), (E, 80), (None, 0), (A, 110),
      (None, 0), (None, 0), (A, 85), (E, 90),
      (A, 108), (None, 0), (G, 78), (A, 112)]

# P2: the answer — climbing, chromatic tension
P2 = [(A, 105), (Bb, 82), (C, 90), (C, 75),
      (D, 95), (None, 0), (C, 80), (A, 100),
      (None, 0), (Bb, 78), (A, 105), (None, 0),
      (G, 85), (A, 110), (None, 0), (None, 0)]

# P3: the freak — wide intervals, unexpected
P3 = [(E, 110), (None, 0), (A, 90), (None, 0),
      (None, 0), (E, 105), (F, 82), (E, 100),
      (A, 112), (None, 0), (None, 0), (None, 0),
      (D, 95), (C, 85), (A, 108), (E, 90)]

# P4: the build — relentless, fewer rests
P4 = [(A, 108), (E, 85), (A, 100), (C, 90),
      (A, 105), (None, 0), (E, 88), (A, 110),
      (G, 82), (A, 108), (C, 92), (E, 95),
      (A, 112), (G, 80), (A, 105), (None, 0)]

# P5: the drop — ALL notes, maximum intensity
P5 = [(A, 115), (Bb, 90), (A, 108), (E, 95),
      (A, 112), (C, 88), (D, 92), (A, 110),
      (E, 98), (F, 85), (E, 105), (A, 115),
      (G, 90), (A, 112), (Bb, 88), (A, 118)]

# ═══════════════════════════════════════════════════════════════════
# ARRANGEMENT — builds intensity through pattern selection
# ═══════════════════════════════════════════════════════════════════

# Bars 1-8: 303 alone — P1 and P2 alternating, sparse
for _ in range(4):
    acid_bar(acid, P1, acid2)
    acid_bar(acid, P2, acid2)

# Bars 9-16: kick enters, still P1/P2
for _ in range(4):
    acid_bar(acid, P1, acid2)
    acid_bar(acid, P2, acid2)

# Bars 17-24: P3 enters — gets weird
for _ in range(2):
    acid_bar(acid, P1, acid2)
    acid_bar(acid, P3, acid2)
    acid_bar(acid, P2, acid2)
    acid_bar(acid, P3, acid2)

# Bars 25-32: P4 takes over — relentless build
for _ in range(4):
    acid_bar(acid, P4, acid2)
    acid_bar(acid, P4, acid2)

# Bars 33-40: BREAKDOWN — sustained notes, filter screaming
for _ in range(2):
    acid.add(A, Duration.WHOLE, velocity=95)
    acid2.add(A1, Duration.WHOLE, velocity=80)
    acid.add(E, Duration.WHOLE, velocity=90)
    acid2.add(Tone.from_string("E1"), Duration.WHOLE, velocity=75)
    acid.add(C, Duration.WHOLE, velocity=88)
    acid2.add(Tone.from_string("C2"), Duration.WHOLE, velocity=78)
    acid.add(A, Duration.WHOLE, velocity=95)
    acid2.add(A1, Duration.WHOLE, velocity=82)

# Bars 41-56: THE DROP — P5 (maximum intensity) cycling with P1
for _ in range(4):
    acid_bar(acid, P5, acid2)
    acid_bar(acid, P1, acid2)
    acid_bar(acid, P5, acid2)
    acid_bar(acid, P3, acid2)

# Bars 57-64: outro — back to P1 alone, filtering down
for _ in range(4):
    acid_bar(acid, P1, acid2)
    acid_bar(acid, P1, acid2)

# ── KICK — enters bar 9 ────────────────────────────────────────
kick = score.part("kick", volume=0.7, humanize=0.03)

for _ in range(8):
    kick.rest(Duration.WHOLE)
for _ in range(48):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=118)
for bar in range(8):
    vel = max(30, 115 - bar * 10)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# ── CLAP — 2 and 4 ─────────────────────────────────────────────
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

# ── HATS — 16ths, enters bar 9 ─────────────────────────────────
hats = score.part("hats", volume=0.22, humanize=0.04, sidechain=0.15)

for _ in range(8):
    hats.rest(Duration.WHOLE)
for _ in range(48):
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=72)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)
        hats.hit(OH if beat % 2 == 1 else CH, Duration.SIXTEENTH, velocity=58)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
for bar in range(8):
    vel = max(18, 65 - bar * 6)
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=vel)
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(12, vel - 28))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(12, vel - 15))
        hats.hit(CH, Duration.SIXTEENTH, velocity=max(12, vel - 30))

# ── TABLA — enters halfway, fusion moment ───────────────────────
TNA = DrumSound.TABLA_NA
TIT = DrumSound.TABLA_TIT
TGE = DrumSound.TABLA_GE
TDHA = DrumSound.TABLA_DHA
TKE = DrumSound.TABLA_KE
TGEB = DrumSound.TABLA_GE_BEND

tabla = score.part("tabla", volume=0.3, reverb=0.25, reverb_decay=1.0,
                   humanize=0.06)

# Bars 1-32: silent
for _ in range(32):
    tabla.rest(Duration.WHOLE)

# Bars 33-56: keherwa groove with fills
for bar in range(24):
    if bar % 8 == 7:
        # Fill with bayan bends
        tabla.hit(TDHA, Duration.EIGHTH, velocity=95, articulation="accent")
        tabla.hit(TGEB, Duration.EIGHTH, velocity=110)
        tabla.hit(TNA, Duration.EIGHTH, velocity=75)
        tabla.hit(TGEB, Duration.EIGHTH, velocity=105)
        tabla.hit(TDHA, Duration.EIGHTH, velocity=90, articulation="accent")
        tabla.hit(TNA, Duration.SIXTEENTH, velocity=65)
        tabla.hit(TKE, Duration.SIXTEENTH, velocity=55)
        tabla.hit(TGEB, Duration.QUARTER, velocity=115)
    else:
        tabla.hit(TDHA, Duration.EIGHTH, velocity=88, articulation="accent")
        tabla.hit(TGE, Duration.EIGHTH, velocity=58)
        tabla.hit(TNA, Duration.EIGHTH, velocity=68)
        tabla.hit(TIT, Duration.EIGHTH, velocity=42)
        tabla.hit(TNA, Duration.EIGHTH, velocity=62)
        tabla.hit(TIT, Duration.EIGHTH, velocity=40)
        tabla.hit(TDHA, Duration.EIGHTH, velocity=82, articulation="accent")
        tabla.hit(TNA, Duration.EIGHTH, velocity=60)

# Bars 57-64: fading
for bar in range(8):
    vel = max(25, 80 - bar * 7)
    tabla.hit(TDHA, Duration.EIGHTH, velocity=vel)
    tabla.hit(TGE, Duration.EIGHTH, velocity=max(20, vel - 25))
    tabla.hit(TNA, Duration.EIGHTH, velocity=max(20, vel - 15))
    tabla.hit(TIT, Duration.EIGHTH, velocity=max(15, vel - 35))
    tabla.hit(TNA, Duration.EIGHTH, velocity=max(20, vel - 20))
    tabla.hit(TIT, Duration.EIGHTH, velocity=max(15, vel - 38))
    tabla.hit(TDHA, Duration.EIGHTH, velocity=max(20, vel - 5))
    tabla.hit(TNA, Duration.EIGHTH, velocity=max(20, vel - 22))

# ── 808 SUB — deep sine, follows the root ───────────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=0.8,
                 lowpass=150, distortion=0.35, distortion_drive=4.0,
                 saturation=0.6, sub_osc=0.7, sidechain=0.3)

for _ in range(8):
    sub.rest(Duration.WHOLE)
for _ in range(48):
    sub.add(A1, Duration.HALF, velocity=95)
    sub.rest(Duration.HALF)
for bar in range(8):
    vel = max(20, 85 - bar * 10)
    sub.add(A1, Duration.HALF, velocity=vel)
    sub.rest(Duration.HALF)

# ── RHODES — dark chords in the background ──────────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.2,
                    reverb=0.7, reverb_type="taj_mahal",
                    tremolo_depth=0.15, tremolo_rate=3.0,
                    sidechain=0.35, humanize=0.08)

prog = [c.transpose(-12) for c in key.progression("i", "VII", "VI", "v")]

for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# Bars 9-56: slow chord changes, atmospheric, octave down
for _ in range(12):
    for chord in prog:
        rhodes.add(chord, Duration.WHOLE, velocity=55)

for bar in range(8):
    rhodes.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 140")
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
