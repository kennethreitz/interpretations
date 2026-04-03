"""
CATHEDRAL — ancient stone, heavy air.
Bagpipe drone, timpani thunder, mellotron choir, tubular bells.
The sound of a building that has stood for a thousand years.
D minor, 60 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("D", "minor")
s = key.scale  # D E F G A Bb C

D  = s[0]; E  = s[1]; F  = s[2]; G  = s[3]
A  = s[4]; Bb = s[5]; C  = s[6]

score = Score("4/4", bpm=60)

prog = key.progression("i", "iv", "VII", "i")
prog2 = key.progression("i", "VI", "iv", "V")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~4:16):
#   Bars  1-8:   Tubular bells alone — echoing in empty stone
#   Bars  9-16:  Bagpipe drone — the ancient breath
#   Bars 17-24:  Mellotron choir enters — voices from the walls
#   Bars 25-32:  Timpani — the heartbeat of the building
#   Bars 33-40:  Pipe organ — the full weight of God
#   Bars 41-48:  All together — the cathedral sings
#   Bars 49-56:  Mellotron choir solo — the most human moment
#   Bars 57-64:  Bells alone again — the echo outlasts us all
# ═══════════════════════════════════════════════════════════════════

# ── TUBULAR BELLS — the space itself ──────────────────────────
bells = score.part("bells", instrument="tubular_bells", volume=0.4,
                   reverb=0.85, reverb_type="taj_mahal",
                   delay=0.3, delay_time=1.0, delay_feedback=0.35,
                   pan=0.15)

# Bars 1-8: alone — one strike, let it ring, another
bells.add(D.add(-12), Duration.WHOLE, velocity=65)
bells.rest(Duration.WHOLE)
bells.rest(Duration.WHOLE)
bells.add(A.add(-12), Duration.WHOLE, velocity=58)
bells.rest(Duration.WHOLE)
bells.rest(Duration.WHOLE)
bells.add(D.add(-12), Duration.WHOLE, velocity=62)
bells.rest(Duration.WHOLE)

# Bars 9-56: every 4 bars
for section in range(12):
    vel = max(30, 60 - section * 2)
    bells.add(D.add(-12), Duration.WHOLE, velocity=vel)
    bells.rest(Duration.WHOLE)
    bells.rest(Duration.WHOLE)
    bells.rest(Duration.WHOLE)

# Bars 57-64: alone again — the ending mirrors the beginning
bells.add(D.add(-12), Duration.WHOLE, velocity=58)
bells.rest(Duration.WHOLE)
bells.rest(Duration.WHOLE)
bells.add(A.add(-12), Duration.WHOLE, velocity=50)
bells.rest(Duration.WHOLE)
bells.rest(Duration.WHOLE)
bells.add(D.add(-12), Duration.WHOLE, velocity=42)
bells.rest(Duration.WHOLE)

# ── BAGPIPE — the ancient drone, enters bar 9 ────────────────
bagpipe = score.part("bagpipe", instrument="bagpipe", volume=0.2,
                     reverb=0.45, reverb_type="cathedral",
                     chorus=0.15, chorus_rate=0.08, chorus_depth=0.008,
                     pan=-0.2, humanize=0.06)

for _ in range(8):
    bagpipe.rest(Duration.WHOLE)

# Bars 9-16: drone enters — D and A, the ancient fifth
for vel in [25, 32, 38, 42, 45, 45, 42, 40]:
    bagpipe.add(D.add(-12), Duration.HALF, velocity=vel)
    bagpipe.add(A.add(-12), Duration.HALF, velocity=max(15, vel - 8))

# Bars 17-40: melody emerges from the drone
bagpipe_melody = [
    (D, Duration.HALF, 52), (E, Duration.QUARTER, 48),
    (F, Duration.QUARTER, 50),
    (G, Duration.HALF, 55), (F, Duration.QUARTER, 48),
    (E, Duration.QUARTER, 45),
    (D, Duration.WHOLE, 52),
    (None, Duration.HALF, 0), (A.add(-12), Duration.HALF, 48),
]
for _ in range(6):
    for note, dur, vel in bagpipe_melody:
        if note is None:
            bagpipe.rest(dur)
        else:
            bagpipe.add(note, dur, velocity=vel)

# Bars 41-48: full power — drone + melody together
bagpipe.set(volume=0.25)
for _ in range(2):
    for note, dur, vel in bagpipe_melody:
        if note is None:
            bagpipe.rest(dur)
        else:
            bagpipe.add(note, dur, velocity=min(70, vel + 8))

# Bars 49-56: drops to drone — choir takes over
bagpipe.set(volume=0.15)
for _ in range(8):
    bagpipe.add(D.add(-12), Duration.HALF, velocity=38)
    bagpipe.add(A.add(-12), Duration.HALF, velocity=30)

# Bars 57-64: fading
for vel in [32, 28, 22, 18, 14, 10, 5, 0]:
    if vel > 0:
        bagpipe.add(D.add(-12), Duration.WHOLE, velocity=vel)
    else:
        bagpipe.rest(Duration.WHOLE)

# ── MELLOTRON CHOIR — voices from the stone, enters bar 17 ────
choir = score.part("choir", instrument="mellotron_choir", volume=0.2,
                   reverb=0.55, reverb_type="cathedral",
                   chorus=0.2, chorus_rate=0.06, chorus_depth=0.01,
                   pan=0.1, humanize=0.08)

for _ in range(16):
    choir.rest(Duration.WHOLE)

# Bars 17-24: slow chords — the walls start singing
for _ in range(2):
    for chord in prog:
        choir.add(chord, Duration.WHOLE, velocity=40)

# Bars 25-40: fuller
for _ in range(4):
    for chord in prog:
        choir.add(chord, Duration.WHOLE, velocity=48)

# Bars 41-48: peak — full voice
choir.set(volume=0.28)
for _ in range(2):
    for chord in prog2:
        choir.add(chord, Duration.WHOLE, velocity=58)

# Bars 49-56: SOLO — the most human moment
choir.set(volume=0.32)
choir_melody = [
    (A, Duration.HALF, 62), (Bb, Duration.QUARTER, 58),
    (A, Duration.QUARTER, 55),
    (G, Duration.HALF, 60), (F, Duration.QUARTER, 55),
    (E, Duration.QUARTER, 52),
    (F, Duration.DOTTED_HALF, 62), (E, Duration.QUARTER, 55),
    (D, Duration.WHOLE, 58),
    (F, Duration.QUARTER, 60), (G, Duration.QUARTER, 58),
    (A, Duration.HALF, 65),
    (Bb, Duration.QUARTER, 60), (A, Duration.QUARTER, 58),
    (G, Duration.HALF, 55),
    (F, Duration.HALF, 52), (E, Duration.HALF, 55),
    (D, Duration.WHOLE, 58),
]
for note, dur, vel in choir_melody:
    choir.add(note, dur, velocity=vel)

# Bars 57-64: fading — the voices retreat into stone
for vel in [48, 42, 35, 28, 22, 15, 10, 0]:
    if vel > 0:
        choir.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        choir.rest(Duration.WHOLE)

# ── TIMPANI — thunder, enters bar 25 ──────────────────────────
timp = score.part("timpani", instrument="timpani", volume=0.5,
                  reverb=0.4, reverb_type="cathedral",
                  delay=0.08, delay_time=0.5, delay_feedback=0.1,
                  pan=-0.1, humanize=0.06)

for _ in range(24):
    timp.rest(Duration.WHOLE)

# Bars 25-32: sparse, heavy — like thunder in stone
timp.add(D.add(-12), Duration.WHOLE, velocity=75)
timp.rest(Duration.WHOLE)
timp.rest(Duration.WHOLE)
timp.add(A.add(-24), Duration.WHOLE, velocity=68)
timp.rest(Duration.WHOLE)
timp.add(D.add(-12), Duration.HALF, velocity=72)
timp.add(D.add(-12), Duration.HALF, velocity=65)
timp.rest(Duration.WHOLE)
timp.add(D.add(-12), Duration.WHOLE, velocity=78)

# Bars 33-40: more active — rolls
for bar in range(8):
    if bar % 4 == 3:
        # Timpani roll — 16th notes crescendo
        for i in range(16):
            timp.add(D.add(-12), Duration.SIXTEENTH, velocity=min(95, 50 + i * 3))
    else:
        timp.add(D.add(-12), Duration.QUARTER, velocity=72)
        timp.rest(Duration.DOTTED_HALF)

# Bars 41-48: peak — full rolls + accents
for bar in range(8):
    if bar % 2 == 1:
        for i in range(16):
            timp.add(D.add(-12), Duration.SIXTEENTH, velocity=min(100, 55 + i * 3))
    else:
        timp.add(D.add(-12), Duration.HALF, velocity=80)
        timp.rest(Duration.QUARTER)
        timp.add(A.add(-24), Duration.QUARTER, velocity=72)

# Bars 49-56: sparse again — under choir solo
for _ in range(4):
    timp.add(D.add(-12), Duration.WHOLE, velocity=55)
    timp.rest(Duration.WHOLE)

# Bars 57-64: fading
for vel in [48, 40, 32, 25, 0, 0, 0, 0]:
    if vel > 0:
        timp.add(D.add(-12), Duration.WHOLE, velocity=vel)
    else:
        timp.rest(Duration.WHOLE)

# ── KICK — the deepest thunder, enters bar 25 ─────────────────
K = DrumSound.KICK
kick = score.part("kick", volume=0.7, humanize=0.03,
                  reverb=0.3, reverb_type="cathedral",
                  distortion=0.1, distortion_drive=2.0)

for _ in range(24):
    kick.rest(Duration.WHOLE)

# Bars 25-32: one hit per bar — synced with timpani
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=95)
    kick.rest(Duration.DOTTED_HALF)

# Bars 33-48: two hits per bar — heartbeat under the organ
for _ in range(16):
    kick.hit(K, Duration.QUARTER, velocity=100)
    kick.rest(Duration.QUARTER)
    kick.hit(K, Duration.QUARTER, velocity=85)
    kick.rest(Duration.QUARTER)

# Bars 49-56: sparse — under choir solo
for _ in range(8):
    kick.hit(K, Duration.HALF, velocity=80)
    kick.rest(Duration.HALF)

# Bars 57-64: fading
for vel in [72, 60, 48, 35, 22, 0, 0, 0]:
    if vel > 0:
        kick.hit(K, Duration.QUARTER, velocity=vel)
        kick.rest(Duration.DOTTED_HALF)
    else:
        kick.rest(Duration.WHOLE)

# ── PIPE ORGAN — the full weight, enters bar 33 ──────────────
organ = score.part("organ", instrument="pipe_organ", volume=0.2,
                   reverb=0.5, reverb_type="cathedral",
                   chorus=0.1, chorus_rate=0.1, chorus_depth=0.005,
                   pan=0.05)

for _ in range(32):
    organ.rest(Duration.WHOLE)

# Bars 33-48: hymn chords — the weight of the building
for _ in range(4):
    for chord in prog:
        organ.add(chord, Duration.WHOLE, velocity=48)

# Bars 49-56: sustains under choir solo
organ.set(volume=0.15)
for _ in range(2):
    for chord in prog:
        organ.add(chord, Duration.WHOLE, velocity=38)

# Bars 57-64: fading
for vel in [35, 30, 25, 20, 15, 10, 5, 0]:
    if vel > 0:
        organ.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        organ.rest(Duration.WHOLE)

# ── MELLOTRON STRINGS — bed, enters bar 33 ────────────────────
strings = score.part("strings", instrument="mellotron_strings", volume=0.12,
                     reverb=0.45, reverb_type="cathedral",
                     pan=-0.15)

for _ in range(32):
    strings.rest(Duration.WHOLE)

# Bars 33-56: tape strings — the warmth
for _ in range(6):
    for chord in prog:
        strings.add(chord, Duration.WHOLE, velocity=42)

# Bars 57-64: fading
for vel in [35, 28, 22, 18, 12, 8, 0, 0]:
    if vel > 0:
        strings.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        strings.rest(Duration.WHOLE)

# ── SUB — the stone floor vibrating ──────────────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.3,
                 lowpass=100, sub_osc=0.3)

for _ in range(24):
    sub.rest(Duration.WHOLE)

for _ in range(32):
    sub.add(D.add(-36), Duration.WHOLE, velocity=40)

for vel in [35, 28, 22, 15, 10, 5, 0, 0]:
    if vel > 0:
        sub.add(D.add(-36), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 60")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing CATHEDRAL (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing CATHEDRAL...")
    play_score(score)
