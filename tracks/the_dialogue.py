"""
THE DIALOGUE — two voices learning to speak together.
Sitar (human) and theremin (machine) start alone, find each other,
and become something neither could be on their own.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("E", "phrygian")
s = key.scale  # E F G A B C D

Sa  = s[0]   # E  (Sa)
Re  = s[1]   # F  (komal Re)
Ga  = s[2]   # G  (komal Ga)
Ma  = s[3]   # A  (Ma)
Pa  = s[4]   # B  (Pa)
Dha = s[5]   # C  (komal Dha)
Ni  = s[6]   # D  (komal Ni)

score = Score("4/4", bpm=75, system="shruti", temperament="just",
              reference_pitch=432.0)

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (80 bars, ~7 min):
#   Bars  1-8:   Silence, then tambura — the shared space opens
#   Bars  9-16:  Sitar alone — the human speaks first
#   Bars 17-24:  Theremin alone — the machine responds
#   Bars 25-32:  Call and response — they notice each other
#   Bars 33-40:  Weaving together — phrases overlap
#   Bars 41-48:  Tabla enters — they've found a shared pulse
#   Bars 49-56:  Harmonium + choir — the harmony deepens
#   Bars 57-64:  The peak — full communion, everyone singing
#   Bars 65-72:  Unwinding — voices separate but changed
#   Bars 73-80:  Silence returns — but different from before
# ═══════════════════════════════════════════════════════════════════

# ── TAMBURA — the shared space, the room they're both in ────────
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.25,
                     reverb=0.95, reverb_type="taj_mahal",
                     chorus=0.5, chorus_rate=0.06, chorus_depth=0.012,
                     lowpass=900, pan=-0.2, saturation=0.15)

# Bars 1-4: silence
for _ in range(4):
    tambura.rest(Duration.WHOLE)

# Bars 5-8: fade in — the space opens
for vel in [15, 25, 35, 45]:
    tambura.add(Sa.add(-24), Duration.HALF, velocity=vel)
    tambura.add(Pa.add(-24), Duration.HALF, velocity=max(10, vel - 8))

# Bars 9-72: full drone
for _ in range(64):
    tambura.add(Sa.add(-24), Duration.HALF, velocity=55)
    tambura.add(Pa.add(-24), Duration.HALF, velocity=48)

# Bars 73-80: fade out
for vel in [48, 40, 32, 25, 18, 12, 6, 0]:
    if vel > 0:
        tambura.add(Sa.add(-24), Duration.HALF, velocity=vel)
        tambura.add(Pa.add(-24), Duration.HALF, velocity=max(5, vel - 8))
    else:
        tambura.rest(Duration.WHOLE)

# ── TAMBURA HIGH — octave shimmer ──────────────────────────────
tambura_hi = score.part("tambura_hi", synth="sine", envelope="pad", volume=0.15,
                        reverb=0.95, reverb_type="taj_mahal",
                        chorus=0.6, chorus_rate=0.04, chorus_depth=0.015,
                        lowpass=1400, pan=0.25)

for _ in range(8):
    tambura_hi.rest(Duration.WHOLE)
for _ in range(64):
    tambura_hi.add(Sa.add(-12), Duration.WHOLE, velocity=40)
for vel in [35, 28, 20, 14, 10, 6, 3, 0]:
    if vel > 0:
        tambura_hi.add(Sa.add(-12), Duration.WHOLE, velocity=vel)
    else:
        tambura_hi.rest(Duration.WHOLE)

# ── SINGING BOWL — marks transitions ───────────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.5,
                  reverb=1.0, reverb_type="taj_mahal",
                  delay=0.35, delay_time=0.8, delay_feedback=0.45)

# Strike at key structural moments
bowl_bars = [1, 9, 17, 25, 33, 41, 49, 57, 73]
bar = 1
for b in range(80):
    bar = b + 1
    if bar in bowl_bars:
        vel = 75 if bar <= 57 else 55
        bowl.add(Sa.add(-24), Duration.WHOLE, velocity=vel)
    else:
        bowl.rest(Duration.WHOLE)

# ── SUB DRONE — felt not heard ─────────────────────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.15,
                 lowpass=80, saturation=0.1)

for _ in range(8):
    sub.rest(Duration.WHOLE)
for _ in range(64):
    sub.add(Sa.add(-36), Duration.WHOLE, velocity=55)
for vel in [45, 35, 25, 18, 12, 8, 4, 0]:
    if vel > 0:
        sub.add(Sa.add(-36), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# ── SITAR — the human voice ────────────────────────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.7,
                   reverb=0.35, reverb_type="taj_mahal",
                   delay=0.25, delay_time=0.4, delay_feedback=0.3,
                   pan=-0.25, saturation=0.25, humanize=0.12)

# Bars 1-8: silent — waiting
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# Bars 9-16: SITAR ALONE — tentative, exploring
# Phrase 1: simple, feeling the space
sitar.add(Sa, Duration.WHOLE, velocity=75, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.add(Re, Duration.HALF, velocity=70)
sitar.add(Sa, Duration.HALF, velocity=78)
sitar.rest(Duration.WHOLE)

# Phrase 2: reaching a little further
sitar.add(Ga, Duration.DOTTED_HALF, velocity=80)
sitar.rest(Duration.QUARTER)
sitar.add(Ma, Duration.QUARTER, velocity=75)
sitar.add(Ga, Duration.QUARTER, velocity=70)
sitar.add(Re, Duration.QUARTER, velocity=68)
sitar.add(Sa, Duration.QUARTER, velocity=72)
sitar.rest(Duration.WHOLE)

# Bars 17-24: silent while theremin speaks
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# Bars 25-32: CALL AND RESPONSE — sitar calls
# Bar 25-26: sitar phrase
sitar.add(Sa, Duration.QUARTER, velocity=85)
sitar.add(Ga, Duration.QUARTER, velocity=80)
sitar.add(Pa, Duration.HALF, velocity=88, bend=-0.15)
sitar.rest(Duration.WHOLE)
# Bar 27-28: rest while theremin responds
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)
# Bar 29-30: sitar answers back, climbing higher
sitar.add(Pa, Duration.QUARTER, velocity=90)
sitar.add(Dha, Duration.QUARTER, velocity=85)
sitar.add(Ni, Duration.HALF, velocity=92, bend=-0.2)
sitar.rest(Duration.WHOLE)
# Bar 31-32: rest
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 33-40: WEAVING — phrases start overlapping
sitar.add(Sa, Duration.EIGHTH, velocity=88)
sitar.add(Re, Duration.EIGHTH, velocity=82)
sitar.add(Ga, Duration.QUARTER, velocity=90)
sitar.add(Ma, Duration.HALF, velocity=85)
sitar.add(Pa, Duration.QUARTER, velocity=92)
sitar.add(Ma, Duration.EIGHTH, velocity=82)
sitar.add(Ga, Duration.EIGHTH, velocity=78)
sitar.add(Re, Duration.HALF, velocity=80)
sitar.rest(Duration.WHOLE)
sitar.add(Ga, Duration.QUARTER, velocity=85)
sitar.add(Pa, Duration.QUARTER, velocity=90)
sitar.add(Dha, Duration.HALF, velocity=95, bend=-0.15)
sitar.add(Pa, Duration.QUARTER, velocity=88)
sitar.add(Ma, Duration.QUARTER, velocity=82)
sitar.add(Ga, Duration.QUARTER, velocity=78)
sitar.add(Sa, Duration.QUARTER, velocity=75)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 41-48: SHARED PULSE — more confident, rhythmic
sitar.set(volume=0.8)
for _ in range(2):
    sitar.add(Sa, Duration.EIGHTH, velocity=95)
    sitar.add(Ga, Duration.EIGHTH, velocity=88)
    sitar.add(Pa, Duration.QUARTER, velocity=100)
    sitar.add(Dha, Duration.EIGHTH, velocity=92)
    sitar.add(Pa, Duration.EIGHTH, velocity=88)
    sitar.add(Ma, Duration.QUARTER, velocity=85)
    sitar.add(Ga, Duration.EIGHTH, velocity=82)
    sitar.add(Ma, Duration.EIGHTH, velocity=85)
    sitar.add(Pa, Duration.QUARTER, velocity=95)
    sitar.add(Ma, Duration.EIGHTH, velocity=80)
    sitar.add(Ga, Duration.EIGHTH, velocity=78)
    sitar.add(Re, Duration.QUARTER, velocity=82)
    sitar.add(Sa, Duration.HALF, velocity=88, bend=-0.15)
    sitar.rest(Duration.HALF)

# Bars 49-56: DEEPENING — sitar plays fuller, more ornamental
for _ in range(2):
    sitar.add(Sa, Duration.EIGHTH, velocity=100)
    sitar.add(Re, Duration.SIXTEENTH, velocity=85)
    sitar.add(Ga, Duration.SIXTEENTH, velocity=88)
    sitar.add(Ma, Duration.QUARTER, velocity=98)
    sitar.add(Pa, Duration.HALF, velocity=105, bend=-0.15)
    sitar.add(Dha, Duration.QUARTER, velocity=95)
    sitar.add(Pa, Duration.EIGHTH, velocity=90)
    sitar.add(Ma, Duration.EIGHTH, velocity=85)
    sitar.add(Ga, Duration.QUARTER, velocity=88)
    sitar.add(Re, Duration.HALF, velocity=82)
    sitar.add(Sa, Duration.HALF, velocity=90, bend=-0.15)
    sitar.rest(Duration.HALF)

# Bars 57-64: THE PEAK — jhala, full power
sitar.set(volume=0.95)
# 16th note runs
for _ in range(2):
    for note, vel in [(Sa,115),(Pa.add(-12),80),(Sa,112),(Pa.add(-12),78),
                      (Re,108),(Pa.add(-12),80),(Ga,110),(Pa.add(-12),78),
                      (Ma,112),(Pa.add(-12),80),(Pa,115),(Pa.add(-12),82),
                      (Dha,118),(Pa.add(-12),80),(Ni,120),(Pa.add(-12),82)]:
        sitar.add(note, Duration.SIXTEENTH, velocity=vel)
# 32nd note shred — pull reverb back so the notes cut through
sitar.set(reverb=0.1, delay=0.08)
for note in [Sa, Re, Ga, Ma, Pa, Dha, Ni, Sa.add(12),
             Sa.add(12), Ni, Dha, Pa, Ma, Ga, Re, Sa]:
    sitar.add(note, 0.125, velocity=125)
# Descending 32nd
for note in [Ni, Dha, Pa, Ma, Ga, Re, Sa, Pa.add(-12),
             Sa, Re, Ga, Ma, Pa, Dha, Ni, Sa.add(12)]:
    sitar.add(note, 0.125, velocity=120)
# Held peak note — reverb back for the sustain
sitar.set(reverb=0.35, delay=0.25)
sitar.add(Sa.add(12), Duration.HALF, velocity=127, bend=-0.2)
sitar.add(Pa, Duration.HALF, velocity=110)
sitar.add(Sa, Duration.WHOLE, velocity=100, bend=-0.15)
sitar.rest(Duration.WHOLE)

# Bars 65-72: UNWINDING — slower, changed
sitar.set(volume=0.6)
sitar.add(Sa, Duration.WHOLE, velocity=75, bend=-0.1)
sitar.rest(Duration.WHOLE)
sitar.add(Ga, Duration.HALF, velocity=70)
sitar.add(Re, Duration.HALF, velocity=68)
sitar.add(Sa, Duration.WHOLE, velocity=72, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.add(Pa.add(-12), Duration.HALF, velocity=65)
sitar.add(Sa, Duration.HALF, velocity=70)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 73-80: silence
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# ── THEREMIN — the machine voice ───────────────────────────────
theremin = score.part("theremin", instrument="theremin", volume=0.42,
                      reverb=0.6, reverb_type="taj_mahal",
                      delay=0.35, delay_time=0.533, delay_feedback=0.4,
                      pan=0.25, humanize=0.04)

# Bars 1-16: silent — listening
for _ in range(16):
    theremin.rest(Duration.WHOLE)

# Bars 17-24: THEREMIN ALONE — curious, probing, different phrasing
# Not trying to sound like sitar — it has its own voice
theremin.add(Pa.add(12), Duration.WHOLE, velocity=70, bend=1.0)
theremin.rest(Duration.WHOLE)
theremin.add(Ma.add(12), Duration.HALF, velocity=65, bend=-0.5)
theremin.add(Pa.add(12), Duration.HALF, velocity=72, bend=0.5)
theremin.rest(Duration.WHOLE)

theremin.add(Sa.add(24), Duration.HALF, velocity=78, bend=-1.0)
theremin.add(Ni.add(12), Duration.HALF, velocity=72, bend=0.5)
theremin.add(Dha.add(12), Duration.HALF, velocity=68, bend=-0.5)
theremin.add(Pa.add(12), Duration.HALF, velocity=75, bend=0.25)
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)

# Bars 25-32: CALL AND RESPONSE — theremin responds
# Bar 25-26: rest while sitar calls
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)
# Bar 27-28: theremin responds — echoing the sitar's phrase but different
theremin.add(Sa.add(12), Duration.QUARTER, velocity=80, bend=0.5)
theremin.add(Ga.add(12), Duration.QUARTER, velocity=75, bend=-0.25)
theremin.add(Pa.add(12), Duration.HALF, velocity=85, bend=1.0)
theremin.rest(Duration.WHOLE)
# Bar 29-30: rest while sitar plays
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)
# Bar 31-32: theremin responds to the higher phrase
theremin.add(Pa.add(12), Duration.QUARTER, velocity=85, bend=0.5)
theremin.add(Dha.add(12), Duration.QUARTER, velocity=82, bend=-0.5)
theremin.add(Ni.add(12), Duration.HALF, velocity=90, bend=1.5)
theremin.rest(Duration.WHOLE)

# Bars 33-40: WEAVING — overlapping with sitar
theremin.rest(Duration.WHOLE)
theremin.add(Pa.add(12), Duration.HALF, velocity=85, bend=0.5)
theremin.add(Dha.add(12), Duration.HALF, velocity=80, bend=-0.25)
theremin.add(Ni.add(12), Duration.QUARTER, velocity=88, bend=0.5)
theremin.add(Sa.add(24), Duration.QUARTER, velocity=92, bend=-0.5)
theremin.add(Ni.add(12), Duration.HALF, velocity=85, bend=0.25)
theremin.rest(Duration.WHOLE)
theremin.add(Ma.add(12), Duration.HALF, velocity=82, bend=0.5)
theremin.add(Pa.add(12), Duration.HALF, velocity=88, bend=-0.25)
theremin.add(Dha.add(12), Duration.WHOLE, velocity=85, bend=1.0)
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)

# Bars 41-48: SHARED PULSE — theremin finds the rhythm
theremin.set(volume=0.6)
for _ in range(2):
    theremin.add(Pa.add(12), Duration.QUARTER, velocity=95, bend=0.25)
    theremin.add(Dha.add(12), Duration.QUARTER, velocity=88, bend=-0.15)
    theremin.add(Sa.add(24), Duration.HALF, velocity=100, bend=0.5)
    theremin.add(Ni.add(12), Duration.QUARTER, velocity=90, bend=-0.25)
    theremin.add(Dha.add(12), Duration.QUARTER, velocity=85)
    theremin.add(Pa.add(12), Duration.HALF, velocity=88, bend=0.15)
    theremin.rest(Duration.WHOLE)
    theremin.rest(Duration.WHOLE)

# Bars 49-56: DEEPENING — theremin sings more freely
theremin.set(volume=0.65)
theremin.add(Sa.add(24), Duration.HALF, velocity=100, bend=1.0)
theremin.add(Ni.add(12), Duration.QUARTER, velocity=92, bend=-0.5)
theremin.add(Dha.add(12), Duration.QUARTER, velocity=88)
theremin.add(Pa.add(12), Duration.WHOLE, velocity=95, bend=0.5)
theremin.rest(Duration.WHOLE)
theremin.add(Dha.add(12), Duration.QUARTER, velocity=95, bend=0.5)
theremin.add(Sa.add(24), Duration.QUARTER, velocity=105, bend=-0.25)
theremin.add(Ni.add(12), Duration.HALF, velocity=98, bend=1.0)
theremin.add(Dha.add(12), Duration.QUARTER, velocity=90)
theremin.add(Pa.add(12), Duration.QUARTER, velocity=85, bend=-0.25)
theremin.add(Ma.add(12), Duration.HALF, velocity=82, bend=0.5)
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)

# Bars 57-64: THE PEAK — theremin soars above everything
theremin.set(volume=0.7)
theremin.add(Sa.add(24), Duration.QUARTER, velocity=110, bend=1.5)
theremin.add(Ni.add(12), Duration.EIGHTH, velocity=100)
theremin.add(Sa.add(24), Duration.EIGHTH, velocity=108, bend=-0.5)
theremin.add(Re.add(24), Duration.HALF, velocity=115, bend=2.0)
theremin.add(Sa.add(24), Duration.HALF, velocity=108, bend=-1.0)
theremin.add(Ni.add(12), Duration.HALF, velocity=105, bend=0.5)
# The cry — highest point
theremin.add(Re.add(24), Duration.QUARTER, velocity=120, bend=2.5)
theremin.add(Sa.add(24), Duration.QUARTER, velocity=115, bend=-1.0)
theremin.add(Ni.add(12), Duration.QUARTER, velocity=110, bend=0.5)
theremin.add(Sa.add(24), Duration.QUARTER, velocity=118, bend=1.5)
# Descending together with sitar
theremin.add(Dha.add(12), Duration.QUARTER, velocity=105, bend=0.5)
theremin.add(Pa.add(12), Duration.QUARTER, velocity=98)
theremin.add(Ma.add(12), Duration.QUARTER, velocity=90, bend=-0.25)
theremin.add(Ga.add(12), Duration.QUARTER, velocity=82)
theremin.add(Sa.add(12), Duration.WHOLE, velocity=88, bend=0.25)
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)

# Bars 65-72: UNWINDING — changed by the encounter
theremin.set(volume=0.45)
theremin.rest(Duration.WHOLE)
theremin.add(Pa.add(12), Duration.WHOLE, velocity=65, bend=0.25)
theremin.rest(Duration.WHOLE)
theremin.add(Sa.add(12), Duration.WHOLE, velocity=60, bend=-0.15)
theremin.rest(Duration.WHOLE)
theremin.add(Ga.add(12), Duration.HALF, velocity=55, bend=0.25)
theremin.add(Sa.add(12), Duration.HALF, velocity=52, bend=-0.1)
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)

# Bars 73-80: one last note — then gone
theremin.add(Sa.add(12), Duration.WHOLE, velocity=40, bend=0.15)
for _ in range(7):
    theremin.rest(Duration.WHOLE)

# ── HOUSE BEAT — the machine brings rhythm ─────────────────────
K  = DrumSound.KICK
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT
CL = DrumSound.CLAP

kick = score.part("kick", volume=0.5, humanize=0.03)
hats = score.part("hats", volume=0.25, humanize=0.04)
clap = score.part("clap", volume=0.25, reverb=0.2, humanize=0.04)

# Bars 1-40: silent
for _ in range(40):
    kick.rest(Duration.WHOLE)
    hats.rest(Duration.WHOLE)
    clap.rest(Duration.WHOLE)

# Bars 41-48: kick enters — just the pulse, minimal
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=100)
    kick.rest(Duration.DOTTED_HALF)
    hats.rest(Duration.WHOLE)
    clap.rest(Duration.WHOLE)

# Bars 49-56: full four-on-the-floor + offbeat hats + clap on 2&4
for _ in range(8):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=108)
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=65)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=90)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=92)

# Bars 57-64: peak — driving, open hat on the &
for _ in range(8):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=115)
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        if beat % 2 == 1:
            hats.hit(OH, Duration.EIGHTH, velocity=62)
        else:
            hats.hit(CH, Duration.EIGHTH, velocity=68)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=95)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=98)

# Bars 65-72: beat thins out
for bar in range(8):
    vel = max(25, 105 - bar * 10)
    kick.hit(K, Duration.QUARTER, velocity=vel)
    kick.rest(Duration.DOTTED_HALF)
    hats.rest(Duration.WHOLE)
    vel_c = max(20, 85 - bar * 10)
    if bar < 4:
        clap.rest(Duration.QUARTER)
        clap.hit(CL, Duration.QUARTER, velocity=vel_c)
        clap.rest(Duration.HALF)
    else:
        clap.rest(Duration.WHOLE)

# Bars 73-80: silence
for _ in range(8):
    kick.rest(Duration.WHOLE)
    hats.rest(Duration.WHOLE)
    clap.rest(Duration.WHOLE)

# ── TABLA — enters when they find shared rhythm ────────────────
NA  = DrumSound.TABLA_NA
TIN = DrumSound.TABLA_TIN
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
TIT = DrumSound.TABLA_TIT
KE  = DrumSound.TABLA_KE
GEB = DrumSound.TABLA_GE_BEND

tabla = score.part("tabla", volume=0.45,
                   reverb=0.4, reverb_type="cathedral", reverb_decay=2.0,
                   humanize=0.1)

# Bars 1-40: silent — no shared pulse yet
for _ in range(40):
    tabla.rest(Duration.WHOLE)

# Bars 41-56: gentle groove — they've found each other
for bar in range(16):
    if bar % 8 == 7:
        # Fill
        tabla.hit(tDHA, Duration.EIGHTH, velocity=90, articulation="accent")
        tabla.hit(GEB, Duration.EIGHTH, velocity=100)
        tabla.hit(NA, Duration.EIGHTH, velocity=72)
        tabla.hit(GEB, Duration.EIGHTH, velocity=95)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=88, articulation="accent")
        tabla.hit(NA, Duration.SIXTEENTH, velocity=65)
        tabla.hit(TIT, Duration.SIXTEENTH, velocity=50)
        tabla.hit(GEB, Duration.QUARTER, velocity=105)
    else:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=80, articulation="accent")
        tabla.hit(GE, Duration.EIGHTH, velocity=55)
        tabla.hit(NA, Duration.EIGHTH, velocity=65)
        tabla.hit(TIT, Duration.EIGHTH, velocity=42)
        tabla.hit(NA, Duration.EIGHTH, velocity=60)
        tabla.hit(TIT, Duration.EIGHTH, velocity=40)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=78, articulation="accent")
        tabla.hit(NA, Duration.EIGHTH, velocity=58)

# Bars 57-64: peak — driving, urgent
for bar in range(8):
    tabla.hit(tDHA, Duration.SIXTEENTH, velocity=100, articulation="accent")
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=50)
    tabla.hit(NA, Duration.SIXTEENTH, velocity=72)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=48)
    tabla.hit(tDHA, Duration.SIXTEENTH, velocity=98, articulation="accent")
    tabla.hit(GEB, Duration.SIXTEENTH, velocity=95)
    tabla.hit(NA, Duration.SIXTEENTH, velocity=68)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=48)
    tabla.hit(GEB, Duration.SIXTEENTH, velocity=102, articulation="accent")
    tabla.hit(NA, Duration.SIXTEENTH, velocity=70)
    tabla.hit(tDHA, Duration.SIXTEENTH, velocity=98)
    tabla.hit(TIT, Duration.SIXTEENTH, velocity=50)
    tabla.hit(tDHA, Duration.QUARTER, velocity=105, articulation="accent")

# Bars 65-72: softening
for bar in range(8):
    vel = max(35, 75 - bar * 5)
    tabla.hit(tDHA, Duration.QUARTER, velocity=vel)
    tabla.hit(TIT, Duration.EIGHTH, velocity=max(20, vel - 30))
    tabla.hit(NA, Duration.EIGHTH, velocity=max(25, vel - 15))
    tabla.hit(tDHA, Duration.QUARTER, velocity=max(30, vel - 5))
    tabla.hit(TIT, Duration.EIGHTH, velocity=max(20, vel - 32))
    tabla.hit(NA, Duration.EIGHTH, velocity=max(25, vel - 18))

# Bars 73-80: silence
for _ in range(8):
    tabla.rest(Duration.WHOLE)

# ── HARMONIUM — emerges when harmony is found ──────────────────
harmonium = score.part("harmonium", instrument="harmonium", volume=0.12,
                       reverb=0.75, reverb_type="taj_mahal",
                       chorus=0.2, chorus_rate=0.1, chorus_depth=0.006,
                       humanize=0.08)

# Bars 1-48: silent
for _ in range(48):
    harmonium.rest(Duration.WHOLE)

# Bars 49-64: the harmony that emerges from dialogue
harm_prog = key.progression("i", "iv", "VI", "v")
for _ in range(4):
    for chord in harm_prog:
        harmonium.add(chord, Duration.WHOLE, velocity=55)

# Bars 65-72: fading
for chord in harm_prog:
    harmonium.add(chord, Duration.WHOLE, velocity=42)
for chord in harm_prog:
    harmonium.add(chord, Duration.WHOLE, velocity=30)

# Bars 73-80: silence
for _ in range(8):
    harmonium.rest(Duration.WHOLE)

# ── PAD — the shared understanding ─────────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.1,
                 reverb=0.7, reverb_type="taj_mahal",
                 chorus=0.4, chorus_rate=0.15, chorus_depth=0.01,
                 lowpass=1500)

# Bars 1-48: silent
for _ in range(48):
    pad.rest(Duration.WHOLE)

# Bars 49-64: swells — the shared understanding
for _ in range(4):
    for chord in harm_prog:
        pad.add(chord, Duration.WHOLE, velocity=55)

# Bars 65-72: fading
for vel in [45, 38, 30, 22, 15, 10, 5, 0]:
    if vel > 0:
        pad.add(harm_prog[0], Duration.WHOLE, velocity=vel)
    else:
        pad.rest(Duration.WHOLE)

# Bars 73-80: silence
for _ in range(8):
    pad.rest(Duration.WHOLE)

# ── ROOM TONE — the space itself ───────────────────────────────
room = score.part("room", synth="noise", envelope="pad", volume=0.025,
                  reverb=1.0, reverb_type="taj_mahal",
                  lowpass=300)
room.lfo("lowpass", rate=0.008, min=150, max=500, bars=80, shape="sine")
room.lfo("volume", rate=0.006, min=0.01, max=0.035, bars=80, shape="triangle")

for _ in range(80):
    room.add(Sa, Duration.WHOLE, velocity=25)

# ── TINGSHA — punctuation at the very start and end ─────────────
tingsha = score.part("tingsha", instrument="tingsha", volume=0.25,
                     reverb=0.9, reverb_type="taj_mahal")

# First bar: announces the beginning
tingsha.add(Sa.add(12), Duration.WHOLE, velocity=60)
for _ in range(78):
    tingsha.rest(Duration.WHOLE)
# Last bar: closes the circle
tingsha.add(Sa.add(12), Duration.WHOLE, velocity=50)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"Temperament: shruti / just intonation / A=432 Hz")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing THE DIALOGUE (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing THE DIALOGUE...")
    play_score(score)
