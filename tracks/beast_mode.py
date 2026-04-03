"""
BEAST MODE — 135 BPM, no mercy.
Trap drums, 808 slides, distorted saw, sitar hook, mellotron drop,
timpani rolls. The hardest track on the album.
G minor, 135 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("G", "minor")
s = key.scale  # G A Bb C D Eb F

G  = s[0]; A  = s[1]; Bb = s[2]; C  = s[3]
D  = s[4]; Eb = s[5]; F  = s[6]

score = Score("4/4", bpm=135)

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

prog = key.progression("i", "VII", "VI", "iv")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (80 bars, ~3:33):
#   Bars  1-4:   808 alone — the warning
#   Bars  5-8:   Kick + hats drop — we're moving
#   Bars  9-16:  Sitar hook — the sample flip
#   Bars 17-24:  Full beat — saw bass, everything locked
#   Bars 25-32:  Mellotron choir drop — the heavens open
#   Bars 33-40:  Breakdown — just 808 + hats, tension
#   Bars 41-48:  Timpani build — the war drums
#   Bars 49-56:  BEAST MODE — everything, max aggression
#   Bars 57-64:  Sitar solo — shredding over the beat
#   Bars 65-72:  Last drop — mellotron + timpani + 808
#   Bars 73-80:  Outro — 808 slides into silence
# ═══════════════════════════════════════════════════════════════════

# ── 808 — the foundation, slides between roots ────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=0.65,
                 lowpass=220, distortion=0.25, distortion_drive=3.5,
                 sub_osc=0.5, saturation=0.4, sidechain=0.5)

# Bars 1-4: alone — just the 808, announces itself
sub.add(G.add(-24), Duration.WHOLE, velocity=35)
sub.add(G.add(-24), Duration.WHOLE, velocity=38)
sub.add(G.add(-24), Duration.HALF, velocity=40)
sub.add(Bb.add(-24), Duration.HALF, velocity=38)
sub.add(G.add(-24), Duration.WHOLE, velocity=42)

# Bars 5-72: follows roots, slides between chords
roots_pattern = [
    (G.add(-24), 40), (G.add(-24), 38),
    (F.add(-24), 40), (G.add(-24), 42),
    (Eb.add(-24), 38), (F.add(-24), 40),
    (D.add(-24), 42), (G.add(-24), 40),
]
for _ in range(8):
    for root, vel in roots_pattern:
        sub.add(root, Duration.WHOLE, velocity=vel)

# Bars 73-80: slides down — dying
for root, vel in [(G.add(-24), 38), (F.add(-24), 35),
                  (Eb.add(-24), 32), (D.add(-24), 28),
                  (C.add(-24), 25), (Bb.add(-24), 22),
                  (A.add(-24), 18), (G.add(-36), 12)]:
    sub.add(root, Duration.WHOLE, velocity=vel)

# ── KICK — hard, distorted ───────────────────────────────────
kick = score.part("kick", volume=0.85, humanize=0.02,
                  distortion=0.12, distortion_drive=2.0)

for _ in range(4):
    kick.rest(Duration.WHOLE)

# Bars 5-32: trap kick pattern — syncopated, heavy
for _ in range(28):
    kick.hit(K, Duration.QUARTER, velocity=118)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=98)
    kick.hit(K, Duration.QUARTER, velocity=112)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=95)

# Bars 33-40: breakdown — half time
for _ in range(8):
    kick.hit(K, Duration.HALF, velocity=115)
    kick.rest(Duration.HALF)

# Bars 41-48: build — kick gets busier
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=118)
    kick.hit(K, Duration.EIGHTH, velocity=100)
    kick.hit(K, Duration.EIGHTH, velocity=95)
    kick.hit(K, Duration.QUARTER, velocity=115)
    kick.hit(K, Duration.EIGHTH, velocity=102)
    kick.hit(K, Duration.EIGHTH, velocity=108)

# Bars 49-72: BEAST MODE + sitar solo + last drop
for _ in range(24):
    kick.hit(K, Duration.QUARTER, velocity=122)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=105)
    kick.hit(K, Duration.QUARTER, velocity=118)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=100)

# Bars 73-80: fading
for vel in [110, 95, 80, 65, 50, 35, 20, 0]:
    if vel > 0:
        kick.hit(K, Duration.QUARTER, velocity=vel)
        kick.rest(Duration.DOTTED_HALF)
    else:
        kick.rest(Duration.WHOLE)

# ── SNARE — crack ────────────────────────────────────────────
snare = score.part("snare", volume=0.5, humanize=0.03,
                   reverb=0.12, distortion=0.08, distortion_drive=1.5,
                   delay=0.05, delay_time=0.222, delay_feedback=0.08,
                   pan=0.05)

for _ in range(4):
    snare.rest(Duration.WHOLE)

# Bars 5-32: 2 and 4
for _ in range(28):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=108)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=110)

# Bars 33-40: breakdown — half time snare
for _ in range(8):
    snare.rest(Duration.HALF)
    snare.hit(S, Duration.HALF, velocity=112)

# Bars 41-48: rolls building
for bar in range(8):
    if bar >= 6:
        # 16th note roll
        for i in range(16):
            snare.hit(S, Duration.SIXTEENTH, velocity=min(115, 70 + i * 3))
    else:
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=108)
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=110)

# Bars 49-72: 2 and 4, harder
for _ in range(24):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=115)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=118)

# Bars 73-80: fading
for vel in [105, 90, 75, 58, 42, 25, 0, 0]:
    if vel > 0:
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=vel)
        snare.rest(Duration.HALF)
    else:
        snare.rest(Duration.WHOLE)

# ── HATS — trap style, evolving ──────────────────────────────
hats = score.part("hats", volume=0.3, pan=0.3, humanize=0.04)

for _ in range(4):
    hats.rest(Duration.WHOLE)

# Bars 5-16: 16ths with ghost notes
for _ in range(12):
    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=72)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=35)

# Bars 17-32: more active — open hat accents
for _ in range(16):
    hats.hit(CH, Duration.SIXTEENTH, velocity=75)
    hats.hit(CH, Duration.SIXTEENTH, velocity=40)
    hats.hit(OH, Duration.SIXTEENTH, velocity=62)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(CH, Duration.SIXTEENTH, velocity=72)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(CH, Duration.SIXTEENTH, velocity=58)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(CH, Duration.SIXTEENTH, velocity=75)
    hats.hit(CH, Duration.SIXTEENTH, velocity=40)
    hats.hit(CH, Duration.SIXTEENTH, velocity=55)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(OH, Duration.SIXTEENTH, velocity=60)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(CH, Duration.SIXTEENTH, velocity=52)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)

# Bars 33-40: breakdown — sparse
for _ in range(8):
    hats.hit(CH, Duration.QUARTER, velocity=55)
    hats.rest(Duration.QUARTER)
    hats.hit(CH, Duration.QUARTER, velocity=48)
    hats.rest(Duration.QUARTER)

# Bars 41-48: build — 32nd note rolls
for bar in range(8):
    if bar % 2 == 1:
        for i in range(32):
            hats.hit(CH, 0.125, velocity=min(82, 38 + i * 2))
    else:
        for beat in range(4):
            hats.hit(CH, Duration.SIXTEENTH, velocity=72)
            hats.hit(CH, Duration.SIXTEENTH, velocity=40)
            hats.hit(CH, Duration.SIXTEENTH, velocity=58)
            hats.hit(CH, Duration.SIXTEENTH, velocity=35)

# Bars 49-72: BEAST MODE — full trap hats
for bar in range(24):
    if bar % 4 == 3:
        for i in range(32):
            hats.hit(CH, 0.125, velocity=min(85, 40 + i * 2))
    else:
        hats.hit(CH, Duration.SIXTEENTH, velocity=78)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(OH, Duration.SIXTEENTH, velocity=65)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(CH, Duration.SIXTEENTH, velocity=75)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)
        hats.hit(CH, Duration.SIXTEENTH, velocity=58)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=78)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=35)
        hats.hit(OH, Duration.SIXTEENTH, velocity=62)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)

# Bars 73-80: fading
for vel in [65, 55, 45, 35, 25, 15, 0, 0]:
    if vel > 0:
        for beat in range(4):
            hats.hit(CH, Duration.EIGHTH, velocity=vel)
            hats.hit(CH, Duration.EIGHTH, velocity=max(12, vel - 25))
    else:
        hats.rest(Duration.WHOLE)

# ── SITAR — the hook, enters bar 9 ───────────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.65,
                   reverb=0.2, reverb_type="taj_mahal",
                   delay=0.15, delay_time=0.222, delay_feedback=0.2,
                   pan=-0.3, humanize=0.08)

for _ in range(8):
    sitar.rest(Duration.WHOLE)

# Bars 9-16: THE HOOK — dark, catchy, repeating
hook = [
    (G, Duration.EIGHTH, 82), (Bb, Duration.EIGHTH, 75),
    (D, Duration.QUARTER, 85), (C, Duration.EIGHTH, 72),
    (Bb, Duration.EIGHTH, 70), (A, Duration.QUARTER, 78),
    (G, Duration.EIGHTH, 80), (None, Duration.EIGHTH, 0),
    (F, Duration.EIGHTH, 72), (G, Duration.EIGHTH, 78),
    (None, Duration.QUARTER, 0),
    (Bb, Duration.EIGHTH, 75), (A, Duration.EIGHTH, 70),
    (G, Duration.HALF, 80),
]
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=vel)

# Bars 17-24: hook continues under full beat
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=max(40, vel - 5))

# Bars 25-32: drops volume — mellotron takes focus
sitar.set(volume=0.3)
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=max(35, vel - 15))

# Bars 33-48: silent through breakdown and build
for _ in range(16):
    sitar.rest(Duration.WHOLE)

# Bars 49-56: hook returns HARD
sitar.set(volume=0.55)
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=min(100, vel + 8))

# Bars 57-64: SITAR SOLO — shredding over the beat
sitar.set(volume=0.65)
# 16th arps
arp_i = [G, Bb, D, Bb, G, D.add(-12), Bb.add(-12), D.add(-12)]
arp_vii = [F, A, C, A, F, C.add(-12), A.add(-12), C.add(-12)]
for _ in range(2):
    for note in arp_i:
        sitar.add(note, Duration.SIXTEENTH, velocity=95)
    for note in arp_vii:
        sitar.add(note, Duration.SIXTEENTH, velocity=92)
# 32nd shred
for note in [G, A, Bb, C, D, Eb, F, G.add(12),
             F, Eb, D, C, Bb, A, G, A]:
    sitar.add(note, 0.125, velocity=108)
for note in [G, D, G.add(12), D, Bb, G, D, Bb.add(-12),
             G, C, Eb, G.add(12), Eb, C, G, Eb.add(-12)]:
    sitar.add(note, 0.125, velocity=112)
# The bends — snap hard, big dynamics
sitar.add(G.add(12), Duration.SIXTEENTH, velocity=118, bend=-2.0)
sitar.add(D, Duration.SIXTEENTH, velocity=75, bend=1.5)
sitar.add(G.add(12), Duration.SIXTEENTH, velocity=120, bend=-1.5)
sitar.add(Bb, Duration.SIXTEENTH, velocity=70, bend=1.0)
sitar.add(D, Duration.SIXTEENTH, velocity=115, bend=-2.0)
sitar.add(G, Duration.SIXTEENTH, velocity=65)
sitar.add(G.add(12), Duration.EIGHTH, velocity=125, bend=-2.5)
sitar.rest(Duration.QUARTER)
sitar.rest(Duration.WHOLE)

# Bars 65-72: hook one more time
sitar.set(volume=0.5)
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=vel)

# Bars 73-80: fading
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=max(20, vel - 25))
for _ in range(4):
    sitar.rest(Duration.WHOLE)

# ── SAW BASS — distorted, enters bar 17 ──────────────────────
saw = score.part("saw_bass", synth="saw", volume=0.35,
                 lowpass=1200,
                 distortion=0.3, distortion_drive=4.0,
                 saturation=0.6, legato=True, glide=0.01,
                 reverb=0.1, reverb_type="spring",
                 delay=0.08, delay_time=0.222, delay_feedback=0.1,
                 sidechain=0.35, pan=0.3)

for _ in range(16):
    saw.rest(Duration.WHOLE)

# Bars 17-32: aggressive bass line — accents on 1, ghosts between
saw_line = [
    (G.add(-12), Duration.SIXTEENTH, 100), (None, Duration.SIXTEENTH, 0),
    (G.add(-12), Duration.SIXTEENTH, 65), (Bb.add(-12), Duration.SIXTEENTH, 60),
    (G.add(-12), Duration.SIXTEENTH, 95), (None, Duration.SIXTEENTH, 0),
    (F.add(-12), Duration.EIGHTH, 58),
    (G.add(-12), Duration.SIXTEENTH, 98), (D.add(-12), Duration.SIXTEENTH, 62),
    (G.add(-12), Duration.SIXTEENTH, 68), (None, Duration.SIXTEENTH, 0),
    (Eb.add(-12), Duration.EIGHTH, 55),
    (G.add(-12), Duration.EIGHTH, 92),
]
for _ in range(16):
    for note, dur, vel in saw_line:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=vel)

# Bars 33-40: silent — breakdown
for _ in range(8):
    saw.rest(Duration.WHOLE)

# Bars 41-48: returns for build
for _ in range(8):
    for note, dur, vel in saw_line:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=vel)

# Bars 49-72: full power
saw.set(volume=0.4)
for _ in range(24):
    for note, dur, vel in saw_line:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=min(105, vel + 5))

# Bars 73-80: fading
saw.set(volume=0.2)
for _ in range(4):
    for note, dur, vel in saw_line:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=max(25, vel - 25))
for _ in range(4):
    saw.rest(Duration.WHOLE)

# ── MELLOTRON CHOIR — the drop, enters bar 25 ────────────────
mello = score.part("mellotron", instrument="mellotron_flute", volume=0.35,
                   reverb=0.45, reverb_type="taj_mahal",
                   chorus=0.2, chorus_rate=0.06, chorus_depth=0.01,
                   pan=-0.15)

for _ in range(24):
    mello.rest(Duration.WHOLE)

# Bars 25-32: THE DROP — choir chords, heavens open
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=55)

# Bars 33-48: silent
for _ in range(16):
    mello.rest(Duration.WHOLE)

# Bars 49-56: back for beast mode
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=58)

# Bars 57-64: under sitar solo
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=50)

# Bars 65-72: last drop — full
mello.set(volume=0.28)
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=62)

# Bars 73-80: fading
for vel in [52, 42, 35, 28, 20, 12, 0, 0]:
    if vel > 0:
        mello.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        mello.rest(Duration.WHOLE)

# ── TIMPANI — war drums, bars 41-48 and 65-72 ────────────────
timp = score.part("timpani", instrument="timpani", volume=0.4,
                  reverb=0.25, reverb_type="cathedral",
                  delay=0.06, delay_time=0.222, delay_feedback=0.08,
                  pan=-0.05)

for _ in range(40):
    timp.rest(Duration.WHOLE)

# Bars 41-48: the build — war drums, 16th rolls crescendo
for bar in range(8):
    if bar < 4:
        timp.add(G.add(-12), Duration.QUARTER, velocity=min(85, 60 + bar * 8))
        timp.rest(Duration.DOTTED_HALF)
    else:
        for i in range(16):
            timp.add(G.add(-12), Duration.SIXTEENTH, velocity=min(98, 55 + i * 3))

# Bars 49-64: sparse hits with the beat
for _ in range(16):
    timp.add(G.add(-12), Duration.QUARTER, velocity=72)
    timp.rest(Duration.DOTTED_HALF)

# Bars 65-72: last drop — full rolls
for bar in range(8):
    if bar % 2 == 1:
        for i in range(16):
            timp.add(G.add(-12), Duration.SIXTEENTH, velocity=min(95, 52 + i * 3))
    else:
        timp.add(G.add(-12), Duration.HALF, velocity=78)
        timp.rest(Duration.HALF)

# Bars 73-80: fading
for vel in [65, 52, 40, 28, 0, 0, 0, 0]:
    if vel > 0:
        timp.add(G.add(-12), Duration.QUARTER, velocity=vel)
        timp.rest(Duration.DOTTED_HALF)
    else:
        timp.rest(Duration.WHOLE)

# ── SINGING BOWL — section markers ───────────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.25,
                  reverb=0.5, reverb_type="taj_mahal",
                  delay=0.12, delay_time=0.444, delay_feedback=0.15,
                  pan=0.2)

markers = {1: 60, 9: 55, 25: 62, 33: 50, 49: 65, 65: 60, 73: 48}
for bar in range(1, 81):
    if bar in markers:
        bowl.add(G.add(-24), Duration.WHOLE, velocity=markers[bar])
    else:
        bowl.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 135")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing BEAST MODE (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing BEAST MODE...")
    play_score(score)
