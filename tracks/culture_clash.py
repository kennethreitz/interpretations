"""
CULTURE CLASH — didgeridoo chord → rhodes → tabla/sitar pop progression →
NES Mario meets Drake → marching snare military finale over 808 fadeout.
A fever dream of musical tourism. ~4 minutes.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

# ── Key: C major ────────────────────────────────────────────────
key = Key("D", "minor")
s = key.scale
prog = key.progression("i", "VII", "VI", "iv")  # Dm - C - Bb - Gm

C  = Tone.from_string("C4")
D  = s[0]; E  = s[1]; F  = s[2]; G  = s[3]
A  = s[4]; Bb = s[5]; Cs = s[6]  # C#/Db for leading tone

score = Score("4/4", bpm=95)

# Tabla bols
NA  = DrumSound.TABLA_NA
TIT = DrumSound.TABLA_TIT
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
KE  = DrumSound.TABLA_KE
GEB = DrumSound.TABLA_GE_BEND
MR  = DrumSound.MARCH_SNARE

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~4 minutes at 95 BPM):
#   Bars  1-8:   Didgeridoo chord + Rhodes
#   Bars  9-24:  Tabla + sitar arp (I-V-vi-IV), 808 enters
#   Bars 25-40:  NES Mario × Drake mashup, tabla continues
#   Bars 41-56:  Marching snare builds, 808 drives
#   Bars 57-64:  Military snare crescendo, everything fades, final hit
# ═══════════════════════════════════════════════════════════════════

# # ── INTRO — Nokia ringtone (commented out)
# intro = score.part("intro", synth="pulse", envelope="staccato", volume=0.35,
#                    lowpass=4000)
# intro.add(E.add(12), Duration.EIGHTH, velocity=95)
# intro.add(D.add(12), Duration.EIGHTH, velocity=90)
# intro.add(Tone.from_string("F#4"), Duration.QUARTER, velocity=88)
# intro.add(Tone.from_string("G#4"), Duration.QUARTER, velocity=85)
# intro.add(Tone.from_string("C#5"), Duration.EIGHTH, velocity=90)
# intro.add(Tone.from_string("B4"), Duration.EIGHTH, velocity=85)
# intro.add(D, Duration.QUARTER, velocity=82)
# intro.add(E, Duration.QUARTER, velocity=80)
# intro.rest(Duration.WHOLE)
# for _ in range(62):
#     intro.rest(Duration.WHOLE)

# ── DRUMS — four on the floor, snare on 2 & 4, trap hats ───────
drums = score.part("kit", volume=0.65, humanize=0.06)

# Bars 1-8: rests
for _ in range(8):
    drums.rest(Duration.WHOLE)

# Bars 9-56: kick + snare + trap hats
K = DrumSound.KICK
S = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

for bar in range(48):
    if bar % 8 == 7:
        # FILL BAR — snare rolls + kick accents
        drums.hit(S, Duration.SIXTEENTH, velocity=100)
        drums.hit(S, Duration.SIXTEENTH, velocity=65)
        drums.hit(S, Duration.SIXTEENTH, velocity=70)
        drums.hit(K, Duration.SIXTEENTH, velocity=105)
        drums.hit(S, Duration.SIXTEENTH, velocity=105)
        drums.hit(S, Duration.SIXTEENTH, velocity=68)
        drums.hit(S, Duration.SIXTEENTH, velocity=72)
        drums.hit(K, Duration.SIXTEENTH, velocity=108)
        drums.hit(S, Duration.SIXTEENTH, velocity=110)
        drums.hit(S, Duration.SIXTEENTH, velocity=70)
        drums.hit(K, Duration.SIXTEENTH, velocity=112)
        drums.hit(S, Duration.SIXTEENTH, velocity=75)
        drums.hit(K, Duration.SIXTEENTH, velocity=115)
        drums.hit(S, Duration.SIXTEENTH, velocity=118, articulation="accent")
        drums.hit(OH, Duration.SIXTEENTH, velocity=90)
        drums.hit(K, Duration.SIXTEENTH, velocity=120, articulation="accent")
    else:
        # Normal bar
        # Beat 1: kick + hat
        drums.hit(K, Duration.SIXTEENTH, velocity=110)
        drums.hit(CH, Duration.SIXTEENTH, velocity=55)
        drums.hit(CH, Duration.SIXTEENTH, velocity=45)
        drums.hit(CH, Duration.SIXTEENTH, velocity=50)
        # Beat 2: snare + hat
        drums.hit(S, Duration.SIXTEENTH, velocity=105)
        drums.hit(CH, Duration.SIXTEENTH, velocity=55)
        drums.hit(CH, Duration.SIXTEENTH, velocity=42)
        drums.hit(CH, Duration.SIXTEENTH, velocity=48)
        # Beat 3: kick + hat (open hat on the &)
        drums.hit(K, Duration.SIXTEENTH, velocity=108)
        drums.hit(CH, Duration.SIXTEENTH, velocity=55)
        drums.hit(OH, Duration.SIXTEENTH, velocity=60)
        drums.hit(CH, Duration.SIXTEENTH, velocity=45)
        # Beat 4: snare + hat rolls
        drums.hit(S, Duration.SIXTEENTH, velocity=108)
        drums.hit(CH, Duration.SIXTEENTH, velocity=52)
        drums.hit(CH, Duration.SIXTEENTH, velocity=48)
        drums.hit(CH, Duration.SIXTEENTH, velocity=55)

# Bars 57-64: fading via velocity
for bar in range(8):
    v = max(10, 100 - bar * 12)
    drums.hit(K, Duration.QUARTER, velocity=v)
    drums.hit(S, Duration.QUARTER, velocity=max(10, v - 10))
    drums.hit(K, Duration.QUARTER, velocity=max(10, v - 5))
    drums.hit(S, Duration.QUARTER, velocity=max(10, v - 15))

# ── DIDGERIDOO CHORD — two drones a fifth apart ────────────────
didge_lo = score.part("didge_lo", instrument="didgeridoo", volume=0.45,
                      lowpass=250)
didge_hi = score.part("didge_hi", instrument="didgeridoo", volume=0.35,
                      lowpass=300, pan=0.2)

# Bars 1-8: drone chord (D2 + A2)
for _ in range(8):
    didge_lo.add(D.add(-24), Duration.WHOLE, velocity=75)
    didge_hi.add(A.add(-24), Duration.WHOLE, velocity=65)
# Bars 9-12: fading
for vel in [60, 50, 35, 20]:
    didge_lo.add(D.add(-24), Duration.WHOLE, velocity=vel)
    didge_hi.add(A.add(-24), Duration.WHOLE, velocity=vel)
# Bars 13-56: silent
for _ in range(44):
    didge_lo.rest(Duration.WHOLE)
    didge_hi.rest(Duration.WHOLE)
# Bars 57-64: DIDGE RETURNS — massive, under the snare crescendo
for vel in [60, 75, 90, 100, 110, 115, 120, 127]:
    didge_lo.add(D.add(-24), Duration.WHOLE, velocity=vel)
    didge_hi.add(A.add(-24), Duration.WHOLE, velocity=vel)

# ── RHODES — from bar 1, the harmonic anchor ───────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.35,
                    reverb=0.6, reverb_type="taj_mahal",
                    chorus=0.3, chorus_rate=0.4, chorus_depth=0.005,
                    tremolo_depth=0.12, tremolo_rate=3.5, humanize=0.08)

# Bars 1-8
for _ in range(2):
    for chord in prog:
        rhodes.add(chord, Duration.WHOLE)

# Bars 9-24: full chords under tabla/sitar
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.WHOLE)

# Bars 25-40: choppy stabs under Mario/Drake
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.QUARTER)
        rhodes.rest(Duration.QUARTER)
        rhodes.add(chord, Duration.QUARTER)
        rhodes.rest(Duration.QUARTER)

# Bars 41-56: half notes, thinning — making room for theremin
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.HALF)
        rhodes.rest(Duration.HALF)

# ── THEREMIN SOLO — wailing over the chaos (bars 41-52) ─────────
theremin = score.part("theremin", instrument="theremin", volume=0.6,
                      reverb=0.5, reverb_type="taj_mahal",
                      delay=0.3, delay_time=0.316, delay_feedback=0.35,
                      pan=0.25, humanize=0.06)

# Bars 1-40: silent
for _ in range(40):
    theremin.rest(Duration.WHOLE)

# Bars 41-42: entrance — slow, eerie, one long note bending up
theremin.add(A, Duration.WHOLE, velocity=90, bend=1.5)
theremin.add(D.add(12), Duration.HALF, velocity=95)
theremin.add(F.add(12), Duration.HALF, velocity=100, bend=-0.5)

# Bars 43-44: the solo takes off — expressive, vocal-like
theremin.add(A.add(12), Duration.QUARTER, velocity=110, bend=0.5)
theremin.add(G.add(12), Duration.EIGHTH, velocity=95)
theremin.add(F.add(12), Duration.EIGHTH, velocity=90)
theremin.add(D.add(12), Duration.HALF, velocity=100, bend=-0.25)
theremin.add(F.add(12), Duration.QUARTER, velocity=105, bend=1.0)
theremin.add(A.add(12), Duration.QUARTER, velocity=112)
theremin.add(D.add(24), Duration.QUARTER, velocity=115, bend=-0.5)
theremin.add(A.add(12), Duration.QUARTER, velocity=100)

# Bars 45-46: climax — reaching for the top, crying
theremin.add(D.add(24), Duration.HALF, velocity=120, bend=2.0)
theremin.add(A.add(12), Duration.QUARTER, velocity=105, bend=0.5)
theremin.add(F.add(12), Duration.QUARTER, velocity=100)
theremin.add(G.add(12), Duration.QUARTER, velocity=110, bend=1.0)
theremin.add(A.add(12), Duration.QUARTER, velocity=115, bend=1.5)
theremin.add(D.add(24), Duration.HALF, velocity=125, bend=-1.0)

# Bars 47-48: fast vibrato-like passages
theremin.add(D.add(24), Duration.EIGHTH, velocity=115, bend=-0.25)
theremin.add(Cs.add(12), Duration.EIGHTH, velocity=100)
theremin.add(D.add(24), Duration.EIGHTH, velocity=118, bend=0.25)
theremin.add(Cs.add(12), Duration.EIGHTH, velocity=100)
theremin.add(A.add(12), Duration.QUARTER, velocity=110, bend=0.5)
theremin.add(F.add(12), Duration.QUARTER, velocity=105, bend=-0.5)
theremin.add(D.add(12), Duration.QUARTER, velocity=100, bend=1.0)
theremin.add(A, Duration.QUARTER, velocity=95)
theremin.add(D.add(12), Duration.HALF, velocity=108, bend=-0.25)

# Bars 49-50: descending, fading — handing off to the mario solo
theremin.add(A, Duration.QUARTER, velocity=90, bend=0.5)
theremin.add(G, Duration.QUARTER, velocity=80)
theremin.add(F, Duration.QUARTER, velocity=75, bend=-0.5)
theremin.add(D, Duration.QUARTER, velocity=70)
theremin.add(A.add(-12), Duration.WHOLE, velocity=60, bend=-1.0)

# Bars 51-52: last gasp
theremin.add(D, Duration.WHOLE, velocity=45, bend=0.5)
theremin.add(D, Duration.WHOLE, velocity=25)

# Bars 53-64: silent
for _ in range(12):
    theremin.rest(Duration.WHOLE)

# Bars 57-64: silent
for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# ── TABLA — enters bar 9 ───────────────────────────────────────
tabla = score.part("tabla", volume=0.35,
                   reverb=0.3, reverb_decay=1.2, humanize=0.08)

# Bars 1-8: rests
for _ in range(8):
    tabla.rest(Duration.WHOLE)

# Bars 9-40: keherwa groove with fills every 4 bars
for bar in range(32):
    if bar % 4 == 3:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=100, articulation="accent")
        tabla.hit(GEB, Duration.EIGHTH, velocity=115)
        tabla.hit(NA, Duration.EIGHTH, velocity=80)
        tabla.hit(GEB, Duration.EIGHTH, velocity=110)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=95, articulation="accent")
        tabla.hit(NA, Duration.SIXTEENTH, velocity=70)
        tabla.hit(KE, Duration.SIXTEENTH, velocity=60)
        tabla.hit(GEB, Duration.QUARTER, velocity=120)
    else:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=95, articulation="accent")
        tabla.hit(GE, Duration.EIGHTH, velocity=65)
        tabla.hit(NA, Duration.EIGHTH, velocity=75)
        tabla.hit(TIT, Duration.EIGHTH, velocity=50)
        tabla.hit(NA, Duration.EIGHTH, velocity=70)
        tabla.hit(TIT, Duration.EIGHTH, velocity=45)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=88, articulation="accent")
        tabla.hit(NA, Duration.EIGHTH, velocity=68)

# Bars 41-48: fading via velocity
for bar in range(8):
    tabla.hit(tDHA, Duration.EIGHTH, velocity=70)
    tabla.hit(GE, Duration.EIGHTH, velocity=45)
    tabla.hit(NA, Duration.EIGHTH, velocity=55)
    tabla.hit(TIT, Duration.EIGHTH, velocity=35)
    tabla.hit(NA, Duration.EIGHTH, velocity=50)
    tabla.hit(TIT, Duration.EIGHTH, velocity=32)
    tabla.hit(tDHA, Duration.EIGHTH, velocity=65)
    tabla.hit(NA, Duration.EIGHTH, velocity=48)

# Bars 49-64: silent
for _ in range(16):
    tabla.rest(Duration.WHOLE)

# ── SITAR — I V vi IV arpeggiated (bars 9-32) ──────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.8,
                   reverb=0.3, reverb_decay=1.5,
                   delay=0.35, delay_time=0.316, delay_feedback=0.4,
                   pan=-0.2, humanize=0.1)

# ── SITAR LOW — octave down double, thickens it up ─────────────
sitar_lo = score.part("sitar_lo", instrument="sitar", volume=0.5,
                      reverb=0.25, reverb_decay=1.2,
                      delay=0.2, delay_time=0.316, delay_feedback=0.3,
                      pan=0.15, humanize=0.1, lowpass=2000)

# Bars 1-8: rests
for _ in range(8):
    sitar.rest(Duration.WHOLE)
    sitar_lo.rest(Duration.WHOLE)

# Bars 9-24: arpeggiated pop progression
# i(Dm) - VII(C) - VI(Bb) - iv(Gm) arpeggiated
arp_chords = [
    [D, F, A, D.add(12), A, F, D, A.add(-12)],
    [C, E, G, C.add(12), G, E, C, G.add(-12)],
    [Bb.add(-12), D, F, Bb, F, D, Bb.add(-12), F.add(-12)],
    [G.add(-12), Bb.add(-12), D, G, D, Bb.add(-12), G.add(-12), D.add(-12)],
]
for _ in range(4):
    for arp in arp_chords:
        for note in arp:
            sitar.add(note, Duration.EIGHTH, velocity=85)
            sitar_lo.add(note.add(-12), Duration.EIGHTH, velocity=70)

# Bars 25-32: fading via velocity
for _ in range(2):
    for arp in arp_chords:
        for note in arp:
            sitar.add(note, Duration.EIGHTH, velocity=55)
            sitar_lo.add(note.add(-12), Duration.EIGHTH, velocity=40)

# Bars 33-64: silent
for _ in range(32):
    sitar.rest(Duration.WHOLE)
    sitar_lo.rest(Duration.WHOLE)

# ── NES MARIO — pulse wave (bars 25-56) ────────────────────────
mario = score.part("mario", synth="square", envelope="staccato", volume=0.25,
                   reverb=0.5, reverb_type="taj_mahal", lowpass=5000,
                   humanize=0.05)

# Bars 1-24: rests
for _ in range(24):
    mario.rest(Duration.WHOLE)

# Bars 25-28: World 1-1 theme
mario_melody = [
    (E.add(12), Duration.EIGHTH), (E.add(12), Duration.EIGHTH),
    (None, Duration.EIGHTH), (E.add(12), Duration.EIGHTH),
    (None, Duration.EIGHTH), (C.add(12), Duration.EIGHTH),
    (E.add(12), Duration.QUARTER),
    (G.add(12), Duration.QUARTER), (None, Duration.QUARTER),
    (G, Duration.QUARTER), (None, Duration.QUARTER),
    (C.add(12), Duration.QUARTER), (None, Duration.EIGHTH),
    (G, Duration.EIGHTH), (None, Duration.QUARTER),
    (E, Duration.QUARTER),
    (None, Duration.EIGHTH), (A, Duration.QUARTER),
    (Bb, Duration.QUARTER), (Tone.from_string("Bb4"), Duration.EIGHTH),
    (A, Duration.QUARTER),
]
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=100)

# Bars 29-32: repeat
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=105)

# Bars 33-40: Mario keeps going — repeat the theme
for _ in range(2):
    for note, dur in mario_melody:
        if note is None:
            mario.rest(dur)
        else:
            mario.add(note, dur, velocity=90)

# Bars 41-48: Mario keeps looping underneath drake
for _ in range(2):
    for note, dur in mario_melody:
        if note is None:
            mario.rest(dur)
        else:
            mario.add(note, dur, velocity=75)

# Bars 49-52: one last Mario statement fading
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=70)

# ══ Bars 53-60: MARIO SOLO — emotional 8-bit shredding ═══════════
# The NES cries out. Fast arps climbing through D minor, getting
# faster and higher. Like watching Mario run out of time.
mario.set(volume=0.45)

# Bars 53-54: 16th note arps — establishing the run
solo_arps_16 = [
    # Dm arp up and down
    D, F, A, D.add(12), A, F, D, A.add(-12),
    F, A, D.add(12), F.add(12), D.add(12), A, F, D,
    # C arp
    C, E, G, C.add(12), G, E, C, G.add(-12),
    E, G, C.add(12), E.add(12), C.add(12), G, E, C,
]
for note in solo_arps_16:
    mario.add(note, Duration.SIXTEENTH, velocity=105)

# Bars 55-56: 32nd notes — faster, climbing higher
solo_arps_32 = [
    # Dm climbing
    D, F, A, D.add(12), F.add(12), A.add(12),
    D.add(24), A.add(12), F.add(12), D.add(12), A, F,
    # Bb arp
    Bb.add(-12), D, F, Bb, D.add(12), F.add(12),
    Bb.add(12), F.add(12), D.add(12), Bb, F, D,
    # Gm arp
    G.add(-12), Bb.add(-12), D, G, Bb, D.add(12),
    G.add(12), D.add(12), Bb, G, D, Bb.add(-12),
    # Back to Dm — reaching for the top
    D, A, D.add(12), A.add(12), D.add(24), A.add(24),
    D.add(24), A.add(12), D.add(12), A, D, A.add(-12),
]
for note in solo_arps_32:
    mario.add(note, 0.125, velocity=110)

# Bars 57-58: the emotional peak — sustained high notes with fast trills
# Hold a high D while trilling between neighbors
mario.add(D.add(24), Duration.QUARTER, velocity=120)
mario.add(Cs.add(12), 0.125, velocity=100)
mario.add(D.add(24), 0.125, velocity=115)
mario.add(Cs.add(12), 0.125, velocity=100)
mario.add(D.add(24), 0.125, velocity=118)
mario.add(E.add(12), Duration.QUARTER, velocity=110)
mario.add(F.add(12), Duration.QUARTER, velocity=115)
# Descending cry
mario.add(D.add(24), Duration.EIGHTH, velocity=120)
mario.add(A.add(12), Duration.EIGHTH, velocity=105)
mario.add(F.add(12), Duration.EIGHTH, velocity=100)
mario.add(D.add(12), Duration.EIGHTH, velocity=95)
mario.add(A, Duration.EIGHTH, velocity=90)
mario.add(F, Duration.EIGHTH, velocity=85)
mario.add(D, Duration.QUARTER, velocity=110)

# Bars 59-60: final blaze — 32nd note scale runs up and down
# Full D minor scale run ascending then descending, twice
scale_up = [D, E, F, G, A, Bb, Cs, D.add(12),
            E.add(12), F.add(12), G.add(12), A.add(12),
            Bb.add(12), Cs.add(12), D.add(24), Cs.add(12)]
scale_down = [Bb.add(12), A.add(12), G.add(12), F.add(12),
              E.add(12), D.add(12), Cs, Bb,
              A, G, F, E, D, E, F, A]
for note in scale_up:
    mario.add(note, 0.125, velocity=115)
for note in scale_down:
    mario.add(note, 0.125, velocity=108)

# Bars 61-64: mario fades into the snare crescendo
mario.add(D.add(12), Duration.WHOLE, velocity=90)  # one last held note
for _ in range(3):
    mario.rest(Duration.WHOLE)

# ── NOKIA — Gran Vals ringtone on pulse wave (bars 49-56) ───────
nokia = score.part("nokia", synth="pulse", envelope="staccato", volume=0.3,
                   reverb=0.4, reverb_type="taj_mahal", lowpass=4000,
                   humanize=0.04)

# Bars 1-48: rests
for _ in range(48):
    nokia.rest(Duration.WHOLE)

# Bars 49-52: the iconic Nokia tune (Gran Vals by Francisco Tárrega)
# E5 D5 F#4 G#4 | C#5 B4 D4 E4 | B4 A4 C#4 E4 | A4
nokia_melody = [
    (E.add(12), Duration.EIGHTH), (D.add(12), Duration.EIGHTH),
    (Tone.from_string("F#4"), Duration.QUARTER), (Tone.from_string("G#4"), Duration.QUARTER),
    (Tone.from_string("C#5"), Duration.EIGHTH), (Tone.from_string("B4"), Duration.EIGHTH),
    (D, Duration.QUARTER), (E, Duration.QUARTER),
    (Tone.from_string("B4"), Duration.EIGHTH), (A, Duration.EIGHTH),
    (Tone.from_string("C#4"), Duration.QUARTER), (E, Duration.QUARTER),
    (A, Duration.HALF), (None, Duration.HALF),
]
for _ in range(2):
    for note, dur in nokia_melody:
        if note is None:
            nokia.rest(dur)
        else:
            nokia.add(note, dur, velocity=95)

# Bars 53-56: nokia fading under the mario solo
for note, dur in nokia_melody:
    if note is None:
        nokia.rest(dur)
    else:
        nokia.add(note, dur, velocity=60)
nokia.rest(Duration.WHOLE)

# Bars 57-64: silent
for _ in range(8):
    nokia.rest(Duration.WHOLE)

# ── DRAKE — steel drum Hotline Bling melody (bars 33-52) ────────
bling = score.part("bling", instrument="steel_drum", volume=0.7,
                   reverb=0.4, reverb_type="taj_mahal",
                   delay=0.3, delay_time=0.316, delay_feedback=0.35,
                   humanize=0.06)

# Bars 1-32: rests
for _ in range(32):
    bling.rest(Duration.WHOLE)

# Bars 33-40: that Hotline Bling melody — hypnotic, descending
drake_melody = [
    (D.add(12), Duration.QUARTER), (C.add(12), Duration.QUARTER),
    (A, Duration.QUARTER), (G, Duration.QUARTER),
    (A, Duration.QUARTER), (None, Duration.QUARTER),
    (G, Duration.QUARTER), (E, Duration.QUARTER),
    (D.add(12), Duration.QUARTER), (C.add(12), Duration.EIGHTH),
    (A, Duration.EIGHTH), (G, Duration.HALF),
    (A, Duration.HALF), (G, Duration.QUARTER),
    (E, Duration.QUARTER),
]
for _ in range(2):
    for note, dur in drake_melody:
        if note is None:
            bling.rest(dur)
        else:
            bling.add(note, dur, velocity=100)

# Bars 41-48: keep going, Mario layered underneath
for _ in range(2):
    for note, dur in drake_melody:
        if note is None:
            bling.rest(dur)
        else:
            bling.add(note, dur, velocity=95)

# Bars 49-52: fading
for note, dur in drake_melody:
    if note is None:
        bling.rest(dur)
    else:
        bling.add(note, dur, velocity=65)

# Bars 53-64: silent
for _ in range(12):
    bling.rest(Duration.WHOLE)

# ── 808 BASS — enters bar 9, throughout ────────────────────────
bass = score.part("bass_808", synth="sine", envelope="pad", volume=0.3,
                  distortion=0.2, distortion_drive=3.0,
                  lowpass=140, lowpass_q=1.8, sub_osc=0.4,
                  humanize=0.06)

# Bars 1-8: rests
for _ in range(8):
    bass.rest(Duration.WHOLE)

# Bars 9-56: 808 following roots
bass_roots = [D.add(-24), C.add(-24), Bb.add(-24), G.add(-24)]
for _ in range(12):
    for root in bass_roots:
        bass.add(root, Duration.HALF, velocity=100)
        bass.rest(Duration.QUARTER)
        bass.add(root, Duration.QUARTER, velocity=85)

# Bars 57-64: fading via velocity
for vel in [70, 60, 50, 40, 30, 20, 10, 5]:
    bass.add(D.add(-24), Duration.WHOLE, velocity=vel)

# ── MARCHING SNARE — military finale (bars 49-64) ──────────────
march = score.part("march", volume=1.0,
                   reverb=0.2, reverb_decay=0.8, humanize=0.03,
                   ensemble=16)

# Bars 1-48: rests
for _ in range(48):
    march.rest(Duration.WHOLE)

# ── LEVEL 1 — Bars 49-50: single hits, lots of space. A warning. ──
march.hit(MR, Duration.HALF, velocity=115, articulation="marcato")
march.rest(Duration.HALF)
march.rest(Duration.HALF)
march.hit(MR, Duration.HALF, velocity=118, articulation="marcato")

# ── LEVEL 2 — Bars 51-52: quarter notes. Marching begins. ────────
for _ in range(2):
    march.hit(MR, Duration.QUARTER, velocity=110, articulation="accent")
    march.hit(MR, Duration.QUARTER, velocity=55)
    march.hit(MR, Duration.QUARTER, velocity=112, articulation="accent")
    march.hit(MR, Duration.QUARTER, velocity=55)

# ── LEVEL 3 — Bars 53-54: 8ths with ghost notes. Getting serious. ─
for _ in range(2):
    march.hit(MR, Duration.EIGHTH, velocity=115, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=48)
    march.hit(MR, Duration.EIGHTH, velocity=55)
    march.hit(MR, Duration.EIGHTH, velocity=112, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=50)
    march.hit(MR, Duration.EIGHTH, velocity=48)
    march.hit(MR, Duration.EIGHTH, velocity=118, articulation="marcato")
    march.hit(MR, Duration.EIGHTH, velocity=50)

# ── LEVEL 4 — Bars 55-56: 16ths. Full paradiddle. ────────────────
for _ in range(2):
    # RLRR LRLL RLRR LRLL
    march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="marcato")
    march.hit(MR, Duration.SIXTEENTH, velocity=50)
    march.hit(MR, Duration.SIXTEENTH, velocity=55)
    march.hit(MR, Duration.SIXTEENTH, velocity=52)
    march.hit(MR, Duration.SIXTEENTH, velocity=122, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=50)
    march.hit(MR, Duration.SIXTEENTH, velocity=52)
    march.hit(MR, Duration.SIXTEENTH, velocity=48)
    march.hit(MR, Duration.SIXTEENTH, velocity=127, articulation="marcato")
    march.hit(MR, Duration.SIXTEENTH, velocity=52)
    march.hit(MR, Duration.SIXTEENTH, velocity=55)
    march.hit(MR, Duration.SIXTEENTH, velocity=50)
    march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=50)
    march.hit(MR, Duration.SIXTEENTH, velocity=52)
    march.hit(MR, Duration.SIXTEENTH, velocity=48)

# ── LEVEL 5 — Bars 57-58: 16ths, louder, accents on every beat ───
for _ in range(2):
    for beat in range(4):
        march.hit(MR, Duration.SIXTEENTH, velocity=127, articulation="marcato")
        march.hit(MR, Duration.SIXTEENTH, velocity=58)
        march.hit(MR, Duration.SIXTEENTH, velocity=62)
        march.hit(MR, Duration.SIXTEENTH, velocity=55)

# ── LEVEL 6 — Bars 59-60: 32nds creep in. Here it comes. ─────────
for _ in range(2):
    # Half bar 16ths, half bar 32nds
    for beat in range(2):
        march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="accent")
        march.hit(MR, Duration.SIXTEENTH, velocity=55)
        march.hit(MR, Duration.SIXTEENTH, velocity=58)
        march.hit(MR, Duration.SIXTEENTH, velocity=52)
    for beat in range(2):
        march.hit(MR, 0.125, velocity=125, articulation="accent")
        march.hit(MR, 0.125, velocity=52)
        march.hit(MR, 0.125, velocity=55)
        march.hit(MR, 0.125, velocity=48)
        march.hit(MR, 0.125, velocity=122, articulation="accent")
        march.hit(MR, 0.125, velocity=50)
        march.hit(MR, 0.125, velocity=55)
        march.hit(MR, 0.125, velocity=48)

# ── LEVEL 7 — Bars 61-62: full 32nd note rolls ───────────────────
for bar in range(2):
    for beat in range(4):
        base = 80 + bar * 15 + beat * 3
        march.hit(MR, 0.125, velocity=min(127, base + 30), articulation="accent")
        march.hit(MR, 0.125, velocity=min(127, base))
        march.hit(MR, 0.125, velocity=min(127, base + 10))
        march.hit(MR, 0.125, velocity=min(127, base))
        march.hit(MR, 0.125, velocity=min(127, base + 25), articulation="accent")
        march.hit(MR, 0.125, velocity=min(127, base + 5))
        march.hit(MR, 0.125, velocity=min(127, base + 15))
        march.hit(MR, 0.125, velocity=min(127, base))

# Bar 63: 32nd note crescendo — wall of snare
for i in range(32):
    vel = min(127, 70 + i * 2)
    art = "accent" if i % 4 == 0 else "marcato" if i % 8 == 0 else ""
    march.hit(MR, 0.125, velocity=vel, articulation=art)

# Bar 64: CADENCE — DCI-style ending
# Flam drags into triplets into unison hits
# Flam drag: grace-MAIN grace-MAIN (tight doubles)
march.hit(MR, 0.125, velocity=55)   # grace
march.hit(MR, Duration.SIXTEENTH, velocity=127, articulation="marcato")  # MAIN
march.hit(MR, 0.125, velocity=55)   # grace
march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="marcato")  # MAIN
# 16th note triplets — six per beat, blazing
for _ in range(4):
    march.hit(MR, 1/6, velocity=127, articulation="marcato")
    march.hit(MR, 1/6, velocity=52)
    march.hit(MR, 1/6, velocity=55)
    march.hit(MR, 1/6, velocity=125, articulation="accent")
    march.hit(MR, 1/6, velocity=50)
    march.hit(MR, 1/6, velocity=55)
# Rimshot quarter notes — CRACK . CRACK . CRACK . CRACK
march.hit(MR, Duration.QUARTER, velocity=127, articulation="marcato")
march.hit(MR, Duration.QUARTER, velocity=127, articulation="marcato")
march.hit(MR, Duration.QUARTER, velocity=127, articulation="marcato")
# THE FINAL RIMSHOT — everything stops
march.hit(MR, Duration.QUARTER, velocity=127, articulation="fermata")

# ── PAD — atmospheric glue throughout ───────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.12,
                 reverb=0.6, reverb_type="taj_mahal",
                 chorus=0.3, chorus_rate=0.2, chorus_depth=0.008,
                 lowpass=1400)
pad.lfo("lowpass", rate=0.03, min=600, max=2000, bars=64, shape="triangle")

for _ in range(16):
    for chord in prog:
        pad.add(chord, Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing CULTURE CLASH (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing CULTURE CLASH...")
    play_score(score)
