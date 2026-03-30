"""
CULTURE CLASH — didgeridoo drone → rhodes → tabla/sitar pop progression →
NES Mario meets Drake → marching snare military finale over 808 fadeout.
A fever dream of musical tourism.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

# ── Key: C major for the pop progression, works for Mario too ───
key = Key("C", "major")
s = key.scale

# Scale degrees
C  = s[0]   # I
D  = s[1]
E  = s[2]
F  = s[3]   # IV
G  = s[4]   # V
A  = s[5]   # vi
B  = s[6]

score = Score("4/4", bpm=95)

# Tabla bols
NA  = DrumSound.TABLA_NA
TIT = DrumSound.TABLA_TIT
GE  = DrumSound.TABLA_GE
tDHA = DrumSound.TABLA_DHA
KE  = DrumSound.TABLA_KE
GEB = DrumSound.TABLA_GE_BEND

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE:
#   Bars  1-4:  Didgeridoo drone + Rhodes enters
#   Bars  5-12: Tabla/sitar — I-V-vi-IV arpeggiated
#   Bars 13-20: NES Mario × Drake mashup
#   Bars 21-24: Marching snare military over 808 fadeout
# ═══════════════════════════════════════════════════════════════════

# ── DIDGERIDOO — opens the whole thing ──────────────────────────
didge = score.part("didgeridoo", instrument="didgeridoo", volume=0.5,
                   reverb=0.7, reverb_type="taj_mahal",
                   chorus=0.2, chorus_rate=0.1, chorus_depth=0.008)

# 4 bars of drone — deep, ancient, primordial
for _ in range(4):
    didge.add(C.add(-24), Duration.WHOLE, velocity=100)

# Continue under rhodes, quieter
didge.set(volume=0.3)
for _ in range(4):
    didge.add(C.add(-24), Duration.WHOLE, velocity=85)

# Fade out as tabla enters
didge.set(volume=0.2)
for _ in range(2):
    didge.add(C.add(-24), Duration.WHOLE, velocity=75)
didge.set(volume=0.1)
for _ in range(2):
    didge.add(C.add(-24), Duration.WHOLE, velocity=65)

# Silent for rest
for _ in range(12):
    didge.rest(Duration.WHOLE)

# ── RHODES — enters bar 3, ethereal chords ──────────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.0,
                    reverb=0.65, reverb_type="taj_mahal",
                    chorus=0.3, chorus_rate=0.4, chorus_depth=0.005,
                    tremolo_depth=0.15, tremolo_rate=3.5)

# Silent bars 1-2
rhodes.rest(Duration.WHOLE)
rhodes.rest(Duration.WHOLE)

# Bars 3-4: fade in with simple chords
rhodes.set(volume=0.25)
prog = key.progression("I", "V", "vi", "IV")
for chord in prog:
    rhodes.add(chord, Duration.WHOLE)

# Bars 5-8: fuller, the progression sings
rhodes.set(volume=0.3)
for chord in prog:
    rhodes.add(chord, Duration.WHOLE)

# Bars 9-12: start breaking up, making room for sitar
rhodes.set(volume=0.25)
for chord in prog:
    rhodes.add(chord, Duration.HALF)
    rhodes.rest(Duration.HALF)

# Bars 13-16: minimal stabs under Mario
rhodes.set(volume=0.15)
for chord in prog:
    rhodes.add(chord, Duration.QUARTER)
    rhodes.rest(Duration.DOTTED_HALF)

# Bars 17-24: silent — hand off to the madness
for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# ── TABLA — enters bar 5 with fills ────────────────────────────
tabla = score.part("tabla", volume=0.0,
                   reverb=0.3, reverb_decay=1.2, humanize=0.08)

# Silent bars 1-4
for _ in range(4):
    tabla.rest(Duration.WHOLE)

# Bars 5-12: keherwa groove
tabla.set(volume=0.35)
for bar in range(8):
    if bar == 3 or bar == 7:
        # Fill bars — bayan showcase
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

# Bars 13-20: tabla continues, slightly quieter under Mario/Drake
tabla.set(volume=0.25)
for bar in range(8):
    if bar == 3 or bar == 7:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=95, articulation="accent")
        tabla.hit(GEB, Duration.QUARTER, velocity=110)
        tabla.hit(NA, Duration.EIGHTH, velocity=75)
        tabla.hit(tDHA, Duration.QUARTER, velocity=90)
        tabla.hit(GEB, Duration.QUARTER, velocity=105)
    else:
        tabla.hit(tDHA, Duration.EIGHTH, velocity=85)
        tabla.hit(GE, Duration.EIGHTH, velocity=60)
        tabla.hit(NA, Duration.EIGHTH, velocity=70)
        tabla.hit(TIT, Duration.EIGHTH, velocity=45)
        tabla.hit(NA, Duration.EIGHTH, velocity=65)
        tabla.hit(TIT, Duration.EIGHTH, velocity=42)
        tabla.hit(tDHA, Duration.EIGHTH, velocity=80)
        tabla.hit(NA, Duration.EIGHTH, velocity=62)

# Bars 21-24: tabla fades
tabla.set(volume=0.15)
for _ in range(2):
    tabla.hit(tDHA, Duration.EIGHTH, velocity=75)
    tabla.hit(GE, Duration.EIGHTH, velocity=55)
    tabla.hit(NA, Duration.EIGHTH, velocity=60)
    tabla.hit(TIT, Duration.EIGHTH, velocity=40)
    tabla.hit(NA, Duration.EIGHTH, velocity=55)
    tabla.hit(TIT, Duration.EIGHTH, velocity=38)
    tabla.hit(tDHA, Duration.EIGHTH, velocity=70)
    tabla.hit(NA, Duration.EIGHTH, velocity=55)
tabla.set(volume=0.0)
for _ in range(2):
    tabla.rest(Duration.WHOLE)

# ── SITAR — I V vi IV arpeggiated (bars 5-12) ──────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.0,
                   reverb=0.45, reverb_type="taj_mahal",
                   delay=0.35, delay_time=0.316, delay_feedback=0.4,
                   pan=-0.2, humanize=0.08)

# Silent bars 1-4
for _ in range(4):
    sitar.rest(Duration.WHOLE)

# Bars 5-12: the eerily familiar I-V-vi-IV arped out
sitar.set(volume=0.45)
arp_chords = [
    # I — C: C E G
    [C, E, G, C.add(12), G, E, C, G.add(-12)],
    # V — G: G B D
    [G.add(-12), B.add(-12), D, G, D, B.add(-12), G.add(-12), D.add(-12)],
    # vi — Am: A C E
    [A.add(-12), C, E, A, E, C, A.add(-12), E.add(-12)],
    # IV — F: F A C
    [F.add(-12), A.add(-12), C, F, C, A.add(-12), F.add(-12), C.add(-12)],
]
for _ in range(2):
    for arp in arp_chords:
        for note in arp:
            sitar.add(note, Duration.EIGHTH, velocity=85)

# Bars 13-20: sitar fades, hands off to NES
sitar.set(volume=0.3)
for arp in arp_chords:
    for note in arp:
        sitar.add(note, Duration.EIGHTH, velocity=70)
sitar.set(volume=0.15)
for arp in arp_chords:
    for note in arp:
        sitar.add(note, Duration.EIGHTH, velocity=55)

# Bars 21-24: silent
for _ in range(4):
    sitar.rest(Duration.WHOLE)

# ── NES MARIO — pulse wave, enters bar 13 ──────────────────────
mario = score.part("mario", synth="square", envelope="staccato", volume=0.0,
                   reverb=0.15, lowpass=6000)

# Silent bars 1-12
for _ in range(12):
    mario.rest(Duration.WHOLE)

# Bars 13-16: World 1-1 theme
mario.set(volume=0.3)
mario_melody = [
    # Bar 1
    (E.add(12), Duration.EIGHTH), (E.add(12), Duration.EIGHTH),
    (None, Duration.EIGHTH), (E.add(12), Duration.EIGHTH),
    (None, Duration.EIGHTH), (C.add(12), Duration.EIGHTH),
    (E.add(12), Duration.QUARTER),
    # Bar 2
    (G.add(12), Duration.QUARTER), (None, Duration.QUARTER),
    (G, Duration.QUARTER), (None, Duration.QUARTER),
    # Bar 3
    (C.add(12), Duration.QUARTER), (None, Duration.EIGHTH),
    (G, Duration.EIGHTH), (None, Duration.QUARTER),
    (E, Duration.QUARTER),
    # Bar 4
    (None, Duration.EIGHTH), (A, Duration.QUARTER),
    (B, Duration.QUARTER), (A.add(12), Duration.EIGHTH),  # Bb
    (A, Duration.QUARTER),
]
for note, dur in mario_melody:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=100)

# Bars 17-20: Hotline Bling melody on pulse wave
# That iconic descending pattern: D C A G... simple, hypnotic
mario.set(volume=0.32)
bling = [
    # Bar 1 — the hook
    (D.add(12), Duration.QUARTER), (C.add(12), Duration.QUARTER),
    (A, Duration.QUARTER), (G, Duration.QUARTER),
    # Bar 2
    (A, Duration.QUARTER), (None, Duration.QUARTER),
    (G, Duration.QUARTER), (E, Duration.QUARTER),
    # Bar 3 — repeat with variation
    (D.add(12), Duration.QUARTER), (C.add(12), Duration.EIGHTH),
    (A, Duration.EIGHTH), (G, Duration.HALF),
    # Bar 4 — resolve
    (A, Duration.HALF), (G, Duration.QUARTER),
    (E, Duration.QUARTER),
]
for note, dur in bling:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=95)

# Bars 21-24: Mario and Drake merge — fast alternating phrases
mario.set(volume=0.28)
mashup = [
    # Mario lick
    (E.add(12), Duration.EIGHTH), (E.add(12), Duration.EIGHTH),
    (None, Duration.EIGHTH), (E.add(12), Duration.EIGHTH),
    # Drake answer
    (D.add(12), Duration.EIGHTH), (C.add(12), Duration.EIGHTH),
    (A, Duration.EIGHTH), (G, Duration.EIGHTH),
    # Mario
    (G.add(12), Duration.QUARTER), (E.add(12), Duration.QUARTER),
    # Drake
    (D.add(12), Duration.QUARTER), (A, Duration.QUARTER),
    # Final — both melodies collide
    (E.add(12), Duration.EIGHTH), (D.add(12), Duration.EIGHTH),
    (C.add(12), Duration.EIGHTH), (G, Duration.EIGHTH),
    (E, Duration.HALF),
    (C.add(12), Duration.WHOLE),
]
for note, dur in mashup:
    if note is None:
        mario.rest(dur)
    else:
        mario.add(note, dur, velocity=90)

# ── 808 BASS — enters bar 5, drives through, fades at end ──────
bass = score.part("bass_808", synth="sine", envelope="pad", volume=0.0,
                  distortion=0.2, distortion_drive=3.0,
                  lowpass=140, lowpass_q=1.8)

# Silent bars 1-4
for _ in range(4):
    bass.rest(Duration.WHOLE)

# Bars 5-12: following the progression roots
bass.set(volume=0.3)
bass_roots = [
    C.add(-24), G.add(-24), A.add(-24), F.add(-24),
]
for _ in range(2):
    for root in bass_roots:
        bass.add(root, Duration.HALF, velocity=100)
        bass.rest(Duration.QUARTER)
        bass.add(root, Duration.QUARTER, velocity=85)

# Bars 13-20: 808 gets harder under Mario/Drake
bass.set(volume=0.35)
for _ in range(2):
    for root in bass_roots:
        bass.add(root, Duration.HALF, velocity=110)
        bass.add(root, Duration.EIGHTH, velocity=90)
        bass.rest(Duration.EIGHTH)
        bass.add(root, Duration.QUARTER, velocity=100)

# Bars 21-24: 808 fades out under marching snare
for vol, vel in [(0.28, 95), (0.2, 85), (0.12, 75), (0.05, 60)]:
    bass.set(volume=vol)
    bass.add(C.add(-24), Duration.WHOLE, velocity=vel)

# ── MARCHING SNARE — military ensemble, bars 21-24 ─────────────
march = score.part("march", volume=0.0,
                   reverb=0.25, reverb_decay=1.0, humanize=0.03)

MR = DrumSound.MARCH_SNARE
MS = DrumSound.MARCH_SNARE  # ghost notes at low velocity

# Silent bars 1-20
for _ in range(20):
    march.rest(Duration.WHOLE)

# Bar 21: entrance — single hits, announcing
march.set(volume=0.5)
march.hit(MR, Duration.QUARTER, velocity=120, articulation="accent")
march.rest(Duration.QUARTER)
march.hit(MR, Duration.QUARTER, velocity=120, articulation="accent")
march.rest(Duration.QUARTER)

# Bar 22: double time — getting serious
march.set(volume=0.6)
march.hit(MR, Duration.EIGHTH, velocity=115, articulation="accent")
march.hit(MR, Duration.EIGHTH, velocity=70)
march.hit(MR, Duration.EIGHTH, velocity=115, articulation="accent")
march.hit(MR, Duration.EIGHTH, velocity=70)
march.hit(MR, Duration.EIGHTH, velocity=118, articulation="accent")
march.hit(MR, Duration.EIGHTH, velocity=72)
march.hit(MR, Duration.EIGHTH, velocity=118, articulation="accent")
march.hit(MR, Duration.EIGHTH, velocity=72)

# Bar 23: full rolls — blazing
march.set(volume=0.7)
for i in range(16):
    vel = 120 if i % 4 == 0 else 65 + (i % 3) * 8
    march.hit(MR, Duration.SIXTEENTH, velocity=vel)

# Bar 24: crescendo roll into final hit
march.set(volume=0.8)
for i in range(14):
    vel = 80 + i * 3
    march.hit(MR, Duration.SIXTEENTH, velocity=min(127, vel))
# FINAL HIT
march.hit(MR, Duration.QUARTER, velocity=127, articulation="fermata")
march.rest(Duration.QUARTER)

# ── PAD — glue, subtle throughout ───────────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.0,
                 reverb=0.6, reverb_type="taj_mahal",
                 chorus=0.3, chorus_rate=0.2, chorus_depth=0.008,
                 lowpass=1400)
pad.lfo("lowpass", rate=0.0625, min=600, max=2000, bars=24, shape="triangle")

# Silent bars 1-4
for _ in range(4):
    pad.rest(Duration.WHOLE)

# Bars 5-24: slowly evolving pad following progression
pad.set(volume=0.12)
for _ in range(5):
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
