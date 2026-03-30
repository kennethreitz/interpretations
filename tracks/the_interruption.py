"""
THE INTERRUPTION — a string quartet gets ambushed by drum & bass.
Classical beauty. Then at bar 33 the breakbeat hits and the strings
just... keep playing. Like a concert in a warehouse.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("D", "minor")
s = key.scale
prog = key.progression("i", "VI", "iv", "V")
prog2 = key.progression("i", "VII", "III", "iv")

D  = s[0]; E  = s[1]; F  = s[2]; G  = s[3]
A  = s[4]; Bb = s[5]; C  = s[6]

score = Score("4/4", bpm=85)

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (80 bars):
#   Bars  1-32:  String quartet — pure classical, no hint of what's coming
#   Bar  33:     THE INTERRUPTION — DnB breakbeat slams in at 170 BPM feel
#   Bars 33-64:  Strings + DnB coexisting, sub bass, the collision
#   Bars 65-80:  Strings win — beat dissolves, quartet plays out
# ═══════════════════════════════════════════════════════════════════

# ── VIOLIN 1 — melody, the lead voice ──────────────────────────
violin1 = score.part("violin_1", instrument="violin", volume=0.35,
                     reverb=0.4, reverb_type="cathedral",
                     humanize=0.1)

# Bars 1-16: opening melody — lyrical, romantic
melody_a = [
    (A, Duration.HALF, 80), (Bb, Duration.QUARTER, 72),
    (A, Duration.QUARTER, 75),
    (G, Duration.HALF, 78), (F, Duration.QUARTER, 70),
    (E, Duration.QUARTER, 68),
    (F, Duration.DOTTED_HALF, 82), (E, Duration.QUARTER, 72),
    (D, Duration.WHOLE, 78),
]
melody_b = [
    (D.add(12), Duration.HALF, 85), (C.add(12), Duration.QUARTER, 78),
    (Bb, Duration.QUARTER, 75),
    (A, Duration.HALF, 80), (G, Duration.QUARTER, 72),
    (F, Duration.QUARTER, 70),
    (G, Duration.HALF, 78), (A, Duration.QUARTER, 75),
    (Bb, Duration.QUARTER, 72),
    (A, Duration.WHOLE, 82),
]
for _ in range(2):
    for note, dur, vel in melody_a:
        violin1.add(note, dur, velocity=vel)
    for note, dur, vel in melody_b:
        violin1.add(note, dur, velocity=vel)

# Bars 17-32: development — higher, more intense
melody_c = [
    (D.add(12), Duration.QUARTER, 88), (E.add(12), Duration.QUARTER, 82),
    (F.add(12), Duration.HALF, 90),
    (E.add(12), Duration.QUARTER, 82), (D.add(12), Duration.QUARTER, 78),
    (C.add(12), Duration.QUARTER, 80), (Bb, Duration.QUARTER, 75),
    (A, Duration.HALF, 85), (G, Duration.QUARTER, 78),
    (A, Duration.QUARTER, 80),
    (D.add(12), Duration.WHOLE, 88),
]
for _ in range(2):
    for note, dur, vel in melody_c:
        violin1.add(note, dur, velocity=vel)
    for note, dur, vel in melody_a:
        violin1.add(note, dur, velocity=vel)

# Bars 33-64: THE INTERRUPTION — strings keep playing, unshaken
for _ in range(4):
    for note, dur, vel in melody_b:
        violin1.add(note, dur, velocity=min(127, vel + 10))
    for note, dur, vel in melody_c:
        violin1.add(note, dur, velocity=min(127, vel + 10))

# Bars 65-80: strings take over again, softer
for _ in range(2):
    for note, dur, vel in melody_a:
        violin1.add(note, dur, velocity=max(40, vel - 10))
    for note, dur, vel in melody_b:
        violin1.add(note, dur, velocity=max(40, vel - 15))

# ── VIOLIN 2 — harmony, follows violin 1 a third below ─────────
violin2 = score.part("violin_2", instrument="violin", volume=0.3,
                     reverb=0.4, reverb_type="cathedral",
                     pan=0.2, humanize=0.1)

# Bars 1-16: harmony part
harm_a = [
    (F, Duration.HALF, 72), (G, Duration.QUARTER, 65),
    (F, Duration.QUARTER, 68),
    (E, Duration.HALF, 70), (D, Duration.QUARTER, 62),
    (C, Duration.QUARTER, 60),
    (D, Duration.DOTTED_HALF, 75), (C, Duration.QUARTER, 65),
    (D, Duration.WHOLE, 70),
]
harm_b = [
    (Bb, Duration.HALF, 78), (A, Duration.QUARTER, 70),
    (G, Duration.QUARTER, 68),
    (F, Duration.HALF, 72), (E, Duration.QUARTER, 65),
    (D, Duration.QUARTER, 62),
    (E, Duration.HALF, 70), (F, Duration.QUARTER, 68),
    (G, Duration.QUARTER, 65),
    (F, Duration.WHOLE, 75),
]
for _ in range(2):
    for note, dur, vel in harm_a:
        violin2.add(note, dur, velocity=vel)
    for note, dur, vel in harm_b:
        violin2.add(note, dur, velocity=vel)

# Bars 17-32
for _ in range(4):
    for note, dur, vel in harm_b:
        violin2.add(note, dur, velocity=vel)

# Bars 33-64
for _ in range(4):
    for note, dur, vel in harm_a:
        violin2.add(note, dur, velocity=min(127, vel + 8))
    for note, dur, vel in harm_b:
        violin2.add(note, dur, velocity=min(127, vel + 8))

# Bars 65-80
for _ in range(2):
    for note, dur, vel in harm_a:
        violin2.add(note, dur, velocity=max(35, vel - 12))
    for note, dur, vel in harm_b:
        violin2.add(note, dur, velocity=max(35, vel - 15))

# ── VIOLA — inner voice, warm ──────────────────────────────────
viola = score.part("viola", instrument="viola", volume=0.28,
                   reverb=0.4, reverb_type="cathedral",
                   pan=-0.15, humanize=0.1)

# Whole note chords throughout — the glue
for _ in range(10):
    for chord in prog:
        viola.add(chord, Duration.WHOLE, velocity=65)
for _ in range(10):
    for chord in prog2:
        viola.add(chord, Duration.WHOLE, velocity=60)

# ── CELLO — bass voice, foundation ─────────────────────────────
cello = score.part("cello", instrument="cello", volume=0.3,
                   reverb=0.35, reverb_type="cathedral",
                   humanize=0.1)

# Walking bass in half notes
cello_line = [
    (D.add(-12), Duration.HALF, 75), (A.add(-24), Duration.HALF, 70),
    (Bb.add(-24), Duration.HALF, 72), (F.add(-12), Duration.HALF, 68),
    (G.add(-12), Duration.HALF, 70), (D.add(-12), Duration.HALF, 72),
    (A.add(-12), Duration.HALF, 75), (E.add(-12), Duration.HALF, 70),
]
for _ in range(20):
    for note, dur, vel in cello_line:
        cello.add(note, dur, velocity=vel)

# ═══════════════════════════════════════════════════════════════════
# BAR 33: THE INTERRUPTION
# DnB breakbeat at double time (feels like 170 even though clock is 85)
# ═══════════════════════════════════════════════════════════════════

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

# ── BREAKBEAT — enters bar 33, no warning ──────────────────────
beat = score.part("breakbeat", volume=0.45, humanize=0.06)

# Bars 1-32: silence — the audience suspects nothing
for _ in range(32):
    beat.rest(Duration.WHOLE)

# Bars 33-64: DnB breakbeat — 16th notes at 85 BPM = 8th notes at 170
# Classic amen-style break
for bar in range(32):
    if bar % 8 == 7:
        # Fill — snare rolls
        for i in range(16):
            vel = min(127, 70 + i * 3)
            beat.hit(S, Duration.SIXTEENTH, velocity=vel)
    else:
        # K---S--K-KS----
        beat.hit(K, Duration.SIXTEENTH, velocity=110)
        beat.hit(CH, Duration.SIXTEENTH, velocity=50)
        beat.hit(CH, Duration.SIXTEENTH, velocity=45)
        beat.hit(CH, Duration.SIXTEENTH, velocity=48)
        beat.hit(S, Duration.SIXTEENTH, velocity=105)
        beat.hit(CH, Duration.SIXTEENTH, velocity=50)
        beat.hit(CH, Duration.SIXTEENTH, velocity=42)
        beat.hit(K, Duration.SIXTEENTH, velocity=95)
        beat.hit(CH, Duration.SIXTEENTH, velocity=48)
        beat.hit(K, Duration.SIXTEENTH, velocity=100)
        beat.hit(S, Duration.SIXTEENTH, velocity=108)
        beat.hit(CH, Duration.SIXTEENTH, velocity=45)
        beat.hit(CH, Duration.SIXTEENTH, velocity=48)
        beat.hit(CH, Duration.SIXTEENTH, velocity=42)
        beat.hit(CH, Duration.SIXTEENTH, velocity=50)
        beat.hit(CH, Duration.SIXTEENTH, velocity=45)

# Bars 65-72: beat thins out — strings winning
for bar in range(8):
    vel = max(25, 100 - bar * 9)
    beat.hit(K, Duration.SIXTEENTH, velocity=vel)
    beat.rest(Duration.SIXTEENTH)
    beat.rest(Duration.SIXTEENTH)
    beat.rest(Duration.SIXTEENTH)
    beat.hit(S, Duration.SIXTEENTH, velocity=max(20, vel - 5))
    beat.rest(Duration.SIXTEENTH)
    beat.rest(Duration.SIXTEENTH)
    beat.hit(K, Duration.SIXTEENTH, velocity=max(20, vel - 10))
    beat.rest(Duration.SIXTEENTH)
    beat.hit(K, Duration.SIXTEENTH, velocity=max(20, vel - 8))
    beat.hit(S, Duration.SIXTEENTH, velocity=max(20, vel - 5))
    beat.rest(Duration.SIXTEENTH)
    beat.rest(Duration.SIXTEENTH)
    beat.rest(Duration.SIXTEENTH)
    beat.rest(Duration.SIXTEENTH)
    beat.rest(Duration.SIXTEENTH)

# Bars 73-80: gone
for _ in range(8):
    beat.rest(Duration.WHOLE)

# ── SUB BASS — DnB sub, enters with the beat ───────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.5,
                 lowpass=120, distortion=0.2, distortion_drive=3.0,
                 sub_osc=0.5, sidechain=0.4)

for _ in range(32):
    sub.rest(Duration.WHOLE)

# Bars 33-64: following the root
sub_roots = [D.add(-24), Bb.add(-24), G.add(-24), A.add(-24)]
for _ in range(8):
    for root in sub_roots:
        sub.add(root, Duration.WHOLE, velocity=95)

# Bars 65-80: fading
for bar in range(16):
    vel = max(20, 90 - bar * 5)
    sub.add(D.add(-24), Duration.WHOLE, velocity=vel)

# ── REESE BASS — detuned saw, DnB signature ────────────────────
reese = score.part("reese", synth="saw", envelope="pad", volume=0.25,
                   lowpass=400, detune=15, spread=0.3,
                   distortion=0.2, sidechain=0.35)

for _ in range(32):
    reese.rest(Duration.WHOLE)

# Bars 33-64: dark, menacing
for _ in range(8):
    for root in sub_roots:
        reese.add(root.add(12), Duration.WHOLE, velocity=75)

# Bars 65-80: fading
for bar in range(16):
    vel = max(15, 70 - bar * 4)
    reese.add(D.add(-12), Duration.WHOLE, velocity=vel)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 85 (DnB section feels like 170)")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing THE INTERRUPTION (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing THE INTERRUPTION...")
    play_score(score)
