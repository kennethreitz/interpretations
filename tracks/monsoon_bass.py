"""
MONSOON BASS — Indian classical meets trip-hop.
Talvin Singh meets Massive Attack. Tabla over breakbeat,
sitar loops through delay fog, 808 sub holds it all down.
"""

from pytheory import Key, Duration, Score, play_score
from pytheory.rhythm import DrumSound

# ── Scale ────────────────────────────────────────────────────────
key = Key("A", "phrygian")
s = key.scale  # A Bb C D E F G

Sa  = s[0]   # A  (Sa)
Re  = s[1]   # Bb (komal Re)
Ga  = s[2]   # C  (komal Ga)
Ma  = s[3]   # D  (Ma)
Pa  = s[4]   # E  (Pa)
Dha = s[5]   # F  (komal Dha)
Ni  = s[6]   # G  (komal Ni)

score = Score("4/4", bpm=98, system="shruti", temperament="just")

# ── Tabla Bols ──────────────────────────────────────────────────
NA  = DrumSound.TABLA_NA
TIT = DrumSound.TABLA_TIT
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
KE  = DrumSound.TABLA_KE
GEB = DrumSound.TABLA_GE_BEND

# ── BREAKBEAT — the spine ───────────────────────────────────────
score.drums("breakbeat", repeats=16, fill="bayan", fill_every=8)
score.set_drum_effects(reverb=0.2, reverb_decay=1.0, volume=0.35, humanize=0.12)

# ── TABLA LAYER — rides on top of the breakbeat ─────────────────
tabla = score.part("tabla", volume=0.0, reverb=0.3, reverb_decay=1.2,
                   humanize=0.08)

# Silent for 4 bars — let the beat establish
for _ in range(4):
    tabla.rest(Duration.WHOLE)

# Bars 5-16: looping tabla pattern (keherwa-influenced)
tabla.set(volume=0.35)
for _ in range(12):
    tabla.hit(tDHA, Duration.EIGHTH, velocity=95, articulation="accent")
    tabla.hit(GE, Duration.EIGHTH, velocity=65)
    tabla.hit(NA, Duration.EIGHTH, velocity=75)
    tabla.hit(TIT, Duration.EIGHTH, velocity=50)
    tabla.hit(NA, Duration.EIGHTH, velocity=70)
    tabla.hit(TIT, Duration.EIGHTH, velocity=45)
    tabla.hit(tDHA, Duration.EIGHTH, velocity=88, articulation="accent")
    tabla.hit(NA, Duration.EIGHTH, velocity=68)

# ── 808 SUB BASS — deep, sustained, minimal ────────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.55,
                 distortion=0.3, distortion_drive=4.0,
                 lowpass=160, lowpass_q=2.0)

# Bars 1-4: just the root, establishing gravity
for _ in range(4):
    sub.add(Sa.add(-24), Duration.HALF)          # Sa low
    sub.rest(Duration.QUARTER)
    sub.add(Sa.add(-24), Duration.QUARTER)

# Bars 5-16: minimal bass line, mostly Sa and Pa
for _ in range(3):
    sub.add(Sa.add(-24), Duration.HALF)
    sub.rest(Duration.QUARTER)
    sub.add(Pa.add(-24), Duration.QUARTER)
    sub.add(Sa.add(-24), Duration.HALF)
    sub.rest(Duration.HALF)
    sub.add(Ma.add(-24), Duration.HALF)
    sub.rest(Duration.QUARTER)
    sub.add(Sa.add(-24), Duration.QUARTER)
    sub.add(Sa.add(-24), Duration.DOTTED_HALF)
    sub.rest(Duration.QUARTER)

# ── SITAR LOOP — hypnotic, delay-drenched ──────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.0,
                   reverb=0.5, reverb_type="taj_mahal",
                   delay=0.45, delay_time=0.306, delay_feedback=0.5,
                   pan=-0.2, saturation=0.2, humanize=0.08)

# Silent for 2 bars
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 3-8: sparse, mysterious — notes float in delay
sitar.set(volume=0.4)
sitar_phrase_a = [
    (Sa, Duration.QUARTER, 85),
    (None, Duration.EIGHTH, 0),
    (Re, Duration.EIGHTH, 70),
    (Ga, Duration.QUARTER, 90),
    (None, Duration.QUARTER, 0),
    # bar 2
    (Ma, Duration.EIGHTH, 80),
    (Ga, Duration.EIGHTH, 70),
    (Re, Duration.QUARTER, 75),
    (Sa, Duration.QUARTER, 65),
    (None, Duration.QUARTER, 0),
]
for _ in range(3):
    for note, dur, vel in sitar_phrase_a:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=vel)

# Bars 9-12: more active, higher register
sitar.set(volume=0.45)
sitar_phrase_b = [
    (Pa, Duration.EIGHTH, 100),
    (Ma, Duration.EIGHTH, 80),
    (Pa, Duration.QUARTER, 95),
    (None, Duration.EIGHTH, 0),
    (Dha, Duration.EIGHTH, 85),
    (Pa, Duration.QUARTER, 90),
    # bar 2
    (Ma, Duration.QUARTER, 80),
    (Ga, Duration.EIGHTH, 70),
    (Re, Duration.EIGHTH, 75),
    (Sa, Duration.HALF, 85),
]
for _ in range(2):
    for note, dur, vel in sitar_phrase_b:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=vel)

# Bars 13-16: climax — faster, descending runs
sitar.set(volume=0.5)
sitar_phrase_c = [
    (Sa.add(12), Duration.EIGHTH, 115),
    (Ni, Duration.EIGHTH, 100),
    (Dha, Duration.EIGHTH, 90),
    (Pa, Duration.EIGHTH, 85),
    (Ma, Duration.QUARTER, 95),
    (Ga, Duration.QUARTER, 80),
    # bar 2
    (Re, Duration.EIGHTH, 75),
    (Sa, Duration.EIGHTH, 70),
    (Re, Duration.QUARTER, 80),
    (Ma, Duration.QUARTER, 90),
    (Sa, Duration.QUARTER, 75),
    (None, Duration.QUARTER, 0),
]
for _ in range(2):
    for note, dur, vel in sitar_phrase_c:
        if note is None:
            sitar.rest(dur)
        else:
            sitar.add(note, dur, velocity=vel)

# ── PAD — dark, atmospheric wash ────────────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.0,
                 reverb=0.7, reverb_type="taj_mahal",
                 chorus=0.4, chorus_rate=0.15, chorus_depth=0.01,
                 lowpass=1400, pan=0.1)
pad.lfo("lowpass", rate=0.0625, min=600, max=2000, bars=16, shape="triangle")

# Silent for 4 bars
for _ in range(4):
    pad.rest(Duration.WHOLE)

# Bars 5-8: creep in
pad.set(volume=0.12)
pad.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=50)
pad.add(Pa.add(-12), Duration.WHOLE, velocity=45)
pad.add(Ma.add(-12), Duration.WHOLE, velocity=50)
pad.add(Pa.add(-12), Duration.WHOLE, velocity=45)
pad.add(Sa.add(-12), Duration.WHOLE, velocity=50)

# Bars 9-12: fuller
pad.set(volume=0.18)
pad.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=60)
pad.hold(Pa.add(-12), Duration.WHOLE * 4, velocity=50)
pad.add(Ga, Duration.WHOLE, velocity=55)
pad.add(Re, Duration.WHOLE, velocity=50)
pad.add(Ga, Duration.WHOLE, velocity=55)
pad.add(Sa, Duration.WHOLE, velocity=60)

# Bars 13-16: biggest
pad.set(volume=0.22)
pad.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=65)
pad.hold(Pa.add(-12), Duration.WHOLE * 4, velocity=55)
pad.hold(Ga, Duration.WHOLE * 2, velocity=50)
pad.add(Ma, Duration.WHOLE, velocity=55)
pad.add(Ga, Duration.WHOLE, velocity=50)
pad.add(Re, Duration.WHOLE, velocity=55)
pad.add(Sa, Duration.WHOLE, velocity=60)

# ── HI-HAT TEXTURE — 16th note shimmer ─────────────────────────
hats = score.part("hats", synth="noise", envelope="staccato", volume=0.0,
                  lowpass=8000, reverb=0.15)

# Silent for 4 bars
for _ in range(4):
    hats.rest(Duration.WHOLE)

# Bars 5-16: subtle 16th note texture with accents
hats.set(volume=0.04)
for _ in range(12):
    for beat in range(4):
        hats.add("C5", Duration.SIXTEENTH, velocity=90)
        hats.set(volume=0.02)
        hats.add("C5", Duration.SIXTEENTH, velocity=60)
        hats.add("C5", Duration.SIXTEENTH, velocity=55)
        hats.set(volume=0.04)
        hats.add("C5", Duration.SIXTEENTH, velocity=75)

# ── TAMBURA — subtle drone, not as prominent as raga midnight ───
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.2,
                     reverb=0.8, reverb_type="taj_mahal",
                     chorus=0.3, chorus_rate=0.08, chorus_depth=0.008,
                     lowpass=1000, pan=-0.3)

for _ in range(16):
    tambura.add(Sa.add(-24), Duration.HALF)
    tambura.add(Pa.add(-24), Duration.HALF)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"Temperament: shruti / just intonation")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing MONSOON BASS (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing MONSOON BASS...")
    play_score(score)
