"""
WAVEFORMS — every oscillator gets a turn.
Sine, triangle, square, saw, FM, PWM, wavefold, supersaw, noise.
Percussive blips stacking into a machine. Occasional sustained pads.
F minor, 118 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("F", "minor")
s = key.scale  # F G Ab Bb C Db Eb

F  = s[0]; G  = s[1]; Ab = s[2]; Bb = s[3]
C  = s[4]; Db = s[5]; Eb = s[6]

score = Score("4/4", bpm=118)

K  = DrumSound.KICK
CH = DrumSound.CLOSED_HAT

prog = key.progression("i", "VII", "VI", "iv")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~3:15):
#   Bars  1-8:   Sine blips — percussive, melodic, setting the grid
#   Bars  9-16:  Triangle joins — harmony, counterpoint
#   Bars 17-24:  Square enters — rhythmic fill, staccato
#   Bars 25-32:  Saw arp — the energy lifts
#   Bars 33-40:  All four interlocking — the machine hums
#   Bars 41-48:  Supersaw pad + kick — the room opens
#   Bars 49-56:  Peak — everything singing, melodic peak
#   Bars 57-64:  Unwind — layers peel away, sine last
# ═══════════════════════════════════════════════════════════════════

# ── SINE — percussive blips, the seed of everything ───────────
sine = score.part("sine", synth="sine", envelope="pluck", volume=0.5,
                  reverb=0.4, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.254, delay_feedback=0.25,
                  pan=-0.15)

# Bars 1-8: melodic blips — the rhythm IS the melody
# F minor: descending, dark. Land on Ab and Db, not C and F.
sine_phrase = [
    (F, Duration.SIXTEENTH, 78), (None, Duration.SIXTEENTH, 0),
    (Eb, Duration.SIXTEENTH, 72), (Db, Duration.SIXTEENTH, 70),
    (None, Duration.EIGHTH, 0),
    (C, Duration.EIGHTH, 68),
    (Db, Duration.SIXTEENTH, 72), (None, Duration.SIXTEENTH, 0),
    (Ab.add(-12), Duration.SIXTEENTH, 65), (None, Duration.SIXTEENTH, 0),
    (None, Duration.QUARTER, 0),
]
sine_phrase_b = [
    (Ab, Duration.SIXTEENTH, 75), (None, Duration.SIXTEENTH, 0),
    (G, Duration.SIXTEENTH, 68), (F, Duration.SIXTEENTH, 72),
    (None, Duration.EIGHTH, 0),
    (Eb, Duration.EIGHTH, 70),
    (Db, Duration.SIXTEENTH, 72), (None, Duration.SIXTEENTH, 0),
    (C, Duration.SIXTEENTH, 65), (None, Duration.SIXTEENTH, 0),
    (None, Duration.QUARTER, 0),
]
for _ in range(4):
    for note, dur, vel in sine_phrase:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=vel)
    for note, dur, vel in sine_phrase_b:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=vel)

# ── SINE PAD — the same waveform, but sustained, opens up ──────
sine_pad = score.part("sine_pad", synth="sine", envelope="pad", volume=0.2,
                      reverb=0.3, reverb_type="taj_mahal",
                      chorus=0.2, chorus_rate=0.06, chorus_depth=0.008,
                      pan=0.15)

# Bars 1-4: silent — let the blips establish
for _ in range(4):
    sine_pad.rest(Duration.WHOLE)

# Bars 5-8: sine opens up — held notes an octave below the blips
sine_pad.add(F.add(-12), Duration.WHOLE, velocity=35)
sine_pad.add(Ab.add(-12), Duration.WHOLE, velocity=38)
sine_pad.add(Db, Duration.WHOLE, velocity=40)
sine_pad.add(F.add(-12), Duration.WHOLE, velocity=35)

# Bars 9-16: wider — octave spread, low and high together
sine_pad.add(F.add(-12), Duration.HALF, velocity=42)
sine_pad.add(Ab, Duration.HALF, velocity=38)
sine_pad.add(Db.add(-12), Duration.WHOLE, velocity=40)
sine_pad.add(F.add(-12), Duration.HALF, velocity=42)
sine_pad.add(C, Duration.HALF, velocity=35)
sine_pad.add(Ab.add(-12), Duration.WHOLE, velocity=40)
sine_pad.add(Db.add(-12), Duration.HALF, velocity=42)
sine_pad.add(Eb, Duration.HALF, velocity=38)
sine_pad.add(F.add(-12), Duration.WHOLE, velocity=40)
sine_pad.add(Ab.add(-12), Duration.WHOLE, velocity=38)

# Bars 17-56: continues — swelling and receding
for _ in range(10):
    sine_pad.add(F.add(-12), Duration.WHOLE, velocity=42)
    sine_pad.add(Ab.add(-12), Duration.WHOLE, velocity=38)
    sine_pad.add(Db.add(-12), Duration.WHOLE, velocity=40)
    sine_pad.add(Eb.add(-12), Duration.WHOLE, velocity=38)

# Bars 57-64: fading
for vel in [35, 30, 25, 20, 15, 10, 5, 0]:
    if vel > 0:
        sine_pad.add(F.add(-12), Duration.WHOLE, velocity=vel)
    else:
        sine_pad.rest(Duration.WHOLE)

# ── TRIANGLE PAD — occasional sustained warmth ─────────────────
tri_pad = score.part("tri_pad", synth="triangle", envelope="pad", volume=0.15,
                     reverb=0.25, reverb_type="cathedral",
                     chorus=0.2, chorus_rate=0.05, chorus_depth=0.01,
                     pan=-0.35)

# Mostly silent — just opens up at transitions
for _ in range(16):
    tri_pad.rest(Duration.WHOLE)
# Bars 17-18: triangle opens up when square enters
tri_pad.add(Ab.add(-12), Duration.WHOLE, velocity=38)
tri_pad.add(Db, Duration.WHOLE, velocity=35)
for _ in range(6):
    tri_pad.rest(Duration.WHOLE)
# Bars 25-26: opens again when saw enters
tri_pad.add(F.add(-12), Duration.WHOLE, velocity=40)
tri_pad.add(Eb, Duration.WHOLE, velocity=35)
for _ in range(6):
    tri_pad.rest(Duration.WHOLE)
# Bars 33-34: opens when kick drops
tri_pad.add(Db, Duration.WHOLE, velocity=42)
tri_pad.add(Ab.add(-12), Duration.WHOLE, velocity=38)
for _ in range(14):
    tri_pad.rest(Duration.WHOLE)
# Bars 49-50: opens at peak
tri_pad.add(F.add(-12), Duration.WHOLE, velocity=45)
tri_pad.add(Ab.add(-12), Duration.WHOLE, velocity=42)
for _ in range(14):
    tri_pad.rest(Duration.WHOLE)

# ── SAW PAD — rare, big, only at the peak ─────────────────────
saw_pad = score.part("saw_pad", synth="saw", envelope="pad", volume=0.12,
                     lowpass=2000,
                     reverb=0.2, reverb_type="spring",
                     chorus=0.3, chorus_rate=0.1, chorus_depth=0.008,
                     pan=0.35)

# Silent until bar 49
for _ in range(48):
    saw_pad.rest(Duration.WHOLE)
# Bars 49-52: the saw opens up — one sustained moment
for chord in prog:
    saw_pad.add(chord, Duration.WHOLE, velocity=40)
# Back to silence
for _ in range(12):
    saw_pad.rest(Duration.WHOLE)

# Bars 9-56: blips continue — the constant thread
for _ in range(24):
    for note, dur, vel in sine_phrase:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=vel)
    for note, dur, vel in sine_phrase_b:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=vel)

# Bars 57-64: fading
for rep in range(4):
    off = rep * -12
    for note, dur, vel in sine_phrase:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=max(20, vel + off))
    for note, dur, vel in sine_phrase_b:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=max(20, vel + off))

# ── TRIANGLE — harmony, enters bar 9 ─────────────────────────
tri = score.part("triangle", synth="triangle", envelope="pluck", volume=0.4,
                 reverb=0.2, reverb_decay=1.0,
                 delay=0.12, delay_time=0.254, delay_feedback=0.2,
                 pan=0.3)

for _ in range(8):
    tri.rest(Duration.WHOLE)

# Bars 9-16: counterpoint — fills the gaps in sine's rhythm
# Triangle: descending thirds, landing on dark notes
tri_phrase = [
    (None, Duration.EIGHTH, 0),
    (Db, Duration.SIXTEENTH, 70), (C, Duration.SIXTEENTH, 65),
    (None, Duration.EIGHTH, 0),
    (Ab.add(-12), Duration.SIXTEENTH, 68), (None, Duration.SIXTEENTH, 0),
    (Bb.add(-12), Duration.SIXTEENTH, 62), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (Ab.add(-12), Duration.EIGHTH, 65),
]
tri_phrase_b = [
    (None, Duration.EIGHTH, 0),
    (F, Duration.SIXTEENTH, 72), (Eb, Duration.SIXTEENTH, 68),
    (None, Duration.EIGHTH, 0),
    (Db, Duration.SIXTEENTH, 70), (None, Duration.SIXTEENTH, 0),
    (C, Duration.SIXTEENTH, 62), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (Db, Duration.EIGHTH, 68),
]
for _ in range(4):
    for note, dur, vel in tri_phrase:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=vel)
    for note, dur, vel in tri_phrase_b:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=vel)

# Bars 17-56: continues
for _ in range(20):
    for note, dur, vel in tri_phrase:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=vel)
    for note, dur, vel in tri_phrase_b:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=vel)

# Bars 57-64: fading
for rep in range(4):
    off = rep * -12
    for note, dur, vel in tri_phrase:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=max(18, vel + off))
    for note, dur, vel in tri_phrase_b:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=max(18, vel + off))

# ── SQUARE — staccato rhythm, enters bar 17 ──────────────────
sq = score.part("square", synth="square", envelope="pluck", volume=0.3,
                lowpass=3500,
                reverb=0.15, reverb_decay=0.8,
                delay=0.1, delay_time=0.127, delay_feedback=0.15,
                pan=-0.4)

for _ in range(16):
    sq.rest(Duration.WHOLE)

# Bars 17-24: rhythmic stabs — off the beat
sq_stab = [
# Square: off-beat stabs — Db and Ab, the minor anchors
    (None, Duration.SIXTEENTH, 0), (Db, Duration.SIXTEENTH, 70),
    (None, Duration.SIXTEENTH, 0), (None, Duration.SIXTEENTH, 0),
    (None, Duration.SIXTEENTH, 0), (Ab.add(-12), Duration.SIXTEENTH, 65),
    (None, Duration.SIXTEENTH, 0), (Db, Duration.SIXTEENTH, 72),
    (None, Duration.EIGHTH, 0),
    (None, Duration.SIXTEENTH, 0), (Ab.add(-12), Duration.SIXTEENTH, 65),
    (None, Duration.QUARTER, 0),
]
for _ in range(8):
    for note, dur, vel in sq_stab:
        if note is None:
            sq.rest(dur)
        else:
            sq.add(note, dur, velocity=vel)

# Bars 25-56: continues
for _ in range(32):
    for note, dur, vel in sq_stab:
        if note is None:
            sq.rest(dur)
        else:
            sq.add(note, dur, velocity=vel)

# Bars 57-64: fading
for rep in range(8):
    off = rep * -8
    for note, dur, vel in sq_stab:
        if note is None:
            sq.rest(dur)
        else:
            sq.add(note, dur, velocity=max(15, vel + off))

# ── SAW ARP — energy lift, enters bar 25 ─────────────────────
saw = score.part("saw", synth="saw", envelope="pluck", volume=0.3,
                 lowpass=4000,
                 distortion=0.05, saturation=0.2,
                 reverb=0.18, reverb_type="spring",
                 delay=0.2, delay_time=0.254, delay_feedback=0.3,
                 pan=0.4)
saw.lfo("lowpass", rate=0.01, min=2000, max=6000, bars=64, shape="triangle")

for _ in range(24):
    saw.rest(Duration.WHOLE)

# Bars 25-32: arpeggio — the energy lifts
# Saw arps — descending shapes, minor triads
arp_a = [C, Ab, F, Ab, C, F, Ab, F]                        # i — Fm descending feel
arp_b = [Bb, G, Eb, G, Bb, Eb, G, Eb]                      # VII — Eb
arp_c = [Ab, F, Db, F, Ab, Db, F.add(-12), Db.add(-12)]    # VI — Db
arp_d = [F, Db, Bb.add(-12), Db, F, Bb.add(-12), Db, F]    # iv — Bbm

for _ in range(2):
    for note in arp_a:
        saw.add(note, Duration.EIGHTH, velocity=68)
    for note in arp_b:
        saw.add(note, Duration.EIGHTH, velocity=65)
    for note in arp_c:
        saw.add(note, Duration.EIGHTH, velocity=70)
    for note in arp_d:
        saw.add(note, Duration.EIGHTH, velocity=68)

# Bars 33-56: continues — the constant motion
for _ in range(6):
    for note in arp_a:
        saw.add(note, Duration.EIGHTH, velocity=72)
    for note in arp_b:
        saw.add(note, Duration.EIGHTH, velocity=68)
    for note in arp_c:
        saw.add(note, Duration.EIGHTH, velocity=72)
    for note in arp_d:
        saw.add(note, Duration.EIGHTH, velocity=70)

# Bars 57-64: fading arps
for rep in range(2):
    off = rep * -15
    for note in arp_a:
        saw.add(note, Duration.EIGHTH, velocity=max(20, 62 + off))
    for note in arp_b:
        saw.add(note, Duration.EIGHTH, velocity=max(20, 58 + off))
    for note in arp_c:
        saw.add(note, Duration.EIGHTH, velocity=max(20, 60 + off))
    for note in arp_d:
        saw.add(note, Duration.EIGHTH, velocity=max(20, 58 + off))

# ── SUPERSAW PAD — the room opens, bar 41 ────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.12,
                 reverb=0.6, reverb_type="taj_mahal",
                 chorus=0.3, chorus_rate=0.15, chorus_depth=0.008,
                 lowpass=2500)

for _ in range(40):
    pad.rest(Duration.WHOLE)

# Bars 41-56: chord pads — warmth behind the blips
for _ in range(4):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=48)

# Bars 57-64: fading
for vel in [42, 35, 28, 22, 15, 10, 5, 0]:
    if vel > 0:
        pad.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        pad.rest(Duration.WHOLE)

# ── FM — metallic, bell-like blips, enters bar 25 ─────────────
fm = score.part("fm", synth="fm", envelope="pluck", volume=0.3,
                reverb=0.3, reverb_type="cathedral",
                delay=0.15, delay_time=0.254, delay_feedback=0.2,
                pan=-0.35)

for _ in range(24):
    fm.rest(Duration.WHOLE)

# FM phrase — metallic, inharmonic, fills gaps
fm_phrase = [
    (Ab, Duration.SIXTEENTH, 68), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (Db, Duration.SIXTEENTH, 65), (None, Duration.SIXTEENTH, 0),
    (Eb, Duration.SIXTEENTH, 70), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (C, Duration.SIXTEENTH, 62), (None, Duration.SIXTEENTH, 0),
    (None, Duration.QUARTER, 0),
]
for _ in range(32):
    for note, dur, vel in fm_phrase:
        if note is None:
            fm.rest(dur)
        else:
            fm.add(note, dur, velocity=vel)

# Bars 57-64: fading
for rep in range(8):
    off = rep * -8
    for note, dur, vel in fm_phrase:
        if note is None:
            fm.rest(dur)
        else:
            fm.add(note, dur, velocity=max(15, vel + off))

# ── PWM — wobbling pulse width, enters bar 33 ─────────────────
pwm = score.part("pwm", synth="pwm", envelope="pluck", volume=0.25,
                 reverb=0.2, reverb_decay=1.0,
                 delay=0.12, delay_time=0.127, delay_feedback=0.18,
                 pan=0.35)

for _ in range(32):
    pwm.rest(Duration.WHOLE)

# PWM phrase — the wobble gives it movement even on single notes
pwm_phrase = [
    (F, Duration.SIXTEENTH, 72), (None, Duration.SIXTEENTH, 0),
    (Eb, Duration.SIXTEENTH, 65), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (Db, Duration.SIXTEENTH, 68), (F, Duration.SIXTEENTH, 70),
    (None, Duration.EIGHTH, 0),
    (Eb, Duration.SIXTEENTH, 65), (None, Duration.SIXTEENTH, 0),
    (None, Duration.QUARTER, 0),
]
for _ in range(24):
    for note, dur, vel in pwm_phrase:
        if note is None:
            pwm.rest(dur)
        else:
            pwm.add(note, dur, velocity=vel)

# Bars 57-64: fading
for rep in range(8):
    off = rep * -8
    for note, dur, vel in pwm_phrase:
        if note is None:
            pwm.rest(dur)
        else:
            pwm.add(note, dur, velocity=max(15, vel + off))

# ── WAVEFOLD — harsh, complex harmonics, enters bar 41 ────────
wf = score.part("wavefold", synth="wavefold", envelope="pluck", volume=0.2,
                reverb=0.15, reverb_decay=0.8,
                delay=0.1, delay_time=0.254, delay_feedback=0.15,
                pan=-0.2)

for _ in range(40):
    wf.rest(Duration.WHOLE)

# Wavefold phrase — aggressive, complex
wf_phrase = [
    (C, Duration.SIXTEENTH, 72), (Db, Duration.SIXTEENTH, 68),
    (None, Duration.EIGHTH, 0),
    (Ab.add(-12), Duration.SIXTEENTH, 65), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (F, Duration.SIXTEENTH, 70), (Eb, Duration.SIXTEENTH, 65),
    (None, Duration.EIGHTH, 0),
    (Db, Duration.EIGHTH, 68),
]
for _ in range(16):
    for note, dur, vel in wf_phrase:
        if note is None:
            wf.rest(dur)
        else:
            wf.add(note, dur, velocity=vel)

# Bars 57-64: fading
for rep in range(8):
    off = rep * -8
    for note, dur, vel in wf_phrase:
        if note is None:
            wf.rest(dur)
        else:
            wf.add(note, dur, velocity=max(15, vel + off))

# ── 808 — sustained sub, the grit underneath ──────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=0.55,
                 lowpass=200, distortion=0.2, distortion_drive=3.0,
                 sub_osc=0.5, saturation=0.4, sidechain=0.3)

for _ in range(16):
    sub.rest(Duration.WHOLE)

# Bars 17-56: sustained 808, follows the chord roots
roots = [F.add(-24), Eb.add(-24), Db.add(-24), Bb.add(-24)]
for _ in range(10):
    for root in roots:
        sub.add(root, Duration.WHOLE, velocity=38)

# Bars 57-64: fading
for vel in [32, 28, 22, 18, 14, 10, 5, 0]:
    if vel > 0:
        sub.add(F.add(-24), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# ── KICK — four on the floor first, alone ──────────────────────
kick = score.part("kick", volume=0.6, humanize=0.03)

for _ in range(24):
    kick.rest(Duration.WHOLE)

# Bars 25-32: just the kick — four on the floor, nothing else
for _ in range(8):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=100)

# Bars 33-56: continues under the full drums
for _ in range(24):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=105)

# Bars 57-64: fading
for vel in [92, 78, 65, 52, 38, 25, 0, 0]:
    if vel > 0:
        for beat in range(4):
            kick.hit(K, Duration.QUARTER, velocity=vel)
    else:
        kick.rest(Duration.WHOLE)

# ── DRUMS — complex rhythmic pattern, enters bar 33 ───────────
S = DrumSound.SNARE
OH = DrumSound.OPEN_HAT

hats = score.part("hats", volume=0.25, pan=0.15, humanize=0.04,
                  delay=0.06, delay_time=0.127, delay_feedback=0.1)

snare = score.part("snare", volume=0.4, humanize=0.04,
                   reverb=0.15, reverb_decay=0.6,
                   delay=0.05, delay_time=0.254, delay_feedback=0.08,
                   pan=0.05)

for _ in range(32):
    hats.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)

# Bars 33-40: rhythmic hats + snare on 2&4 — the groove locks
for _ in range(8):
    # Hats: 16ths with accents and ghost notes
    hats.hit(CH, Duration.SIXTEENTH, velocity=72)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(CH, Duration.SIXTEENTH, velocity=55)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(CH, Duration.SIXTEENTH, velocity=68)
    hats.hit(CH, Duration.SIXTEENTH, velocity=40)
    hats.hit(OH, Duration.SIXTEENTH, velocity=58)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(CH, Duration.SIXTEENTH, velocity=72)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(CH, Duration.SIXTEENTH, velocity=52)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(CH, Duration.SIXTEENTH, velocity=65)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(OH, Duration.SIXTEENTH, velocity=55)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    # Snare: 2 and 4 with ghost notes
    snare.rest(Duration.EIGHTH)
    snare.hit(S, Duration.SIXTEENTH, velocity=40)  # ghost
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.QUARTER, velocity=95)     # 2
    snare.rest(Duration.EIGHTH)
    snare.hit(S, Duration.SIXTEENTH, velocity=38)  # ghost
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.QUARTER, velocity=98)     # 4

# Bars 41-48: tighter — more ghost notes, busier
for _ in range(8):
    hats.hit(CH, Duration.SIXTEENTH, velocity=75)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(CH, Duration.SIXTEENTH, velocity=58)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(OH, Duration.SIXTEENTH, velocity=62)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(CH, Duration.SIXTEENTH, velocity=55)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(CH, Duration.SIXTEENTH, velocity=72)
    hats.hit(CH, Duration.SIXTEENTH, velocity=40)
    hats.hit(CH, Duration.SIXTEENTH, velocity=58)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(OH, Duration.SIXTEENTH, velocity=60)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(CH, Duration.SIXTEENTH, velocity=55)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    # Snare with more ghosts
    snare.hit(S, Duration.SIXTEENTH, velocity=35)  # ghost
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.SIXTEENTH, velocity=38)  # ghost
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.QUARTER, velocity=98)     # 2
    snare.hit(S, Duration.SIXTEENTH, velocity=35)  # ghost
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.SIXTEENTH, velocity=40)  # ghost
    snare.rest(Duration.SIXTEENTH)
    snare.hit(S, Duration.QUARTER, velocity=100)    # 4

# Bars 49-56: peak — snare fills every 4 bars
for bar in range(8):
    if bar % 4 == 3:
        # Fill — 16th note snare roll
        for i in range(16):
            snare.hit(S, Duration.SIXTEENTH, velocity=min(110, 60 + i * 3))
        for i in range(16):
            hats.hit(CH, Duration.SIXTEENTH, velocity=min(80, 45 + i * 2))
    else:
        hats.hit(CH, Duration.SIXTEENTH, velocity=78)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=60)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(OH, Duration.SIXTEENTH, velocity=65)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)
        hats.hit(CH, Duration.SIXTEENTH, velocity=58)
        hats.hit(CH, Duration.SIXTEENTH, velocity=35)
        hats.hit(CH, Duration.SIXTEENTH, velocity=75)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(OH, Duration.SIXTEENTH, velocity=62)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)
        hats.hit(CH, Duration.SIXTEENTH, velocity=58)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        snare.rest(Duration.EIGHTH)
        snare.hit(S, Duration.SIXTEENTH, velocity=40)
        snare.rest(Duration.SIXTEENTH)
        snare.hit(S, Duration.QUARTER, velocity=100)
        snare.rest(Duration.EIGHTH)
        snare.hit(S, Duration.SIXTEENTH, velocity=42)
        snare.rest(Duration.SIXTEENTH)
        snare.hit(S, Duration.QUARTER, velocity=102)

# Bars 57-64: fading
for vel in [88, 75, 62, 48, 35, 22, 0, 0]:
    if vel > 0:
        for beat in range(4):
            hats.hit(CH, Duration.EIGHTH, velocity=max(15, vel - 20))
            hats.hit(CH, Duration.EIGHTH, velocity=max(12, vel - 35))
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=vel)
        snare.rest(Duration.HALF)
    else:
        hats.rest(Duration.WHOLE)
        snare.rest(Duration.WHOLE)

# ── MELODIC PEAK — sine lead, bars 49-56 ─────────────────────
lead = score.part("lead", synth="sine", volume=0.55,
                  reverb=0.25, reverb_type="taj_mahal",
                  delay=0.18, delay_time=0.254, delay_feedback=0.25,
                  pan=-0.05)

for _ in range(48):
    lead.rest(Duration.WHOLE)

# Bars 49-56: the melody sings above everything
# Lead melody — descending, minor, Db-C pull at the heart
lead_melody = [
    (Ab, Duration.HALF, 80), (G, Duration.QUARTER, 72),
    (F, Duration.QUARTER, 70),
    (Eb, Duration.HALF, 75), (Db, Duration.QUARTER, 72),
    (C, Duration.QUARTER, 68),
    (Db, Duration.DOTTED_HALF, 78), (C, Duration.QUARTER, 70),
    (Ab.add(-12), Duration.WHOLE, 72),
    (F, Duration.QUARTER, 75), (G, Duration.QUARTER, 70),
    (Ab, Duration.HALF, 78),
    (Bb, Duration.QUARTER, 72), (Ab, Duration.QUARTER, 70),
    (G, Duration.HALF, 68), (F, Duration.HALF, 72),
    (F, Duration.WHOLE, 70),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in lead_melody:
    if note is None:
        lead.rest(dur)
    else:
        lead.add(note, dur, velocity=vel)

# Bars 57-64: one last phrase, dissolving
lead.add(Ab, Duration.HALF, velocity=65)
lead.add(G, Duration.HALF, velocity=58)
lead.add(F, Duration.WHOLE, velocity=52)
for _ in range(6):
    lead.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
# EXTENSION — solos, harmonies, and a proper ending (bars 65-96)
# The track doesn't fade — it evolves.
# ═══════════════════════════════════════════════════════════════════

# ── Bars 65-72: FM SOLO — metallic melody floats above the bed ──
# Everything else drops to drones/pads, FM takes the spotlight
sine.add(F.add(-12), Duration.WHOLE, velocity=40)
sine.add(F.add(-12), Duration.WHOLE, velocity=40)
sine.add(F.add(-12), Duration.WHOLE, velocity=40)
sine.add(F.add(-12), Duration.WHOLE, velocity=40)
sine.add(F.add(-12), Duration.WHOLE, velocity=40)
sine.add(F.add(-12), Duration.WHOLE, velocity=40)
sine.add(F.add(-12), Duration.WHOLE, velocity=40)
sine.add(F.add(-12), Duration.WHOLE, velocity=40)

for _ in range(8):
    tri.rest(Duration.WHOLE)

for _ in range(8):
    sq.rest(Duration.WHOLE)

# Saw holds a drone
for _ in range(8):
    saw.add(F.add(-12), Duration.WHOLE, velocity=35)

# FM solo melody — bell-like, singing
fm_solo = [
    (Ab, Duration.QUARTER, 75), (G, Duration.EIGHTH, 68),
    (F, Duration.EIGHTH, 65), (Eb, Duration.HALF, 72),
    (Db, Duration.QUARTER, 70), (C, Duration.QUARTER, 65),
    (Db, Duration.HALF, 72), (Eb, Duration.HALF, 68),
    (F, Duration.QUARTER, 75), (Ab, Duration.QUARTER, 72),
    (G, Duration.QUARTER, 68), (F, Duration.QUARTER, 72),
    (Eb, Duration.HALF, 70), (Db, Duration.HALF, 72),
    (C, Duration.QUARTER, 65), (Db, Duration.QUARTER, 70),
    (F, Duration.HALF, 75),
    (Ab, Duration.QUARTER, 78), (Bb, Duration.QUARTER, 72),
    (Ab, Duration.QUARTER, 70), (G, Duration.QUARTER, 65),
    (F, Duration.WHOLE, 72),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in fm_solo:
    if note is None:
        fm.rest(dur)
    else:
        fm.add(note, dur, velocity=vel)

for _ in range(8):
    pwm.rest(Duration.WHOLE)
for _ in range(8):
    wf.rest(Duration.WHOLE)

# Supersaw pad underneath
for _ in range(2):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=42)

# Sub continues
for _ in range(8):
    sub.add(F.add(-24), Duration.WHOLE, velocity=35)

# Drums light
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=85)
    kick.rest(Duration.DOTTED_HALF)
for _ in range(8):
    hats.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)

sine_pad.add(F.add(-12), Duration.WHOLE, velocity=35)
sine_pad.add(Ab.add(-12), Duration.WHOLE, velocity=32)
sine_pad.add(Db, Duration.WHOLE, velocity=35)
sine_pad.add(F.add(-12), Duration.WHOLE, velocity=32)
sine_pad.add(Ab.add(-12), Duration.WHOLE, velocity=35)
sine_pad.add(Db, Duration.WHOLE, velocity=32)
sine_pad.add(F.add(-12), Duration.WHOLE, velocity=30)
sine_pad.add(F.add(-12), Duration.WHOLE, velocity=28)

for _ in range(8):
    tri_pad.rest(Duration.WHOLE)
for _ in range(8):
    saw_pad.rest(Duration.WHOLE)
for _ in range(8):
    lead.rest(Duration.WHOLE)

# ── Bars 73-80: SAW + SQUARE DUET — harmony in thirds ──────────
# Two voices singing together, harmonized
duet_melody = [
    (F, Duration.QUARTER, 72), (G, Duration.QUARTER, 68),
    (Ab, Duration.HALF, 75),
    (Bb, Duration.QUARTER, 70), (Ab, Duration.EIGHTH, 65),
    (G, Duration.EIGHTH, 62), (F, Duration.HALF, 68),
    (Eb, Duration.QUARTER, 65), (F, Duration.QUARTER, 70),
    (G, Duration.HALF, 72),
    (Ab, Duration.WHOLE, 75),
    (Bb, Duration.QUARTER, 72), (C, Duration.QUARTER, 70),
    (Bb, Duration.QUARTER, 68), (Ab, Duration.QUARTER, 72),
    (G, Duration.HALF, 70), (F, Duration.HALF, 72),
    (F, Duration.WHOLE, 68),
    (None, Duration.WHOLE, 0),
]
# Harmony — a third below
duet_harmony = [
    (Db, Duration.QUARTER, 65), (Eb, Duration.QUARTER, 62),
    (F, Duration.HALF, 68),
    (G, Duration.QUARTER, 62), (F, Duration.EIGHTH, 58),
    (Eb, Duration.EIGHTH, 55), (Db, Duration.HALF, 60),
    (C, Duration.QUARTER, 58), (Db, Duration.QUARTER, 62),
    (Eb, Duration.HALF, 65),
    (F, Duration.WHOLE, 68),
    (G, Duration.QUARTER, 65), (Ab, Duration.QUARTER, 62),
    (G, Duration.QUARTER, 60), (F, Duration.QUARTER, 65),
    (Eb, Duration.HALF, 62), (Db, Duration.HALF, 65),
    (Db, Duration.WHOLE, 62),
    (None, Duration.WHOLE, 0),
]

saw.set(volume=0.4)
for note, dur, vel in duet_melody:
    if note is None:
        saw.rest(dur)
    else:
        saw.add(note, dur, velocity=vel)

sq.set(volume=0.3)
for note, dur, vel in duet_harmony:
    if note is None:
        sq.rest(dur)
    else:
        sq.add(note, dur, velocity=vel)

# Others hold drones or rest
for _ in range(8):
    sine.add(F.add(-12), Duration.WHOLE, velocity=35)
for _ in range(8):
    tri.rest(Duration.WHOLE)
for _ in range(8):
    fm.rest(Duration.WHOLE)
for _ in range(8):
    pwm.rest(Duration.WHOLE)
for _ in range(8):
    wf.rest(Duration.WHOLE)
for _ in range(2):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=38)
for _ in range(8):
    sub.add(F.add(-24), Duration.WHOLE, velocity=32)
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=90)
    kick.rest(Duration.QUARTER)
    kick.hit(K, Duration.QUARTER, velocity=82)
    kick.rest(Duration.QUARTER)
for _ in range(8):
    hats.rest(Duration.EIGHTH)
    hats.hit(CH, Duration.EIGHTH, velocity=48)
    hats.rest(Duration.EIGHTH)
    hats.hit(CH, Duration.EIGHTH, velocity=42)
    hats.rest(Duration.HALF)
for _ in range(8):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=75)
    snare.rest(Duration.HALF)
for _ in range(8):
    sine_pad.rest(Duration.WHOLE)
for _ in range(8):
    tri_pad.rest(Duration.WHOLE)
for _ in range(8):
    saw_pad.rest(Duration.WHOLE)
for _ in range(8):
    lead.rest(Duration.WHOLE)

# ── Bars 81-88: CANON — sine, triangle, PWM in staggered entries ─
# Same phrase, entering 2 beats apart — three voices in a round
canon_phrase = [
    (Ab, Duration.QUARTER, 72), (G, Duration.EIGHTH, 65),
    (F, Duration.EIGHTH, 62), (Eb, Duration.QUARTER, 68),
    (Db, Duration.QUARTER, 70),
    (C, Duration.QUARTER, 65), (Db, Duration.QUARTER, 68),
    (F, Duration.HALF, 72),
]

# Sine starts
for note, dur, vel in canon_phrase:
    sine.add(note, dur, velocity=vel)
for note, dur, vel in canon_phrase:
    sine.add(note, dur, velocity=max(20, vel - 10))

# Triangle enters 2 beats late
tri.rest(Duration.HALF)
for note, dur, vel in canon_phrase:
    tri.add(note, dur, velocity=max(20, vel - 5))
for note, dur, vel in canon_phrase:
    tri.add(note, dur, velocity=max(20, vel - 12))
tri.rest(Duration.HALF)

# PWM enters 4 beats late
pwm.rest(Duration.WHOLE)
for note, dur, vel in canon_phrase:
    pwm.add(note, dur, velocity=max(20, vel - 8))
for note, dur, vel in canon_phrase:
    pwm.add(note, dur, velocity=max(20, vel - 15))
pwm.rest(Duration.WHOLE)

# Others drone
for _ in range(8):
    sq.rest(Duration.WHOLE)
saw.set(volume=0.25)
for _ in range(8):
    saw.add(F.add(-12), Duration.WHOLE, velocity=30)
for _ in range(8):
    fm.rest(Duration.WHOLE)
for _ in range(8):
    wf.rest(Duration.WHOLE)
for _ in range(2):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=35)
for _ in range(8):
    sub.add(F.add(-24), Duration.WHOLE, velocity=30)
for _ in range(8):
    kick.rest(Duration.WHOLE)
for _ in range(8):
    hats.rest(Duration.WHOLE)
for _ in range(8):
    snare.rest(Duration.WHOLE)
for _ in range(8):
    sine_pad.rest(Duration.WHOLE)
tri_pad.add(Ab.add(-12), Duration.WHOLE, velocity=35)
tri_pad.add(Db, Duration.WHOLE, velocity=32)
for _ in range(6):
    tri_pad.rest(Duration.WHOLE)
for _ in range(8):
    saw_pad.rest(Duration.WHOLE)
for _ in range(8):
    lead.rest(Duration.WHOLE)

# ── Bars 89-96: FINALE — all 9 back together, then dissolve ────
# One last full statement, then they leave one by one

# Everyone plays their phrase one more time — fortissimo
sine.set(volume=0.45)
for _ in range(4):
    for note, dur, vel in sine_phrase:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=vel)
    for note, dur, vel in sine_phrase_b:
        if note is None:
            sine.rest(dur)
        else:
            sine.add(note, dur, velocity=max(20, vel - 15))

tri.set(volume=0.35)
for _ in range(4):
    for note, dur, vel in tri_phrase:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=vel)
    for note, dur, vel in tri_phrase_b:
        if note is None:
            tri.rest(dur)
        else:
            tri.add(note, dur, velocity=max(18, vel - 15))

sq.set(volume=0.25)
for _ in range(8):
    for note, dur, vel in sq_stab:
        if note is None:
            sq.rest(dur)
        else:
            sq.add(note, dur, velocity=max(20, vel - 15))

saw.set(volume=0.3)
for _ in range(4):
    for note in arp_a:
        saw.add(note, Duration.EIGHTH, velocity=55)
    for note in arp_b:
        saw.add(note, Duration.EIGHTH, velocity=52)

fm.set(volume=0.2)
for _ in range(8):
    for note, dur, vel in fm_phrase:
        if note is None:
            fm.rest(dur)
        else:
            fm.add(note, dur, velocity=max(18, vel - 18))

pwm.set(volume=0.18)
for _ in range(8):
    for note, dur, vel in pwm_phrase:
        if note is None:
            pwm.rest(dur)
        else:
            pwm.add(note, dur, velocity=max(15, vel - 20))

wf.set(volume=0.12)
for _ in range(8):
    for note, dur, vel in wf_phrase:
        if note is None:
            wf.rest(dur)
        else:
            wf.add(note, dur, velocity=max(15, vel - 22))

for _ in range(2):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=35)

for vel in [30, 25, 22, 18, 15, 12, 8, 0]:
    if vel > 0:
        sub.add(F.add(-24), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

for vel in [80, 68, 55, 42, 30, 18, 0, 0]:
    if vel > 0:
        for beat in range(4):
            kick.hit(K, Duration.QUARTER, velocity=vel)
    else:
        kick.rest(Duration.WHOLE)

for vel in [45, 38, 30, 22, 15, 0, 0, 0]:
    if vel > 0:
        for beat in range(4):
            hats.rest(Duration.EIGHTH)
            hats.hit(CH, Duration.EIGHTH, velocity=vel)
    else:
        hats.rest(Duration.WHOLE)

for vel in [70, 58, 45, 32, 20, 0, 0, 0]:
    if vel > 0:
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=vel)
        snare.rest(Duration.HALF)
    else:
        snare.rest(Duration.WHOLE)

for vel in [30, 25, 20, 15, 10, 5, 0, 0]:
    if vel > 0:
        sine_pad.add(F.add(-12), Duration.WHOLE, velocity=vel)
    else:
        sine_pad.rest(Duration.WHOLE)

for _ in range(8):
    tri_pad.rest(Duration.WHOLE)
for _ in range(8):
    saw_pad.rest(Duration.WHOLE)

for _ in range(8):
    lead.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 118")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing WAVEFORMS (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing WAVEFORMS...")
    play_score(score)
