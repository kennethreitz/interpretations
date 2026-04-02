"""
VOICES — they start as one. Then they multiply.
They come from everywhere. They overlap. They won't stop.
Until they do.
F# minor, 65 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("F#", "minor")
s = key.scale  # F# G# A B C# D E

Fs = s[0]; Gs = s[1]; A  = s[2]; B  = s[3]
Cs = s[4]; D  = s[5]; E  = s[6]

score = Score("4/4", bpm=65)

prog = key.progression("i", "VI", "iv", "v")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (56 bars, ~3:27):
#   Bars  1-8:   One voice — alone, quiet, almost comforting
#   Bars  9-16:  A second voice — from the other side
#   Bars 17-24:  They multiply — three, four, overlapping
#   Bars 25-32:  Overwhelm — voices everywhere, can't think
#   Bars 33-40:  The piano — reality trying to reach you
#   Bars 41-48:  Clearing — voices thin, piano gets louder
#   Bars 49-56:  Silence — just breath. One last whisper. Gone.
# ═══════════════════════════════════════════════════════════════════

# ── VOICE 1 — the first one, left side, "aah" ─────────────────
v1 = score.part("voice_1", instrument="vocal", volume=0.2,
                reverb=0.5, reverb_type="taj_mahal",
                delay=0.15, delay_time=0.923, delay_feedback=0.2,
                pan=-0.4, humanize=0.06)

# Bars 1-8: alone — slow, sustained, almost like a lullaby
v1.add(Fs, Duration.WHOLE, velocity=45, lyric="aah")
v1.rest(Duration.WHOLE)
v1.add(A, Duration.WHOLE, velocity=42, lyric="aah")
v1.rest(Duration.WHOLE)
v1.add(Fs, Duration.HALF, velocity=48, lyric="ooh")
v1.add(E, Duration.HALF, velocity=42, lyric="aah")
v1.rest(Duration.WHOLE)
v1.add(Cs, Duration.WHOLE, velocity=45, lyric="aah")
v1.rest(Duration.WHOLE)

# Bars 9-16: continues, a little more insistent
v1.add(Fs, Duration.HALF, velocity=50, lyric="aah")
v1.add(Gs, Duration.HALF, velocity=48, lyric="eeh")
v1.rest(Duration.WHOLE)
v1.add(A, Duration.HALF, velocity=52, lyric="ooh")
v1.rest(Duration.HALF)
v1.add(Fs, Duration.HALF, velocity=48, lyric="aah")
v1.rest(Duration.HALF)
v1.add(B, Duration.WHOLE, velocity=55, lyric="aah")
v1.add(A, Duration.HALF, velocity=50, lyric="eeh")
v1.add(Fs, Duration.HALF, velocity=48, lyric="aah")
v1.rest(Duration.WHOLE)
v1.rest(Duration.WHOLE)

# Bars 17-24: faster, more fragmented
v1.add(Fs, Duration.QUARTER, velocity=55, lyric="aah")
v1.rest(Duration.QUARTER)
v1.add(A, Duration.QUARTER, velocity=52, lyric="eeh")
v1.rest(Duration.QUARTER)
v1.add(Cs, Duration.QUARTER, velocity=58, lyric="aah")
v1.add(B, Duration.QUARTER, velocity=52, lyric="ooh")
v1.rest(Duration.HALF)
v1.add(Fs, Duration.QUARTER, velocity=55, lyric="aah")
v1.rest(Duration.QUARTER)
v1.rest(Duration.HALF)
v1.add(E, Duration.QUARTER, velocity=58, lyric="eeh")
v1.add(Fs, Duration.QUARTER, velocity=55, lyric="aah")
v1.add(A, Duration.QUARTER, velocity=60, lyric="aah")
v1.rest(Duration.QUARTER)
v1.add(Cs, Duration.HALF, velocity=62, lyric="ooh")
v1.add(B, Duration.QUARTER, velocity=55, lyric="aah")
v1.rest(Duration.QUARTER)
v1.add(Fs, Duration.QUARTER, velocity=58, lyric="eeh")
v1.rest(Duration.DOTTED_HALF)
v1.rest(Duration.WHOLE)

# Bars 25-32: overwhelm — rapid, overlapping
v1.set(volume=0.25)
for _ in range(4):
    v1.add(Fs, Duration.EIGHTH, velocity=62, lyric="aah")
    v1.rest(Duration.EIGHTH)
    v1.add(A, Duration.EIGHTH, velocity=58, lyric="eeh")
    v1.add(Cs, Duration.EIGHTH, velocity=60, lyric="aah")
    v1.rest(Duration.QUARTER)
    v1.add(B, Duration.EIGHTH, velocity=55, lyric="ooh")
    v1.rest(Duration.EIGHTH)
for _ in range(4):
    v1.add(Fs, Duration.QUARTER, velocity=55, lyric="aah")
    v1.add(E, Duration.EIGHTH, velocity=50, lyric="eeh")
    v1.rest(Duration.EIGHTH)
    v1.rest(Duration.HALF)

# Bars 33-48: fading as piano enters
v1.set(volume=0.18)
for vel in [48, 42, 38, 35, 30, 25, 20, 15]:
    v1.add(Fs, Duration.HALF, velocity=vel, lyric="aah")
    v1.rest(Duration.HALF)
for vel in [12, 10, 8, 5, 0, 0, 0, 0]:
    if vel > 0:
        v1.add(Fs, Duration.WHOLE, velocity=vel, lyric="aah")
    else:
        v1.rest(Duration.WHOLE)

# Bars 49-56: gone
for _ in range(8):
    v1.rest(Duration.WHOLE)

# ── VOICE 2 — enters bar 9, right side, "ooh" ────────────────
v2 = score.part("voice_2", instrument="vocal", volume=0.18,
                reverb=0.45, reverb_type="cathedral",
                delay=0.12, delay_time=0.692, delay_feedback=0.18,
                pan=0.35, humanize=0.06)

for _ in range(8):
    v2.rest(Duration.WHOLE)

# Bars 9-16: the second voice — different rhythm, different vowel
v2.rest(Duration.HALF)
v2.add(Cs, Duration.WHOLE, velocity=42, lyric="ooh")
v2.rest(Duration.HALF)
v2.add(B, Duration.HALF, velocity=45, lyric="ooh")
v2.rest(Duration.HALF)
v2.add(A, Duration.WHOLE, velocity=40, lyric="eeh")
v2.rest(Duration.WHOLE)
v2.add(Cs, Duration.HALF, velocity=48, lyric="ooh")
v2.add(D, Duration.HALF, velocity=42, lyric="aah")
v2.rest(Duration.WHOLE)
v2.add(B, Duration.WHOLE, velocity=45, lyric="ooh")
v2.rest(Duration.WHOLE)

# Bars 17-24: more active, clashing with v1
v2.add(A, Duration.QUARTER, velocity=50, lyric="ooh")
v2.add(B, Duration.QUARTER, velocity=48, lyric="ooh")
v2.rest(Duration.HALF)
v2.add(Cs, Duration.HALF, velocity=52, lyric="eeh")
v2.rest(Duration.HALF)
v2.add(D, Duration.QUARTER, velocity=55, lyric="ooh")
v2.rest(Duration.QUARTER)
v2.add(B, Duration.QUARTER, velocity=50, lyric="aah")
v2.add(A, Duration.QUARTER, velocity=48, lyric="ooh")
v2.rest(Duration.WHOLE)
v2.add(Cs, Duration.QUARTER, velocity=55, lyric="eeh")
v2.add(D, Duration.QUARTER, velocity=52, lyric="ooh")
v2.rest(Duration.HALF)
v2.add(E, Duration.HALF, velocity=58, lyric="ooh")
v2.add(Cs, Duration.HALF, velocity=52, lyric="aah")
v2.rest(Duration.WHOLE)

# Bars 25-32: overwhelm
v2.set(volume=0.22)
for _ in range(4):
    v2.rest(Duration.EIGHTH)
    v2.add(Cs, Duration.EIGHTH, velocity=58, lyric="ooh")
    v2.add(D, Duration.EIGHTH, velocity=55, lyric="ooh")
    v2.rest(Duration.EIGHTH)
    v2.add(B, Duration.EIGHTH, velocity=52, lyric="eeh")
    v2.rest(Duration.EIGHTH)
    v2.add(A, Duration.EIGHTH, velocity=55, lyric="ooh")
    v2.rest(Duration.EIGHTH)
for _ in range(4):
    v2.rest(Duration.QUARTER)
    v2.add(Cs, Duration.QUARTER, velocity=50, lyric="ooh")
    v2.add(B, Duration.EIGHTH, velocity=48, lyric="eeh")
    v2.rest(Duration.QUARTER)
    v2.rest(Duration.EIGHTH)

# Bars 33-48: fading
v2.set(volume=0.15)
for vel in [45, 40, 35, 30, 25, 20, 15, 10, 8, 5, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        v2.add(Cs, Duration.HALF, velocity=vel, lyric="ooh")
        v2.rest(Duration.HALF)
    else:
        v2.rest(Duration.WHOLE)

for _ in range(8):
    v2.rest(Duration.WHOLE)

# ── VOICE 3 — enters bar 17, behind you, "eeh" ───────────────
v3 = score.part("voice_3", instrument="choir", volume=0.12,
                reverb=0.6, reverb_type="taj_mahal",
                chorus=0.3, chorus_rate=0.08, chorus_depth=0.01,
                delay=0.1, delay_time=0.462, delay_feedback=0.15,
                pan=-0.15)

for _ in range(16):
    v3.rest(Duration.WHOLE)

# Bars 17-24: chord tones, sustained — like a room humming
for _ in range(2):
    for chord in prog:
        v3.add(chord, Duration.WHOLE, velocity=35)

# Bars 25-32: louder, pressing in
v3.set(volume=0.18)
for _ in range(2):
    for chord in prog:
        v3.add(chord, Duration.WHOLE, velocity=45)

# Bars 33-48: fading
for vel in [40, 35, 30, 25, 20, 15, 12, 8, 5, 0, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        v3.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        v3.rest(Duration.WHOLE)

for _ in range(8):
    v3.rest(Duration.WHOLE)

# ── VOICE 4 — enters bar 21, whispers, everywhere ────────────
v4 = score.part("voice_4", instrument="vocal", volume=0.1,
                reverb=0.35,
                delay=0.2, delay_time=0.346, delay_feedback=0.25,
                pan=0.45, humanize=0.04)

for _ in range(20):
    v4.rest(Duration.WHOLE)

# Bars 21-32: whispered fragments — fast, ghostly
whispers = [
    (Fs.add(12), Duration.EIGHTH, 35, "eeh"),
    (None, Duration.QUARTER, 0, ""),
    (A.add(12), Duration.EIGHTH, 30, "aah"),
    (None, Duration.HALF, 0, ""),
    (Cs.add(12), Duration.EIGHTH, 38, "eeh"),
    (None, Duration.EIGHTH, 0, ""),
    (B, Duration.QUARTER, 32, "ooh"),
    (None, Duration.QUARTER, 0, ""),
    (None, Duration.HALF, 0, ""),
    (E.add(12), Duration.EIGHTH, 35, "eeh"),
    (None, Duration.DOTTED_QUARTER, 0, ""),
    (Fs.add(12), Duration.EIGHTH, 38, "aah"),
    (None, Duration.QUARTER, 0, ""),
    (None, Duration.HALF, 0, ""),
    (D.add(12), Duration.EIGHTH, 32, "ooh"),
    (None, Duration.DOTTED_QUARTER, 0, ""),
]
for _ in range(3):
    for note, dur, vel, lyric in whispers:
        if note is None:
            v4.rest(dur)
        else:
            v4.add(note, dur, velocity=vel, lyric=lyric)

# Bars 33-56: gone
for _ in range(24):
    v4.rest(Duration.WHOLE)

# ── VOICE 5 — enters bar 25, the loudest, most insistent ─────
v5 = score.part("voice_5", instrument="vocal", volume=0.15,
                reverb=0.3, reverb_decay=1.0,
                delay=0.08, delay_time=0.231, delay_feedback=0.12,
                pan=-0.3)

for _ in range(24):
    v5.rest(Duration.WHOLE)

# Bars 25-32: demanding, repetitive — the one you can't ignore
for _ in range(8):
    v5.add(Fs, Duration.QUARTER, velocity=55, lyric="aah")
    v5.add(Fs, Duration.EIGHTH, velocity=48, lyric="aah")
    v5.rest(Duration.EIGHTH)
    v5.add(Fs, Duration.QUARTER, velocity=52, lyric="aah")
    v5.rest(Duration.QUARTER)

# Bars 33-40: fading
for vel in [48, 42, 35, 28, 22, 15, 10, 5]:
    v5.add(Fs, Duration.QUARTER, velocity=vel, lyric="aah")
    v5.rest(Duration.DOTTED_HALF)

# Bars 41-56: gone
for _ in range(16):
    v5.rest(Duration.WHOLE)

# ── PIANO — reality, bars 33 onward ───────────────────────────
# The thing that's real. Cuts through the voices.
piano = score.part("piano", instrument="piano", volume=0.45,
                   reverb=0.35, reverb_type="taj_mahal",
                   delay=0.2, delay_time=0.346, delay_feedback=0.3,
                   pan=0.1, humanize=0.1)

for _ in range(32):
    piano.rest(Duration.WHOLE)

# Bars 33-36: trying to reach you — single notes, tentative
piano.add(Fs, Duration.QUARTER, velocity=55)
piano.rest(Duration.DOTTED_HALF)
piano.rest(Duration.WHOLE)
piano.add(A, Duration.QUARTER, velocity=52)
piano.rest(Duration.QUARTER)
piano.add(Fs, Duration.QUARTER, velocity=48)
piano.rest(Duration.QUARTER)
piano.rest(Duration.WHOLE)

# Bars 37-40: getting through — a melody forms
piano.add(Fs, Duration.QUARTER, velocity=60)
piano.add(A, Duration.QUARTER, velocity=55)
piano.add(B, Duration.HALF, velocity=62)
piano.add(Cs, Duration.QUARTER, velocity=58)
piano.add(B, Duration.EIGHTH, velocity=52)
piano.add(A, Duration.EIGHTH, velocity=50)
piano.add(Fs, Duration.HALF, velocity=55)
piano.rest(Duration.QUARTER)
piano.add(E, Duration.QUARTER, velocity=52)
piano.add(Fs, Duration.QUARTER, velocity=58)
piano.add(A, Duration.QUARTER, velocity=55)
piano.add(B, Duration.WHOLE, velocity=62)

# Bars 41-48: the melody is real — you can hold onto it
piano.set(volume=0.55)
piano.add(Fs, Duration.QUARTER, velocity=68)
piano.add(A, Duration.QUARTER, velocity=62)
piano.add(Cs.add(12), Duration.HALF, velocity=72)
piano.add(B, Duration.QUARTER, velocity=65)
piano.add(A, Duration.EIGHTH, velocity=58)
piano.add(Gs, Duration.EIGHTH, velocity=55)
piano.add(Fs, Duration.HALF, velocity=62)
piano.rest(Duration.QUARTER)
piano.add(E, Duration.QUARTER, velocity=58)
piano.add(Fs, Duration.QUARTER, velocity=65)
piano.add(A, Duration.QUARTER, velocity=62)
piano.add(B, Duration.HALF, velocity=68)
piano.add(A, Duration.HALF, velocity=62)
piano.add(Fs, Duration.QUARTER, velocity=60)
piano.add(E, Duration.QUARTER, velocity=55)
piano.add(D, Duration.QUARTER, velocity=52)
piano.add(Fs, Duration.QUARTER, velocity=58)
piano.add(Fs, Duration.WHOLE, velocity=65)
piano.rest(Duration.WHOLE)

# Bars 49-56: silence — just breath
piano.add(Fs, Duration.WHOLE, velocity=50)
piano.rest(Duration.WHOLE)
piano.rest(Duration.WHOLE)
piano.add(Fs.add(-12), Duration.HALF, velocity=42)
piano.rest(Duration.HALF)
piano.rest(Duration.WHOLE)
piano.rest(Duration.WHOLE)
piano.rest(Duration.WHOLE)
piano.rest(Duration.WHOLE)

# ── SINGING BOWL — marks the silence ───────────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.25,
                  reverb=0.7, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.923, delay_feedback=0.2,
                  pan=-0.1)

for _ in range(48):
    bowl.rest(Duration.WHOLE)

# Bar 49: the silence arrives — one bowl strike
bowl.add(Fs.add(-24), Duration.WHOLE, velocity=55)
for _ in range(7):
    bowl.rest(Duration.WHOLE)

# ── LAST WHISPER — one final voice, bar 55, barely there ───────
last = score.part("last_whisper", instrument="vocal", volume=0.06,
                  reverb=0.6, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.923, delay_feedback=0.2,
                  pan=0.4)

for _ in range(54):
    last.rest(Duration.WHOLE)

# Bar 55: one syllable. Then nothing.
last.add(Fs, Duration.HALF, velocity=25, lyric="aah")
last.rest(Duration.HALF)
last.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 65")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing VOICES (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing VOICES...")
    play_score(score)
