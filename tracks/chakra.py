"""
CHAKRA — a journey from root to crown through seven frequency activations.

Each section targets a chakra's Solfeggio frequency, with metric modulation
creating natural tempo increases (quarter = previous triplet, ×3/2 ratio).

  1. Root (Muladhara)     — 396 Hz, 60 BPM  — grounding, deep
  2. Sacral (Svadhisthana) — 417 Hz, 90 BPM  — flow, sensual
  3. Solar Plexus (Manipura) — 528 Hz, 90 BPM — power, transformation
  4. Heart (Anahata)       — 639 Hz, 108 BPM — love, connection
  5. Throat (Vishuddha)    — 741 Hz, 108 BPM — expression, truth
  6. Third Eye (Ajna)      — 852 Hz, 135 BPM — intuition, vision
  7. Crown (Sahasrara)     — 963 Hz, 135 BPM → silence — unity, dissolution
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

# ── Solfeggio tones — exact chakra frequencies ──────────────────
# We'll use Tone objects at specific frequencies via .from_hz()
# and also use scale tones for melodic content

score = Score("4/4", bpm=60, reference_pitch=432.0)

# Bowl tones — root note of each section's key, ascending through octaves
# At A=432 Hz, everything sits in the "healing" frequency space

# ── Keys for each chakra section ────────────────────────────────
# Root/Sacral: G major (grounding)
# Solar/Heart: C major (warm, open)
# Throat/Third Eye: E major (bright, expressive)
# Crown: dissolves into pure frequency

key_lower = Key("G", "major")    # root, sacral
key_middle = Key("C", "major")   # solar, heart
key_upper = Key("E", "major")    # throat, third eye

sl = key_lower.scale
sm = key_middle.scale
su = key_upper.scale

# ═══════════════════════════════════════════════════════════════════
# 1. ROOT — MULADHARA (396 Hz) — 60 BPM, 8 bars
#    Deep, slow, grounding. Tambura drone + harmonium + singing bowl.
# ═══════════════════════════════════════════════════════════════════

# ── Ukulele — gentle opening, intimate ──────────────────────────
uke = score.part("uke", instrument="ukulele", volume=0.2,
                 reverb=0.4, reverb_type="taj_mahal",
                 humanize=0.1)

# ROOT: simple fingerpicked G chord — lots of space
for _ in range(4):
    uke.add(sl[0], Duration.QUARTER, velocity=60)
    uke.rest(Duration.QUARTER)
    uke.add(sl[2], Duration.QUARTER, velocity=55)
    uke.add(sl[4], Duration.QUARTER, velocity=50)
# Sacral: uke continues gently
for _ in range(4):
    uke.add(sl[0], Duration.QUARTER, velocity=50)
    uke.rest(Duration.QUARTER)
    uke.add(sl[4], Duration.QUARTER, velocity=45)
    uke.rest(Duration.QUARTER)
# Rest of piece: silent
for _ in range(48):
    uke.rest(Duration.WHOLE)

# ── 808 Sub — deep grounding tone ──────────────────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.2,
                 lowpass=100, distortion=0.1, distortion_drive=2.0)

# Sub drone throughout — changes root with each section
# ROOT (8 bars)
for _ in range(8):
    sub.add(sl[0].add(-24), Duration.WHOLE, velocity=70)
# SACRAL (8 bars) — same root
for _ in range(8):
    sub.add(sl[0].add(-24), Duration.WHOLE, velocity=72)
# SOLAR (8 bars) — shifts to C
for _ in range(8):
    sub.add(sm[0].add(-24), Duration.WHOLE, velocity=75)
# HEART (8 bars) — stays C
for _ in range(8):
    sub.add(sm[0].add(-24), Duration.WHOLE, velocity=72)
# THROAT (8 bars) — shifts to E
for _ in range(8):
    sub.add(su[0].add(-24), Duration.WHOLE, velocity=70)
# THIRD EYE (8 bars) — stays E
for _ in range(8):
    sub.add(su[0].add(-24), Duration.WHOLE, velocity=68)
# CROWN (8 bars) — fading
for vel in [60, 50, 40, 30, 20, 10, 5, 0]:
    if vel > 0:
        sub.add(su[0].add(-12), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# ── Tambura — Sa-Pa drone in G ──────────────────────────────────
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.12,
                     reverb=0.8, reverb_type="taj_mahal",
                     chorus=0.3, chorus_rate=0.08, chorus_depth=0.01,
                     lowpass=1000, pan=-0.25)

# ROOT: G drone — enters bar 3, giving uke space first
tambura.rest(Duration.WHOLE)
tambura.rest(Duration.WHOLE)
for _ in range(6):
    tambura.add(sl[0].add(-24), Duration.HALF)   # G2
    tambura.add(sl[4].add(-24), Duration.HALF)   # D3

# ── Harmonium — low register, breathing ─────────────────────────
harmonium = score.part("harmonium", instrument="harmonium", volume=0.08,
                       reverb=0.6, reverb_type="taj_mahal",
                       chorus=0.2, chorus_rate=0.15, chorus_depth=0.008,
                       humanize=0.08)

# ROOT: simple I chord, dropped an octave, lots of rests
root_prog = key_lower.progression("I", "IV")
for chord in root_prog:
    harmonium.rest(Duration.WHOLE)
    harmonium.add(chord, Duration.WHOLE, velocity=65)
for chord in root_prog:
    harmonium.rest(Duration.WHOLE)
    harmonium.add(chord, Duration.WHOLE, velocity=55)

# ── Singing bowl — real singing bowl synth ──────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.2,
                  reverb=0.9, reverb_type="taj_mahal")

# Strike every 4 bars — maximum space to ring
bowl.add(sl[0].add(-12), Duration.WHOLE, velocity=75)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.add(sl[0].add(-12), Duration.WHOLE, velocity=70)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)

# ── Rhodes — very sparse, low ──────────────────────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.15,
                    reverb=0.6, reverb_type="taj_mahal",
                    tremolo_depth=0.1, tremolo_rate=3.0,
                    humanize=0.08)

# ROOT: one arp every 2 bars
rhodes.add(sl[0].add(-12), Duration.QUARTER, velocity=55)
rhodes.add(sl[2].add(-12), Duration.QUARTER, velocity=50)
rhodes.add(sl[4].add(-12), Duration.QUARTER, velocity=45)
rhodes.rest(Duration.QUARTER)
rhodes.rest(Duration.WHOLE)
rhodes.add(sl[0], Duration.QUARTER, velocity=50)
rhodes.add(sl[2], Duration.QUARTER, velocity=45)
rhodes.add(sl[4], Duration.QUARTER, velocity=40)
rhodes.rest(Duration.QUARTER)
for _ in range(5):
    rhodes.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# 2. SACRAL — SVADHISTHANA (417 Hz) — 90 BPM, 8 bars
#    Flowing, sensual. Sitar enters. Tempo lifts.
# ═══════════════════════════════════════════════════════════════════
score.set_tempo(90)

# Tambura continues — same root for sacral
for _ in range(8):
    tambura.add(sl[0].add(-24), Duration.HALF)
    tambura.add(sl[4].add(-24), Duration.HALF)

# Harmonium — I IV V IV
sacral_prog = key_lower.progression("I", "IV", "V", "IV")
for _ in range(2):
    for chord in sacral_prog:
        harmonium.add(chord, Duration.WHOLE)

# Bowl shifts to 417 Hz
for _ in range(4):
    bowl.add(sl[0].add(2), Duration.WHOLE, velocity=80)
    bowl.rest(Duration.WHOLE)

# Rhodes — fuller arps
for _ in range(4):
    for t in [sl[0], sl[2], sl[4], sl[2]]:
        rhodes.add(t, Duration.EIGHTH, velocity=75)
    for t in [sl[3], sl[4], sl[2], sl[0]]:
        rhodes.add(t, Duration.EIGHTH, velocity=70)

for _ in range(4):
    rhodes.rest(Duration.WHOLE)

# ── Sitar enters — flowing melody ──────────────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.25,
                   reverb=0.4, reverb_type="taj_mahal",
                   delay=0.3, delay_time=0.333, delay_feedback=0.35,
                   pan=-0.15, humanize=0.1)

# Silent during root (8 bars at 60bpm)
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# Sacral: gentle melody
sitar_sacral = [
    (sl[0], Duration.QUARTER, 80), (sl[2], Duration.QUARTER, 75),
    (sl[4], Duration.HALF, 85),
    (sl[3], Duration.QUARTER, 75), (sl[2], Duration.EIGHTH, 70),
    (sl[1], Duration.EIGHTH, 65), (sl[0], Duration.HALF, 80),
]
for _ in range(2):
    for note, dur, vel in sitar_sacral:
        sitar.add(note, dur, velocity=vel)
for _ in range(4):
    sitar.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# 3. SOLAR PLEXUS — MANIPURA (528 Hz) — 90 BPM stays, 8 bars
#    Power, fire. Tabla enters. Energy builds.
# ═══════════════════════════════════════════════════════════════════

# Tambura shifts to C
for _ in range(8):
    tambura.add(sm[0].add(-24), Duration.HALF)   # C2
    tambura.add(sm[4].add(-24), Duration.HALF)   # G2

# Harmonium — brighter, C major
solar_prog = key_middle.progression("I", "V", "IV", "I")
for _ in range(2):
    for chord in solar_prog:
        harmonium.add(chord, Duration.WHOLE)

# Bowl at 528 Hz — the "love frequency"
for _ in range(4):
    bowl.add(sm[0], Duration.WHOLE, velocity=85)
    bowl.rest(Duration.WHOLE)

# Rhodes — more active
for _ in range(4):
    for t in [sm[0], sm[2], sm[4], sm[0].add(12)]:
        rhodes.add(t, Duration.EIGHTH, velocity=80)
    for t in [sm[4], sm[2], sm[0], sm[4].add(-12)]:
        rhodes.add(t, Duration.EIGHTH, velocity=75)
for _ in range(4):
    rhodes.rest(Duration.WHOLE)

# Sitar — stronger, climbing
sitar_solar = [
    (sm[0], Duration.EIGHTH, 85), (sm[2], Duration.EIGHTH, 80),
    (sm[4], Duration.QUARTER, 95),
    (sm[0].add(12), Duration.QUARTER, 100),
    (sm[4], Duration.EIGHTH, 85), (sm[2], Duration.EIGHTH, 80),
    (sm[0], Duration.HALF, 90),
]
for _ in range(2):
    for note, dur, vel in sitar_solar:
        sitar.add(note, dur, velocity=vel)
for _ in range(4):
    sitar.rest(Duration.WHOLE)

# ── Tabla enters — gentle at first ─────────────────────────────
tabla = score.part("tabla", volume=0.18,
                   reverb=0.25, reverb_decay=1.2, humanize=0.08)

NA  = DrumSound.TABLA_NA
TIT = DrumSound.TABLA_TIT
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
GEB = DrumSound.TABLA_GE_BEND

# Silent for root + sacral (16 bars)
for _ in range(16):
    tabla.rest(Duration.WHOLE)

# Solar: light keherwa
for _ in range(8):
    tabla.hit(tDHA, Duration.EIGHTH, velocity=80)
    tabla.hit(GE, Duration.EIGHTH, velocity=55)
    tabla.hit(NA, Duration.EIGHTH, velocity=65)
    tabla.hit(TIT, Duration.EIGHTH, velocity=42)
    tabla.hit(NA, Duration.EIGHTH, velocity=60)
    tabla.hit(TIT, Duration.EIGHTH, velocity=40)
    tabla.hit(tDHA, Duration.EIGHTH, velocity=75)
    tabla.hit(NA, Duration.EIGHTH, velocity=58)

# ═══════════════════════════════════════════════════════════════════
# 4. HEART — ANAHATA (639 Hz) — 108 BPM, 8 bars
#    Love, openness. Everything blooms. Metric modulation: ×6/5
# ═══════════════════════════════════════════════════════════════════
score.set_tempo(108)

# Tambura stays on C — heart center
for _ in range(8):
    tambura.add(sm[0].add(-24), Duration.HALF)
    tambura.add(sm[4].add(-24), Duration.HALF)

# Harmonium — open, warm
heart_prog = key_middle.progression("I", "vi", "IV", "V")
for _ in range(2):
    for chord in heart_prog:
        harmonium.add(chord, Duration.WHOLE)

# Bowl at 639 Hz
for _ in range(4):
    bowl.add(sm[0].add(7), Duration.WHOLE, velocity=88)
    bowl.rest(Duration.WHOLE)

# Rhodes — flowing arps
for _ in range(8):
    for t in [sm[0], sm[2], sm[4], sm[0].add(12), sm[4], sm[2]]:
        rhodes.add(t, Duration.EIGHTH, velocity=78)
    rhodes.rest(Duration.QUARTER)

# Sitar — emotional, singing
sitar_heart = [
    (sm[4], Duration.QUARTER, 100),
    (sm[0].add(12), Duration.QUARTER, 110),
    (sm[6], Duration.EIGHTH, 90),
    (sm[4], Duration.EIGHTH, 85),
    (sm[2], Duration.HALF, 95),
    (sm[0], Duration.QUARTER, 85),
    (sm[2], Duration.QUARTER, 90),
    (sm[4], Duration.HALF, 100),
    (sm[2], Duration.QUARTER, 85),
    (sm[0], Duration.QUARTER, 80),
]
for _ in range(2):
    for note, dur, vel in sitar_heart:
        sitar.add(note, dur, velocity=vel)
for _ in range(4):
    sitar.rest(Duration.WHOLE)

# Tabla — livelier
for _ in range(8):
    tabla.hit(tDHA, Duration.EIGHTH, velocity=90, articulation="accent")
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=50)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=45)
    tabla.hit(NA, Duration.EIGHTH, velocity=70)
    tabla.hit(GEB, Duration.EIGHTH, velocity=95)
    tabla.hit(NA, Duration.EIGHTH, velocity=65)
    tabla.hit(tDHA, Duration.EIGHTH, velocity=85)
    tabla.hit(TIT, Duration.EIGHTH, velocity=48)

# ═══════════════════════════════════════════════════════════════════
# 5. THROAT — VISHUDDHA (741 Hz) — 108 BPM stays, 8 bars
#    Expression. Theremin enters — the voice.
# ═══════════════════════════════════════════════════════════════════

# Tambura shifts to E
for _ in range(8):
    tambura.add(su[0].add(-12), Duration.HALF)   # E3
    tambura.add(su[4].add(-12), Duration.HALF)   # B3

# Harmonium — bright E major
throat_prog = key_upper.progression("I", "V", "vi", "IV")
for _ in range(2):
    for chord in throat_prog:
        harmonium.add(chord, Duration.WHOLE)

# Bowl at 741 Hz
for _ in range(4):
    bowl.add(su[0], Duration.WHOLE, velocity=85)
    bowl.rest(Duration.WHOLE)

# Rhodes — staccato arps, rhythmic
for _ in range(8):
    for t in [su[0], su[2], su[4], su[0].add(12)]:
        rhodes.add(t, Duration.SIXTEENTH, velocity=80)
    rhodes.rest(Duration.HALF)

# Sitar — higher register, faster
sitar_throat = [
    (su[0].add(12), Duration.EIGHTH, 105),
    (su[6], Duration.EIGHTH, 95),
    (su[4], Duration.EIGHTH, 90),
    (su[2], Duration.EIGHTH, 85),
    (su[0], Duration.QUARTER, 95),
    (su[4], Duration.QUARTER, 100),
]
for _ in range(4):
    for note, dur, vel in sitar_throat:
        sitar.add(note, dur, velocity=vel)

# Tabla — more intensity
for bar in range(8):
    if bar % 4 == 3:
        # Fill
        tabla.hit(tDHA, Duration.EIGHTH, velocity=100, articulation="accent")
        tabla.hit(GEB, Duration.EIGHTH, velocity=115)
        tabla.hit(NA, Duration.SIXTEENTH, velocity=75)
        tabla.hit(TIT, Duration.SIXTEENTH, velocity=55)
        tabla.hit(GEB, Duration.EIGHTH, velocity=110)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=95)
        tabla.hit(NA, Duration.EIGHTH, velocity=70)
        tabla.hit(GEB, Duration.QUARTER, velocity=120)
    else:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=95, articulation="accent")
        tabla.hit(TIT, Duration.SIXTEENTH, velocity=50)
        tabla.hit(TIT, Duration.SIXTEENTH, velocity=45)
        tabla.hit(NA, Duration.EIGHTH, velocity=72)
        tabla.hit(GEB, Duration.EIGHTH, velocity=100)
        tabla.hit(NA, Duration.EIGHTH, velocity=68)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=88)
        tabla.hit(TIT, Duration.EIGHTH, velocity=50)

# ── Theremin — the voice of the throat chakra ───────────────────
theremin = score.part("theremin", instrument="theremin", volume=0.25,
                      reverb=0.5, reverb_type="taj_mahal",
                      delay=0.25, delay_time=0.278, delay_feedback=0.3,
                      pan=0.2, humanize=0.06)

# Silent for root+sacral+solar+heart (32 bars)
for _ in range(32):
    theremin.rest(Duration.WHOLE)

# Throat: theremin wails — long bends, expressive
theremin.add(su[4], Duration.HALF, velocity=95, bend=1.0)
theremin.add(su[0].add(12), Duration.HALF, velocity=105, bend=-0.5)
theremin.add(su[2], Duration.QUARTER, velocity=90)
theremin.add(su[4], Duration.QUARTER, velocity=100, bend=0.5)
theremin.add(su[0].add(12), Duration.HALF, velocity=110, bend=1.5)
theremin.add(su[6], Duration.QUARTER, velocity=100, bend=-0.5)
theremin.add(su[4], Duration.QUARTER, velocity=95)
theremin.add(su[2], Duration.HALF, velocity=90, bend=1.0)
theremin.add(su[0], Duration.HALF, velocity=85)
for _ in range(4):
    theremin.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# 6. THIRD EYE — AJNA (852 Hz) — 135 BPM, 8 bars
#    Vision. Everything accelerates. Sitar shreds. Intense.
# ═══════════════════════════════════════════════════════════════════
score.set_tempo(135)

# Tambura on E — higher energy
for _ in range(8):
    tambura.add(su[0].add(-12), Duration.HALF)
    tambura.add(su[4].add(-12), Duration.HALF)

# Harmonium — rapid chord changes
eye_prog = key_upper.progression("I", "V", "vi", "IV", "I", "V", "vi", "IV")
for chord in eye_prog:
    harmonium.add(chord, Duration.HALF)

# Bowl at 852 Hz
for _ in range(4):
    bowl.add(su[0].add(7), Duration.WHOLE, velocity=90)
    bowl.rest(Duration.WHOLE)

# Rhodes — 16th note arps
for _ in range(4):
    for t in [su[0], su[2], su[4], su[0].add(12),
              su[4], su[2], su[0], su[4].add(-12)]:
        rhodes.add(t, Duration.SIXTEENTH, velocity=82)
    for t in [su[3], su[4], su[0].add(12), su[4],
              su[2], su[0], su[4].add(-12), su[0]]:
        rhodes.add(t, Duration.SIXTEENTH, velocity=78)

for _ in range(4):
    rhodes.rest(Duration.WHOLE)

# Sitar — fast arps, visionary
for _ in range(4):
    for t in [su[0], su[2], su[4], su[0].add(12),
              su[4], su[2], su[0], su[4].add(-12)]:
        sitar.add(t, Duration.SIXTEENTH, velocity=100)
    for t in [su[2], su[4], su[0].add(12), su[2].add(12),
              su[0].add(12), su[4], su[2], su[0]]:
        sitar.add(t, Duration.SIXTEENTH, velocity=95)
for _ in range(4):
    sitar.rest(Duration.WHOLE)

# Tabla — full energy
for bar in range(8):
    tabla.hit(tDHA, Duration.SIXTEENTH, velocity=100, articulation="accent")
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=52)
    tabla.hit(NA, Duration.SIXTEENTH, velocity=75)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=48)
    tabla.hit(tDHA, Duration.SIXTEENTH, velocity=98)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=50)
    tabla.hit(GEB, Duration.SIXTEENTH, velocity=105)
    tabla.hit(NA, Duration.SIXTEENTH, velocity=70)
    tabla.hit(tDHA, Duration.SIXTEENTH, velocity=102, articulation="accent")
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=52)
    tabla.hit(NA, Duration.SIXTEENTH, velocity=72)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=48)
    tabla.hit(GEB, Duration.SIXTEENTH, velocity=108)
    tabla.hit(NA, Duration.SIXTEENTH, velocity=68)
    tabla.hit(tDHA, Duration.SIXTEENTH, velocity=95)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=50)

# Theremin — intense, high, bending
theremin.add(su[0].add(12), Duration.QUARTER, velocity=110, bend=2.0)
theremin.add(su[4].add(12), Duration.QUARTER, velocity=115, bend=-1.0)
theremin.add(su[2].add(12), Duration.EIGHTH, velocity=105)
theremin.add(su[0].add(12), Duration.EIGHTH, velocity=100)
theremin.add(su[4], Duration.HALF, velocity=108, bend=1.5)
theremin.add(su[0].add(24), Duration.HALF, velocity=120, bend=2.0)
theremin.add(su[4].add(12), Duration.HALF, velocity=110, bend=-1.5)
for _ in range(5):
    theremin.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# 7. CROWN — SAHASRARA (963 Hz) — 135 BPM → dissolve, 8 bars
#    Unity. Everything simplifies. Pure frequency. Silence.
# ═══════════════════════════════════════════════════════════════════

# Tambura — rises to crown, then fades
for vel in [80, 75, 65, 55, 45, 35, 20, 10]:
    tambura.add(su[0], Duration.HALF, velocity=vel)
    tambura.add(su[4], Duration.HALF, velocity=max(5, vel - 10))

# Harmonium — one sustained chord, fading
harmonium.add(key_upper.progression("I")[0], Duration.WHOLE, velocity=80)
harmonium.add(key_upper.progression("I")[0], Duration.WHOLE, velocity=65)
harmonium.add(key_upper.progression("I")[0], Duration.WHOLE, velocity=50)
harmonium.add(key_upper.progression("I")[0], Duration.WHOLE, velocity=35)
for _ in range(4):
    harmonium.rest(Duration.WHOLE)

# Bowl at 963 Hz — the crown. Rings alone.
bowl.add(su[0].add(12), Duration.WHOLE, velocity=95)
bowl.add(su[0].add(12), Duration.WHOLE, velocity=90)
bowl.add(su[0].add(12), Duration.WHOLE, velocity=80)
bowl.add(su[0].add(12), Duration.WHOLE, velocity=65)
bowl.add(su[0].add(12), Duration.WHOLE, velocity=50)
bowl.add(su[0].add(12), Duration.WHOLE, velocity=35)
bowl.add(su[0].add(12), Duration.WHOLE, velocity=20)
bowl.rest(Duration.WHOLE)

# Rhodes — one last arp, dissolving
rhodes.add(su[0], Duration.QUARTER, velocity=65)
rhodes.add(su[2], Duration.QUARTER, velocity=55)
rhodes.add(su[4], Duration.QUARTER, velocity=45)
rhodes.add(su[0].add(12), Duration.QUARTER, velocity=35)
for _ in range(7):
    rhodes.rest(Duration.WHOLE)

# Sitar — one held note, fading
sitar.add(su[0].add(12), Duration.WHOLE, velocity=70, bend=0.5)
sitar.add(su[0].add(12), Duration.WHOLE, velocity=50)
for _ in range(6):
    sitar.rest(Duration.WHOLE)

# Tabla — one final soft DHA, then silence
tabla.hit(tDHA, Duration.WHOLE, velocity=50)
for _ in range(7):
    tabla.rest(Duration.WHOLE)

# Theremin — highest note, dissolving into the cosmos
theremin.add(su[0].add(12), Duration.WHOLE, velocity=90, bend=3.0)
theremin.add(su[0].add(12), Duration.WHOLE, velocity=70, bend=2.0)
theremin.add(su[0].add(12), Duration.WHOLE, velocity=45, bend=1.0)
for _ in range(5):
    theremin.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")
print()
print("  Root (396 Hz)      → 60 BPM")
print("  Sacral (417 Hz)    → 90 BPM")
print("  Solar (528 Hz)     → 90 BPM")
print("  Heart (639 Hz)     → 108 BPM")
print("  Throat (741 Hz)    → 108 BPM")
print("  Third Eye (852 Hz) → 135 BPM")
print("  Crown (963 Hz)     → 135 BPM → silence")
print()

if "--live" in sys.argv:
    print("Playing CHAKRA (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing CHAKRA...")
    play_score(score)
