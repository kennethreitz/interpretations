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

# ── DIDGERIDOO CHORD — two drones a fifth apart ────────────────
didge_lo = score.part("didge_lo", instrument="didgeridoo", volume=0.25,
                      lowpass=300)
didge_hi = score.part("didge_hi", instrument="didgeridoo", volume=0.18,
                      lowpass=400, pan=0.2)

# Bars 1-8: drone chord (D2 + A2)
for _ in range(8):
    didge_lo.add(D.add(-24), Duration.WHOLE, velocity=75)
    didge_hi.add(A.add(-24), Duration.WHOLE, velocity=65)
# Bars 9-12: fading
for vel in [60, 50, 35, 20]:
    didge_lo.add(D.add(-24), Duration.WHOLE, velocity=vel)
    didge_hi.add(A.add(-24), Duration.WHOLE, velocity=vel)
# Rest of track: silent via rests
for _ in range(52):
    didge_lo.rest(Duration.WHOLE)
    didge_hi.rest(Duration.WHOLE)

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

# Bars 41-56: half notes, thinning
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.HALF)
        rhodes.rest(Duration.HALF)

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
                   reverb=0.45, reverb_type="taj_mahal",
                   delay=0.35, delay_time=0.316, delay_feedback=0.4,
                   pan=-0.2, humanize=0.1)

# Bars 1-8: rests
for _ in range(8):
    sitar.rest(Duration.WHOLE)

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

# Bars 25-32: fading via velocity
for _ in range(2):
    for arp in arp_chords:
        for note in arp:
            sitar.add(note, Duration.EIGHTH, velocity=55)

# Bars 33-64: silent
for _ in range(32):
    sitar.rest(Duration.WHOLE)

# ── NES MARIO — pulse wave (bars 25-56) ────────────────────────
mario = score.part("mario", synth="square", envelope="staccato", volume=0.4,
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

# Bars 33-40: Drake Hotline Bling melody
drake = [
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
    for note, dur in drake:
        if note is None:
            mario.rest(dur)
        else:
            mario.add(note, dur, velocity=95)

# Bars 41-48: Mario × Drake alternating
for _ in range(2):
    mario.add(E.add(12), Duration.EIGHTH, velocity=100)
    mario.add(E.add(12), Duration.EIGHTH, velocity=95)
    mario.rest(Duration.EIGHTH)
    mario.add(E.add(12), Duration.EIGHTH, velocity=100)
    mario.add(C.add(12), Duration.EIGHTH, velocity=90)
    mario.add(E.add(12), Duration.QUARTER, velocity=95)
    mario.rest(Duration.EIGHTH)
    mario.add(D.add(12), Duration.QUARTER, velocity=90)
    mario.add(C.add(12), Duration.QUARTER, velocity=85)
    mario.add(A, Duration.QUARTER, velocity=80)
    mario.add(G, Duration.QUARTER, velocity=85)
    mario.add(E, Duration.HALF, velocity=80)
    mario.rest(Duration.HALF)

# Bars 49-52: one last Mario statement fading
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=70)

# Bars 53-64: silent
for _ in range(12):
    mario.rest(Duration.WHOLE)

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
march = score.part("march", volume=0.5,
                   reverb=0.2, reverb_decay=0.8, humanize=0.03)

# Bars 1-48: rests
for _ in range(48):
    march.rest(Duration.WHOLE)

# Bars 49-50: entrance — two big accents per bar, military call
for _ in range(2):
    march.hit(MR, Duration.QUARTER, velocity=120, articulation="marcato")
    march.rest(Duration.QUARTER)
    march.hit(MR, Duration.EIGHTH, velocity=115, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=60)
    march.rest(Duration.QUARTER)

# Bars 51-52: doubled — answer with authority
for _ in range(2):
    march.hit(MR, Duration.EIGHTH, velocity=120, articulation="marcato")
    march.hit(MR, Duration.EIGHTH, velocity=55)
    march.hit(MR, Duration.EIGHTH, velocity=118, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=55)
    march.hit(MR, Duration.QUARTER, velocity=125, articulation="marcato")
    march.hit(MR, Duration.EIGHTH, velocity=60)
    march.hit(MR, Duration.EIGHTH, velocity=55)

# Bars 53-54: double time with ghost notes
for _ in range(2):
    march.hit(MR, Duration.SIXTEENTH, velocity=120, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=40)
    march.hit(MR, Duration.SIXTEENTH, velocity=45)
    march.hit(MR, Duration.SIXTEENTH, velocity=118, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=42)
    march.hit(MR, Duration.SIXTEENTH, velocity=120, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=40)
    march.hit(MR, Duration.SIXTEENTH, velocity=45)
    march.hit(MR, Duration.SIXTEENTH, velocity=122, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=42)
    march.hit(MR, Duration.SIXTEENTH, velocity=40)
    march.hit(MR, Duration.SIXTEENTH, velocity=118, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="marcato")
    march.hit(MR, Duration.SIXTEENTH, velocity=45)
    march.hit(MR, Duration.SIXTEENTH, velocity=42)
    march.hit(MR, Duration.SIXTEENTH, velocity=40)

# Bars 55-56: paradiddle pattern — RLRR LRLL with accents
for _ in range(2):
    march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="marcato")  # R
    march.hit(MR, Duration.SIXTEENTH, velocity=55)   # l
    march.hit(MR, Duration.SIXTEENTH, velocity=60)   # r
    march.hit(MR, Duration.SIXTEENTH, velocity=58)   # r
    march.hit(MR, Duration.SIXTEENTH, velocity=122, articulation="accent")   # L
    march.hit(MR, Duration.SIXTEENTH, velocity=55)   # r
    march.hit(MR, Duration.SIXTEENTH, velocity=58)   # l
    march.hit(MR, Duration.SIXTEENTH, velocity=55)   # l
    march.hit(MR, Duration.SIXTEENTH, velocity=127, articulation="marcato")  # R
    march.hit(MR, Duration.SIXTEENTH, velocity=55)
    march.hit(MR, Duration.SIXTEENTH, velocity=60)
    march.hit(MR, Duration.SIXTEENTH, velocity=55)
    march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="accent")
    march.hit(MR, Duration.SIXTEENTH, velocity=55)
    march.hit(MR, Duration.SIXTEENTH, velocity=58)
    march.hit(MR, Duration.SIXTEENTH, velocity=55)

# Bars 57-60: full 16th note barrage — accents every beat
for _ in range(4):
    for beat in range(4):
        march.hit(MR, Duration.SIXTEENTH, velocity=125, articulation="marcato")
        march.hit(MR, Duration.SIXTEENTH, velocity=50)
        march.hit(MR, Duration.SIXTEENTH, velocity=55)
        march.hit(MR, Duration.SIXTEENTH, velocity=48)

# Bars 61-63: crescendo — getting louder every beat
for bar in range(3):
    for beat in range(4):
        base = 70 + bar * 15 + beat * 3
        march.hit(MR, Duration.SIXTEENTH, velocity=min(127, base + 25), articulation="accent")
        march.hit(MR, Duration.SIXTEENTH, velocity=min(127, base))
        march.hit(MR, Duration.SIXTEENTH, velocity=min(127, base + 5))
        march.hit(MR, Duration.SIXTEENTH, velocity=min(127, base))

# Bar 64: fastest possible into one massive hit
for i in range(14):
    march.hit(MR, Duration.SIXTEENTH, velocity=min(127, 95 + i * 2))
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
