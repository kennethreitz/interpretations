"""
THE TEMPLE — devotional layers inside a vast stone chamber.
Every sound fills the room. The reverb IS the instrument.

A Phrygian (Bhairavi), shruti just intonation, A=432 Hz, 65 BPM.
Singing bowls, tambura, harmonium, sitar, bansuri, tabla.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("A", "phrygian")
s = key.scale  # A Bb C D E F G

Sa  = s[0]   # A  (Sa)
Re  = s[1]   # Bb (komal Re)
Ga  = s[2]   # C  (komal Ga)
Ma  = s[3]   # D  (Ma)
Pa  = s[4]   # E  (Pa)
Dha = s[5]   # F  (komal Dha)
Ni  = s[6]   # G  (komal Ni)

score = Score("4/4", bpm=65, system="shruti", temperament="just",
              reference_pitch=432.0)

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (72 bars, ~7 min):
#   Bars  1-8:   Singing bowl alone — the space announces itself
#   Bars  9-16:  Tambura drone fades in — Sa-Pa, the foundation
#   Bars 17-24:  Harmonium breathes — slow chords, glacial
#   Bars 25-40:  Sitar enters — sparse melody, ornamental
#   Bars 33-48:  Bansuri (flute) — long held notes with bends
#   Bars 41-48:  Tabla — softest possible, just a heartbeat
#   Bars 49-56:  TABLA SOLO — peshkara → kaida → tukra → tihai
#   Bars 57-68:  SITAR SOLO — gat → jhala → tihai (3 sitars)
#   Bars 69-72:  Everything dissolving back into silence
# ═══════════════════════════════════════════════════════════════════

# ── ROOM TONE — the reverb tail of an empty temple ──────────────
room = score.part("room", synth="noise", envelope="pad", volume=0.03,
                  reverb=1.0, reverb_type="taj_mahal",
                  lowpass=300)
room.lfo("lowpass", rate=0.01, min=150, max=500, bars=72, shape="sine")
room.lfo("volume", rate=0.008, min=0.015, max=0.04, bars=72, shape="triangle")

for _ in range(72):
    room.add(Sa, Duration.WHOLE, velocity=25)

# ── SINGING BOWL — the space itself ─────────────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.55,
                  reverb=1.0, reverb_type="taj_mahal",
                  delay=0.3, delay_time=0.923, delay_feedback=0.45)

# Bars 1-8: solo — one strike, let it ring, another strike
bowl.add(Sa.add(-24), Duration.WHOLE, velocity=80)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.add(Pa.add(-24), Duration.WHOLE, velocity=72)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.add(Sa.add(-12), Duration.WHOLE, velocity=68)

# Bars 9-16: every 4 bars
bowl.add(Sa.add(-24), Duration.WHOLE, velocity=75)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.add(Pa.add(-24), Duration.WHOLE, velocity=70)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)
bowl.rest(Duration.WHOLE)

# Bars 17-72: every 8 bars, fading gradually
for section in range(7):
    vel = max(30, 70 - section * 5)
    bowl.add(Sa.add(-24), Duration.WHOLE, velocity=vel)
    for _ in range(7):
        bowl.rest(Duration.WHOLE)

# ── SINGING BOWL HIGH — shimmer, octave above ──────────────────
bowl_hi = score.part("bowl_hi", instrument="singing_bowl_ring", volume=0.3,
                     reverb=1.0, reverb_type="taj_mahal",
                     delay=0.25, delay_time=0.692, delay_feedback=0.4,
                     pan=0.25)

# Bars 1-16: silent
for _ in range(16):
    bowl_hi.rest(Duration.WHOLE)

# Bars 17-64: gentle ring every 6 bars offset from the low bowl
for _ in range(4):
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.add(Sa, Duration.WHOLE, velocity=50)
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.add(Pa, Duration.WHOLE, velocity=45)
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.rest(Duration.WHOLE)
    bowl_hi.add(Ma, Duration.WHOLE, velocity=42)
    bowl_hi.rest(Duration.WHOLE)

# Bars 65-72: silent through ending
for _ in range(8):
    bowl_hi.rest(Duration.WHOLE)

# ── TAMBURA — the drone bed ────────────────────────────────────
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.25,
                     reverb=0.8, reverb_type="taj_mahal",
                     chorus=0.5, chorus_rate=0.06, chorus_depth=0.012,
                     lowpass=900, pan=-0.2, saturation=0.15)

# Bars 1-8: silent — bowl alone
for _ in range(8):
    tambura.rest(Duration.WHOLE)

# Bars 9-16: fade in
for vel in [15, 20, 25, 30, 35, 40, 45, 50]:
    tambura.add(Sa.add(-24), Duration.HALF, velocity=vel)
    tambura.add(Pa.add(-24), Duration.HALF, velocity=max(10, vel - 8))

# Bars 17-64: full drone — Sa-Pa cycle
for _ in range(48):
    tambura.add(Sa.add(-24), Duration.HALF, velocity=55)
    tambura.add(Pa.add(-24), Duration.HALF, velocity=48)

# Bars 65-72: fade out
for vel in [50, 42, 35, 28, 20, 14, 8, 0]:
    if vel > 0:
        tambura.add(Sa.add(-24), Duration.HALF, velocity=vel)
        tambura.add(Pa.add(-24), Duration.HALF, velocity=max(5, vel - 8))
    else:
        tambura.rest(Duration.WHOLE)

# ── TAMBURA HIGH — octave shimmer, widens the drone ────────────
tambura_hi = score.part("tambura_hi", synth="sine", envelope="pad", volume=0.18,
                        reverb=0.85, reverb_type="taj_mahal",
                        chorus=0.6, chorus_rate=0.04, chorus_depth=0.015,
                        lowpass=1400, pan=0.25, saturation=0.1)

# Bars 1-16: silent
for _ in range(16):
    tambura_hi.rest(Duration.WHOLE)

# Bars 17-64: Sa drone an octave up
for _ in range(48):
    tambura_hi.add(Sa.add(-12), Duration.WHOLE, velocity=42)

# Bars 65-72: fade
for vel in [35, 28, 20, 14, 10, 6, 3, 0]:
    if vel > 0:
        tambura_hi.add(Sa.add(-12), Duration.WHOLE, velocity=vel)
    else:
        tambura_hi.rest(Duration.WHOLE)

# ── HARMONIUM — breathing chords ───────────────────────────────
harmonium = score.part("harmonium", instrument="harmonium", volume=0.12,
                       reverb=0.75, reverb_type="taj_mahal",
                       chorus=0.15, chorus_rate=0.08, chorus_depth=0.005,
                       humanize=0.08)

# Bars 1-16: silent
for _ in range(16):
    harmonium.rest(Duration.WHOLE)

# Bars 17-24: breathe in, breathe out — one chord per 2 bars
harm_chords = key.progression("i", "iv", "i", "v")
for chord in harm_chords:
    harmonium.add(chord, Duration.WHOLE, velocity=50)
    harmonium.rest(Duration.WHOLE)

# Bars 25-48: fuller, still glacial
for _ in range(3):
    for chord in harm_chords:
        harmonium.add(chord, Duration.WHOLE, velocity=55)
        harmonium.rest(Duration.WHOLE)

# Bars 49-56: one last cycle, warmer
harm_chords_2 = key.progression("i", "VI", "iv", "i")
for chord in harm_chords_2:
    harmonium.add(chord, Duration.WHOLE, velocity=52)
    harmonium.rest(Duration.WHOLE)

# Bars 57-64: holds through tabla/sitar solos
for _ in range(2):
    for chord in harm_chords:
        harmonium.add(chord, Duration.WHOLE, velocity=48)
        harmonium.rest(Duration.WHOLE)

# Bars 65-72: fading — just i chord dissolving
harmonium.add(key.progression("i")[0], Duration.WHOLE, velocity=40)
harmonium.rest(Duration.WHOLE)
harmonium.add(key.progression("i")[0], Duration.WHOLE, velocity=30)
harmonium.rest(Duration.WHOLE)
harmonium.add(key.progression("i")[0], Duration.WHOLE, velocity=20)
for _ in range(3):
    harmonium.rest(Duration.WHOLE)

# ── SITAR — sparse, ornamental melody ──────────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.55,
                   reverb=0.6, reverb_type="taj_mahal",
                   delay=0.35, delay_time=0.461, delay_feedback=0.4,
                   pan=-0.15, saturation=0.2, humanize=0.1)

# Bars 1-24: silent
for _ in range(24):
    sitar.rest(Duration.WHOLE)

# Bars 25-28: alap — slow, exploring the raga, lots of space
sitar.add(Sa, Duration.WHOLE, velocity=70, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.add(Re, Duration.HALF, velocity=65)
sitar.add(Sa, Duration.HALF, velocity=72)
sitar.rest(Duration.WHOLE)

# Bars 29-32: reaching upward
sitar.add(Ga, Duration.DOTTED_HALF, velocity=78)
sitar.rest(Duration.QUARTER)
sitar.add(Ma, Duration.QUARTER, velocity=72)
sitar.add(Ga, Duration.QUARTER, velocity=68)
sitar.add(Re, Duration.QUARTER, velocity=65)
sitar.add(Sa, Duration.QUARTER, velocity=70)
sitar.rest(Duration.WHOLE)

# Bars 33-36: the peak phrase — Pa reached
sitar.hold(Sa.add(-12), Duration.WHOLE * 2, velocity=55)
sitar.add(Pa, Duration.HALF, velocity=85, bend=-0.2)
sitar.add(Ma, Duration.QUARTER, velocity=75)
sitar.add(Ga, Duration.QUARTER, velocity=70)
sitar.add(Re, Duration.HALF, velocity=68)
sitar.add(Sa, Duration.HALF, velocity=72)

# Bars 37-40: descending, settling
sitar.add(Dha.add(-12), Duration.HALF, velocity=65)
sitar.add(Pa.add(-12), Duration.HALF, velocity=60)
sitar.add(Sa, Duration.WHOLE, velocity=70, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 41-48: second statement — more ornamental
sitar.hold(Sa.add(-12), Duration.WHOLE * 2, velocity=55)
sitar.add(Re, Duration.EIGHTH, velocity=65)
sitar.add(Ga, Duration.EIGHTH, velocity=70)
sitar.add(Ma, Duration.QUARTER, velocity=78)
sitar.add(Pa, Duration.HALF, velocity=82)
sitar.add(Dha, Duration.QUARTER, velocity=75, bend=-0.25)
sitar.add(Pa, Duration.QUARTER, velocity=72)
sitar.add(Ma, Duration.QUARTER, velocity=68)
sitar.add(Ga, Duration.QUARTER, velocity=65)
sitar.add(Re, Duration.HALF, velocity=62)
sitar.add(Sa, Duration.WHOLE, velocity=70, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 49-56: sitar responds to tabla solo — short phrases between the bols
sitar.add(Sa, Duration.HALF, velocity=72, bend=-0.15)
sitar.rest(Duration.HALF)
sitar.rest(Duration.WHOLE)
sitar.add(Ga, Duration.QUARTER, velocity=68)
sitar.add(Re, Duration.QUARTER, velocity=65)
sitar.add(Sa, Duration.HALF, velocity=70)
sitar.rest(Duration.WHOLE)
sitar.add(Pa, Duration.QUARTER, velocity=78)
sitar.add(Ma, Duration.EIGHTH, velocity=70)
sitar.add(Ga, Duration.EIGHTH, velocity=65)
sitar.add(Re, Duration.HALF, velocity=68)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# Bars 57-70: SITAR SOLO — the temple speaks through the strings
# Gat → Jhala → Tihai. Builds from meditative to ecstatic.
# Dry sitar — cuts through the reverb wash.
# ═══════════════════════════════════════════════════════════════════
solo = score.part("sitar_solo", instrument="sitar", volume=1.0,
                  reverb=0.45, reverb_type="taj_mahal",
                  delay=0.2, delay_time=0.461, delay_feedback=0.3,
                  pan=-0.2, saturation=0.3, humanize=0.08)

# Second sitar — panned right, slightly less volume, adds width
solo_r = score.part("sitar_solo_r", instrument="sitar", volume=0.85,
                    reverb=0.4, reverb_type="taj_mahal",
                    delay=0.25, delay_time=0.346, delay_feedback=0.3,
                    pan=0.35, saturation=0.25, humanize=0.12)

# Third sitar — center-ish, octave down, thickens the bottom
solo_low = score.part("sitar_solo_low", instrument="sitar", volume=0.7,
                      reverb=0.5, reverb_type="taj_mahal",
                      delay=0.15, delay_time=0.461, delay_feedback=0.25,
                      pan=-0.05, saturation=0.2, humanize=0.1,
                      lowpass=2500)

# All solos silent for bars 1-56 (tabla solo is 49-56)
for _ in range(56):
    solo.rest(Duration.WHOLE)
    solo_r.rest(Duration.WHOLE)
    solo_low.rest(Duration.WHOLE)

# Wet sitar drops to drone during both solos
sitar.set(volume=0.25)
sitar.hold(Sa.add(-12), Duration.WHOLE * 24, velocity=50)

# Bars 57-58: GAT — confident, full velocity
solo.add(Sa.add(12), Duration.QUARTER, velocity=120)
solo.add(Ni, Duration.EIGHTH, velocity=110)
solo.add(Dha, Duration.EIGHTH, velocity=105)
solo.add(Pa, Duration.QUARTER, velocity=115)
solo.add(Ma, Duration.QUARTER, velocity=108)
solo.add(Ga, Duration.EIGHTH, velocity=100)
solo.add(Ma, Duration.EIGHTH, velocity=105)
solo.add(Pa, Duration.QUARTER, velocity=118)
solo.add(Dha, Duration.EIGHTH, velocity=108)
solo.add(Pa, Duration.EIGHTH, velocity=105)
solo.add(Ma, Duration.QUARTER, velocity=100)

# Bars 59-60: GAT develops — climbing, with 32nd note shred bursts
solo.add(Pa, Duration.QUARTER, velocity=118)
solo.add(Sa.add(12), Duration.QUARTER, velocity=125, bend=-0.15)
# 32nd note burst — ripping up the scale
solo.add(Re, 0.125, velocity=115)
solo.add(Ga, 0.125, velocity=118)
solo.add(Ma, 0.125, velocity=120)
solo.add(Pa, 0.125, velocity=122)
solo.add(Dha, 0.125, velocity=125)
solo.add(Ni, 0.125, velocity=127)
solo.add(Sa.add(12), 0.125, velocity=127)
solo.add(Ni, 0.125, velocity=122)
# Back to 8ths
solo.add(Pa, Duration.QUARTER, velocity=115)
solo.add(Ma, Duration.EIGHTH, velocity=108)
solo.add(Ga, Duration.EIGHTH, velocity=105)
solo.add(Re, Duration.QUARTER, velocity=100)
solo.add(Sa, Duration.QUARTER, velocity=110, bend=-0.2)

# Bars 61-62: JHALA — chikari 16ths, full power
solo.add(Sa.add(12), Duration.SIXTEENTH, velocity=125)
solo.add(Pa, Duration.SIXTEENTH, velocity=95)
solo.add(Sa.add(12), Duration.SIXTEENTH, velocity=122)
solo.add(Pa, Duration.SIXTEENTH, velocity=92)
solo.add(Ni, Duration.SIXTEENTH, velocity=120)
solo.add(Pa, Duration.SIXTEENTH, velocity=95)
solo.add(Dha, Duration.SIXTEENTH, velocity=118)
solo.add(Pa, Duration.SIXTEENTH, velocity=92)
solo.add(Ma, Duration.SIXTEENTH, velocity=115)
solo.add(Pa, Duration.SIXTEENTH, velocity=95)
solo.add(Dha, Duration.SIXTEENTH, velocity=120)
solo.add(Pa, Duration.SIXTEENTH, velocity=92)
solo.add(Ni, Duration.SIXTEENTH, velocity=122)
solo.add(Pa, Duration.SIXTEENTH, velocity=95)
solo.add(Sa.add(12), Duration.SIXTEENTH, velocity=127)
solo.add(Pa, Duration.SIXTEENTH, velocity=95)
# Bar 62 — 32nd note shred ascending then descending
solo.add(Sa, 0.125, velocity=118)
solo.add(Re, 0.125, velocity=120)
solo.add(Ga, 0.125, velocity=122)
solo.add(Ma, 0.125, velocity=125)
solo.add(Pa, 0.125, velocity=127)
solo.add(Dha, 0.125, velocity=127)
solo.add(Ni, 0.125, velocity=127)
solo.add(Sa.add(12), 0.125, velocity=127)
solo.add(Sa.add(12), 0.125, velocity=127)
solo.add(Ni, 0.125, velocity=125)
solo.add(Dha, 0.125, velocity=122)
solo.add(Pa, 0.125, velocity=120)
solo.add(Ma, 0.125, velocity=118)
solo.add(Ga, 0.125, velocity=115)
solo.add(Re, 0.125, velocity=112)
solo.add(Sa, 0.125, velocity=110)
# 32nd note shred back up — higher this time
solo.add(Re, 0.125, velocity=118)
solo.add(Ma, 0.125, velocity=122)
solo.add(Dha, 0.125, velocity=125)
solo.add(Sa.add(12), 0.125, velocity=127)
solo.add(Re.add(12), 0.125, velocity=127, bend=-0.2)
solo.add(Sa.add(12), 0.125, velocity=125)
solo.add(Ni, 0.125, velocity=122)
solo.add(Pa, 0.125, velocity=118)

# Bars 63-64: PEAK — furious 16ths + 32nd shred runs
solo.add(Sa.add(12), Duration.SIXTEENTH, velocity=127)
solo.add(Pa, Duration.SIXTEENTH, velocity=100)
solo.add(Sa.add(12), Duration.SIXTEENTH, velocity=127)
solo.add(Pa, Duration.SIXTEENTH, velocity=98)
solo.add(Ni, Duration.SIXTEENTH, velocity=125)
solo.add(Pa, Duration.SIXTEENTH, velocity=100)
solo.add(Dha, Duration.SIXTEENTH, velocity=122)
solo.add(Pa, Duration.SIXTEENTH, velocity=98)
# 32nd note blaze — the fastest moment
solo.add(Sa.add(12), 0.125, velocity=127, bend=-0.2)
solo.add(Ni, 0.125, velocity=125)
solo.add(Sa.add(12), 0.125, velocity=127)
solo.add(Dha, 0.125, velocity=122)
solo.add(Pa, 0.125, velocity=120)
solo.add(Dha, 0.125, velocity=122)
solo.add(Ni, 0.125, velocity=125)
solo.add(Sa.add(12), 0.125, velocity=127)
# Full descending 32nd note run
solo.add(Sa.add(12), 0.125, velocity=127)
solo.add(Ni, 0.125, velocity=125)
solo.add(Dha, 0.125, velocity=122)
solo.add(Pa, 0.125, velocity=120)
solo.add(Ma, 0.125, velocity=118)
solo.add(Ga, 0.125, velocity=115)
solo.add(Re, 0.125, velocity=112)
solo.add(Sa, 0.125, velocity=110)
# Rocket back up
solo.add(Re, 0.125, velocity=118)
solo.add(Ga, 0.125, velocity=122)
solo.add(Ma, 0.125, velocity=125)
solo.add(Pa, 0.125, velocity=127)
solo.add(Dha, 0.125, velocity=127)
solo.add(Ni, 0.125, velocity=127)
solo.add(Sa.add(12), 0.125, velocity=127)
solo.add(Re.add(12), 0.125, velocity=127)

# Bars 65-66: TIHAI — three-fold cadence, maximum impact
solo.add(Sa.add(12), Duration.EIGHTH, velocity=127, bend=-0.15)
solo.add(Ni, Duration.SIXTEENTH, velocity=118)
solo.add(Dha, Duration.SIXTEENTH, velocity=112)
solo.add(Pa, Duration.QUARTER, velocity=122)
solo.rest(Duration.EIGHTH)
# 2nd
solo.add(Sa.add(12), Duration.EIGHTH, velocity=127, bend=-0.15)
solo.add(Ni, Duration.SIXTEENTH, velocity=120)
solo.add(Dha, Duration.SIXTEENTH, velocity=115)
solo.add(Pa, Duration.QUARTER, velocity=125)
solo.rest(Duration.EIGHTH)
# 3rd — strongest
solo.add(Sa.add(12), Duration.EIGHTH, velocity=127, bend=-0.15)
solo.add(Ni, Duration.SIXTEENTH, velocity=125)
solo.add(Dha, Duration.SIXTEENTH, velocity=120)
solo.add(Pa, Duration.QUARTER, velocity=127)
# SAM — home
solo.rest(Duration.QUARTER)
solo.add(Sa, Duration.DOTTED_HALF, velocity=120, bend=-0.25)

# Bars 69-72: aftermath — ringing out, returning to stillness
solo.set(volume=0.5)
solo.add(Sa, Duration.WHOLE, velocity=70, bend=-0.15)
solo.add(Sa, Duration.WHOLE, velocity=45, bend=-0.1)
for _ in range(2):
    solo.rest(Duration.WHOLE)

# ── SITAR RIGHT — enters at jhala, adds stereo width ───────────
# Bars 49-52: silent (gat is solo only)
for _ in range(4):
    solo_r.rest(Duration.WHOLE)

# Bars 53-54: jhala doubled — same pattern, panned right
solo_r.set(volume=0.45)
solo_r.add(Sa.add(12), Duration.EIGHTH, velocity=100)
solo_r.add(Pa, Duration.EIGHTH, velocity=65)
solo_r.add(Sa.add(12), Duration.EIGHTH, velocity=98)
solo_r.add(Pa, Duration.EIGHTH, velocity=62)
solo_r.add(Ni, Duration.EIGHTH, velocity=95)
solo_r.add(Pa, Duration.EIGHTH, velocity=65)
solo_r.add(Dha, Duration.EIGHTH, velocity=92)
solo_r.add(Pa, Duration.EIGHTH, velocity=62)
solo_r.add(Ma, Duration.EIGHTH, velocity=88)
solo_r.add(Pa, Duration.EIGHTH, velocity=65)
solo_r.add(Dha, Duration.EIGHTH, velocity=95)
solo_r.add(Pa, Duration.EIGHTH, velocity=62)
solo_r.rest(Duration.QUARTER)
solo_r.rest(Duration.QUARTER)

# Bars 55-56: 16ths doubled
solo_r.set(volume=0.5)
for note, vel in [(Sa.add(12),110),(Pa,70),(Ni,102),(Pa,68),
                  (Dha,100),(Pa,65),(Pa,95),(Ma,62),
                  (Ma,90),(Pa,68),(Dha,102),(Pa,65),
                  (Ni,108),(Pa,70),(Sa.add(12),112),(Pa,68)]:
    solo_r.add(note, Duration.SIXTEENTH, velocity=vel)
for note, vel in [(Sa.add(12),115),(Re.add(12),110),(Sa.add(12),108),(Ni,100),
                  (Dha,95),(Pa,90),(Ma,82),(Ga,78),
                  (Re,70),(Sa,65),(Re,72),(Ga,80),
                  (Ma,88),(Pa,95),(Dha,102),(Ni,110)]:
    solo_r.add(note, Duration.SIXTEENTH, velocity=vel)

# Bars 57-58: peak doubled
solo_r.set(volume=0.55)
for note, vel in [(Sa.add(12),120),(Pa,72),(Sa.add(12),118),(Pa,70),
                  (Ni,112),(Pa,72),(Dha,110),(Pa,70),
                  (Sa.add(12),122),(Ni,110),(Dha,105),(Pa,100),
                  (Ma,92),(Ga,85),(Re,78),(Sa,70)]:
    solo_r.add(note, Duration.SIXTEENTH, velocity=vel)
for note, vel in [(Sa.add(12),122),(Re.add(12),118),(Sa.add(12),115),(Ni,108),
                  (Sa.add(12),120),(Ni,105),(Dha,100),(Pa,95),
                  (Ma,88),(Ga,80),(Re,72),(Sa,68),
                  (Re,75),(Ga,82),(Ma,90),(Pa,105)]:
    solo_r.add(note, Duration.SIXTEENTH, velocity=vel)

# Bars 59-60: tihai doubled
solo_r.add(Sa.add(12), Duration.EIGHTH, velocity=110, bend=-0.15)
solo_r.add(Ni, Duration.SIXTEENTH, velocity=90)
solo_r.add(Dha, Duration.SIXTEENTH, velocity=82)
solo_r.add(Pa, Duration.QUARTER, velocity=100)
solo_r.rest(Duration.EIGHTH)
solo_r.add(Sa.add(12), Duration.EIGHTH, velocity=115, bend=-0.15)
solo_r.add(Ni, Duration.SIXTEENTH, velocity=95)
solo_r.add(Dha, Duration.SIXTEENTH, velocity=88)
solo_r.add(Pa, Duration.QUARTER, velocity=105)
solo_r.rest(Duration.EIGHTH)
solo_r.add(Sa.add(12), Duration.EIGHTH, velocity=122, bend=-0.15)
solo_r.add(Ni, Duration.SIXTEENTH, velocity=102)
solo_r.add(Dha, Duration.SIXTEENTH, velocity=95)
solo_r.add(Pa, Duration.QUARTER, velocity=110)
solo_r.rest(Duration.QUARTER)
solo_r.add(Sa, Duration.DOTTED_HALF, velocity=90, bend=-0.25)

# Bars 69-72: fade
solo_r.add(Sa, Duration.WHOLE, velocity=55, bend=-0.15)
for _ in range(3):
    solo_r.rest(Duration.WHOLE)

# ── SITAR LOW — octave down, enters at peak for thickness ──────
# Bars 57-64: silent (enters at bar 65)
for _ in range(8):
    solo_low.rest(Duration.WHOLE)

# Bars 57-58: peak doubled octave down — massive
solo_low.set(volume=0.35)
for note, vel in [(Sa,115),(Pa.add(-12),70),(Sa,112),(Pa.add(-12),68),
                  (Ni.add(-12),108),(Pa.add(-12),70),(Dha.add(-12),105),(Pa.add(-12),68),
                  (Sa,118),(Ni.add(-12),105),(Dha.add(-12),100),(Pa.add(-12),95),
                  (Ma.add(-12),88),(Ga.add(-12),82),(Re.add(-12),75),(Sa.add(-12),68)]:
    solo_low.add(note, Duration.SIXTEENTH, velocity=vel)
for note, vel in [(Sa,118),(Re,112),(Sa,110),(Ni.add(-12),102),
                  (Sa,115),(Ni.add(-12),100),(Dha.add(-12),95),(Pa.add(-12),90),
                  (Ma.add(-12),82),(Ga.add(-12),78),(Re.add(-12),72),(Sa.add(-12),65),
                  (Re.add(-12),70),(Ga.add(-12),78),(Ma.add(-12),85),(Pa.add(-12),95)]:
    solo_low.add(note, Duration.SIXTEENTH, velocity=vel)

# Bars 59-60: tihai octave down
solo_low.add(Sa, Duration.EIGHTH, velocity=105)
solo_low.add(Ni.add(-12), Duration.SIXTEENTH, velocity=85)
solo_low.add(Dha.add(-12), Duration.SIXTEENTH, velocity=78)
solo_low.add(Pa.add(-12), Duration.QUARTER, velocity=95)
solo_low.rest(Duration.EIGHTH)
solo_low.add(Sa, Duration.EIGHTH, velocity=110)
solo_low.add(Ni.add(-12), Duration.SIXTEENTH, velocity=90)
solo_low.add(Dha.add(-12), Duration.SIXTEENTH, velocity=82)
solo_low.add(Pa.add(-12), Duration.QUARTER, velocity=100)
solo_low.rest(Duration.EIGHTH)
solo_low.add(Sa, Duration.EIGHTH, velocity=118)
solo_low.add(Ni.add(-12), Duration.SIXTEENTH, velocity=98)
solo_low.add(Dha.add(-12), Duration.SIXTEENTH, velocity=90)
solo_low.add(Pa.add(-12), Duration.QUARTER, velocity=108)
solo_low.rest(Duration.QUARTER)
solo_low.add(Sa.add(-12), Duration.DOTTED_HALF, velocity=85, bend=-0.25)

# Bars 69-72: fade
solo_low.add(Sa.add(-12), Duration.WHOLE, velocity=55)
for _ in range(3):
    solo_low.rest(Duration.WHOLE)

# Wet sitar resumes for the ending (bars 69-72)
sitar.set(volume=0.4)
sitar.add(Sa, Duration.WHOLE, velocity=55, bend=-0.15)
for _ in range(3):
    sitar.rest(Duration.WHOLE)

# ── BANSURI (flute) — long tones, breathy, ethereal ────────────
# Using triangle wave + heavy reverb to approximate bansuri
bansuri = score.part("bansuri", synth="triangle", envelope="pad", volume=0.2,
                     reverb=0.85, reverb_type="taj_mahal",
                     chorus=0.3, chorus_rate=0.15, chorus_depth=0.008,
                     delay=0.2, delay_time=0.461, delay_feedback=0.3,
                     lowpass=3000, pan=0.3, humanize=0.06)

# Bars 1-32: silent
for _ in range(32):
    bansuri.rest(Duration.WHOLE)

# Bars 33-40: long held notes — like breathing through bamboo
bansuri.add(Pa, Duration.WHOLE, velocity=55, bend=0.15)
bansuri.add(Pa, Duration.WHOLE, velocity=52)
bansuri.rest(Duration.WHOLE)
bansuri.add(Ma, Duration.WHOLE, velocity=50, bend=-0.1)
bansuri.add(Ga, Duration.DOTTED_HALF, velocity=48)
bansuri.rest(Duration.QUARTER)
bansuri.rest(Duration.WHOLE)
bansuri.add(Pa, Duration.WHOLE, velocity=55, bend=0.2)
bansuri.rest(Duration.WHOLE)

# Bars 41-48: a slow melody emerges
bansuri.add(Sa.add(12), Duration.HALF, velocity=60, bend=-0.15)
bansuri.add(Ni, Duration.HALF, velocity=55)
bansuri.add(Dha, Duration.WHOLE, velocity=52, bend=0.1)
bansuri.rest(Duration.WHOLE)
bansuri.add(Pa, Duration.HALF, velocity=58, bend=0.15)
bansuri.add(Dha, Duration.HALF, velocity=55, bend=-0.1)
bansuri.add(Pa, Duration.WHOLE, velocity=52)
bansuri.add(Ma, Duration.HALF, velocity=50)
bansuri.add(Ga, Duration.HALF, velocity=48, bend=0.1)
bansuri.rest(Duration.WHOLE)

# Bars 49-56: singing with sitar — call and response
bansuri.rest(Duration.WHOLE)
bansuri.rest(Duration.WHOLE)
bansuri.add(Ni, Duration.WHOLE, velocity=62, bend=0.2)
bansuri.add(Dha, Duration.HALF, velocity=58)
bansuri.add(Pa, Duration.HALF, velocity=55, bend=-0.15)
bansuri.rest(Duration.WHOLE)
bansuri.rest(Duration.WHOLE)
bansuri.add(Ga, Duration.WHOLE, velocity=50, bend=0.1)
bansuri.add(Sa, Duration.WHOLE, velocity=48, bend=-0.1)

# Bars 57-64: holds a quiet drone under the solos
for _ in range(8):
    bansuri.add(Sa, Duration.WHOLE, velocity=30, bend=0.05)

# Bars 65-72: dissolving — one last breath
bansuri.add(Sa, Duration.WHOLE, velocity=35, bend=0.1)
bansuri.add(Sa, Duration.WHOLE, velocity=25)
for _ in range(6):
    bansuri.rest(Duration.WHOLE)

# ── THEREMIN — emotional peak, wailing above the sitars ─────────
theremin = score.part("theremin", instrument="theremin", volume=0.4,
                      reverb=0.6, reverb_type="taj_mahal",
                      delay=0.3, delay_time=0.461, delay_feedback=0.35,
                      pan=0.15, humanize=0.06)

# Bars 1-62: silent — waiting for the peak
for _ in range(62):
    theremin.rest(Duration.WHOLE)

# Bars 63-64: entrance — one long note rising from nothing
theremin.add(Pa, Duration.WHOLE, velocity=70, bend=1.5)
theremin.add(Sa.add(12), Duration.WHOLE, velocity=85, bend=-0.5)

# Bars 65-66: the solo takes flight — soaring above the sitar jhala
theremin.add(Sa.add(12), Duration.QUARTER, velocity=105, bend=0.5)
theremin.add(Ni, Duration.EIGHTH, velocity=92)
theremin.add(Dha, Duration.EIGHTH, velocity=88)
theremin.add(Pa, Duration.HALF, velocity=95, bend=-0.25)
theremin.add(Dha, Duration.QUARTER, velocity=100, bend=1.0)
theremin.add(Sa.add(12), Duration.QUARTER, velocity=112, bend=0.5)
theremin.add(Re.add(12), Duration.HALF, velocity=118, bend=-0.5)
theremin.add(Sa.add(12), Duration.HALF, velocity=108)

# Bars 67-68: climax — highest point, the cry
theremin.add(Re.add(12), Duration.QUARTER, velocity=120, bend=2.0)
theremin.add(Sa.add(12), Duration.QUARTER, velocity=115, bend=1.0)
theremin.add(Ni, Duration.QUARTER, velocity=110, bend=0.5)
theremin.add(Sa.add(12), Duration.QUARTER, velocity=125, bend=-1.0)
# Descending — the release
theremin.add(Dha, Duration.QUARTER, velocity=105, bend=0.5)
theremin.add(Pa, Duration.QUARTER, velocity=95)
theremin.add(Ma, Duration.QUARTER, velocity=85, bend=-0.5)
theremin.add(Ga, Duration.QUARTER, velocity=75)

# Bars 69-72: fading — one last held note dissolving
theremin.add(Sa, Duration.WHOLE, velocity=65, bend=0.25)
theremin.add(Sa, Duration.WHOLE, velocity=40, bend=-0.15)
for _ in range(2):
    theremin.rest(Duration.WHOLE)

# ── TABLA — the softest heartbeat ──────────────────────────────
NA  = DrumSound.TABLA_NA
TIN = DrumSound.TABLA_TIN
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
TIT = DrumSound.TABLA_TIT
KE  = DrumSound.TABLA_KE
GEB = DrumSound.TABLA_GE_BEND

tabla = score.part("tabla", volume=0.4,
                   reverb=0.6, reverb_type="cathedral", reverb_decay=2.5, humanize=0.1)

# Bars 1-40: silent — no pulse yet
for _ in range(40):
    tabla.rest(Duration.WHOLE)

# Bars 41-48: barely there — slow tintal, all ghost notes
for bar in range(8):
    if bar % 8 == 7:
        # Gentle fill
        tabla.hit(tDHA, Duration.QUARTER, velocity=85, articulation="accent")
        tabla.hit(GEB, Duration.QUARTER, velocity=95)
        tabla.hit(NA, Duration.EIGHTH, velocity=68)
        tabla.hit(TIT, Duration.EIGHTH, velocity=52)
        tabla.hit(GEB, Duration.QUARTER, velocity=90)
    else:
        tabla.hit(tDHA, Duration.QUARTER, velocity=75)
        tabla.hit(TIT, Duration.EIGHTH, velocity=48)
        tabla.hit(NA, Duration.EIGHTH, velocity=58)
        tabla.hit(tDHA, Duration.QUARTER, velocity=72)
        tabla.hit(TIT, Duration.EIGHTH, velocity=45)
        tabla.hit(NA, Duration.EIGHTH, velocity=55)

# Bars 49-56: tabla accompaniment continues under the tabla solo
for bar in range(8):
    tabla.hit(tDHA, Duration.QUARTER, velocity=65)
    tabla.hit(TIT, Duration.EIGHTH, velocity=40)
    tabla.hit(NA, Duration.EIGHTH, velocity=48)
    tabla.hit(tDHA, Duration.QUARTER, velocity=62)
    tabla.hit(TIT, Duration.EIGHTH, velocity=38)
    tabla.hit(NA, Duration.EIGHTH, velocity=45)

# Bars 57-64: stays under the sitar solo, supportive
for bar in range(8):
    tabla.hit(tDHA, Duration.QUARTER, velocity=70)
    tabla.hit(TIT, Duration.EIGHTH, velocity=42)
    tabla.hit(NA, Duration.EIGHTH, velocity=52)
    tabla.hit(tDHA, Duration.QUARTER, velocity=68)
    tabla.hit(TIT, Duration.EIGHTH, velocity=40)
    tabla.hit(NA, Duration.EIGHTH, velocity=50)

# Bars 65-72: one last dha, then silence
tabla.hit(tDHA, Duration.HALF, velocity=50)
tabla.rest(Duration.HALF)
for _ in range(7):
    tabla.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# TABLA SOLO — Peshkara → Kaida → Tukra → Tihai (bars 49-56)
# Dry, present, builds from dignified to virtuosic.
# Overlaps into sitar solo — last 2 bars (57-58) they play together.
# ═══════════════════════════════════════════════════════════════════
tabla_solo = score.part("tabla_solo", volume=0.6,
                        reverb=0.15, reverb_decay=0.8,
                        humanize=0.06)

# Bars 1-48: silent
for _ in range(48):
    tabla_solo.rest(Duration.WHOLE)

# ── Bar 49: PESHKARA — theme stated, strong on the beat ─────────
tabla_solo.hit(tDHA, Duration.QUARTER, velocity=105, articulation="accent")
tabla_solo.hit(GE, Duration.EIGHTH, velocity=78)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=72)
tabla_solo.hit(tDHA, Duration.QUARTER, velocity=98, articulation="accent")
tabla_solo.hit(NA, Duration.EIGHTH, velocity=70)
tabla_solo.hit(KE, Duration.EIGHTH, velocity=60)

# ── Bar 50: PESHKARA answer — bayan responds ──────────────────
tabla_solo.hit(tDHA, Duration.QUARTER, velocity=108, articulation="accent")
tabla_solo.hit(GEB, Duration.EIGHTH, velocity=112)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=75)
tabla_solo.hit(GEB, Duration.QUARTER, velocity=115, articulation="accent")
tabla_solo.hit(NA, Duration.EIGHTH, velocity=70)
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=95)

# ── Bar 51: KAIDA — developing, 8ths ───────────────────────────
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=102, articulation="accent")
tabla_solo.hit(GE, Duration.EIGHTH, velocity=72)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=68)
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=98)
tabla_solo.hit(GEB, Duration.EIGHTH, velocity=108, articulation="accent")
tabla_solo.hit(NA, Duration.EIGHTH, velocity=72)
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=95)
tabla_solo.hit(KE, Duration.EIGHTH, velocity=60)

# ── Bar 52: KAIDA variation — more bayan ──────────────────────
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=105, articulation="accent")
tabla_solo.hit(GEB, Duration.EIGHTH, velocity=112)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=75)
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=100)
tabla_solo.hit(GEB, Duration.QUARTER, velocity=118, articulation="accent")
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=95)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=70)

# ── Bar 53: TUKRA — 16ths into 32nd note cascade ───────────────
tabla_solo.hit(tDHA, Duration.SIXTEENTH, velocity=110, articulation="accent")
tabla_solo.hit(TIT, Duration.SIXTEENTH, velocity=50)
tabla_solo.hit(NA, Duration.SIXTEENTH, velocity=78)
tabla_solo.hit(TIT, Duration.SIXTEENTH, velocity=48)
tabla_solo.hit(tDHA, Duration.SIXTEENTH, velocity=108, articulation="accent")
tabla_solo.hit(GEB, Duration.SIXTEENTH, velocity=105)
tabla_solo.hit(NA, Duration.SIXTEENTH, velocity=75)
tabla_solo.hit(TIT, Duration.SIXTEENTH, velocity=48)
# 32nd note burst — hands flying
tabla_solo.hit(tDHA, 0.125, velocity=115, articulation="accent")
tabla_solo.hit(TIT, 0.125, velocity=55)
tabla_solo.hit(NA, 0.125, velocity=82)
tabla_solo.hit(TIT, 0.125, velocity=52)
tabla_solo.hit(GEB, 0.125, velocity=118)
tabla_solo.hit(NA, 0.125, velocity=78)
tabla_solo.hit(tDHA, 0.125, velocity=120, articulation="accent")
tabla_solo.hit(GEB, 0.125, velocity=115)

# ── Bar 54: TUKRA — full 32nd note shred ──────────────────────
# First half: 32nd note roll building
tabla_solo.hit(tDHA, 0.125, velocity=112, articulation="accent")
tabla_solo.hit(TIT, 0.125, velocity=55)
tabla_solo.hit(NA, 0.125, velocity=80)
tabla_solo.hit(TIT, 0.125, velocity=52)
tabla_solo.hit(tDHA, 0.125, velocity=118, articulation="accent")
tabla_solo.hit(GEB, 0.125, velocity=115)
tabla_solo.hit(NA, 0.125, velocity=82)
tabla_solo.hit(TIT, 0.125, velocity=55)
tabla_solo.hit(GEB, 0.125, velocity=120, articulation="accent")
tabla_solo.hit(tDHA, 0.125, velocity=122)
tabla_solo.hit(NA, 0.125, velocity=85)
tabla_solo.hit(GEB, 0.125, velocity=125)
tabla_solo.hit(tDHA, 0.125, velocity=125, articulation="accent")
tabla_solo.hit(GEB, 0.125, velocity=127)
tabla_solo.hit(tDHA, 0.125, velocity=127, articulation="accent")
tabla_solo.hit(GEB, 0.125, velocity=127)

# ── Bar 55: TIHAI — three-fold cadence on the beat ──────────────
# 1st
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=105, articulation="accent")
tabla_solo.hit(NA, Duration.SIXTEENTH, velocity=78)
tabla_solo.hit(GEB, Duration.SIXTEENTH, velocity=108)
tabla_solo.rest(Duration.EIGHTH)
# 2nd
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=115, articulation="accent")
tabla_solo.hit(NA, Duration.SIXTEENTH, velocity=82)
tabla_solo.hit(GEB, Duration.SIXTEENTH, velocity=115)
tabla_solo.rest(Duration.EIGHTH)
# 3rd — strongest
tabla_solo.hit(tDHA, Duration.EIGHTH, velocity=125, articulation="accent")
tabla_solo.hit(NA, Duration.SIXTEENTH, velocity=90)
tabla_solo.hit(GEB, Duration.SIXTEENTH, velocity=122)

# ── Bar 56: SAM + handoff ───────────────────────────────────────
tabla_solo.hit(tDHA, Duration.WHOLE, velocity=120, articulation="fermata")

# Bars 57-58: tabla solo continues under sitar — supportive fills
tabla_solo.set(volume=0.35)
tabla_solo.hit(tDHA, Duration.QUARTER, velocity=80, articulation="accent")
tabla_solo.hit(GE, Duration.EIGHTH, velocity=55)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=62)
tabla_solo.hit(GEB, Duration.QUARTER, velocity=85)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=58)
tabla_solo.hit(TIT, Duration.EIGHTH, velocity=42)
tabla_solo.hit(tDHA, Duration.QUARTER, velocity=75)
tabla_solo.hit(GEB, Duration.EIGHTH, velocity=80)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=55)
tabla_solo.hit(tDHA, Duration.QUARTER, velocity=70)
tabla_solo.hit(TIT, Duration.EIGHTH, velocity=40)
tabla_solo.hit(NA, Duration.EIGHTH, velocity=48)

# Bars 59-72: silent — sitar owns the space
for _ in range(14):
    tabla_solo.rest(Duration.WHOLE)

# ── TINGSHA — crystalline accents, very sparse ──────────────────
tingsha = score.part("tingsha", instrument="tingsha", volume=0.15,
                     reverb=0.5, reverb_decay=2.5)

# One strike every ~8 bars, offset from bowl
for _ in range(4):
    tingsha.rest(Duration.WHOLE)
tingsha.add(Sa.add(12), Duration.WHOLE, velocity=50)
for _ in range(7):
    tingsha.rest(Duration.WHOLE)
tingsha.add(Pa.add(12), Duration.WHOLE, velocity=45)
for _ in range(7):
    tingsha.rest(Duration.WHOLE)
tingsha.add(Sa.add(12), Duration.WHOLE, velocity=42)
for _ in range(7):
    tingsha.rest(Duration.WHOLE)
tingsha.add(Ma.add(12), Duration.WHOLE, velocity=38)
for _ in range(7):
    tingsha.rest(Duration.WHOLE)
tingsha.add(Sa.add(12), Duration.WHOLE, velocity=35)
for _ in range(7):
    tingsha.rest(Duration.WHOLE)
tingsha.add(Sa.add(12), Duration.WHOLE, velocity=28)
for _ in range(7):
    tingsha.rest(Duration.WHOLE)
# Rest out through solos and ending
for _ in range(20):
    tingsha.rest(Duration.WHOLE)

# ── KICK — the temple's heartbeat ───────────────────────────────
K = DrumSound.KICK
kick = score.part("kick", volume=0.55, humanize=0.03)

# Bars 1-48: silent
for _ in range(48):
    kick.rest(Duration.WHOLE)

# Bars 49-56: enters with tabla solo — slow pulse, beat 1 only
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=100)
    kick.rest(Duration.DOTTED_HALF)

# Bars 57-64: sitar gat/jhala — four on the floor, building
for bar in range(8):
    vel = min(120, 100 + bar * 3)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# Bars 65-68: peak — full power
for _ in range(4):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=120)

# Bars 69-72: fading out with everything
for bar in range(4):
    vel = max(25, 110 - bar * 25)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# ── SUB DRONE — deep sine, barely audible grounding ────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.15,
                 lowpass=80, saturation=0.1)

# Bars 1-8: silent
for _ in range(8):
    sub.rest(Duration.WHOLE)

# Bars 9-64: deep Sa drone — felt more than heard
for _ in range(56):
    sub.add(Sa.add(-36), Duration.WHOLE, velocity=55)

# Bars 65-72: fade
for vel in [45, 35, 25, 18, 12, 8, 4, 0]:
    if vel > 0:
        sub.add(Sa.add(-36), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"Temperament: shruti / just intonation / A=432 Hz")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing THE TEMPLE (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing THE TEMPLE...")
    play_score(score)
