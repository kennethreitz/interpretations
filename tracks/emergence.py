"""
EMERGENCE — the acoustic world births the electronic one.
Singing bowls, tingsha, didgeridoo, sitar — then the synths arrive.
E minor, 100 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("E", "minor")
s = key.scale  # E F# G A B C D

E  = s[0]; Fs = s[1]; G  = s[2]; A  = s[3]
B  = s[4]; C  = s[5]; D  = s[6]

score = Score("4/4", bpm=100)

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT

prog = key.progression("i", "VII", "VI", "iv")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (88 bars, ~5:17):
#   Bars  1-8:   Bowls + tingsha — a room full of ringing metal
#   Bars  9-16:  Didgeridoo + mellotron flute — the drone bed
#   Bars 17-24:  Sitar enters — 8ths, then 16th arps building
#   Bars 25-32:  Sitar 16th arps full + 32nd fills — the swarm
#   Bars 33-40:  THE SHIFT — synths emerge from the acoustic bed
#   Bars 41-48:  Synths take over — saw, square, FM, the machine
#   Bars 49-56:  Both worlds — sitar + synths together
#   Bars 57-64:  PEAK — everything, 32nd shreds, mellotron chords
#   Bars 65-72:  Mellotron solo — the bridge between worlds
#   Bars 73-80:  Unwinding — synths fade, acoustic returns
#   Bars 81-88:  Bowls alone — where we started, changed
# ═══════════════════════════════════════════════════════════════════

# ── SINGING BOWLS — a chorus, mostly dry ───────────────────────
bowl_1 = score.part("bowl_low", instrument="singing_bowl", volume=0.4,
                    reverb=0.4, reverb_type="taj_mahal",
                    delay=0.1, delay_time=0.6, delay_feedback=0.15,
                    pan=-0.35)

bowl_2 = score.part("bowl_mid", instrument="singing_bowl_ring", volume=0.35,
                    reverb=0.35, reverb_type="taj_mahal",
                    delay=0.08, delay_time=0.45, delay_feedback=0.12,
                    pan=0.25)

bowl_3 = score.part("bowl_hi", instrument="singing_bowl_ring", volume=0.3,
                    reverb=0.3, reverb_type="taj_mahal",
                    delay=0.06, delay_time=0.3, delay_feedback=0.1,
                    pan=-0.15)

# Bars 1-8: the room — bowls at different intervals, cascading
# Low bowl: every 2 bars
for _ in range(4):
    bowl_1.add(E.add(-24), Duration.WHOLE, velocity=68)
    bowl_1.rest(Duration.WHOLE)

# Mid bowl: offset, every 3 bars roughly
bowl_2.rest(Duration.WHOLE)
bowl_2.add(B.add(-12), Duration.WHOLE, velocity=60)
bowl_2.rest(Duration.WHOLE)
bowl_2.rest(Duration.WHOLE)
bowl_2.add(E.add(-12), Duration.WHOLE, velocity=58)
bowl_2.rest(Duration.WHOLE)
bowl_2.add(B.add(-12), Duration.WHOLE, velocity=55)
bowl_2.rest(Duration.WHOLE)

# High bowl: sparse, bright
bowl_3.rest(Duration.WHOLE)
bowl_3.rest(Duration.WHOLE)
bowl_3.add(E, Duration.WHOLE, velocity=52)
bowl_3.rest(Duration.WHOLE)
bowl_3.rest(Duration.WHOLE)
bowl_3.add(B, Duration.WHOLE, velocity=48)
bowl_3.rest(Duration.WHOLE)
bowl_3.rest(Duration.WHOLE)

# Bars 9-72: bowls continue sparser
for bar in range(64):
    if bar % 8 == 0:
        bowl_1.add(E.add(-24), Duration.WHOLE, velocity=max(35, 60 - bar // 4))
    else:
        bowl_1.rest(Duration.WHOLE)
    if bar % 10 == 3:
        bowl_2.add(B.add(-12), Duration.WHOLE, velocity=max(30, 52 - bar // 4))
    else:
        bowl_2.rest(Duration.WHOLE)
    if bar % 12 == 5:
        bowl_3.add(E, Duration.WHOLE, velocity=max(25, 45 - bar // 4))
    else:
        bowl_3.rest(Duration.WHOLE)

# Bars 73-80: bowls come back stronger — returning
for vel in [45, 52, 58, 62, 65, 60, 55, 50]:
    bowl_1.add(E.add(-24), Duration.WHOLE, velocity=vel)
for _ in range(4):
    bowl_2.add(B.add(-12), Duration.WHOLE, velocity=55)
    bowl_2.rest(Duration.WHOLE)
for _ in range(4):
    bowl_3.rest(Duration.WHOLE)
    bowl_3.add(E, Duration.WHOLE, velocity=48)

# Bars 81-88: bowls alone — ending
for vel in [62, 58, 52, 48, 42, 35, 28, 20]:
    bowl_1.add(E.add(-24), Duration.WHOLE, velocity=vel)
for vel in [50, 45, 40, 35, 28, 22, 0, 0]:
    if vel > 0:
        bowl_2.add(B.add(-12), Duration.WHOLE, velocity=vel)
    else:
        bowl_2.rest(Duration.WHOLE)
for vel in [42, 38, 32, 25, 0, 0, 0, 0]:
    if vel > 0:
        bowl_3.add(E, Duration.WHOLE, velocity=vel)
    else:
        bowl_3.rest(Duration.WHOLE)

# ── TINGSHA — crystalline hits, dry and present ────────────────
ting_1 = score.part("tingsha_l", instrument="tingsha", volume=0.22,
                    reverb=0.35, reverb_type="taj_mahal",
                    delay=0.08, delay_time=0.6, delay_feedback=0.1,
                    pan=-0.4)

ting_2 = score.part("tingsha_r", instrument="tingsha", volume=0.2,
                    reverb=0.3, reverb_type="taj_mahal",
                    delay=0.06, delay_time=0.45, delay_feedback=0.08,
                    pan=0.4)

# Bars 1-8: scattered between the bowls — left and right
ting_hits_l = {2: (E, 55), 5: (B, 50), 7: (Fs, 48)}
ting_hits_r = {1: (B, 52), 4: (E, 48), 6: (A, 45), 8: (Fs, 50)}
for bar in range(1, 89):
    if bar in ting_hits_l:
        note, vel = ting_hits_l[bar]
        ting_1.add(note.add(12), Duration.WHOLE, velocity=vel)
    elif bar > 8 and bar % 6 == 2 and bar < 73:
        ting_1.add(E.add(12), Duration.WHOLE, velocity=max(25, 45 - bar // 5))
    elif bar > 72 and bar % 3 == 0:
        ting_1.add(E.add(12), Duration.WHOLE, velocity=max(20, 48 - (bar - 73) * 3))
    else:
        ting_1.rest(Duration.WHOLE)

    if bar in ting_hits_r:
        note, vel = ting_hits_r[bar]
        ting_2.add(note.add(12), Duration.WHOLE, velocity=vel)
    elif bar > 8 and bar % 7 == 4 and bar < 73:
        ting_2.add(B.add(12), Duration.WHOLE, velocity=max(25, 42 - bar // 5))
    elif bar > 72 and bar % 3 == 1:
        ting_2.add(B.add(12), Duration.WHOLE, velocity=max(20, 45 - (bar - 73) * 3))
    else:
        ting_2.rest(Duration.WHOLE)

# ── DIDGERIDOO — primal drone, enters bar 9 ───────────────────
didge = score.part("didge", instrument="didgeridoo", volume=0.1,
                   reverb=0.2, reverb_type="cathedral",
                   chorus=0.15, chorus_rate=0.05, chorus_depth=0.008,
                   lowpass=350, pan=0.05)

for _ in range(8):
    didge.rest(Duration.WHOLE)

for _ in range(24):
    didge.add(E.add(-24), Duration.WHOLE, velocity=60)

# Bars 33-72: fades as synths enter
for vel in [52, 45, 38, 30, 22, 15, 10, 5]:
    didge.add(E.add(-24), Duration.WHOLE, velocity=vel)
for _ in range(32):
    didge.rest(Duration.WHOLE)

# Bars 73-80: returns
for vel in [15, 22, 30, 38, 45, 40, 32, 22]:
    didge.add(E.add(-24), Duration.WHOLE, velocity=vel)

for _ in range(8):
    didge.rest(Duration.WHOLE)

# ── MELLOTRON FLUTE — lively, enters bar 9 ────────────────────
mello = score.part("mellotron", instrument="mellotron_flute", volume=0.3,
                   reverb=0.25, reverb_type="taj_mahal",
                   delay=0.1, delay_time=0.3, delay_feedback=0.15,
                   pan=-0.2, humanize=0.1)

for _ in range(8):
    mello.rest(Duration.WHOLE)

# Bars 9-16: lively melody — not just held chords, actual phrases
mello_phrase_a = [
    (E, Duration.QUARTER, 65), (G, Duration.EIGHTH, 58),
    (A, Duration.EIGHTH, 60), (B, Duration.QUARTER, 68),
    (None, Duration.QUARTER, 0),
    (A, Duration.QUARTER, 62), (G, Duration.EIGHTH, 55),
    (Fs, Duration.EIGHTH, 52), (E, Duration.HALF, 60),
    (None, Duration.QUARTER, 0), (D, Duration.QUARTER, 55),
    (E, Duration.QUARTER, 62), (G, Duration.QUARTER, 58),
    (B, Duration.HALF, 65), (A, Duration.HALF, 60),
    (G, Duration.WHOLE, 62),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in mello_phrase_a:
    if note is None:
        mello.rest(dur)
    else:
        mello.add(note, dur, velocity=vel)

# Bars 17-32: continues underneath sitar
for _ in range(4):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=50)

# Bars 33-40: transition — mellotron chords while synths emerge
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=55)

# Bars 41-48: drops out — synths own this
for _ in range(8):
    mello.rest(Duration.WHOLE)

# Bars 49-56: returns — both worlds together
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=52)

# Bars 57-64: PEAK — mellotron chords full
mello.set(volume=0.35)
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=62)

# Bars 65-72: MELLOTRON SOLO — the bridge between worlds
mello.set(volume=0.4)
mello_solo = [
    (B, Duration.HALF, 72), (A, Duration.QUARTER, 65),
    (G, Duration.QUARTER, 62),
    (Fs, Duration.HALF, 68), (E, Duration.QUARTER, 60),
    (D, Duration.QUARTER, 58),
    (E, Duration.DOTTED_HALF, 70), (Fs, Duration.QUARTER, 62),
    (G, Duration.WHOLE, 65),
    (A, Duration.QUARTER, 68), (B, Duration.QUARTER, 72),
    (A, Duration.QUARTER, 65), (G, Duration.QUARTER, 62),
    (Fs, Duration.HALF, 68), (E, Duration.HALF, 65),
    (D, Duration.HALF, 60), (E, Duration.HALF, 65),
    (E, Duration.WHOLE, 68),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in mello_solo:
    if note is None:
        mello.rest(dur)
    else:
        mello.add(note, dur, velocity=vel)

# Bars 73-80: fading chords
for vel in [55, 48, 42, 35, 28, 22, 15, 8]:
    mello.add(prog[0], Duration.WHOLE, velocity=vel)

# Bars 81-88: gone
for _ in range(8):
    mello.rest(Duration.WHOLE)

# ── SITAR — enters bar 17, builds from 8ths to 16ths to shreds ─
sitar = score.part("sitar", instrument="sitar", volume=0.55,
                   reverb=0.2, reverb_type="taj_mahal",
                   delay=0.12, delay_time=0.3, delay_feedback=0.2,
                   pan=-0.25, saturation=0.2, humanize=0.1)

for _ in range(16):
    sitar.rest(Duration.WHOLE)

# Bars 17-20: 8th note melody — introducing itself
sitar.add(E, Duration.EIGHTH, velocity=75)
sitar.add(G, Duration.EIGHTH, velocity=70)
sitar.add(A, Duration.QUARTER, velocity=78)
sitar.add(B, Duration.EIGHTH, velocity=72)
sitar.add(A, Duration.EIGHTH, velocity=70)
sitar.add(G, Duration.HALF, velocity=75)
sitar.add(Fs, Duration.EIGHTH, velocity=68)
sitar.add(E, Duration.EIGHTH, velocity=65)
sitar.add(D, Duration.QUARTER, velocity=70)
sitar.add(E, Duration.HALF, velocity=72)
sitar.rest(Duration.WHOLE)
sitar.add(B, Duration.EIGHTH, velocity=78)
sitar.add(A, Duration.EIGHTH, velocity=72)
sitar.add(G, Duration.QUARTER, velocity=75)
sitar.add(Fs, Duration.EIGHTH, velocity=68)
sitar.add(E, Duration.EIGHTH, velocity=70)
sitar.add(D, Duration.HALF, velocity=72)

# Bars 21-24: 16th arps begin — the swarm starts, dynamics build
arp_i  = [E, G, B, G, E, B.add(-12), G.add(-12), B.add(-12)]
arp_vii = [D, Fs, A, Fs, D, A.add(-12), Fs.add(-12), A.add(-12)]
arp_vi = [C, E, G, E, C, G.add(-12), E.add(-12), G.add(-12)]
arp_iv = [A.add(-12), C, E, C, A.add(-12), E.add(-12), C.add(-12), E.add(-12)]

# Each arp crescendos: first note accented, middle soft, peak at top
def sitar_arp(part, notes, base_vel, dur=Duration.SIXTEENTH):
    vels = [base_vel, base_vel-12, base_vel-8, base_vel+5,  # accent, dip, rise, peak
            base_vel-5, base_vel-15, base_vel-18, base_vel-10]
    for note, vel in zip(notes, vels):
        part.add(note, dur, velocity=max(30, vel))

# Building: 65 → 72 → 78 → 82
for arp, base in [(arp_i, 65), (arp_vii, 70), (arp_vi, 75), (arp_iv, 80)]:
    sitar_arp(sitar, arp, base)
    sitar_arp(sitar, arp, max(40, base - 8))

# Bars 25-32: full 16th arps with 32nd fills every 4 bars
sitar.set(volume=0.6)
for bar in range(8):
    if bar % 4 == 3:
        # 32nd note fill — crescendo up, decrescendo down
        up = [E, Fs, G, A, B, C, D, E.add(12)]
        down = [D, C, B, A, G, Fs, E, D]
        for i, note in enumerate(up):
            sitar.add(note, 0.125, velocity=min(110, 75 + i * 5))
        for i, note in enumerate(down):
            sitar.add(note, 0.125, velocity=max(60, 105 - i * 5))
    else:
        base = [85, 82, 88, 85][bar % 4]  # i louder, vi loudest
        sitar_arp(sitar, [arp_i, arp_vii, arp_vi, arp_iv][bar % 4], base)
        sitar_arp(sitar, [arp_i, arp_vii, arp_vi, arp_iv][bar % 4], max(40, base - 8))

# Bars 33-40: sitar pulls back — making room for synths
sitar.set(volume=0.45)
for _ in range(4):
    sitar_arp(sitar, arp_i, 68)
    sitar_arp(sitar, arp_i, 58)
    sitar_arp(sitar, arp_vii, 65)
    sitar_arp(sitar, arp_vii, 55)

# Bars 41-48: sitar drops out — synths own this
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# Bars 49-56: BOTH WORLDS — sitar arps over synths, more intensity
sitar.set(volume=0.55)
for bar in range(8):
    if bar % 4 == 3:
        # 32nd fill — massive crescendo
        up = [E, Fs, G, A, B, C, D, E.add(12)]
        down = [E.add(12), D, C, B, A, G, Fs, E]
        for i, note in enumerate(up):
            sitar.add(note, 0.125, velocity=min(115, 80 + i * 5))
        for i, note in enumerate(down):
            sitar.add(note, 0.125, velocity=max(65, 110 - i * 6))
    else:
        base = [88, 85, 92, 88][bar % 4]
        sitar_arp(sitar, [arp_i, arp_vii, arp_vi, arp_iv][bar % 4], base)
        sitar_arp(sitar, [arp_i, arp_vii, arp_vi, arp_iv][bar % 4], max(45, base - 10))

# Bars 57-64: PEAK — sitar shredding with maximum dynamics
sitar.set(volume=0.65)
for bar in range(8):
    if bar % 2 == 1:
        # 32nd note shred — crescendo up, accent the peak
        shred_a = [E, G, B, E.add(12), B, G, E, B.add(-12)]
        shred_b = [E, A, C, E.add(12), C, A, E, C.add(-12)]
        for i, note in enumerate(shred_a):
            sitar.add(note, 0.125, velocity=min(118, 82 + i * 5))
        for i, note in enumerate(shred_b):
            sitar.add(note, 0.125, velocity=max(70, 115 - i * 5))
    else:
        sitar_arp(sitar, arp_i, 95)
        sitar_arp(sitar, arp_vi, 92)

# Bars 65-72: drops back — mellotron solo
sitar.set(volume=0.35)
for _ in range(4):
    for arp in [arp_i, arp_vii]:
        for note in arp:
            sitar.add(note, Duration.SIXTEENTH, velocity=60)
        for note in arp:
            sitar.add(note, Duration.SIXTEENTH, velocity=55)

# Bars 73-80: returns for the ending
sitar.set(volume=0.5)
for bar in range(4):
    arp = [arp_i, arp_vii, arp_vi, arp_iv][bar]
    for note in arp:
        sitar.add(note, Duration.SIXTEENTH, velocity=max(40, 75 - bar * 8))
    for note in arp:
        sitar.add(note, Duration.SIXTEENTH, velocity=max(35, 70 - bar * 8))
# Fade
for vel in [55, 42, 30, 18]:
    for note in arp_i:
        sitar.add(note, Duration.SIXTEENTH, velocity=vel)
    for note in arp_i:
        sitar.add(note, Duration.SIXTEENTH, velocity=max(12, vel - 8))

# Bars 81-88: gone
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# THE SYNTHS — emerge from the acoustic bed at bar 33
# ═══════════════════════════════════════════════════════════════════

# ── SAW — the main synth voice ────────────────────────────────
saw = score.part("saw", synth="saw", volume=0.4,
                 lowpass=4000,
                 distortion=0.15, distortion_drive=2.0,
                 saturation=0.5, legato=True, glide=0.03,
                 reverb=0.2, reverb_type="spring",
                 delay=0.2, delay_time=0.3, delay_feedback=0.25,
                 pan=0.25)
saw.lfo("lowpass", rate=0.012, min=1500, max=7000, bars=88, shape="triangle")

for _ in range(32):
    saw.rest(Duration.WHOLE)

# Bars 33-40: emerges — mono line, rhythmic
saw_riff = [
    (E, Duration.SIXTEENTH, 82), (None, Duration.SIXTEENTH, 0),
    (E, Duration.SIXTEENTH, 78), (G, Duration.SIXTEENTH, 72),
    (E, Duration.SIXTEENTH, 85), (None, Duration.SIXTEENTH, 0),
    (D, Duration.EIGHTH, 70),
    (E, Duration.SIXTEENTH, 88), (B.add(-12), Duration.SIXTEENTH, 72),
    (E, Duration.SIXTEENTH, 80), (None, Duration.SIXTEENTH, 0),
    (C, Duration.EIGHTH, 75),
    (E, Duration.EIGHTH, 85),
]
for _ in range(8):
    for note, dur, vel in saw_riff:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=vel)

# Bars 41-48: full power — synths own this
saw.set(volume=0.5)
for _ in range(8):
    for note, dur, vel in saw_riff:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=min(100, vel + 8))

# Bars 49-64: continues through both worlds + peak
for _ in range(16):
    for note, dur, vel in saw_riff:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=min(105, vel + 10))

# Bars 65-80: fading
saw.set(volume=0.3)
for _ in range(8):
    for note, dur, vel in saw_riff:
        if note is None:
            saw.rest(dur)
        else:
            saw.add(note, dur, velocity=max(30, vel - 15))
for _ in range(8):
    saw.rest(Duration.WHOLE)

# ── FM — metallic texture ────────────────────────────────────
fm = score.part("fm", synth="fm", envelope="pluck", volume=0.2,
                reverb=0.2, reverb_type="cathedral",
                delay=0.12, delay_time=0.3, delay_feedback=0.15,
                pan=-0.3)

for _ in range(40):
    fm.rest(Duration.WHOLE)

# Bars 41-64: bell blips
fm_blip = [
    (B, Duration.QUARTER, 60), (None, Duration.QUARTER, 0),
    (A, Duration.QUARTER, 55), (None, Duration.QUARTER, 0),
]
for _ in range(24):
    for note, dur, vel in fm_blip:
        if note is None:
            fm.rest(dur)
        else:
            fm.add(note, dur, velocity=vel)

# Bars 65-88: fading
for vel in [50, 42, 35, 28, 22, 15, 0, 0]:
    if vel > 0:
        fm.add(B, Duration.QUARTER, velocity=vel)
        fm.rest(Duration.DOTTED_HALF)
    else:
        fm.rest(Duration.WHOLE)
for _ in range(16):
    fm.rest(Duration.WHOLE)

# ── SQUARE — counter rhythm ───────────────────────────────────
square = score.part("square", synth="square", volume=0.25,
                    lowpass=2500,
                    distortion=0.1, distortion_drive=1.5,
                    reverb=0.12, reverb_type="taj_mahal",
                    delay=0.1, delay_time=0.45, delay_feedback=0.15,
                    detune=6, pan=0.35)

for _ in range(40):
    square.rest(Duration.WHOLE)

sq_line = [
    (None, Duration.SIXTEENTH, 0), (E, Duration.SIXTEENTH, 70),
    (None, Duration.EIGHTH, 0),
    (G, Duration.SIXTEENTH, 65), (None, Duration.SIXTEENTH, 0),
    (E, Duration.EIGHTH, 72),
    (None, Duration.SIXTEENTH, 0), (D, Duration.SIXTEENTH, 62),
    (E, Duration.SIXTEENTH, 68), (None, Duration.SIXTEENTH, 0),
    (B.add(-12), Duration.EIGHTH, 65),
    (E, Duration.EIGHTH, 72),
]
for _ in range(24):
    for note, dur, vel in sq_line:
        if note is None:
            square.rest(dur)
        else:
            square.add(note, dur, velocity=vel)

for _ in range(24):
    square.rest(Duration.WHOLE)

# ── SUPERSAW PAD — the synth wall ─────────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.12,
                 reverb=0.4, reverb_type="taj_mahal",
                 chorus=0.3, chorus_rate=0.15, chorus_depth=0.008,
                 lowpass=2500)

for _ in range(40):
    pad.rest(Duration.WHOLE)

for _ in range(6):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=48)

for vel in [42, 35, 28, 22, 15, 10, 5, 0]:
    if vel > 0:
        pad.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        pad.rest(Duration.WHOLE)
for _ in range(16):
    pad.rest(Duration.WHOLE)

# ── DRUMS — enters bar 33 ────────────────────────────────────
kick = score.part("kick", volume=0.6, humanize=0.03,
                  distortion=0.08, distortion_drive=1.5)
snare = score.part("snare", volume=0.4, humanize=0.04,
                   reverb=0.15, delay=0.05, delay_time=0.3,
                   delay_feedback=0.08, pan=0.05)
hats = score.part("hats", volume=0.22, pan=0.15, humanize=0.04)

for _ in range(32):
    kick.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)
    hats.rest(Duration.WHOLE)

for _ in range(40):
    kick.hit(K, Duration.QUARTER, velocity=105)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=88)
    kick.hit(K, Duration.QUARTER, velocity=100)
    kick.rest(Duration.QUARTER)

    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=92)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=95)

    for beat in range(4):
        hats.hit(CH, Duration.SIXTEENTH, velocity=65)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(CH, Duration.SIXTEENTH, velocity=52)
        hats.hit(CH, Duration.SIXTEENTH, velocity=35)

# Bars 73-80: fading
for vel in [92, 78, 65, 52, 38, 25, 0, 0]:
    if vel > 0:
        kick.hit(K, Duration.QUARTER, velocity=vel)
        kick.rest(Duration.DOTTED_HALF)
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=max(15, vel - 10))
        snare.rest(Duration.HALF)
        hats.hit(CH, Duration.QUARTER, velocity=max(15, vel - 30))
        hats.rest(Duration.DOTTED_HALF)
    else:
        kick.rest(Duration.WHOLE)
        snare.rest(Duration.WHOLE)
        hats.rest(Duration.WHOLE)

for _ in range(8):
    kick.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)
    hats.rest(Duration.WHOLE)

# ── SUB — enters bar 33 ──────────────────────────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.5,
                 lowpass=150, distortion=0.15, distortion_drive=2.5,
                 sub_osc=0.4, sidechain=0.3)

for _ in range(32):
    sub.rest(Duration.WHOLE)

roots = [E.add(-24), D.add(-24), C.add(-24), A.add(-24)]
for _ in range(10):
    for root in roots:
        sub.add(root, Duration.WHOLE, velocity=35)

for vel in [30, 25, 20, 15, 10, 5, 0, 0]:
    if vel > 0:
        sub.add(E.add(-24), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

for _ in range(8):
    sub.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 100")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing EMERGENCE (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing EMERGENCE...")
    play_score(score)
