"""
GRAVITY — heavy. Piano, 808, snap. The weight of it all.
C minor, 88 BPM. No gimmicks. Just pressure.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("C", "minor")
s = key.scale  # C D Eb F G Ab Bb

C  = s[0]; D  = s[1]; Eb = s[2]; F  = s[3]
G  = s[4]; Ab = s[5]; Bb = s[6]

score = Score("4/4", bpm=88)

prog = key.progression("i", "VI", "iv", "VII")
prog2 = key.progression("i", "VII", "VI", "v")

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT
CL = DrumSound.CLAP

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~2:55):
#   Bars  1-4:   Piano alone — the weight
#   Bars  5-8:   808 enters — the floor drops
#   Bars  9-16:  Drums — boom bap + trap hats
#   Bars 17-24:  Full groove — everything locked
#   Bars 25-32:  Melody — Rhodes sings over the beat
#   Bars 33-40:  Breakdown — stripped back, just piano + 808
#   Bars 41-48:  Build — drums return harder, strings swell
#   Bars 49-56:  Peak — everything, hats going wild
#   Bars 57-64:  Outro — peeling away, piano last
# ═══════════════════════════════════════════════════════════════════

# ── PIANO — the foundation, dark chords ────────────────────────
piano = score.part("piano", instrument="piano", volume=0.5,
                   reverb=0.4, reverb_type="taj_mahal",
                   delay=0.12, delay_time=0.341, delay_feedback=0.2,
                   pan=-0.15, humanize=0.1)

# Piano patterns — sparse hits, let the space breathe
# Pattern A: stab, silence, low octave hit
def piano_bar_a(chord, vel):
    piano.add(chord, Duration.EIGHTH, velocity=vel)
    piano.rest(Duration.QUARTER)
    piano.rest(Duration.EIGHTH)
    piano.rest(Duration.QUARTER)
    piano.add(chord, Duration.EIGHTH, velocity=max(30, vel - 20))
    piano.rest(Duration.EIGHTH)

# Pattern B: low single note, space, high stab
def piano_bar_b(root, vel):
    piano.add(root.add(-12), Duration.EIGHTH, velocity=vel)
    piano.rest(Duration.DOTTED_QUARTER)
    piano.rest(Duration.EIGHTH)
    piano.add(root.add(12), Duration.SIXTEENTH, velocity=max(30, vel - 10))
    piano.rest(Duration.SIXTEENTH)
    piano.rest(Duration.QUARTER)

# Pattern C: two quick stabs then nothing
def piano_bar_c(chord, vel):
    piano.rest(Duration.EIGHTH)
    piano.add(chord, Duration.SIXTEENTH, velocity=vel)
    piano.rest(Duration.SIXTEENTH)
    piano.add(chord, Duration.EIGHTH, velocity=max(30, vel - 15))
    piano.rest(Duration.HALF)
    piano.rest(Duration.QUARTER)

single_roots = [C, Ab.add(-12), F, Bb]

# Bars 1-4: alone — just drops into silence
for i, chord in enumerate(prog):
    piano_bar_a(chord, 78)

# Bars 5-8: 808 enters, piano gets sparser
for i, (chord, root) in enumerate(zip(prog, single_roots)):
    piano_bar_b(root, 75)

# Bars 9-32: alternating patterns, never predictable
for section in range(6):
    p = prog if section % 2 == 0 else prog2
    r = single_roots if section % 2 == 0 else [C, Bb, Ab.add(-12), G]
    vel = 78
    piano_bar_a(p[0], vel)
    piano_bar_b(r[1], vel)
    piano_bar_c(p[2], vel)
    piano_bar_a(p[3], vel)

# Bars 33-40: breakdown — barely there, single low notes
for root in single_roots * 2:
    piano.add(root.add(-12), Duration.QUARTER, velocity=55)
    piano.rest(Duration.DOTTED_HALF)

# Bars 41-56: back, patterns return harder
for section in range(4):
    p = prog if section % 2 == 0 else prog2
    r = single_roots if section % 2 == 0 else [C, Bb, Ab.add(-12), G]
    vel = 82
    piano_bar_a(p[0], vel)
    piano_bar_c(p[1], vel)
    piano_bar_b(r[2], vel)
    piano_bar_a(p[3], vel)

# Bars 57-64: fading — one note per bar, dissolving
for root, vel in zip([C, Eb, G, Ab, Eb, C, G.add(-12), C.add(-12)],
                     [65, 58, 52, 45, 38, 32, 25, 18]):
    piano.add(root, Duration.QUARTER, velocity=vel)
    piano.rest(Duration.DOTTED_HALF)

# ── 808 — the floor, slides between roots ─────────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=0.7,
                 lowpass=200, distortion=0.2, distortion_drive=3.0,
                 sub_osc=0.5, saturation=0.4, sidechain=0.35)

# Bars 1-4: silent
for _ in range(4):
    sub.rest(Duration.WHOLE)

# Bars 5-64: 808 — continuous wave, one root per bar
roots = [C.add(-24), Ab.add(-24), F.add(-24), Bb.add(-24)]
roots2 = [C.add(-24), Bb.add(-24), Ab.add(-24), G.add(-24)]

for section in range(15):
    r = roots if section % 2 == 0 else roots2
    vel = 42 if section < 12 else max(18, 42 - (section - 12) * 8)
    for root in r:
        sub.add(root, Duration.WHOLE, velocity=vel)

# ── KICK — boom bap pocket ────────────────────────────────────
kick = score.part("kick", volume=0.8, humanize=0.04,
                  distortion=0.08, distortion_drive=1.5)

# Bars 1-8: silent
for _ in range(8):
    kick.rest(Duration.WHOLE)

# Bars 9-32: boom bap — kick on 1, and-of-2, 3
for _ in range(24):
    kick.hit(K, Duration.QUARTER, velocity=112)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=95)
    kick.hit(K, Duration.QUARTER, velocity=108)
    kick.rest(Duration.QUARTER)

# Bars 33-40: breakdown — just beat 1
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=100)
    kick.rest(Duration.DOTTED_HALF)

# Bars 41-56: back full, harder
for _ in range(16):
    kick.hit(K, Duration.QUARTER, velocity=118)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=100)
    kick.hit(K, Duration.QUARTER, velocity=112)
    kick.rest(Duration.QUARTER)

# Bars 57-64: fading
for vel in [105, 95, 85, 75, 62, 48, 35, 22]:
    kick.hit(K, Duration.QUARTER, velocity=vel)
    kick.rest(Duration.DOTTED_HALF)

# ── SNARE — crack on 2 and 4 ──────────────────────────────────
snare = score.part("snare", volume=0.55, humanize=0.04,
                   reverb=0.2, reverb_decay=0.8,
                   delay=0.08, delay_time=0.341, delay_feedback=0.12,
                   pan=0.05)

for _ in range(8):
    snare.rest(Duration.WHOLE)

# Bars 9-32: 2 and 4
for _ in range(24):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=105)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=108)

# Bars 33-40: breakdown — ghost snares
for _ in range(8):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=55)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=50)

# Bars 41-56: back hard
for _ in range(16):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=110)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=112)

# Bars 57-64: fading
for vel in [100, 88, 75, 62, 50, 38, 25, 15]:
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=vel)
    snare.rest(Duration.HALF)

# ── HATS — trap-style, evolving patterns ───────────────────────
hats = score.part("hats", volume=0.28, pan=0.2, humanize=0.05)

for _ in range(8):
    hats.rest(Duration.WHOLE)

# Bars 9-16: simple 8ths
for _ in range(8):
    for beat in range(4):
        hats.hit(CH, Duration.EIGHTH, velocity=72)
        hats.hit(CH, Duration.EIGHTH, velocity=48)

# Bars 17-24: 16ths creep in
for _ in range(8):
    hats.hit(CH, Duration.EIGHTH, velocity=72)
    hats.hit(CH, Duration.EIGHTH, velocity=48)
    hats.hit(CH, Duration.SIXTEENTH, velocity=68)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(CH, Duration.EIGHTH, velocity=55)
    hats.hit(CH, Duration.EIGHTH, velocity=72)
    hats.hit(CH, Duration.EIGHTH, velocity=48)
    hats.hit(OH, Duration.EIGHTH, velocity=62)

# Bars 25-32: more active, triplet feel creeps in
for _ in range(8):
    hats.hit(CH, Duration.EIGHTH, velocity=72)
    hats.hit(CH, Duration.SIXTEENTH, velocity=52)
    hats.hit(CH, Duration.SIXTEENTH, velocity=48)
    hats.hit(CH, Duration.SIXTEENTH, velocity=68)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(CH, Duration.SIXTEENTH, velocity=55)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(CH, Duration.EIGHTH, velocity=72)
    hats.hit(CH, Duration.SIXTEENTH, velocity=48)
    hats.hit(CH, Duration.SIXTEENTH, velocity=52)
    hats.hit(OH, Duration.EIGHTH, velocity=60)

# Bars 33-40: breakdown — barely there
for _ in range(8):
    hats.hit(CH, Duration.QUARTER, velocity=35)
    hats.rest(Duration.DOTTED_HALF)

# Bars 41-48: build back — 16ths
for _ in range(8):
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=72)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)

# Bars 49-56: PEAK — 32nd note hat rolls scattered
for bar in range(8):
    if bar % 2 == 1:
        # 32nd note roll bar
        for i in range(32):
            vel = min(90, 40 + (i % 8) * 6)
            hats.hit(CH, 0.125, velocity=vel)
    else:
        # Normal 16th bar with open hat
        hats.hit(CH, Duration.SIXTEENTH, velocity=75)
        hats.hit(CH, Duration.SIXTEENTH, velocity=45)
        hats.hit(CH, Duration.SIXTEENTH, velocity=58)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=70)
        hats.hit(CH, Duration.SIXTEENTH, velocity=45)
        hats.hit(OH, Duration.SIXTEENTH, velocity=62)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=72)
        hats.hit(CH, Duration.SIXTEENTH, velocity=48)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=68)
        hats.hit(CH, Duration.SIXTEENTH, velocity=45)
        hats.hit(OH, Duration.SIXTEENTH, velocity=60)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)

# Bars 57-64: fading
for vel in [60, 52, 44, 36, 28, 22, 15, 0]:
    if vel > 0:
        for beat in range(4):
            hats.hit(CH, Duration.EIGHTH, velocity=vel)
            hats.hit(CH, Duration.EIGHTH, velocity=max(12, vel - 25))
    else:
        hats.rest(Duration.WHOLE)

# ── TAMBURA — buried drone, barely there, just warmth ──────────
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.08,
                     reverb=0.5, reverb_type="taj_mahal",
                     chorus=0.3, chorus_rate=0.06, chorus_depth=0.01,
                     lowpass=800, pan=-0.3)

for _ in range(4):
    tambura.rest(Duration.WHOLE)
for _ in range(52):
    tambura.add(C.add(-24), Duration.WHOLE, velocity=35)
for vel in [28, 22, 16, 10, 6, 3, 0, 0]:
    if vel > 0:
        tambura.add(C.add(-24), Duration.WHOLE, velocity=vel)
    else:
        tambura.rest(Duration.WHOLE)

# ── SINGING BOWL — bookends, marks the gravity ────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.3,
                  reverb=0.8, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.682, delay_feedback=0.2,
                  pan=0.2)

bowl.add(C.add(-24), Duration.WHOLE, velocity=65)
for _ in range(62):
    bowl.rest(Duration.WHOLE)
bowl.add(C.add(-24), Duration.WHOLE, velocity=50)

# ── SITAR — one bend in the breakdown, like a ghost ───────────
sitar = score.part("sitar", instrument="sitar", volume=0.25,
                   reverb=0.35, reverb_type="taj_mahal",
                   delay=0.2, delay_time=0.341, delay_feedback=0.3,
                   pan=0.3, humanize=0.08)

for _ in range(34):
    sitar.rest(Duration.WHOLE)

# Bar 35-36: one long bent note — the sample flip moment
sitar.add(Eb, Duration.WHOLE, velocity=65, bend=-0.25)
sitar.add(C, Duration.WHOLE, velocity=55, bend=0.15)

# Bar 37: quick ornamental phrase then gone
sitar.add(Eb, Duration.QUARTER, velocity=60)
sitar.add(D, Duration.EIGHTH, velocity=55)
sitar.add(C, Duration.EIGHTH, velocity=52)
sitar.add(Bb.add(-12), Duration.HALF, velocity=58, bend=-0.15)

for _ in range(27):
    sitar.rest(Duration.WHOLE)

# ── CLAP — layered with snare for weight ───────────────────────
clap = score.part("clap", volume=0.2, reverb=0.15,
                  delay=0.06, delay_time=0.341, delay_feedback=0.1,
                  pan=-0.08, humanize=0.04)

for _ in range(16):
    clap.rest(Duration.WHOLE)

# Bars 17-32: layered on snare hits
for _ in range(16):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=82)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=85)

# Bars 33-40: silent
for _ in range(8):
    clap.rest(Duration.WHOLE)

# Bars 41-56: back
for _ in range(16):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=85)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=88)

# Bars 57-64: silent
for _ in range(8):
    clap.rest(Duration.WHOLE)

# ── RHODES — melody enters bar 25, the soul ───────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.3,
                    reverb=0.5, reverb_type="taj_mahal",
                    delay=0.2, delay_time=0.341, delay_feedback=0.3,
                    tremolo_depth=0.1, tremolo_rate=2.5,
                    pan=0.25, humanize=0.08)

for _ in range(24):
    rhodes.rest(Duration.WHOLE)

# Bars 25-32: melody — simple, soulful, singing
melody = [
    (Eb.add(12), Duration.HALF, 80), (D.add(12), Duration.QUARTER, 72),
    (C.add(12), Duration.QUARTER, 75),
    (Bb, Duration.HALF, 78), (Ab, Duration.QUARTER, 70),
    (G, Duration.QUARTER, 72),
    (Ab, Duration.DOTTED_HALF, 80), (G, Duration.QUARTER, 72),
    (F, Duration.HALF, 75), (Eb, Duration.HALF, 78),
    (G, Duration.HALF, 80), (Ab, Duration.QUARTER, 75),
    (Bb, Duration.QUARTER, 72),
    (C.add(12), Duration.HALF, 82), (Bb, Duration.QUARTER, 75),
    (Ab, Duration.QUARTER, 70),
    (G, Duration.WHOLE, 78),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in melody:
    if note is None:
        rhodes.rest(dur)
    else:
        rhodes.add(note, dur, velocity=vel)

# Bars 33-40: silent through breakdown
for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# Bars 41-48: melody returns, stronger
for note, dur, vel in melody:
    if note is None:
        rhodes.rest(dur)
    else:
        rhodes.add(note, dur, velocity=min(127, vel + 8))

# Bars 49-56: variation — higher, more intense
melody2 = [
    (G.add(12), Duration.QUARTER, 85), (Ab.add(12), Duration.QUARTER, 82),
    (Bb.add(12), Duration.HALF, 88),
    (Ab.add(12), Duration.QUARTER, 80), (G.add(12), Duration.QUARTER, 78),
    (Eb.add(12), Duration.HALF, 82),
    (D.add(12), Duration.QUARTER, 78), (Eb.add(12), Duration.QUARTER, 80),
    (G.add(12), Duration.HALF, 85),
    (C.add(12), Duration.WHOLE, 82),
    (Bb, Duration.HALF, 78), (Ab, Duration.QUARTER, 72),
    (G, Duration.QUARTER, 70),
    (Eb, Duration.WHOLE, 75),
    (None, Duration.WHOLE, 0),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in melody2:
    if note is None:
        rhodes.rest(dur)
    else:
        rhodes.add(note, dur, velocity=vel)

# Bars 57-64: one last phrase, fading
rhodes.add(Eb.add(12), Duration.HALF, velocity=65)
rhodes.add(C.add(12), Duration.HALF, velocity=58)
rhodes.add(G, Duration.WHOLE, velocity=50)
for _ in range(6):
    rhodes.rest(Duration.WHOLE)

# ── STRINGS — swell at bar 41, the drama ──────────────────────
strings = score.part("strings", instrument="string_ensemble", volume=0.15,
                     reverb=0.6, reverb_type="cathedral",
                     chorus=0.2, chorus_rate=0.15, chorus_depth=0.006,
                     pan=-0.2)

for _ in range(40):
    strings.rest(Duration.WHOLE)

# Bars 41-56: slow swells under the beat
for _ in range(4):
    for chord in prog:
        strings.add(chord, Duration.WHOLE, velocity=48)

# Bars 57-64: fading
for vel in [42, 35, 28, 22, 18, 12, 8, 0]:
    if vel > 0:
        strings.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        strings.rest(Duration.WHOLE)

# ── VINYL — lo-fi texture throughout ──────────────────────────
vinyl = score.part("vinyl", synth="noise", envelope="pad", volume=0.025,
                   lowpass=1500, highpass=500,
                   distortion=0.3, distortion_drive=2.5,
                   saturation=0.5, pan=0.1)

for _ in range(64):
    vinyl.add(C, Duration.WHOLE, velocity=20)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 88")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing GRAVITY (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing GRAVITY...")
    play_score(score)
