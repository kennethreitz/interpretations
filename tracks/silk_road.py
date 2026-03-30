"""
SILK ROAD — a caravan picking up musicians along the ancient trade route.
Each civilization layers on top, nobody leaves. D minor throughout.

China → India → Persia → Mediterranean → All Together
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("D", "minor")
s = key.scale

# D minor: D E F G A Bb C
D  = s[0]; E  = s[1]; F  = s[2]; G  = s[3]
A  = s[4]; Bb = s[5]; C  = s[6]

score = Score("4/4", bpm=95)

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (80 bars, ~5 min):
#   Bars  1-16:  China — koto solo, pentatonic
#   Bars 17-32:  India — sitar + tabla join the koto
#   Bars 33-48:  Persia — mandolin (oud) + doumbek layer in
#   Bars 49-64:  Mediterranean — guitar + cajon, flamenco tinge
#   Bars 65-80:  All Together — full caravan, everyone plays
# ═══════════════════════════════════════════════════════════════════

# ── KOTO — China, pentatonic, sparse ───────────────────────────
# D minor pentatonic: D F G A C (removes E and Bb)
koto = score.part("koto", instrument="koto", volume=0.4,
                  reverb=0.5, reverb_type="taj_mahal",
                  delay=0.2, delay_time=0.316, delay_feedback=0.3,
                  humanize=0.1)

# Bars 1-16: solo koto — contemplative, lots of space
koto_phrases = [
    # Phrase 1: simple, announcing
    [(D.add(12), Duration.HALF, 80), (None, Duration.QUARTER, 0),
     (A, Duration.QUARTER, 70)],
    [(G, Duration.QUARTER, 75), (F, Duration.QUARTER, 68),
     (D, Duration.HALF, 72)],
    # Phrase 2: climbing
    [(None, Duration.QUARTER, 0), (A, Duration.QUARTER, 75),
     (C.add(12), Duration.QUARTER, 82), (D.add(12), Duration.QUARTER, 78)],
    [(F.add(12), Duration.HALF, 85), (D.add(12), Duration.QUARTER, 75),
     (None, Duration.QUARTER, 0)],
    # Phrase 3: descending
    [(D.add(12), Duration.QUARTER, 80), (C.add(12), Duration.EIGHTH, 72),
     (A, Duration.EIGHTH, 68), (G, Duration.HALF, 75)],
    [(F, Duration.QUARTER, 70), (D, Duration.QUARTER, 65),
     (None, Duration.HALF, 0)],
    # Phrase 4: resolving
    [(A, Duration.QUARTER, 78), (G, Duration.EIGHTH, 70),
     (F, Duration.EIGHTH, 65), (G, Duration.QUARTER, 72),
     (A, Duration.QUARTER, 75)],
    [(D, Duration.WHOLE, 80)],
]
for _ in range(2):
    for phrase in koto_phrases:
        for note, dur, vel in phrase:
            if note is None:
                koto.rest(dur)
            else:
                koto.add(note, dur, velocity=vel)

# Bars 17-80: koto continues, same phrases, quieter as others join
for _ in range(2):
    for phrase in koto_phrases:
        for note, dur, vel in phrase:
            if note is None:
                koto.rest(dur)
            else:
                koto.add(note, dur, velocity=max(35, vel - 15))

for _ in range(6):
    for phrase in koto_phrases:
        for note, dur, vel in phrase:
            if note is None:
                koto.rest(dur)
            else:
                koto.add(note, dur, velocity=max(30, vel - 25))

# ── SITAR — India, enters bar 17 ───────────────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.45,
                   reverb=0.35, reverb_type="taj_mahal",
                   delay=0.25, delay_time=0.333, delay_feedback=0.3,
                   pan=-0.2, humanize=0.1)

# Bars 1-16: silent
for _ in range(16):
    sitar.rest(Duration.WHOLE)

# Bars 17-32: sitar melody — raga-influenced, ornamental
sitar_phrases = [
    [(D, Duration.HALF, 85), (E, Duration.QUARTER, 75),
     (F, Duration.QUARTER, 80)],
    [(G, Duration.QUARTER, 85), (A, Duration.EIGHTH, 78),
     (G, Duration.EIGHTH, 72), (F, Duration.HALF, 80)],
    [(A, Duration.QUARTER, 90), (Bb, Duration.EIGHTH, 82),
     (A, Duration.EIGHTH, 78), (G, Duration.QUARTER, 75),
     (F, Duration.QUARTER, 70)],
    [(E, Duration.QUARTER, 72), (D, Duration.DOTTED_HALF, 85)],
]
for _ in range(4):
    for phrase in sitar_phrases:
        for note, dur, vel in phrase:
            sitar.add(note, dur, velocity=vel)

# Bars 33-80: sitar continues through all sections
for _ in range(12):
    for phrase in sitar_phrases:
        for note, dur, vel in phrase:
            sitar.add(note, dur, velocity=vel)

# ── TABLA — India, enters bar 17 ───────────────────────────────
NA  = DrumSound.TABLA_NA
TIT = DrumSound.TABLA_TIT
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
GEB = DrumSound.TABLA_GE_BEND

tabla = score.part("tabla", volume=0.3, reverb=0.2, reverb_decay=1.0,
                   humanize=0.08)

for _ in range(16):
    tabla.rest(Duration.WHOLE)

# Bars 17-80: keherwa groove throughout
for bar in range(64):
    if bar % 8 == 7:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=95, articulation="accent")
        tabla.hit(GEB, Duration.EIGHTH, velocity=108)
        tabla.hit(NA, Duration.EIGHTH, velocity=72)
        tabla.hit(GEB, Duration.EIGHTH, velocity=105)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=90, articulation="accent")
        tabla.hit(NA, Duration.SIXTEENTH, velocity=62)
        tabla.hit(TIT, Duration.SIXTEENTH, velocity=52)
        tabla.hit(GEB, Duration.QUARTER, velocity=112)
    else:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=85, articulation="accent")
        tabla.hit(GE, Duration.EIGHTH, velocity=55)
        tabla.hit(NA, Duration.EIGHTH, velocity=65)
        tabla.hit(TIT, Duration.EIGHTH, velocity=42)
        tabla.hit(NA, Duration.EIGHTH, velocity=60)
        tabla.hit(TIT, Duration.EIGHTH, velocity=38)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=80, articulation="accent")
        tabla.hit(NA, Duration.EIGHTH, velocity=58)

# ── MANDOLIN (oud) — Persia, enters bar 33 ─────────────────────
oud = score.part("oud", instrument="mandolin", volume=0.4,
                 reverb=0.4, reverb_type="cathedral",
                 delay=0.15, delay_time=0.25, delay_feedback=0.25,
                 pan=0.2, humanize=0.08)

for _ in range(32):
    oud.rest(Duration.WHOLE)

# Bars 33-80: maqam-influenced melody — chromatic ornaments
oud_phrases = [
    # Descending maqam feel
    [(A, Duration.EIGHTH, 88), (Bb, Duration.EIGHTH, 78),
     (A, Duration.QUARTER, 85), (G, Duration.QUARTER, 80),
     (F, Duration.QUARTER, 75)],
    [(E, Duration.EIGHTH, 72), (F, Duration.EIGHTH, 68),
     (E, Duration.QUARTER, 75), (D, Duration.HALF, 82)],
    # Climbing with ornaments
    [(D, Duration.EIGHTH, 80), (E, Duration.SIXTEENTH, 70),
     (F, Duration.SIXTEENTH, 72), (G, Duration.QUARTER, 82),
     (A, Duration.QUARTER, 88), (None, Duration.QUARTER, 0)],
    [(Bb, Duration.QUARTER, 85), (A, Duration.EIGHTH, 78),
     (G, Duration.EIGHTH, 72), (A, Duration.HALF, 80)],
]
for _ in range(12):
    for phrase in oud_phrases:
        for note, dur, vel in phrase:
            if note is None:
                oud.rest(dur)
            else:
                oud.add(note, dur, velocity=vel)

# ── DOUMBEK — Persia, enters bar 33 ────────────────────────────
DKD = DrumSound.DOUMBEK_DUM
DKT = DrumSound.DOUMBEK_TEK
DKK = DrumSound.DOUMBEK_KA

doumbek = score.part("doumbek", volume=0.3, reverb=0.15, humanize=0.06)

for _ in range(32):
    doumbek.rest(Duration.WHOLE)

# Bars 33-80: maqsoum-inspired rhythm
for bar in range(48):
    if bar % 8 == 7:
        # Fill
        doumbek.hit(DKD, Duration.SIXTEENTH, velocity=100, articulation="accent")
        doumbek.hit(DKT, Duration.SIXTEENTH, velocity=65)
        doumbek.hit(DKT, Duration.SIXTEENTH, velocity=62)
        doumbek.hit(DKD, Duration.SIXTEENTH, velocity=95)
        doumbek.hit(DKT, Duration.SIXTEENTH, velocity=68)
        doumbek.hit(DKK, Duration.SIXTEENTH, velocity=58)
        doumbek.hit(DKD, Duration.SIXTEENTH, velocity=100, articulation="accent")
        doumbek.hit(DKT, Duration.SIXTEENTH, velocity=65)
        doumbek.hit(DKT, Duration.SIXTEENTH, velocity=60)
        doumbek.hit(DKK, Duration.SIXTEENTH, velocity=55)
        doumbek.hit(DKD, Duration.SIXTEENTH, velocity=98)
        doumbek.hit(DKT, Duration.SIXTEENTH, velocity=62)
        doumbek.hit(DKD, Duration.QUARTER, velocity=110, articulation="marcato")
    else:
        # Maqsoum: DUM-tek-tek-DUM-tek
        doumbek.hit(DKD, Duration.EIGHTH, velocity=90)
        doumbek.hit(DKT, Duration.EIGHTH, velocity=60)
        doumbek.hit(DKT, Duration.EIGHTH, velocity=58)
        doumbek.hit(DKD, Duration.EIGHTH, velocity=85)
        doumbek.hit(DKT, Duration.EIGHTH, velocity=62)
        doumbek.hit(DKT, Duration.EIGHTH, velocity=55)
        doumbek.hit(DKT, Duration.EIGHTH, velocity=58)
        doumbek.hit(DKT, Duration.EIGHTH, velocity=52)

# ── GUITAR — Mediterranean, enters bar 49 ──────────────────────
guitar = score.part("guitar", instrument="acoustic_guitar", volume=0.35,
                    reverb=0.35, reverb_type="cathedral",
                    humanize=0.1)

for _ in range(48):
    guitar.rest(Duration.WHOLE)

# Bars 49-80: fingerpicked arpeggios — flamenco-tinged
prog = key.progression("i", "VII", "VI", "v")
guitar_arps = [
    # i — Dm
    [D.add(-12), A.add(-12), D, F, A, F, D, A.add(-12)],
    # VII — C
    [C.add(-12), G.add(-12), C, E, G, E, C, G.add(-12)],
    # VI — Bb
    [Bb.add(-24), F.add(-12), Bb.add(-12), D, F, D, Bb.add(-12), F.add(-12)],
    # v — Am
    [A.add(-24), E.add(-12), A.add(-12), C, E, C, A.add(-12), E.add(-12)],
]
for _ in range(8):
    for arp in guitar_arps:
        for note in arp:
            guitar.add(note, Duration.EIGHTH, velocity=75)

# ── CAJON — Mediterranean, enters bar 49 ────────────────────────
CS = DrumSound.CAJON_SLAP
CT = DrumSound.CAJON_TAP
CSS = DrumSound.CAJON_SLAP_SNARE

cajon = score.part("cajon", volume=0.25, reverb=0.3, reverb_type="cathedral",
                   humanize=0.08)

for _ in range(48):
    cajon.rest(Duration.WHOLE)

# Bars 49-80: flamenco-ish groove
for bar in range(32):
    if bar % 4 == 3:
        # Fill
        cajon.hit(CSS, Duration.SIXTEENTH, velocity=100, articulation="accent")
        cajon.hit(CT, Duration.SIXTEENTH, velocity=55)
        cajon.hit(CSS, Duration.SIXTEENTH, velocity=98)
        cajon.hit(CT, Duration.SIXTEENTH, velocity=52)
        cajon.hit(CSS, Duration.SIXTEENTH, velocity=102, articulation="accent")
        cajon.hit(CT, Duration.SIXTEENTH, velocity=55)
        cajon.hit(CS, Duration.SIXTEENTH, velocity=95)
        cajon.hit(CT, Duration.SIXTEENTH, velocity=50)
        cajon.hit(CSS, Duration.SIXTEENTH, velocity=105, articulation="accent")
        cajon.hit(CT, Duration.SIXTEENTH, velocity=55)
        cajon.hit(CS, Duration.SIXTEENTH, velocity=92)
        cajon.hit(CT, Duration.SIXTEENTH, velocity=52)
        cajon.hit(CSS, Duration.QUARTER, velocity=110, articulation="marcato")
    else:
        cajon.hit(CS, Duration.EIGHTH, velocity=88, articulation="accent")
        cajon.hit(CT, Duration.EIGHTH, velocity=48)
        cajon.hit(CSS, Duration.EIGHTH, velocity=82)
        cajon.hit(CT, Duration.EIGHTH, velocity=45)
        cajon.hit(CS, Duration.EIGHTH, velocity=85, articulation="accent")
        cajon.hit(CT, Duration.EIGHTH, velocity=50)
        cajon.hit(CSS, Duration.EIGHTH, velocity=78)
        cajon.hit(CT, Duration.EIGHTH, velocity=45)

# ── TAMBURA — the thread connecting everything ──────────────────
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.15,
                     reverb=0.7, reverb_type="taj_mahal",
                     chorus=0.3, chorus_rate=0.08, chorus_depth=0.01,
                     lowpass=1000)

for _ in range(80):
    tambura.add(D.add(-24), Duration.HALF)
    tambura.add(A.add(-24), Duration.HALF)

# ── PAD — swells in the last section ───────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.1,
                 reverb=0.6, reverb_type="taj_mahal",
                 chorus=0.4, chorus_rate=0.2, chorus_depth=0.008,
                 lowpass=1800)

for _ in range(64):
    pad.rest(Duration.WHOLE)

# Bars 65-80: all together, pad glues it
for _ in range(4):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=60)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 95")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing SILK ROAD (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing SILK ROAD...")
    play_score(score)
