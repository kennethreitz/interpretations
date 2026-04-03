"""
SLEIGHT OF HAND — you never see the next move coming.
Every section is a surprise. Each one beautiful.
Together, they shouldn't work. They do.
D minor, 100 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("D", "minor")
s = key.scale  # D E F G A Bb C

D  = s[0]; E  = s[1]; F  = s[2]; G  = s[3]
A  = s[4]; Bb = s[5]; C  = s[6]

score = Score("4/4", bpm=100)

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

prog = key.progression("i", "VII", "VI", "v")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (72 bars, ~4:19):
#   Bars  1-8:   Music box — innocent, delicate, a lullaby
#   Bars  9-16:  Didgeridoo drone — the room changes completely
#   Bars 17-24:  Piano jazz chords — wait, where are we?
#   Bars 25-32:  808 + trap hats slam in — now it's hip hop
#   Bars 33-40:  Everything drops to solo theremin — aching, alone
#   Bars 41-48:  Choir swells from nowhere — cathedral out of thin air
#   Bars 49-56:  Acid 303 rips through the choir — what??
#   Bars 57-64:  Music box returns — but now the 808 is underneath
#   Bars 65-72:  Everything at once — the trick revealed
# ═══════════════════════════════════════════════════════════════════

# ── MUSIC BOX — innocent opening, you think you know this track ──
box = score.part("music_box", instrument="music_box", volume=0.35,
                 reverb=0.5, reverb_type="taj_mahal",
                 delay=0.2, delay_time=0.3, delay_feedback=0.3,
                 pan=-0.2, humanize=0.08)

# Bars 1-8: simple melody — like a child's toy
box_melody = [
    (D.add(12), Duration.QUARTER, 72), (F.add(12), Duration.QUARTER, 68),
    (A.add(12), Duration.HALF, 75),
    (G.add(12), Duration.QUARTER, 70), (F.add(12), Duration.EIGHTH, 65),
    (E.add(12), Duration.EIGHTH, 62), (D.add(12), Duration.HALF, 68),
    (A, Duration.QUARTER, 65), (D.add(12), Duration.QUARTER, 70),
    (F.add(12), Duration.HALF, 72),
    (E.add(12), Duration.QUARTER, 68), (D.add(12), Duration.QUARTER, 65),
    (C.add(12), Duration.QUARTER, 62), (D.add(12), Duration.QUARTER, 70),
    (None, Duration.QUARTER, 0), (A.add(12), Duration.QUARTER, 72),
    (G.add(12), Duration.QUARTER, 68), (F.add(12), Duration.QUARTER, 65),
    (D.add(12), Duration.WHOLE, 72),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in box_melody:
    if note is None:
        box.rest(dur)
    else:
        box.add(note, dur, velocity=vel)

# Bars 9-56: silent
for _ in range(48):
    box.rest(Duration.WHOLE)

# Bars 57-64: RETURNS — same melody, but everything's different now
box.set(volume=0.3)
for note, dur, vel in box_melody:
    if note is None:
        box.rest(dur)
    else:
        box.add(note, dur, velocity=max(30, vel - 8))

# Bars 65-72: continues into the finale, fading
for note, dur, vel in box_melody[:10]:
    if note is None:
        box.rest(dur)
    else:
        box.add(note, dur, velocity=max(25, vel - 20))
for _ in range(4):
    box.rest(Duration.WHOLE)

# ── DIDGERIDOO — the room changes, bar 9 ─────────────────────
didge = score.part("didge", instrument="didgeridoo", volume=0.12,
                   reverb=0.35, reverb_type="cathedral",
                   chorus=0.2, chorus_rate=0.05, chorus_depth=0.01,
                   lowpass=350, pan=0.1)

for _ in range(8):
    didge.rest(Duration.WHOLE)

# Bars 9-16: primal drone — where did the music box go?
for _ in range(8):
    didge.add(D.add(-24), Duration.WHOLE, velocity=62)

# Bars 17-24: fades under the piano
for vel in [52, 42, 32, 22, 15, 10, 5, 0]:
    if vel > 0:
        didge.add(D.add(-24), Duration.WHOLE, velocity=vel)
    else:
        didge.rest(Duration.WHOLE)

# Silent rest of track
for _ in range(48):
    didge.rest(Duration.WHOLE)

# ── SINGING BOWL — transitions, the thread ───────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.3,
                  reverb=0.8, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.6, delay_feedback=0.2,
                  pan=0.25)

# Strike at every section change
section_bars = {1: 60, 9: 65, 17: 58, 25: 70, 33: 62, 41: 68,
                49: 55, 57: 65, 65: 72}
for bar in range(1, 73):
    if bar in section_bars:
        bowl.add(D.add(-24), Duration.WHOLE, velocity=section_bars[bar])
    else:
        bowl.rest(Duration.WHOLE)

# ── PIANO — jazz chords out of nowhere, bar 17 ───────────────
piano = score.part("piano", instrument="piano", volume=0.4,
                   reverb=0.45, reverb_type="taj_mahal",
                   delay=0.1, delay_time=0.3, delay_feedback=0.15,
                   pan=-0.15, humanize=0.1)

for _ in range(16):
    piano.rest(Duration.WHOLE)

# Bars 17-24: jazzy — extended chords, unexpected voicings
jazz_prog = key.progression("i", "iv", "VII", "III")
for _ in range(2):
    for chord in jazz_prog:
        piano.add(chord, Duration.EIGHTH, velocity=72)
        piano.rest(Duration.QUARTER)
        piano.rest(Duration.EIGHTH)
        piano.add(chord, Duration.EIGHTH, velocity=58)
        piano.rest(Duration.QUARTER)
        piano.rest(Duration.EIGHTH)

# Bars 25-32: stays through the beat drop — anchoring the chaos
for _ in range(2):
    for chord in jazz_prog:
        piano.add(chord, Duration.EIGHTH, velocity=68)
        piano.rest(Duration.DOTTED_QUARTER)
        piano.rest(Duration.HALF)

# Bars 33-40: silent — theremin owns this
for _ in range(8):
    piano.rest(Duration.WHOLE)

# Bars 41-48: returns under choir — gentle arps
for _ in range(2):
    for chord in prog:
        piano.add(chord, Duration.QUARTER, velocity=52)
        piano.rest(Duration.DOTTED_HALF)

# Bars 49-56: silent — 303 owns this
for _ in range(8):
    piano.rest(Duration.WHOLE)

# Bars 57-72: underneath the music box return
for _ in range(4):
    for chord in prog:
        piano.add(chord, Duration.EIGHTH, velocity=55)
        piano.rest(Duration.DOTTED_QUARTER)
        piano.rest(Duration.HALF)

# ── 808 — slams in at bar 25 ─────────────────────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=0.6,
                 lowpass=200, distortion=0.2, distortion_drive=3.0,
                 sub_osc=0.5, saturation=0.4, sidechain=0.3)

roots = [D.add(-24), C.add(-24), Bb.add(-24), A.add(-24)]

for _ in range(24):
    sub.rest(Duration.WHOLE)

# Bars 25-32: drops in — the shock
for _ in range(2):
    for root in roots:
        sub.add(root, Duration.WHOLE, velocity=40)

# Bars 33-40: stays through theremin — the weight underneath
for _ in range(8):
    sub.add(D.add(-24), Duration.WHOLE, velocity=30)

# Bars 41-48: fades under choir
for vel in [28, 25, 22, 18, 15, 12, 8, 0]:
    if vel > 0:
        sub.add(D.add(-24), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# Bars 49-56: back with the 303
for _ in range(2):
    for root in roots:
        sub.add(root, Duration.WHOLE, velocity=38)

# Bars 57-72: underneath the music box — the big reveal
for _ in range(4):
    for root in roots:
        sub.add(root, Duration.WHOLE, velocity=35)

# ── TRAP HATS — with the 808, bar 25 ─────────────────────────
hats = score.part("hats", volume=0.25, pan=0.2, humanize=0.05)

for _ in range(24):
    hats.rest(Duration.WHOLE)

# Bars 25-32: trap hats — 16ths with rolls
for bar in range(8):
    if bar % 4 == 3:
        for i in range(32):
            hats.hit(CH, 0.125, velocity=min(85, 40 + i * 2))
    else:
        for beat in range(4):
            hats.hit(CH, Duration.SIXTEENTH, velocity=70)
            hats.hit(CH, Duration.SIXTEENTH, velocity=42)
            hats.hit(CH, Duration.SIXTEENTH, velocity=55)
            hats.hit(CH, Duration.SIXTEENTH, velocity=38)

# Bars 33-56: silent
for _ in range(24):
    hats.rest(Duration.WHOLE)

# Bars 57-64: back with the music box — gentler
for _ in range(8):
    for beat in range(4):
        hats.hit(CH, Duration.EIGHTH, velocity=58)
        hats.hit(CH, Duration.EIGHTH, velocity=35)

# Bars 65-72: full trap hats for the finale
for bar in range(8):
    if bar % 4 == 3:
        for i in range(32):
            hats.hit(CH, 0.125, velocity=min(90, 42 + i * 2))
    else:
        for beat in range(4):
            hats.hit(CH, Duration.SIXTEENTH, velocity=72)
            hats.hit(CH, Duration.SIXTEENTH, velocity=45)
            hats.hit(CH, Duration.SIXTEENTH, velocity=58)
            hats.hit(CH, Duration.SIXTEENTH, velocity=40)

# ── KICK + SNARE — boom bap, bars 25-32 and 57-72 ────────────
kick = score.part("kick", volume=0.7, humanize=0.04,
                  distortion=0.08, distortion_drive=1.5)

snare = score.part("snare", volume=0.5, humanize=0.04,
                   reverb=0.2, reverb_decay=0.8,
                   delay=0.06, delay_time=0.3, delay_feedback=0.1,
                   pan=0.05)

for _ in range(24):
    kick.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)

# Bars 25-32: the drop
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=110)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=92)
    kick.hit(K, Duration.QUARTER, velocity=105)
    kick.rest(Duration.QUARTER)

    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=102)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=105)

# Bars 33-56: silent
for _ in range(24):
    kick.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)

# Bars 57-72: back for the reveal + finale
for _ in range(16):
    kick.hit(K, Duration.QUARTER, velocity=108)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=90)
    kick.hit(K, Duration.QUARTER, velocity=102)
    kick.rest(Duration.QUARTER)

    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=100)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=102)

# ── THEREMIN — solo, bar 33, the emotional gut punch ──────────
theremin = score.part("theremin", instrument="theremin", volume=0.35,
                      reverb=0.4, reverb_type="taj_mahal",
                      delay=0.12, delay_time=0.3, delay_feedback=0.15,
                      pan=-0.1, humanize=0.06)

for _ in range(32):
    theremin.rest(Duration.WHOLE)

# Bars 33-40: alone with just the 808 — aching
theremin.add(A, Duration.WHOLE, velocity=72, bend=0.5)
theremin.add(F, Duration.WHOLE, velocity=68, bend=-0.25)
theremin.rest(Duration.WHOLE)
theremin.add(D.add(12), Duration.HALF, velocity=78, bend=1.0)
theremin.add(C.add(12), Duration.HALF, velocity=72, bend=-0.5)
theremin.add(Bb, Duration.WHOLE, velocity=70, bend=0.25)
theremin.rest(Duration.WHOLE)
theremin.add(A, Duration.HALF, velocity=65, bend=-0.15)
theremin.add(D, Duration.HALF, velocity=60)
theremin.rest(Duration.WHOLE)

# Bars 41-72: silent
for _ in range(32):
    theremin.rest(Duration.WHOLE)

# ── CHOIR — swells from nowhere, bar 41 ──────────────────────
choir = score.part("choir", instrument="mellotron_choir", volume=0.15,
                   reverb=0.8, reverb_type="cathedral",
                   chorus=0.3, chorus_rate=0.08, chorus_depth=0.012,
                   pan=0.2)

for _ in range(40):
    choir.rest(Duration.WHOLE)

# Bars 41-48: cathedral appears — where did this come from?
for vel in [25, 32, 38, 42, 45, 48, 50, 52]:
    choir.add(prog[vel % 4], Duration.WHOLE, velocity=vel)

# Bars 49-56: continues under the 303
for _ in range(2):
    for chord in prog:
        choir.add(chord, Duration.WHOLE, velocity=45)

# Bars 57-64: fading
for vel in [42, 38, 32, 28, 22, 18, 12, 0]:
    if vel > 0:
        choir.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        choir.rest(Duration.WHOLE)

# Bars 65-72: silent
for _ in range(8):
    choir.rest(Duration.WHOLE)

# ── ACID 303 — rips through the choir, bar 49 ────────────────
acid = score.part("303", synth="saw", volume=0.4,
                  lowpass=2000, lowpass_q=10.0,
                  distortion=0.3, distortion_drive=3.5,
                  saturation=0.7, legato=True, glide=0.05,
                  reverb=0.2, reverb_type="spring",
                  delay=0.2, delay_time=0.3, delay_feedback=0.3,
                  pan=-0.25)
acid.lfo("lowpass", rate=0.02, min=600, max=8000, bars=8, shape="saw")

for _ in range(48):
    acid.rest(Duration.WHOLE)

# Bars 49-56: acid line — screaming through the choir
acid_pattern = [
    (D, Duration.SIXTEENTH, 105), (None, Duration.SIXTEENTH, 0),
    (D, Duration.SIXTEENTH, 98), (F, Duration.SIXTEENTH, 92),
    (D, Duration.SIXTEENTH, 108), (None, Duration.SIXTEENTH, 0),
    (C, Duration.EIGHTH, 88),
    (D, Duration.SIXTEENTH, 110), (A.add(-12), Duration.SIXTEENTH, 95),
    (D, Duration.SIXTEENTH, 102), (None, Duration.SIXTEENTH, 0),
    (Bb.add(-12), Duration.EIGHTH, 92),
    (D, Duration.EIGHTH, 108),
]
for _ in range(8):
    for note, dur, vel in acid_pattern:
        if note is None:
            acid.rest(dur)
        else:
            acid.add(note, dur, velocity=vel)

# Bars 57-72: silent — it was just a visit
for _ in range(16):
    acid.rest(Duration.WHOLE)

# ── STRINGS — only in the finale, the grand reveal ───────────
strings = score.part("strings", instrument="string_ensemble", volume=0.12,
                     reverb=0.55, reverb_type="cathedral",
                     chorus=0.2, chorus_rate=0.15, chorus_depth=0.006,
                     pan=-0.2)

for _ in range(64):
    strings.rest(Duration.WHOLE)

# Bars 65-72: everything together — strings tie the bow
for vel in [30, 38, 45, 50, 52, 48, 40, 28]:
    strings.add(prog[vel % 4], Duration.WHOLE, velocity=vel)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 100")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing SLEIGHT OF HAND (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing SLEIGHT OF HAND...")
    play_score(score)
