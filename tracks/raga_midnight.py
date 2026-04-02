"""
RAGA MIDNIGHT — a Bhairavi raga in four movements.
Alap, jor, gat, jhala — the traditional Hindustani form.
Tambura drone, sitar melody, dhol, hand-written tabla solo.
Then the 808 drops and the sitar comes back over thunder.
D Phrygian, shruti just intonation, 90 BPM.
"""

from pytheory import Key, Duration, Score, play_score
from pytheory.rhythm import DrumSound

# ── Scale & Sargam ──────────────────────────────────────────────
key = Key("D", "phrygian")
s = key.scale  # D Eb F G A Bb C

Sa  = s[0]   # D  (Sa)
Re  = s[1]   # Eb (komal Re)
Ga  = s[2]   # F  (komal Ga)
Ma  = s[3]   # G  (Ma)
Pa  = s[4]   # A  (Pa)
Dha = s[5]   # Bb (komal Dha)
Ni  = s[6]   # C  (komal Ni)

score = Score("4/4", bpm=90, system="shruti", temperament="just")

# ── Tabla Bols ──────────────────────────────────────────────────
NA  = DrumSound.TABLA_NA
TIN = DrumSound.TABLA_TIN
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
TIT = DrumSound.TABLA_TIT
KE  = DrumSound.TABLA_KE
GEB = DrumSound.TABLA_GE_BEND

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (48 bars, ~2:08):
#   Bars  1-8:   Tambura alone — the space opens, no rhythm
#   Bars  9-16:  Sitar alap — slow, meditative, exploring the raga
#   Bars 17-24:  Jor — rhythm emerges, sitar climbs to Pa and beyond
#   Bars 25-32:  Gat — dhol + drums enter, the composition begins
#   Bars 33-40:  Jhala — fast chikari, sitar arp enters, climax
#   Bars 41-44:  Sitar finale — descending runs, last burst
#   Bars 45-48:  Tabla solo — the voice speaks alone
# ═══════════════════════════════════════════════════════════════════

# ── TABLA DRUMS — auto-generated, enters bar 25 ────────────────
score.drums("tabla solo", repeats=40, fill="bayan", fill_every=8)
score.set_drum_effects(reverb=0.2, reverb_decay=0.8, volume=0.35, humanize=0.1)

# ── DHOL — the driving heartbeat, enters bar 25 ────────────────
dhol = score.part("dhol", synth="sine", volume=0.0,
                  reverb=0.25, reverb_decay=1.0,
                  delay=0.1, delay_time=0.333, delay_feedback=0.15,
                  humanize=0.08)

# Bars 1-24: silent — no rhythm yet
for _ in range(24):
    dhol.rest(Duration.WHOLE)

# Bars 25-32: dhol drives the gat
dhol.set(volume=0.7)
for _ in range(8):
    dhol.hit(DrumSound.DHOL_BOTH, Duration.QUARTER, velocity=100, articulation="accent")
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=70)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=80)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=65)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=60)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=75)
    dhol.hit(DrumSound.DHOL_BOTH, Duration.EIGHTH, velocity=90, articulation="accent")

# Bars 33-40: jhala — dhol stays strong
for _ in range(8):
    dhol.hit(DrumSound.DHOL_BOTH, Duration.QUARTER, velocity=105, articulation="accent")
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=72)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=82)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=68)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=62)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=78)
    dhol.hit(DrumSound.DHOL_BOTH, Duration.EIGHTH, velocity=92, articulation="accent")

# Bars 41-44: fade out during sitar finale
for vel in [85, 65, 42, 22]:
    dhol.hit(DrumSound.DHOL_BOTH, Duration.QUARTER, velocity=vel, articulation="accent")
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 25))
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=max(15, vel - 15))
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 30))
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 35))
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=max(15, vel - 20))
    dhol.hit(DrumSound.DHOL_BOTH, Duration.EIGHTH, velocity=max(15, vel - 10))

# Bars 45-48: silent through tabla solo
for _ in range(4):
    dhol.rest(Duration.WHOLE)

# ── TAMBURA — the earth beneath everything ──────────────────────
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.3,
                     reverb=0.45, reverb_type="taj_mahal",
                     chorus=0.4, chorus_rate=0.1, chorus_depth=0.01,
                     lowpass=1200, pan=-0.3, saturation=0.2)

# Bars 1-40: Sa-Pa drone cycle — the foundation
for _ in range(40):
    tambura.add(Sa.add(-24), Duration.HALF)
    tambura.add(Pa.add(-24), Duration.HALF)

# Bars 41-48: fade out for finale and tabla solo
for vel in [55, 45, 35, 25, 18, 12, 8, 5]:
    tambura.add(Sa.add(-24), Duration.HALF, velocity=vel)
    tambura.add(Pa.add(-24), Duration.HALF, velocity=max(5, vel - 8))

# ── TAMBURA HIGH — the sky above ────────────────────────────────
tambura_hi = score.part("tambura_hi", synth="sine", envelope="pad", volume=0.3,
                        reverb=0.45, reverb_type="taj_mahal",
                        chorus=0.5, chorus_rate=0.08, chorus_depth=0.012,
                        lowpass=2000, pan=0.3, saturation=0.15)

for _ in range(40):
    tambura_hi.add(Sa.add(-12), Duration.WHOLE)
for vel in [50, 38, 25, 15, 10, 6, 3, 0]:
    if vel > 0:
        tambura_hi.add(Sa.add(-12), Duration.WHOLE, velocity=vel)
    else:
        tambura_hi.rest(Duration.WHOLE)

# ── SITAR — the raga melody ────────────────────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.75,
                   reverb=0.25, reverb_type="taj_mahal",
                   delay=0.2, delay_time=0.333, delay_feedback=0.25,
                   pan=-0.15, saturation=0.25, humanize=0.1)

# Bars 1-8: silent — tambura alone, the space breathes
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# ── Alap — slow, meditative (bars 9-16) ────────────────────────
# Exploring Sa, Re, Ga — no rush
sitar.add(Sa, Duration.WHOLE, velocity=70, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.add(Re, Duration.HALF, velocity=65)
sitar.add(Sa, Duration.HALF, velocity=75)
sitar.rest(Duration.WHOLE)

sitar.add(Ga, Duration.DOTTED_HALF, velocity=82)
sitar.rest(Duration.QUARTER)
sitar.add(Ma, Duration.QUARTER, velocity=75)
sitar.add(Ga, Duration.QUARTER, velocity=70)
sitar.add(Re, Duration.QUARTER, velocity=68)
sitar.add(Sa, Duration.QUARTER, velocity=72, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.HALF)
sitar.add(Pa.add(-12), Duration.HALF, velocity=65)

# ── Jor — rhythm emerges (bars 17-24) ──────────────────────────
# Climbing higher — Pa, Dha, reaching for Ni
sitar.add(Sa, Duration.QUARTER, velocity=80)
sitar.add(Re, Duration.QUARTER, velocity=75)
sitar.add(Ga, Duration.QUARTER, velocity=85)
sitar.add(Ma, Duration.QUARTER, velocity=80)
sitar.add(Pa, Duration.HALF, velocity=90, bend=-0.15)
sitar.add(Ma, Duration.QUARTER, velocity=78)
sitar.add(Ga, Duration.QUARTER, velocity=75)
sitar.add(Re, Duration.HALF, velocity=80)
sitar.add(Sa, Duration.HALF, velocity=82, bend=-0.15)
sitar.rest(Duration.WHOLE)

# Second jor phrase — reaching higher
sitar.add(Ma, Duration.QUARTER, velocity=85)
sitar.add(Pa, Duration.QUARTER, velocity=92)
sitar.add(Dha, Duration.QUARTER, velocity=88)
sitar.add(Pa, Duration.QUARTER, velocity=85)
sitar.add(Ma, Duration.QUARTER, velocity=80)
sitar.add(Ga, Duration.QUARTER, velocity=75)
sitar.add(Re, Duration.QUARTER, velocity=72)
sitar.add(Sa, Duration.QUARTER, velocity=78, bend=-0.15)

# Touching Ni for the first time — the peak of exploration
sitar.add(Pa, Duration.QUARTER, velocity=95)
sitar.add(Dha, Duration.QUARTER, velocity=90)
sitar.add(Ni, Duration.HALF, velocity=100, bend=-0.2)
sitar.add(Dha, Duration.QUARTER, velocity=85)
sitar.add(Pa, Duration.QUARTER, velocity=82)
sitar.add(Ma, Duration.QUARTER, velocity=78)
sitar.add(Sa, Duration.QUARTER, velocity=75, bend=-0.15)

# ── Gat — the composition (bars 25-32) ─────────────────────────
sitar.add(Sa.add(12), Duration.QUARTER, velocity=110)
sitar.add(Ni, Duration.EIGHTH, velocity=90)
sitar.add(Dha, Duration.EIGHTH, velocity=80)
sitar.add(Pa, Duration.QUARTER, velocity=95)
sitar.add(Ma, Duration.QUARTER, velocity=75)
sitar.add(Ga, Duration.EIGHTH, velocity=65)
sitar.add(Ma, Duration.EIGHTH, velocity=80)
sitar.add(Pa, Duration.QUARTER, velocity=100)
sitar.add(Dha, Duration.EIGHTH, velocity=85)
sitar.add(Pa, Duration.EIGHTH, velocity=75)
sitar.add(Ma, Duration.QUARTER, velocity=70)

# Gat develops — climbing higher
sitar.add(Pa, Duration.QUARTER, velocity=90)
sitar.add(Sa.add(12), Duration.QUARTER, velocity=115, bend=-0.15)
sitar.add(Ni, Duration.EIGHTH, velocity=95)
sitar.add(Dha, Duration.EIGHTH, velocity=85)
sitar.add(Pa, Duration.QUARTER, velocity=80)
sitar.add(Ma, Duration.QUARTER, velocity=75)
sitar.add(Ga, Duration.QUARTER, velocity=65)
sitar.add(Re, Duration.QUARTER, velocity=55)
sitar.add(Sa, Duration.HALF, velocity=80, bend=-0.2)

# Gat repeats with variation
sitar.add(Sa.add(12), Duration.QUARTER, velocity=112)
sitar.add(Ni, Duration.EIGHTH, velocity=92)
sitar.add(Dha, Duration.EIGHTH, velocity=82)
sitar.add(Pa, Duration.QUARTER, velocity=98)
sitar.add(Dha, Duration.EIGHTH, velocity=88)
sitar.add(Pa, Duration.EIGHTH, velocity=82)
sitar.add(Ma, Duration.QUARTER, velocity=78)
sitar.add(Ga, Duration.EIGHTH, velocity=72)
sitar.add(Ma, Duration.EIGHTH, velocity=78)
sitar.add(Pa, Duration.QUARTER, velocity=102)
sitar.add(Sa.add(12), Duration.QUARTER, velocity=118, bend=-0.15)
sitar.add(Ni, Duration.EIGHTH, velocity=98)
sitar.add(Dha, Duration.EIGHTH, velocity=88)
sitar.add(Pa, Duration.QUARTER, velocity=85)
sitar.add(Ma, Duration.QUARTER, velocity=78)
sitar.add(Ga, Duration.QUARTER, velocity=68)
sitar.add(Sa, Duration.QUARTER, velocity=72, bend=-0.15)

# ── Jhala — fast climax (bars 33-40) ───────────────────────────
sitar.set(volume=0.8)
# Chikari alternation — melody + open string
for note, vel in [(Sa.add(12), 120), (Ni, 110), (Dha, 105),
                  (Pa, 115), (Ma, 100), (Dha, 110),
                  (Ni, 115), (Sa.add(12), 120)]:
    sitar.add(note, Duration.EIGHTH, velocity=vel)
    sitar.add(Pa, Duration.EIGHTH, velocity=75)

# Ascending run
for note, vel in [(Sa.add(12), 115), (Re.add(12), 120),
                  (Sa.add(12), 115), (Ni, 105),
                  (Dha, 95), (Pa, 85), (Ma, 75), (Ga, 65)]:
    sitar.add(note, Duration.EIGHTH, velocity=vel)

# Second jhala phrase — wider, more urgent
for note, vel in [(Sa.add(12), 122), (Pa, 78), (Ni, 115), (Pa, 75),
                  (Dha, 108), (Pa, 78), (Pa, 100), (Ma, 72),
                  (Ma, 95), (Pa, 78), (Dha, 110), (Pa, 75),
                  (Ni, 115), (Pa, 78), (Sa.add(12), 125), (Pa, 80)]:
    sitar.add(note, Duration.SIXTEENTH, velocity=vel)

# Descending 16ths
for note in [Sa.add(12), Ni, Dha, Pa, Ma, Ga, Re, Sa,
             Re, Ga, Ma, Pa, Dha, Ni, Sa.add(12), Re.add(12)]:
    sitar.add(note, Duration.SIXTEENTH, velocity=115)

# One more ascending wave
for note in [Sa.add(12), Re.add(12), Sa.add(12), Ni,
             Dha, Pa, Ma, Ga, Re, Sa, Re, Ga,
             Ma, Pa, Dha, Ni]:
    sitar.add(note, Duration.SIXTEENTH, velocity=118)

sitar.add(Sa.add(12), Duration.HALF, velocity=120, bend=-0.2)
sitar.add(Pa, Duration.HALF, velocity=105)

# ── Sitar Finale (bars 41-44) ──────────────────────────────────
sitar.set(volume=0.7)
sitar.add(Sa, Duration.HALF, bend=-0.25, velocity=100)
sitar.add(Pa, Duration.HALF, bend=-0.25, velocity=110)
# Fast descending run
sitar.add(Sa.add(12), Duration.QUARTER, velocity=120)
sitar.add(Dha, Duration.EIGHTH, velocity=90)
sitar.add(Pa, Duration.EIGHTH, velocity=100)
sitar.add(Ma, Duration.EIGHTH, velocity=80)
sitar.add(Ga, Duration.EIGHTH, velocity=70)
sitar.add(Re, Duration.EIGHTH, velocity=60)
sitar.add(Sa, Duration.EIGHTH, velocity=50)
# Last burst — 16ths
for note, vel in [(Sa.add(12), 127), (Ni, 115), (Dha, 105), (Pa, 95),
                  (Ma, 85), (Ga, 75), (Re, 60), (Sa, 45)]:
    sitar.add(note, Duration.SIXTEENTH, velocity=vel)
sitar.rest(Duration.HALF)
# Final held Sa
sitar.add(Sa, Duration.WHOLE, bend=-0.25, velocity=90)

# Bars 45-48: tabla solo — sitar drops out then returns
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
# Bar 48: one final strike
sitar.add(Sa.add(12), Duration.QUARTER, velocity=127)
sitar.add(Sa, Duration.DOTTED_HALF, velocity=80)

# ── SITAR ARP — shimmering cascade, enters bar 33 ──────────────
sitar_arp = score.part("sitar_arp", instrument="sitar", volume=0.65,
                       reverb=0.15, reverb_decay=0.8,
                       delay=0.25, delay_time=0.167, delay_feedback=0.3,
                       lowpass=3500, pan=0.4, saturation=0.2, humanize=0.1)

# Bars 1-32: silent
for _ in range(32):
    sitar_arp.rest(Duration.WHOLE)

# Bars 33-40: rapid arpeggio patterns
arp_phrases = [
    [Sa, Ga, Pa, Sa.add(12), Pa, Ga, Sa, Pa.add(-12),
     Sa, Ga, Pa, Sa.add(12), Pa, Ga, Sa, Pa.add(-12)],
    [Re, Ma, Dha, Re.add(12), Dha, Ma, Re, Dha.add(-12),
     Re, Ma, Dha, Re.add(12), Dha, Ma, Re, Dha.add(-12)],
    [Ga, Pa, Ni, Ga.add(12), Ni, Pa, Ga, Ni.add(-12),
     Ga, Pa, Ni, Ga.add(12), Ni, Pa, Ga, Ni.add(-12)],
    [Re, Ma, Dha, Re.add(12), Dha, Ma, Sa, Pa.add(-12),
     Sa, Ga, Pa, Sa.add(12), Pa, Ga, Sa, Pa.add(-12)],
]
for _ in range(2):
    for phrase in arp_phrases:
        for note in phrase:
            sitar_arp.add(note, Duration.SIXTEENTH)

# Bars 41-44: fade out
for vel in [50, 35, 20, 10]:
    for note in arp_phrases[0]:
        sitar_arp.add(note, Duration.SIXTEENTH, velocity=vel)

# Bars 45-48: silent
for _ in range(4):
    sitar_arp.rest(Duration.WHOLE)

# ── TABLA SOLO (bars 45-48) — the voice speaks alone ───────────
tabla = score.part("tabla_solo", volume=0.35,
                   reverb=0.2, reverb_decay=1.2,
                   delay=0.15, delay_time=0.333, delay_feedback=0.25,
                   humanize=0.05)

# Silent for 44 bars
for _ in range(44):
    tabla.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# TABLA SOLO — Peshkara → Kaida → Tukra → Tihai
# ═══════════════════════════════════════════════════════════════════

# ── Bar 45: PESHKARA — theme stated with dignity ──────────────
tabla.hit(tDHA, Duration.QUARTER, velocity=105, articulation="accent")
tabla.hit(GE, Duration.EIGHTH, velocity=78)
tabla.hit(NA, Duration.EIGHTH, velocity=72)
tabla.hit(tDHA, Duration.QUARTER, velocity=98, articulation="accent")
tabla.hit(NA, Duration.EIGHTH, velocity=70)
tabla.hit(KE, Duration.EIGHTH, velocity=60)

# ── Bar 46: KAIDA — developing, clean 8ths and 16ths ──────────
tabla.hit(tDHA, Duration.EIGHTH, velocity=108, articulation="accent")
tabla.hit(GE, Duration.EIGHTH, velocity=82)
tabla.hit(NA, Duration.EIGHTH, velocity=78)
tabla.hit(tDHA, Duration.EIGHTH, velocity=102)
tabla.hit(GEB, Duration.EIGHTH, velocity=112, articulation="accent")
tabla.hit(NA, Duration.EIGHTH, velocity=80)
tabla.hit(tDHA, Duration.EIGHTH, velocity=105)
tabla.hit(KE, Duration.EIGHTH, velocity=65)
# 16ths
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=110, articulation="accent")
tabla.hit(GE, Duration.SIXTEENTH, velocity=78)
tabla.hit(NA, Duration.SIXTEENTH, velocity=82)
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=105)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=115, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=80)
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=108)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=118)
tabla.hit(tDHA, Duration.QUARTER, velocity=115, articulation="accent")
tabla.hit(GEB, Duration.QUARTER, velocity=120)

# ── Bar 47: TUKRA — virtuosic, all 16ths ──────────────────────
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=112, articulation="accent")
tabla.hit(GE, Duration.SIXTEENTH, velocity=82)
tabla.hit(NA, Duration.SIXTEENTH, velocity=85)
tabla.hit(TIT, Duration.SIXTEENTH, velocity=55)
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=115, articulation="accent")
tabla.hit(GEB, Duration.SIXTEENTH, velocity=110)
tabla.hit(NA, Duration.SIXTEENTH, velocity=82)
tabla.hit(TIT, Duration.SIXTEENTH, velocity=55)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=118, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=80)
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=112)
tabla.hit(GE, Duration.SIXTEENTH, velocity=78)
tabla.hit(tDHA, Duration.QUARTER, velocity=120, articulation="accent")

# ── Bar 48: TIHAI — three-fold cadence ─────────────────────────
tabla.hit(tDHA, Duration.EIGHTH, velocity=108, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=82)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=110)
tabla.rest(Duration.EIGHTH)
tabla.hit(tDHA, Duration.EIGHTH, velocity=118, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=88)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=118)
tabla.rest(Duration.EIGHTH)
tabla.hit(tDHA, Duration.EIGHTH, velocity=127, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=95)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=125)
# SAM
tabla.rest(Duration.QUARTER)
tabla.hit(tDHA, Duration.DOTTED_HALF, velocity=127, articulation="fermata")

# ═══════════════════════════════════════════════════════════════════
# THE DROP — sitar returns with 808, bars 49-56
# ═══════════════════════════════════════════════════════════════════

# Extend tambura for the drop
tambura.set(volume=0.25)
for _ in range(8):
    tambura.add(Sa.add(-24), Duration.HALF, velocity=50)
    tambura.add(Pa.add(-24), Duration.HALF, velocity=42)

# Extend tambura_hi
for _ in range(8):
    tambura_hi.add(Sa.add(-12), Duration.WHOLE, velocity=35)

# Extend dhol — comes back for the drop
for _ in range(6):
    dhol.hit(DrumSound.DHOL_BOTH, Duration.QUARTER, velocity=95, articulation="accent")
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=68)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=78)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=62)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=58)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=72)
    dhol.hit(DrumSound.DHOL_BOTH, Duration.EIGHTH, velocity=88, articulation="accent")
# Fade last 2 bars
for vel in [70, 40]:
    dhol.hit(DrumSound.DHOL_BOTH, Duration.QUARTER, velocity=vel)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 25))
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=max(15, vel - 15))
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 30))
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 35))
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=max(15, vel - 20))
    dhol.hit(DrumSound.DHOL_BOTH, Duration.EIGHTH, velocity=max(15, vel - 10))

# ── 808 — the floor drops in ──────────────────────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=1.0,
                 lowpass=250, distortion=0.3, distortion_drive=4.0,
                 sub_osc=0.5, sidechain=0.3, saturation=0.5)

# Bars 1-48: silent
for _ in range(48):
    sub.rest(Duration.WHOLE)

# Bars 49-56: 808 drops — Re, Ga, Re, Pa below — builds intensity
bass_pattern = [
    (Re.add(-24), 20), (Ga.add(-24), 27), (Re.add(-24), 33), (Pa.add(-36), 40),
]
for cycle in range(2):
    for note, vel in bass_pattern:
        sub.add(note, Duration.WHOLE, velocity=vel + cycle * 5)

# ── Sitar reprise — gat returns over the 808 ──────────────────
sitar.set(volume=0.85)
# Repeat the gat — the main composition, now with weight underneath
sitar.add(Sa.add(12), Duration.QUARTER, velocity=115)
sitar.add(Ni, Duration.EIGHTH, velocity=95)
sitar.add(Dha, Duration.EIGHTH, velocity=85)
sitar.add(Pa, Duration.QUARTER, velocity=100)
sitar.add(Ma, Duration.QUARTER, velocity=80)
sitar.add(Ga, Duration.EIGHTH, velocity=70)
sitar.add(Ma, Duration.EIGHTH, velocity=82)
sitar.add(Pa, Duration.QUARTER, velocity=105)
sitar.add(Dha, Duration.EIGHTH, velocity=90)
sitar.add(Pa, Duration.EIGHTH, velocity=80)
sitar.add(Ma, Duration.QUARTER, velocity=75)

sitar.add(Pa, Duration.QUARTER, velocity=95)
sitar.add(Sa.add(12), Duration.QUARTER, velocity=120, bend=-0.15)
sitar.add(Ni, Duration.EIGHTH, velocity=100)
sitar.add(Dha, Duration.EIGHTH, velocity=90)
sitar.add(Pa, Duration.QUARTER, velocity=85)
sitar.add(Ma, Duration.QUARTER, velocity=80)
sitar.add(Ga, Duration.QUARTER, velocity=70)
sitar.add(Re, Duration.QUARTER, velocity=65)
sitar.add(Sa, Duration.HALF, velocity=85, bend=-0.2)

# Final 16th note burst — one last blaze
for note, vel in [(Sa.add(12), 125), (Ni, 118), (Dha, 112), (Pa, 105),
                  (Ma, 98), (Ga, 90), (Re, 82), (Sa, 75)]:
    sitar.add(note, Duration.SIXTEENTH, velocity=vel)
sitar.rest(Duration.HALF)

# Last Sa — ringing out over the 808
sitar.add(Sa, Duration.WHOLE, velocity=90, bend=-0.25)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Extend cascade for the drop
sitar_arp.set(volume=0.5)
for _ in range(2):
    for phrase in arp_phrases:
        for note in phrase:
            sitar_arp.add(note, Duration.SIXTEENTH, velocity=70)
# Fade
for vel in [50, 30]:
    for note in arp_phrases[0]:
        sitar_arp.add(note, Duration.SIXTEENTH, velocity=vel)
for _ in range(2):
    sitar_arp.rest(Duration.WHOLE)

# Tabla solo part rests through the drop
for _ in range(8):
    tabla.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"Temperament: shruti / just intonation")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing RAGA MIDNIGHT (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing RAGA MIDNIGHT...")
    play_score(score)
