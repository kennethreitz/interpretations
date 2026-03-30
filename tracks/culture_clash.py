"""
CULTURE CLASH — didgeridoo drone → rhodes → tabla/sitar pop progression →
NES Mario meets Drake → marching snare military finale over 808 fadeout.
A fever dream of musical tourism. ~4 minutes.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

# ── Key: C major ────────────────────────────────────────────────
key = Key("C", "major")
s = key.scale
prog = key.progression("I", "V", "vi", "IV")

C  = s[0]; D  = s[1]; E  = s[2]; F  = s[3]
G  = s[4]; A  = s[5]; B  = s[6]

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
#   Bars  1-8:   Didgeridoo drone, Rhodes fades in
#   Bars  9-24:  Tabla + sitar arp (I-V-vi-IV), 808 enters
#   Bars 25-40:  NES Mario × Drake mashup, tabla continues
#   Bars 41-56:  Marching snare builds, 808 drives
#   Bars 57-64:  Military snare crescendo, everything fades, final hit
# ═══════════════════════════════════════════════════════════════════

# ── DIDGERIDOO — ancient drone opening ──────────────────────────
didge = score.part("didgeridoo", instrument="didgeridoo", volume=0.45,
                   reverb=0.6, reverb_type="taj_mahal",
                   chorus=0.2, chorus_rate=0.1, chorus_depth=0.008)

# Bars 1-8: full drone
for _ in range(8):
    didge.add(C.add(-24), Duration.WHOLE, velocity=95)
# Bars 9-16: fading under tabla/sitar
for vol in [0.35, 0.35, 0.25, 0.25, 0.15, 0.15, 0.08, 0.08]:
    didge.set(volume=vol)
    didge.add(C.add(-24), Duration.WHOLE, velocity=80)
# Silent rest of track
for _ in range(48):
    didge.rest(Duration.WHOLE)

# ── RHODES — enters bar 3, ethereal ────────────────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.0,
                    reverb=0.6, reverb_type="taj_mahal",
                    chorus=0.3, chorus_rate=0.4, chorus_depth=0.005,
                    tremolo_depth=0.12, tremolo_rate=3.5)

rhodes.rest(Duration.WHOLE)
rhodes.rest(Duration.WHOLE)

# Bars 3-8: gentle chords, fading in
rhodes.set(volume=0.2)
for chord in prog:
    rhodes.add(chord, Duration.WHOLE)
rhodes.set(volume=0.3)
for chord in prog[:2]:
    rhodes.add(chord, Duration.WHOLE)

# Bars 9-24: full chords under tabla/sitar
rhodes.set(volume=0.3)
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.WHOLE)

# Bars 25-40: choppy stabs under Mario/Drake
rhodes.set(volume=0.2)
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.QUARTER)
        rhodes.rest(Duration.QUARTER)
        rhodes.add(chord, Duration.QUARTER)
        rhodes.rest(Duration.QUARTER)

# Bars 41-56: fading out
rhodes.set(volume=0.12)
for _ in range(2):
    for chord in prog:
        rhodes.add(chord, Duration.HALF)
        rhodes.rest(Duration.HALF)
rhodes.set(volume=0.0)
for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# Bars 57-64: silent
for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# ── TABLA — enters bar 9 ───────────────────────────────────────
tabla = score.part("tabla", volume=0.0,
                   reverb=0.3, reverb_decay=1.2, humanize=0.08)

for _ in range(8):
    tabla.rest(Duration.WHOLE)

# Bars 9-40: keherwa groove with fills every 4 bars
tabla.set(volume=0.35)
for bar in range(32):
    if bar % 4 == 3:
        # Fill bar
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

# Bars 41-56: tabla fading
tabla.set(volume=0.25)
for bar in range(8):
    tabla.hit(tDHA, Duration.EIGHTH, velocity=80)
    tabla.hit(GE, Duration.EIGHTH, velocity=55)
    tabla.hit(NA, Duration.EIGHTH, velocity=65)
    tabla.hit(TIT, Duration.EIGHTH, velocity=42)
    tabla.hit(NA, Duration.EIGHTH, velocity=60)
    tabla.hit(TIT, Duration.EIGHTH, velocity=40)
    tabla.hit(tDHA, Duration.EIGHTH, velocity=75)
    tabla.hit(NA, Duration.EIGHTH, velocity=58)
tabla.set(volume=0.0)
for _ in range(8):
    tabla.rest(Duration.WHOLE)

# Bars 57-64: silent
for _ in range(8):
    tabla.rest(Duration.WHOLE)

# ── SITAR — I V vi IV arpeggiated (bars 9-24) ──────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.0,
                   reverb=0.45, reverb_type="taj_mahal",
                   delay=0.35, delay_time=0.316, delay_feedback=0.4,
                   pan=-0.2, humanize=0.08)

for _ in range(8):
    sitar.rest(Duration.WHOLE)

# Bars 9-24: arpeggiated pop progression
sitar.set(volume=0.45)
arp_chords = [
    [C, E, G, C.add(12), G, E, C, G.add(-12)],
    [G.add(-12), B.add(-12), D, G, D, B.add(-12), G.add(-12), D.add(-12)],
    [A.add(-12), C, E, A, E, C, A.add(-12), E.add(-12)],
    [F.add(-12), A.add(-12), C, F, C, A.add(-12), F.add(-12), C.add(-12)],
]
for _ in range(4):
    for arp in arp_chords:
        for note in arp:
            sitar.add(note, Duration.EIGHTH, velocity=85)

# Bars 25-32: sitar fading out
sitar.set(volume=0.3)
for _ in range(2):
    for arp in arp_chords:
        for note in arp:
            sitar.add(note, Duration.EIGHTH, velocity=70)

# Silent rest
sitar.set(volume=0.0)
for _ in range(32):
    sitar.rest(Duration.WHOLE)

# ── NES MARIO — pulse wave (bars 25-40) ────────────────────────
mario = score.part("mario", synth="square", envelope="staccato", volume=0.0,
                   reverb=0.15, lowpass=6000)

for _ in range(24):
    mario.rest(Duration.WHOLE)

# Bars 25-28: World 1-1 theme
mario.set(volume=0.3)
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
    (B, Duration.QUARTER), (Tone.from_string("Bb4"), Duration.EIGHTH),
    (A, Duration.QUARTER),
]
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=100)

# Bars 29-32: repeat with variation
mario.set(volume=0.32)
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=105)

# Bars 33-36: Drake-style melody on pulse wave
# Hotline Bling inspired descending pattern
mario.set(volume=0.32)
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
mario.set(volume=0.28)
for _ in range(2):
    # Mario lick
    mario.add(E.add(12), Duration.EIGHTH, velocity=100)
    mario.add(E.add(12), Duration.EIGHTH, velocity=95)
    mario.rest(Duration.EIGHTH)
    mario.add(E.add(12), Duration.EIGHTH, velocity=100)
    mario.add(C.add(12), Duration.EIGHTH, velocity=90)
    mario.add(E.add(12), Duration.QUARTER, velocity=95)
    mario.rest(Duration.EIGHTH)
    # Drake answer
    mario.add(D.add(12), Duration.QUARTER, velocity=90)
    mario.add(C.add(12), Duration.QUARTER, velocity=85)
    mario.add(A, Duration.QUARTER, velocity=80)
    mario.add(G, Duration.QUARTER, velocity=85)
    mario.add(E, Duration.HALF, velocity=80)
    mario.rest(Duration.HALF)

# Bars 49-56: fading out
mario.set(volume=0.18)
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=80)
mario.set(volume=0.0)
for _ in range(4):
    mario.rest(Duration.WHOLE)

# Bars 57-64: silent
for _ in range(8):
    mario.rest(Duration.WHOLE)

# ── 808 BASS — enters bar 9, throughout ────────────────────────
bass = score.part("bass_808", synth="sine", envelope="pad", volume=0.0,
                  distortion=0.2, distortion_drive=3.0,
                  lowpass=140, lowpass_q=1.8)

for _ in range(8):
    bass.rest(Duration.WHOLE)

# Bars 9-56: 808 following roots
bass.set(volume=0.3)
bass_roots = [C.add(-24), G.add(-24), A.add(-24), F.add(-24)]
for _ in range(12):
    for root in bass_roots:
        bass.add(root, Duration.HALF, velocity=100)
        bass.rest(Duration.QUARTER)
        bass.add(root, Duration.QUARTER, velocity=85)

# Bars 57-64: fadeout
for vol in [0.25, 0.2, 0.15, 0.1, 0.06, 0.03, 0.01, 0.0]:
    bass.set(volume=vol)
    bass.add(C.add(-24), Duration.WHOLE, velocity=80)

# ── MARCHING SNARE — military finale (bars 49-64) ──────────────
march = score.part("march", volume=0.0,
                   reverb=0.2, reverb_decay=0.8, humanize=0.03)

for _ in range(48):
    march.rest(Duration.WHOLE)

# Bars 49-52: entrance — spare, ominous
march.set(volume=0.35)
for _ in range(4):
    march.hit(MR, Duration.QUARTER, velocity=110, articulation="accent")
    march.rest(Duration.QUARTER)
    march.hit(MR, Duration.QUARTER, velocity=105, articulation="accent")
    march.rest(Duration.QUARTER)

# Bars 53-56: double time
march.set(volume=0.45)
for _ in range(4):
    march.hit(MR, Duration.EIGHTH, velocity=112, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=65)
    march.hit(MR, Duration.EIGHTH, velocity=112, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=65)
    march.hit(MR, Duration.EIGHTH, velocity=115, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=68)
    march.hit(MR, Duration.EIGHTH, velocity=115, articulation="accent")
    march.hit(MR, Duration.EIGHTH, velocity=68)

# Bars 57-60: 16th note rolls
march.set(volume=0.55)
for _ in range(4):
    for i in range(16):
        vel = 118 if i % 4 == 0 else 62 + (i % 3) * 8
        march.hit(MR, Duration.SIXTEENTH, velocity=vel)

# Bars 61-63: blazing crescendo
march.set(volume=0.65)
for bar in range(3):
    for i in range(16):
        vel = min(127, 75 + bar * 10 + i * 2)
        march.hit(MR, Duration.SIXTEENTH, velocity=vel)

# Bar 64: final roll into massive hit
march.set(volume=0.8)
for i in range(12):
    march.hit(MR, Duration.SIXTEENTH, velocity=min(127, 90 + i * 3))
march.hit(MR, Duration.QUARTER, velocity=127, articulation="fermata")

# ── PAD — atmospheric glue ──────────────────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.0,
                 reverb=0.6, reverb_type="taj_mahal",
                 chorus=0.3, chorus_rate=0.2, chorus_depth=0.008,
                 lowpass=1400)
pad.lfo("lowpass", rate=0.03, min=600, max=2000, bars=64, shape="triangle")

for _ in range(8):
    pad.rest(Duration.WHOLE)

pad.set(volume=0.12)
for _ in range(14):
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
