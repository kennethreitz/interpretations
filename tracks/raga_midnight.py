"""
RAGA MIDNIGHT — tabla solo with tambura drone, sitar melody, and dhol.
Drenched in reverb. Pythagorean tuning for that pure fifth resonance.
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
NA  = DrumSound.TABLA_NA       # sharp dayan rim
TIN = DrumSound.TABLA_TIN     # open dayan ring
GE  = DrumSound.TABLA_GE      # deep bayan bass
tDHA = DrumSound.TABLA_DHA    # both drums (prefixed to avoid sargam clash)
TIT = DrumSound.TABLA_TIT     # light dayan flick
KE  = DrumSound.TABLA_KE      # muted bayan slap
GEB = DrumSound.TABLA_GE_BEND # bayan bend

# ── TABLA — with fills every 8 bars ─────────────────────────────
score.drums("tabla solo", repeats=20, fill="bayan", fill_every=8)
score.set_drum_effects(reverb=0.4, reverb_decay=1.8, volume=0.35, humanize=0.1)

# ── DHOL — the driving heartbeat, enters bar 9 ─────────────────
dhol = score.part("heartbeat", synth="sine", volume=0.0,
                  reverb=0.25, reverb_decay=1.0,
                  delay=0.1, delay_time=0.333, delay_feedback=0.15,
                  humanize=0.08)

# Silent for 8 bars
for _ in range(8):
    dhol.rest(Duration.WHOLE)

# Bars 9-16: dhol drives the gat and jhala
dhol.set(volume=0.7)
for _ in range(8):
    dhol.hit(DrumSound.DHOL_BOTH, Duration.QUARTER, velocity=100, articulation="accent")
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=70)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=80)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=65)
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=60)
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=75)
    dhol.hit(DrumSound.DHOL_BOTH, Duration.EIGHTH, velocity=90, articulation="accent")

# Bars 17-20: fade out — velocity list
for vel in [80, 60, 40, 20]:
    dhol.hit(DrumSound.DHOL_BOTH, Duration.QUARTER, velocity=vel, articulation="accent")
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 25))
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=max(15, vel - 15))
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 30))
    dhol.hit(DrumSound.DHOL_TILLI, Duration.EIGHTH, velocity=max(15, vel - 35))
    dhol.hit(DrumSound.DHOL_DAGGA, Duration.EIGHTH, velocity=max(15, vel - 20))
    dhol.hit(DrumSound.DHOL_BOTH, Duration.EIGHTH, velocity=max(15, vel - 10))

# Silent through tabla solo
for _ in range(4):
    dhol.rest(Duration.WHOLE)

# ── TAMBURA — the earth beneath everything ───────────────────────
tambura = score.part("earth", synth="sine", envelope="pad", volume=0.3,
                     reverb=0.45, reverb_type="taj_mahal",
                     chorus=0.4, chorus_rate=0.1, chorus_depth=0.01,
                     lowpass=1200, pan=-0.3, saturation=0.2)

# Sa-Pa drone cycle
for _ in range(20):
    tambura.add(Sa.add(-24), Duration.HALF)   # Sa low (D2)
    tambura.add(Pa.add(-24), Duration.HALF)   # Pa low (A2)
# Fade out for tabla solo — velocity list
for vel in [50, 38, 25, 12]:
    tambura.add(Sa.add(-24), Duration.HALF, velocity=vel)
    tambura.add(Pa.add(-24), Duration.HALF, velocity=max(5, vel - 8))

# ── TAMBURA HIGH — the sky above ─────────────────────────────────
tambura_hi = score.part("sky", synth="sine", envelope="pad", volume=0.3,
                        reverb=0.45, reverb_type="taj_mahal",
                        chorus=0.5, chorus_rate=0.08, chorus_depth=0.012,
                        lowpass=2000, pan=0.3, saturation=0.15)

for _ in range(20):
    tambura_hi.add(Sa.add(-12), Duration.WHOLE)  # Sa mid (D3)
for vel in [45, 30, 15, 5]:
    tambura_hi.add(Sa.add(-12), Duration.WHOLE, velocity=vel)

# ── SITAR — raga melody ─────────────────────────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.75,
                   reverb=0.25, reverb_type="taj_mahal",
                   delay=0.2, delay_time=0.333, delay_feedback=0.25,
                   pan=-0.15, saturation=0.25, humanize=0.1)

# ── Alap — slow, meditative opening (bars 1-4) ──────────────────
sitar.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=60)       # Sa drone
sitar.add(Sa, Duration.HALF, velocity=70)                       # Sa
sitar.rest(Duration.HALF)
sitar.hold(Sa.add(-12), Duration.WHOLE * 2, velocity=55)
sitar.add(Re, Duration.QUARTER, velocity=60)                    # Re (komal)
sitar.add(Sa, Duration.HALF, velocity=80)                       # Sa
sitar.rest(Duration.QUARTER)
sitar.hold(Pa.add(-12), Duration.WHOLE, velocity=50)            # Pa drone
sitar.add(Pa.add(-12), Duration.HALF, velocity=65)              # Pa low
sitar.add(Sa, Duration.QUARTER, velocity=75)                    # Sa
sitar.add(Re, Duration.QUARTER, velocity=90)                    # Re — peak
sitar.hold(Sa.add(-12), Duration.WHOLE, velocity=55)
sitar.add(Ga, Duration.DOTTED_HALF, velocity=100)               # Ga — strongest
sitar.rest(Duration.QUARTER)

# ── Jor — picking up rhythm (bars 5-8) ──────────────────────────
sitar.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=60)
sitar.hold(Ma, Duration.HALF, velocity=70)                      # double stop
sitar.add(Ma, Duration.QUARTER, velocity=90)                    # Ma
sitar.add(Ga, Duration.QUARTER, velocity=75)                    # Ga
sitar.add(Re, Duration.QUARTER, velocity=70)                    # Re
sitar.add(Sa, Duration.QUARTER, velocity=65)                    # Sa — descend
sitar.hold(Pa.add(-12), Duration.WHOLE, velocity=55)
sitar.add(Pa.add(-12), Duration.QUARTER, velocity=60)           # Pa low
sitar.add(Sa, Duration.EIGHTH, velocity=70)                     # Sa
sitar.add(Re, Duration.EIGHTH, velocity=80)                     # Re
sitar.add(Ga, Duration.QUARTER, velocity=95)                    # Ga — climb
sitar.add(Ma, Duration.QUARTER, velocity=105)                   # Ma
sitar.hold(Sa.add(-12), Duration.HALF, velocity=55)
sitar.add(Pa, Duration.QUARTER, velocity=110)                   # Pa — peak
sitar.add(Ma, Duration.EIGHTH, velocity=85)                     # Ma
sitar.add(Ga, Duration.EIGHTH, velocity=75)                     # Ga
sitar.add(Re, Duration.QUARTER, velocity=65)                    # Re
sitar.add(Sa, Duration.QUARTER, velocity=55)                    # Sa — settle
sitar.hold(Pa.add(-12), Duration.WHOLE, velocity=50)
sitar.add(Sa, Duration.HALF, velocity=60)                       # Sa
sitar.rest(Duration.HALF)

# ── Gat — main composition (bars 9-12) ──────────────────────────
sitar.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=65)
sitar.hold(Pa.add(-12), Duration.WHOLE * 2, velocity=55)
sitar.add(Sa.add(12), Duration.QUARTER, velocity=110)           # Sa high
sitar.add(Ni, Duration.EIGHTH, velocity=90)                     # Ni
sitar.add(Dha, Duration.EIGHTH, velocity=80)                    # Dha
sitar.add(Pa, Duration.QUARTER, velocity=95)                    # Pa
sitar.add(Ma, Duration.QUARTER, velocity=75)                    # Ma
sitar.add(Ga, Duration.EIGHTH, velocity=65)                     # Ga
sitar.add(Ma, Duration.EIGHTH, velocity=80)                     # Ma
sitar.add(Pa, Duration.QUARTER, velocity=100)                   # Pa
sitar.hold(Sa.add(-12), Duration.HALF, velocity=60)
sitar.add(Dha, Duration.EIGHTH, velocity=85)                    # Dha
sitar.add(Pa, Duration.EIGHTH, velocity=75)                     # Pa
sitar.add(Ma, Duration.QUARTER, velocity=70)                    # Ma
sitar.hold(Pa.add(-12), Duration.WHOLE, velocity=55)
sitar.add(Pa, Duration.QUARTER, velocity=90)                    # Pa
sitar.add(Sa.add(12), Duration.QUARTER, velocity=115)           # Sa high — climax
sitar.add(Ni, Duration.EIGHTH, velocity=95)                     # Ni
sitar.add(Dha, Duration.EIGHTH, velocity=85)                    # Dha
sitar.add(Pa, Duration.QUARTER, velocity=80)                    # Pa
sitar.hold(Sa.add(-12), Duration.WHOLE, velocity=60)
sitar.add(Ma, Duration.QUARTER, velocity=75)                    # Ma
sitar.add(Ga, Duration.QUARTER, velocity=65)                    # Ga
sitar.add(Re, Duration.QUARTER, velocity=55)                    # Re
sitar.add(Sa, Duration.QUARTER, velocity=50)                    # Sa — resolve

# ── Jhala — fast climax (bars 13-16) ────────────────────────────
sitar.set(volume=0.8)
sitar.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=70)
sitar.hold(Pa.add(-12), Duration.WHOLE * 4, velocity=65)
sitar.hold(Sa, Duration.WHOLE * 2, velocity=60)                 # chikari
sitar.add(Sa.add(12), Duration.EIGHTH, velocity=120)            # Sa high accented
sitar.add(Pa, Duration.EIGHTH, velocity=75)                     # Pa chikari
sitar.add(Sa.add(12), Duration.EIGHTH, velocity=115)            # Sa high
sitar.add(Pa, Duration.EIGHTH, velocity=70)                     # Pa
sitar.add(Ni, Duration.EIGHTH, velocity=110)                    # Ni
sitar.add(Pa, Duration.EIGHTH, velocity=75)                     # Pa
sitar.add(Dha, Duration.EIGHTH, velocity=105)                   # Dha
sitar.add(Pa, Duration.EIGHTH, velocity=70)                     # Pa
sitar.add(Ma, Duration.EIGHTH, velocity=100)                    # Ma
sitar.add(Pa, Duration.EIGHTH, velocity=75)                     # Pa
sitar.add(Dha, Duration.EIGHTH, velocity=110)                   # Dha
sitar.add(Pa, Duration.EIGHTH, velocity=70)                     # Pa
sitar.add(Ma, Duration.EIGHTH, velocity=95)                     # Ma
sitar.add(Ga, Duration.EIGHTH, velocity=85)                     # Ga
sitar.add(Re, Duration.EIGHTH, velocity=75)                     # Re
sitar.add(Sa, Duration.EIGHTH, velocity=65)                     # Sa — descend
sitar.hold(Sa.add(-12), Duration.WHOLE * 2, velocity=70)
sitar.add(Sa.add(12), Duration.EIGHTH, velocity=125)            # Sa high — back up!
sitar.add(Re.add(12), Duration.EIGHTH, velocity=120)            # Re high
sitar.add(Sa.add(12), Duration.EIGHTH, velocity=115)            # Sa high
sitar.add(Ni, Duration.EIGHTH, velocity=105)                    # Ni
sitar.add(Dha, Duration.EIGHTH, velocity=95)                    # Dha
sitar.add(Pa, Duration.EIGHTH, velocity=85)                     # Pa
sitar.add(Ma, Duration.EIGHTH, velocity=75)                     # Ma
sitar.add(Ga, Duration.EIGHTH, velocity=65)                     # Ga
sitar.add(Re, Duration.EIGHTH, velocity=55)                     # Re
sitar.add(Sa, Duration.EIGHTH, velocity=50)                     # Sa
sitar.add(Re, Duration.EIGHTH, velocity=60)                     # Re — upturn
sitar.add(Ga, Duration.EIGHTH, velocity=70)                     # Ga
sitar.hold(Sa.add(-12), Duration.DOTTED_HALF, velocity=65)
sitar.hold(Pa.add(-12), Duration.DOTTED_HALF, velocity=55)
sitar.add(Ma, Duration.QUARTER, velocity=80)                    # Ma
sitar.add(Sa, Duration.HALF, velocity=60)                       # Sa — land

# ── Sitar Finale (bars 17-20) ───────────────────────────────────
sitar.set(volume=0.7)
sitar.hold(Sa.add(-12), Duration.WHOLE * 4, velocity=65)
sitar.hold(Pa.add(-12), Duration.WHOLE * 4, velocity=55)
sitar.add(Sa, Duration.HALF, bend=-0.25, velocity=100)          # Sa with shimmer
sitar.add(Pa, Duration.HALF, bend=-0.25, velocity=110)          # Pa with shimmer
# Fast descending run
sitar.add(Sa.add(12), Duration.QUARTER, velocity=120)           # Sa high
sitar.add(Dha, Duration.EIGHTH, velocity=90)                    # Dha
sitar.add(Pa, Duration.EIGHTH, velocity=100)                    # Pa
sitar.add(Ma, Duration.EIGHTH, velocity=80)                     # Ma
sitar.add(Ga, Duration.EIGHTH, velocity=70)                     # Ga
sitar.add(Re, Duration.EIGHTH, velocity=60)                     # Re
sitar.add(Sa, Duration.EIGHTH, velocity=50)                     # Sa
# Last burst — fast 16ths
sitar.add(Sa.add(12), Duration.SIXTEENTH, velocity=127)         # Sa high — full force
sitar.add(Ni, Duration.SIXTEENTH, velocity=115)                 # Ni
sitar.add(Dha, Duration.SIXTEENTH, velocity=105)                # Dha
sitar.add(Pa, Duration.SIXTEENTH, velocity=95)                  # Pa
sitar.add(Ma, Duration.SIXTEENTH, velocity=85)                  # Ma
sitar.add(Ga, Duration.SIXTEENTH, velocity=75)                  # Ga
sitar.add(Re, Duration.SIXTEENTH, velocity=60)                  # Re
sitar.add(Sa, Duration.SIXTEENTH, velocity=45)                  # Sa — fade
sitar.rest(Duration.HALF)
# Final held note — Sa, home
sitar.hold(Sa.add(-12), Duration.WHOLE, velocity=70)
sitar.hold(Pa.add(-12), Duration.WHOLE, velocity=60)
sitar.add(Sa, Duration.WHOLE, bend=-0.25, velocity=90)          # Sa

# ── Tabla solo (bars 21-24) — sitar drops out ───────────────────
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
# Bar 24: sitar returns with one final strike
sitar.hold(Sa.add(-12), Duration.WHOLE, velocity=80)
sitar.hold(Pa.add(-12), Duration.WHOLE, velocity=70)
sitar.hold(Sa, Duration.WHOLE, velocity=60)
sitar.add(Sa.add(12), Duration.QUARTER, velocity=127)           # Sa high!
sitar.add(Sa, Duration.DOTTED_HALF, velocity=80)                # Sa — ring out

# ── SITAR ARP — shimmering cascade ──────────────────────────────
sitar_arp = score.part("cascade", instrument="sitar", volume=0.65,
                       reverb=0.15, reverb_decay=0.8,
                       delay=0.25, delay_time=0.167, delay_feedback=0.3,
                       lowpass=3500, pan=0.4, saturation=0.2, humanize=0.1)

# Silent for 8 bars
for _ in range(8):
    sitar_arp.rest(Duration.WHOLE)

# Bars 9-16: rapid arpeggio patterns built from scale
# Sa-Ga-Pa-Sa' ascending/descending
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

# Fade out during finale
sitar_arp.set(volume=0.15)
for phrase in arp_phrases[:2]:
    for note in phrase:
        sitar_arp.add(note, Duration.SIXTEENTH)
sitar_arp.set(volume=0.0)
for _ in range(6):
    sitar_arp.rest(Duration.WHOLE)

# ── TABLA SOLO (bars 21-24) — the voice speaks alone ────────────
tabla = score.part("voice", volume=0.35,
                   reverb=0.2, reverb_decay=1.2,
                   delay=0.15, delay_time=0.333, delay_feedback=0.25,
                   humanize=0.05)

# Silent for 20 bars
for _ in range(20):
    tabla.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# TABLA SOLO — Peshkara → Kaida → Tukra → Tihai
# ═══════════════════════════════════════════════════════════════════

# ── Bar 21: PESHKARA — theme stated with dignity ────────────────
tabla.hit(tDHA, Duration.QUARTER, velocity=110, articulation="accent")
tabla.hit(GE, Duration.EIGHTH, velocity=90)
tabla.hit(NA, Duration.EIGHTH, velocity=85)
tabla.hit(tDHA, Duration.QUARTER, velocity=105)
tabla.hit(TIT, Duration.SIXTEENTH, velocity=60)
tabla.hit(TIT, Duration.SIXTEENTH, velocity=55)
tabla.hit(NA, Duration.EIGHTH, velocity=80)
tabla.hit(KE, Duration.EIGHTH, velocity=70)
# Repeat with bayan bend answer
tabla.hit(tDHA, Duration.QUARTER, velocity=112, articulation="accent")
tabla.hit(GEB, Duration.EIGHTH, velocity=120)
tabla.hit(NA, Duration.EIGHTH, velocity=88)
tabla.hit(tDHA, Duration.EIGHTH, velocity=100)
tabla.rest(Duration.EIGHTH)
tabla.hit(GEB, Duration.QUARTER, velocity=125)

# ── Bar 22: KAIDA — developing, clean 8ths and 16ths ───────────
tabla.hit(tDHA, Duration.EIGHTH, velocity=108, articulation="accent")
tabla.hit(GE, Duration.EIGHTH, velocity=82)
tabla.hit(NA, Duration.EIGHTH, velocity=78)
tabla.hit(tDHA, Duration.EIGHTH, velocity=102)
tabla.hit(GEB, Duration.EIGHTH, velocity=112, articulation="accent")
tabla.hit(NA, Duration.EIGHTH, velocity=80)
tabla.hit(tDHA, Duration.EIGHTH, velocity=105)
tabla.hit(KE, Duration.EIGHTH, velocity=65)
# Second half: 16ths
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

# ── Bar 23: TUKRA — virtuosic, all 16ths on the grid ───────────
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
# Second half: 16ths building
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=115, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=85)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=120)
tabla.hit(TIT, Duration.SIXTEENTH, velocity=58)
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=118, articulation="accent")
tabla.hit(GEB, Duration.SIXTEENTH, velocity=122)
tabla.hit(NA, Duration.SIXTEENTH, velocity=88)
tabla.hit(tDHA, Duration.SIXTEENTH, velocity=120)
tabla.hit(GEB, Duration.QUARTER, velocity=127, articulation="accent")

# ── Bar 24: TIHAI — three-fold cadence, clean on the grid ──────
# 1st
tabla.hit(tDHA, Duration.EIGHTH, velocity=108, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=82)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=110)
tabla.rest(Duration.EIGHTH)
# 2nd
tabla.hit(tDHA, Duration.EIGHTH, velocity=118, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=88)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=118)
tabla.rest(Duration.EIGHTH)
# 3rd — strongest
tabla.hit(tDHA, Duration.EIGHTH, velocity=127, articulation="accent")
tabla.hit(NA, Duration.SIXTEENTH, velocity=95)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=125)
# SAM
tabla.rest(Duration.QUARTER)
tabla.hit(tDHA, Duration.DOTTED_HALF, velocity=127, articulation="fermata")

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
