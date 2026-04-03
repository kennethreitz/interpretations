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

# ── HARPSICHORD — baroque opening, sets the scene ───────────────
harpsi = score.part("harpsichord", instrument="harpsichord", volume=0.3,
                    reverb=0.55, reverb_type="cathedral",
                    delay=0.15, delay_time=0.35, delay_feedback=0.2,
                    pan=0.1, humanize=0.08)

# Bars 1-16: arpeggiated chords — elegant, formal
for _ in range(4):
    for chord in prog:
        harpsi.add(chord, Duration.QUARTER, velocity=72)
        harpsi.rest(Duration.QUARTER)
        harpsi.add(chord, Duration.QUARTER, velocity=65)
        harpsi.rest(Duration.QUARTER)

# Bars 17-32: thinner, violins take over
for _ in range(2):
    for chord in prog:
        harpsi.add(chord, Duration.HALF, velocity=55)
        harpsi.rest(Duration.HALF)
for _ in range(8):
    harpsi.rest(Duration.WHOLE)

# Bars 33-64: gone — obliterated by the beat
for _ in range(32):
    harpsi.rest(Duration.WHOLE)

# Bars 65-80: returns for the ending — full circle
for _ in range(2):
    for chord in prog:
        harpsi.add(chord, Duration.QUARTER, velocity=60)
        harpsi.rest(Duration.QUARTER)
        harpsi.add(chord, Duration.QUARTER, velocity=52)
        harpsi.rest(Duration.QUARTER)
for _ in range(8):
    harpsi.rest(Duration.WHOLE)

# ── FLUTE — soaring above the quartet, baroque ornamental ───────
flute = score.part("flute", instrument="flute", volume=0.22,
                   reverb=0.5, reverb_type="cathedral",
                   delay=0.12, delay_time=0.35, delay_feedback=0.15,
                   pan=0.3, humanize=0.1)

# Bars 1-4: silent — let the harpsichord set the scene
for _ in range(4):
    flute.rest(Duration.WHOLE)

# Bars 5-16: ornamental melody — floats above the strings
flute_a = [
    (D.add(12), Duration.QUARTER, 78), (E.add(12), Duration.EIGHTH, 72),
    (F.add(12), Duration.EIGHTH, 75), (A.add(12), Duration.HALF, 80),
    (G.add(12), Duration.QUARTER, 75), (F.add(12), Duration.EIGHTH, 70),
    (E.add(12), Duration.EIGHTH, 68), (D.add(12), Duration.HALF, 72),
    (F.add(12), Duration.QUARTER, 78), (G.add(12), Duration.QUARTER, 75),
    (A.add(12), Duration.HALF, 82),
    (Bb.add(12), Duration.QUARTER, 78), (A.add(12), Duration.EIGHTH, 72),
    (G.add(12), Duration.EIGHTH, 70), (F.add(12), Duration.HALF, 75),
]
flute_b = [
    (A.add(12), Duration.HALF, 80), (Bb.add(12), Duration.QUARTER, 75),
    (A.add(12), Duration.QUARTER, 72),
    (G.add(12), Duration.QUARTER, 70), (F.add(12), Duration.EIGHTH, 65),
    (E.add(12), Duration.EIGHTH, 62), (D.add(12), Duration.HALF, 68),
    (None, Duration.QUARTER, 0), (F.add(12), Duration.EIGHTH, 72),
    (G.add(12), Duration.EIGHTH, 75), (A.add(12), Duration.HALF, 80),
    (D.add(12), Duration.WHOLE, 75),
]
for _ in range(2):
    for note, dur, vel in flute_a:
        flute.add(note, dur, velocity=vel)
    for note, dur, vel in flute_b:
        if note is None:
            flute.rest(dur)
        else:
            flute.add(note, dur, velocity=vel)

# Bars 17-32: more active — 16th note runs between phrases
flute_c = [
    (D.add(12), Duration.EIGHTH, 82), (E.add(12), Duration.SIXTEENTH, 75),
    (F.add(12), Duration.SIXTEENTH, 78), (G.add(12), Duration.QUARTER, 80),
    (A.add(12), Duration.HALF, 85),
    (G.add(12), Duration.EIGHTH, 78), (F.add(12), Duration.SIXTEENTH, 72),
    (E.add(12), Duration.SIXTEENTH, 70), (D.add(12), Duration.QUARTER, 75),
    (F.add(12), Duration.HALF, 78),
    (A.add(12), Duration.QUARTER, 85), (Bb.add(12), Duration.EIGHTH, 80),
    (A.add(12), Duration.EIGHTH, 78), (G.add(12), Duration.HALF, 75),
    (D.add(12), Duration.WHOLE, 72),
]
for _ in range(4):
    for note, dur, vel in flute_c:
        flute.add(note, dur, velocity=vel)

# Bars 33-64: keeps playing through the interruption — unshaken
flute.set(volume=0.4)
for _ in range(4):
    for note, dur, vel in flute_a:
        flute.add(note, dur, velocity=min(127, vel + 8))
    for note, dur, vel in flute_b:
        if note is None:
            flute.rest(dur)
        else:
            flute.add(note, dur, velocity=min(127, vel + 8))

# Bars 65-80: returns to gentle — the quartet wins
flute.set(volume=0.3)
for _ in range(2):
    for note, dur, vel in flute_a:
        flute.add(note, dur, velocity=max(40, vel - 10))
    for note, dur, vel in flute_b:
        if note is None:
            flute.rest(dur)
        else:
            flute.add(note, dur, velocity=max(40, vel - 12))

# ── HARP — arpeggiated chords, delicate, angelic ────────────────
harp = score.part("harp", instrument="harp", volume=0.28,
                  reverb=0.25, reverb_decay=1.0,
                  delay=0.1, delay_time=0.353, delay_feedback=0.15,
                  pan=-0.25, humanize=0.1)

# Bars 1-8: silent — let harpsichord establish
for _ in range(8):
    harp.rest(Duration.WHOLE)

# Bars 9-32: arpeggiated chords — cascading 16ths
harp_arps = {
    "i":   [D.add(-12), A.add(-12), D, F, A, F, D, A.add(-12)],
    "VI":  [Bb.add(-24), F.add(-12), Bb.add(-12), D, F, D, Bb.add(-12), F.add(-12)],
    "iv":  [G.add(-12), Bb.add(-12), D, G, Bb, G, D, Bb.add(-12)],
    "V":   [A.add(-24), E.add(-12), A.add(-12), C, E, C, A.add(-12), E.add(-12)],
}
chord_order = ["i", "VI", "iv", "V"]
for _ in range(6):
    for name in chord_order:
        for note in harp_arps[name]:
            harp.add(note, Duration.EIGHTH, velocity=62)

# Bars 33-48: keeps going through the interruption, quieter
harp.set(volume=0.18)
for _ in range(4):
    for name in chord_order:
        for note in harp_arps[name]:
            harp.add(note, Duration.EIGHTH, velocity=55)

# Bars 49-64: silent — overwhelmed
for _ in range(16):
    harp.rest(Duration.WHOLE)

# Bars 65-80: returns for the ending
harp.set(volume=0.22)
for _ in range(4):
    for name in chord_order:
        for note in harp_arps[name]:
            harp.add(note, Duration.EIGHTH, velocity=58)

# ── VIOLIN 1 — melody, the lead voice ──────────────────────────
violin1 = score.part("violin_1", instrument="violin", volume=0.4,
                     reverb=0.5, reverb_type="cathedral",
                     chorus=0.18, chorus_rate=0.3, chorus_depth=0.006,
                     delay=0.1, delay_time=0.25, delay_feedback=0.15,
                     pan=-0.35, humanize=0.1)

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
violin2 = score.part("violin_2", instrument="violin", volume=0.32,
                     reverb=0.5, reverb_type="cathedral",
                     chorus=0.18, chorus_rate=0.25, chorus_depth=0.006,
                     delay=0.1, delay_time=0.28, delay_feedback=0.12,
                     pan=0.4, humanize=0.1)

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
viola = score.part("viola", instrument="viola", volume=0.3,
                   reverb=0.5, reverb_type="cathedral",
                   chorus=0.15, chorus_rate=0.2, chorus_depth=0.006,
                   pan=-0.15, humanize=0.1)

# Whole note chords throughout — the glue
for _ in range(10):
    for chord in prog:
        viola.add(chord, Duration.WHOLE, velocity=65)
for _ in range(10):
    for chord in prog2:
        viola.add(chord, Duration.WHOLE, velocity=60)

# ── CELLO — bass voice, foundation ─────────────────────────────
cello = score.part("cello", instrument="cello", volume=0.35,
                   reverb=0.45, reverb_type="cathedral",
                   chorus=0.1, chorus_rate=0.15, chorus_depth=0.004,
                   pan=0.15, humanize=0.1)

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
beat = score.part("breakbeat", volume=0.9, humanize=0.06,
                  reverb=0.25, reverb_decay=1.0,
                  delay=0.15, delay_time=0.353, delay_feedback=0.2,
                  pan=-0.1)

# Bars 1-32: silence — the audience suspects nothing
for _ in range(32):
    beat.rest(Duration.WHOLE)

# Bars 33-64: DnB breakbeat — 16th notes at 85 BPM = 8th notes at 170
# Classic amen-style break
for bar in range(32):
    if bar % 8 == 7:
        # Fill — snare into 32nd note hat cascade
        beat.hit(S, Duration.SIXTEENTH, velocity=108)
        beat.hit(S, Duration.SIXTEENTH, velocity=105)
        beat.hit(K, Duration.SIXTEENTH, velocity=110)
        beat.hit(S, Duration.SIXTEENTH, velocity=100)
        # 32nd note hat roll
        for i in range(8):
            vel = min(127, 55 + i * 8)
            beat.hit(CH, 0.125, velocity=vel)
        # Back to snare hits
        beat.hit(S, Duration.SIXTEENTH, velocity=112)
        beat.hit(K, Duration.SIXTEENTH, velocity=115)
        beat.hit(S, Duration.SIXTEENTH, velocity=118)
        beat.hit(S, Duration.SIXTEENTH, velocity=120)
    elif bar % 4 == 3:
        # Mini fill — 32nd hat flurry on beat 4
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
        # 32nd note hat burst
        for i in range(8):
            beat.hit(CH, 0.125, velocity=min(90, 50 + i * 5))
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

# ── 808 KICK — four on the floor, the slap ─────────────────────
kick808 = score.part("kick808", volume=1.0, humanize=0.03,
                     distortion=0.1, distortion_drive=1.5)

for _ in range(32):
    kick808.rest(Duration.WHOLE)

# Bars 33-64: FOUR ON THE FLOOR — hits like a truck
for _ in range(32):
    for beat_num in range(4):
        kick808.hit(K, Duration.QUARTER, velocity=125)

# Bars 65-72: fading
for bar in range(8):
    vel = max(30, 120 - bar * 12)
    for beat_num in range(4):
        kick808.hit(K, Duration.QUARTER, velocity=vel)

# Bars 73-80: gone
for _ in range(8):
    kick808.rest(Duration.WHOLE)

# ── SUB BASS — DnB sub, enters with the beat ───────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.9,
                 lowpass=150, distortion=0.25, distortion_drive=3.5,
                 sub_osc=0.7, sidechain=0.6)

for _ in range(32):
    sub.rest(Duration.WHOLE)

# Bars 33-64: following the root
sub_roots = [D.add(-24), Bb.add(-24), G.add(-24), A.add(-24)]
for _ in range(8):
    for root in sub_roots:
        sub.add(root, Duration.WHOLE, velocity=95)

# Bars 65-80: fading
for vel in [85, 78, 70, 62, 55, 48, 40, 35, 30, 25, 22, 20, 18, 15, 12, 8]:
    sub.add(D.add(-24), Duration.WHOLE, velocity=vel)

# ── REESE BASS — detuned saw, DnB signature ────────────────────
reese = score.part("reese", synth="drift", envelope="pad", volume=0.28,
                   lowpass=400, detune=15, spread=0.3,
                   distortion=0.2, sidechain=0.55,
                   reverb=0.2, reverb_decay=1.5,
                   delay=0.1, delay_time=0.706, delay_feedback=0.2,
                   pan=0.15)

for _ in range(32):
    reese.rest(Duration.WHOLE)

# Bars 33-64: dark, menacing
for _ in range(8):
    for root in sub_roots:
        reese.add(root.add(12), Duration.WHOLE, velocity=75)

# Bars 65-80: fading
for vel in [65, 58, 52, 46, 40, 35, 30, 26, 22, 18, 16, 14, 12, 10, 8, 5]:
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
