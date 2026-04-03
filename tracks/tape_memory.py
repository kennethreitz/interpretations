"""
TAPE MEMORY — mellotron dreams surrounded by new synthesis.
Warm analog tape meets FM bells, wavefold grit, drifting oscillators.
Everything pytheory can do in one track.
Db minor, 90 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("Db", "minor")
s = key.scale  # Db Eb Fb Gb Ab Bbb Cb  (enharmonic: C# D# E F# G# A B)

Db = s[0]; Eb = s[1]; Fb = s[2]; Gb = s[3]
Ab = s[4]; Bbb = s[5]; Cb = s[6]
# Use enharmonic names for readability
F = Fb; Bb = Bbb; C = Cb

score = Score("4/4", bpm=90)

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT

prog = key.progression("i", "VII", "VI", "iv")
prog2 = key.progression("i", "v", "VI", "iv")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (80 bars, ~5:20):
#   Bars  1-8:   Mellotron alone — warm, warbly, the tape
#   Bars  9-16:  FM bells join — metallic shimmer above
#   Bars 17-24:  Drift oscillator — analog warmth underneath
#   Bars 25-32:  Crotales + granular texture — crystalline layers
#   Bars 33-40:  Drums + hard_sync bass — the groove arrives
#   Bars 41-48:  PWM lead melody — wobbling, alive
#   Bars 49-56:  Wavefold + ring_mod — the dark textures
#   Bars 57-64:  Everything together — the full palette
#   Bars 65-72:  Mellotron solo reprise — back to the heart
#   Bars 73-80:  Dissolve — tape runs out
# ═══════════════════════════════════════════════════════════════════

# ── MELLOTRON — the heart, warm tape chords ───────────────────
mello = score.part("mellotron", instrument="mellotron_flute", volume=0.4,
                   reverb=0.4, reverb_type="taj_mahal",
                   delay=0.12, delay_time=0.333, delay_feedback=0.2,
                   pan=-0.1, humanize=0.1)

# Bars 1-8: alone — whole note chords, the tape warbles
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=65)

# Bars 9-24: continues underneath everything
for _ in range(4):
    for chord in prog2:
        mello.add(chord, Duration.WHOLE, velocity=58)

# Bars 25-32: switches to arpeggiated
mello_arp = [Db, F, Ab, F, Db, Ab.add(-12), F.add(-12), Ab.add(-12)]
for _ in range(8):
    for note in mello_arp:
        mello.add(note, Duration.EIGHTH, velocity=55)

# Bars 33-56: chord pads under the groove
for _ in range(6):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=52)

# Bars 57-64: full — louder for the peak
mello.set(volume=0.45)
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=65)

# Bars 65-72: SOLO REPRISE — melody on mellotron
mello.set(volume=0.5)
mello_melody = [
    (Ab, Duration.HALF, 72), (Gb, Duration.QUARTER, 65),
    (F, Duration.QUARTER, 62),
    (Eb, Duration.HALF, 68), (Db, Duration.QUARTER, 62),
    (C.add(-12), Duration.QUARTER, 58),
    (Db, Duration.DOTTED_HALF, 70), (Eb, Duration.QUARTER, 65),
    (F, Duration.WHOLE, 68),
    (Ab, Duration.QUARTER, 72), (Bb, Duration.QUARTER, 68),
    (Ab, Duration.QUARTER, 65), (Gb, Duration.QUARTER, 62),
    (F, Duration.HALF, 68), (Eb, Duration.HALF, 65),
    (Db, Duration.WHOLE, 70),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in mello_melody:
    if note is None:
        mello.rest(dur)
    else:
        mello.add(note, dur, velocity=vel)

# Bars 73-80: tape runs out — fading, slowing feeling
for vel in [58, 50, 42, 35, 28, 20, 12, 5]:
    mello.add(Db, Duration.WHOLE, velocity=vel)

# ── FM — metallic bells, enters bar 9 ────────────────────────
fm = score.part("fm_bells", synth="fm", envelope="pluck", volume=0.25,
                reverb=0.35, reverb_type="cathedral",
                delay=0.2, delay_time=0.333, delay_feedback=0.25,
                pan=0.3)

for _ in range(8):
    fm.rest(Duration.WHOLE)

# Bars 9-16: bell-like blips — high, crystalline
fm_phrase = [
    (Ab, Duration.QUARTER, 65), (None, Duration.QUARTER, 0),
    (Bb, Duration.QUARTER, 60), (None, Duration.QUARTER, 0),
    (None, Duration.QUARTER, 0), (F, Duration.QUARTER, 62),
    (None, Duration.HALF, 0),
]
for _ in range(4):
    for note, dur, vel in fm_phrase:
        if note is None:
            fm.rest(dur)
        else:
            fm.add(note, dur, velocity=vel)

# Bars 17-56: continues, evolving
for _ in range(20):
    for note, dur, vel in fm_phrase:
        if note is None:
            fm.rest(dur)
        else:
            fm.add(note, dur, velocity=vel)

# Bars 57-64: peak
fm.set(volume=0.3)
for _ in range(4):
    for note, dur, vel in fm_phrase:
        if note is None:
            fm.rest(dur)
        else:
            fm.add(note, dur, velocity=min(80, vel + 8))

# Bars 65-80: fading
for vel in [55, 48, 42, 35, 28, 22, 15, 10, 8, 5, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        fm.add(Ab, Duration.QUARTER, velocity=vel)
        fm.rest(Duration.DOTTED_HALF)
    else:
        fm.rest(Duration.WHOLE)

# ── DRIFT — analog warmth, enters bar 17 ─────────────────────
drift = score.part("drift", synth="drift", envelope="pad", volume=0.18,
                   reverb=0.4, reverb_type="taj_mahal",
                   chorus=0.3, chorus_rate=0.04, chorus_depth=0.012,
                   pan=-0.25)

for _ in range(16):
    drift.rest(Duration.WHOLE)

# Bars 17-72: slow drifting drone — the analog warmth
for _ in range(56):
    drift.add(Db.add(-12), Duration.WHOLE, velocity=42)

# Bars 73-80: fading
for vel in [35, 28, 22, 15, 10, 6, 3, 0]:
    if vel > 0:
        drift.add(Db.add(-12), Duration.WHOLE, velocity=vel)
    else:
        drift.rest(Duration.WHOLE)

# ── CROTALES — crystalline, enters bar 25 ─────────────────────
crot = score.part("crotales", instrument="crotales", volume=0.2,
                  reverb=0.5, reverb_type="taj_mahal",
                  delay=0.2, delay_time=0.667, delay_feedback=0.25,
                  pan=0.35)

for _ in range(24):
    crot.rest(Duration.WHOLE)

# Bars 25-32: sparse strikes — like tiny bells in the distance
crot_strikes = {25: (Ab, 58), 27: (F, 52), 29: (Bb, 55), 31: (Db, 50)}
for bar in range(25, 33):
    if bar in crot_strikes:
        note, vel = crot_strikes[bar]
        crot.add(note, Duration.WHOLE, velocity=vel)
    else:
        crot.rest(Duration.WHOLE)

# Bars 33-56: continues sparse
for bar in range(33, 57):
    if bar % 4 == 1:
        crot.add(Ab, Duration.WHOLE, velocity=48)
    elif bar % 6 == 0:
        crot.add(F, Duration.WHOLE, velocity=45)
    else:
        crot.rest(Duration.WHOLE)

# Bars 57-80: fading
for bar in range(57, 81):
    if bar % 5 == 0 and bar < 73:
        crot.add(Db, Duration.WHOLE, velocity=max(25, 50 - (bar - 57)))
    else:
        crot.rest(Duration.WHOLE)

# ── GRANULAR — texture, enters bar 25 ─────────────────────────
grain = score.part("grain", instrument="granular_texture", volume=0.1,
                   reverb=0.45, reverb_type="taj_mahal",
                   delay=0.1, delay_time=0.5, delay_feedback=0.15,
                   pan=-0.35)

for _ in range(24):
    grain.rest(Duration.WHOLE)

# Bars 25-64: evolving texture — slowly shifting notes
grain_notes = [Db, F, Ab, Eb, Bb, Gb, F, Db]
for note in grain_notes:
    for _ in range(5):
        grain.add(note, Duration.WHOLE, velocity=35)

# Bars 65-80: fading
for vel in [30, 25, 22, 18, 15, 12, 8, 5, 0, 0, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        grain.add(Db, Duration.WHOLE, velocity=vel)
    else:
        grain.rest(Duration.WHOLE)

# ── HARD_SYNC — bass, enters bar 33 ──────────────────────────
sync = score.part("hard_sync", synth="hard_sync", volume=0.3,
                  lowpass=800,
                  distortion=0.15, distortion_drive=2.0,
                  reverb=0.15, reverb_type="spring",
                  delay=0.08, delay_time=0.333, delay_feedback=0.1,
                  pan=0.1)

for _ in range(32):
    sync.rest(Duration.WHOLE)

# Bars 33-64: bass line — hard_sync has that aggressive buzz
roots = [Db.add(-12), Bb.add(-24), Gb.add(-12), Ab.add(-12)]
for _ in range(8):
    for root in roots:
        sync.add(root, Duration.HALF, velocity=72)
        sync.rest(Duration.HALF)

# Bars 65-80: fading
for vel in [62, 52, 42, 32, 22, 15, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        sync.add(Db.add(-12), Duration.HALF, velocity=vel)
        sync.rest(Duration.HALF)
    else:
        sync.rest(Duration.WHOLE)

# ── DRUMS — enters bar 33 ────────────────────────────────────
kick = score.part("kick", volume=0.55, humanize=0.03)
snare = score.part("snare", volume=0.35, humanize=0.04,
                   reverb=0.15, delay=0.05, delay_time=0.333,
                   delay_feedback=0.08, pan=0.05)
hats = score.part("hats", volume=0.2, pan=0.15, humanize=0.04)

for _ in range(32):
    kick.rest(Duration.WHOLE)
    snare.rest(Duration.WHOLE)
    hats.rest(Duration.WHOLE)

# Bars 33-64: groove
for _ in range(32):
    kick.hit(K, Duration.QUARTER, velocity=98)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=82)
    kick.hit(K, Duration.QUARTER, velocity=92)
    kick.rest(Duration.QUARTER)

    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=88)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=90)

    for beat in range(4):
        hats.hit(CH, Duration.EIGHTH, velocity=58)
        hats.hit(CH, Duration.EIGHTH, velocity=35)

# Bars 65-72: lighter under mellotron solo
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=78)
    kick.rest(Duration.DOTTED_HALF)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=65)
    snare.rest(Duration.HALF)
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=42)

# Bars 73-80: fading
for vel in [68, 55, 42, 30, 20, 0, 0, 0]:
    if vel > 0:
        kick.hit(K, Duration.QUARTER, velocity=vel)
        kick.rest(Duration.DOTTED_HALF)
        snare.rest(Duration.WHOLE)
        hats.hit(CH, Duration.QUARTER, velocity=max(15, vel - 30))
        hats.rest(Duration.DOTTED_HALF)
    else:
        kick.rest(Duration.WHOLE)
        snare.rest(Duration.WHOLE)
        hats.rest(Duration.WHOLE)

# ── PWM — lead melody, enters bar 41 ─────────────────────────
pwm = score.part("pwm_lead", synth="pwm", volume=0.35,
                 reverb=0.25, reverb_decay=1.2,
                 delay=0.15, delay_time=0.333, delay_feedback=0.2,
                 pan=-0.2, humanize=0.06)

for _ in range(40):
    pwm.rest(Duration.WHOLE)

# Bars 41-48: melody — the PWM wobble makes each note alive
pwm_melody = [
    (Ab, Duration.HALF, 72), (Gb, Duration.QUARTER, 65),
    (F, Duration.QUARTER, 68),
    (Eb, Duration.HALF, 70), (F, Duration.QUARTER, 65),
    (Gb, Duration.QUARTER, 68),
    (Ab, Duration.DOTTED_HALF, 75), (Gb, Duration.QUARTER, 68),
    (F, Duration.WHOLE, 70),
    (Eb, Duration.QUARTER, 68), (F, Duration.QUARTER, 72),
    (Gb, Duration.HALF, 70),
    (Ab, Duration.QUARTER, 75), (Bb, Duration.QUARTER, 72),
    (Ab, Duration.HALF, 70),
    (Gb, Duration.HALF, 68), (F, Duration.HALF, 72),
    (Db, Duration.WHOLE, 70),
]
for note, dur, vel in pwm_melody:
    pwm.add(note, dur, velocity=vel)

# Bars 49-56: repeats with variation
for note, dur, vel in pwm_melody:
    pwm.add(note, dur, velocity=max(30, vel - 5))

# Bars 57-64: peak — louder
pwm.set(volume=0.4)
for note, dur, vel in pwm_melody:
    pwm.add(note, dur, velocity=min(90, vel + 5))

# Bars 65-80: fading
for vel in [60, 52, 44, 38, 30, 22, 15, 8, 0, 0, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        pwm.add(Db, Duration.HALF, velocity=vel)
        pwm.rest(Duration.HALF)
    else:
        pwm.rest(Duration.WHOLE)

# ── WAVEFOLD — dark texture, enters bar 49 ───────────────────
wfold = score.part("wavefold", synth="wavefold", envelope="pluck", volume=0.15,
                   lowpass=3000,
                   reverb=0.2, reverb_decay=1.0,
                   delay=0.1, delay_time=0.167, delay_feedback=0.15,
                   pan=0.25)

for _ in range(48):
    wfold.rest(Duration.WHOLE)

# Bars 49-64: dark rhythmic texture — the grit
wf_pattern = [
    (Db, Duration.SIXTEENTH, 62), (None, Duration.SIXTEENTH, 0),
    (F, Duration.SIXTEENTH, 58), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (Ab, Duration.SIXTEENTH, 60), (None, Duration.SIXTEENTH, 0),
    (None, Duration.EIGHTH, 0),
    (Eb, Duration.SIXTEENTH, 55), (None, Duration.SIXTEENTH, 0),
    (None, Duration.QUARTER, 0),
]
for _ in range(16):
    for note, dur, vel in wf_pattern:
        if note is None:
            wfold.rest(dur)
        else:
            wfold.add(note, dur, velocity=vel)

# Bars 65-80: fading
for rep in range(16):
    off = rep * -4
    for note, dur, vel in wf_pattern:
        if note is None:
            wfold.rest(dur)
        else:
            wfold.add(note, dur, velocity=max(12, vel + off))

# ── RING MOD — alien texture, enters bar 49 ──────────────────
ring = score.part("ring_mod", synth="ring_mod", envelope="pluck", volume=0.1,
                  reverb=0.3, reverb_type="cathedral",
                  delay=0.15, delay_time=0.5, delay_feedback=0.2,
                  pan=-0.4)

for _ in range(48):
    ring.rest(Duration.WHOLE)

# Bars 49-64: sparse alien blips — inharmonic, unsettling beauty
ring_hits = {49: (Ab, 50), 51: (F, 45), 53: (Db, 48), 55: (Eb, 42),
             57: (Ab, 52), 59: (Bb, 48), 61: (F, 50), 63: (Db, 45)}
for bar in range(49, 65):
    if bar in ring_hits:
        note, vel = ring_hits[bar]
        ring.add(note, Duration.WHOLE, velocity=vel)
    else:
        ring.rest(Duration.WHOLE)

# Bars 65-80: fading
for vel in [38, 32, 28, 22, 18, 12, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        ring.add(Db, Duration.WHOLE, velocity=vel)
    else:
        ring.rest(Duration.WHOLE)

# ── SINGING BOWL — transition markers ─────────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.3,
                  reverb=0.7, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.667, delay_feedback=0.2,
                  pan=0.2)

section_bars = {1: 62, 9: 58, 17: 55, 25: 60, 33: 65, 41: 58,
                49: 62, 57: 68, 65: 60, 73: 50}
for bar in range(1, 81):
    if bar in section_bars:
        bowl.add(Db.add(-24), Duration.WHOLE, velocity=section_bars[bar])
    else:
        bowl.rest(Duration.WHOLE)

# ── TINGSHA — crystalline accents ─────────────────────────────
tingsha = score.part("tingsha", instrument="tingsha", volume=0.18,
                     reverb=0.5, reverb_type="taj_mahal",
                     delay=0.2, delay_time=1.0, delay_feedback=0.2,
                     pan=-0.3)

tingsha_bars = {4: (Ab, 50), 12: (F, 45), 20: (Db, 48),
                28: (Bb, 45), 36: (Ab, 50), 52: (F, 45),
                60: (Db, 52), 68: (Ab, 48)}
for bar in range(1, 81):
    if bar in tingsha_bars:
        note, vel = tingsha_bars[bar]
        tingsha.add(note, Duration.WHOLE, velocity=vel)
    else:
        tingsha.rest(Duration.WHOLE)

# ── THEREMIN — emotional peak solo, bars 57-64 ────────────────
theremin = score.part("theremin", instrument="theremin", volume=0.35,
                      reverb=0.35, reverb_type="taj_mahal",
                      delay=0.15, delay_time=0.333, delay_feedback=0.2,
                      pan=0.15, humanize=0.06)

for _ in range(56):
    theremin.rest(Duration.WHOLE)

# Bars 57-58: entrance — rising from the texture, one held note
theremin.add(Ab, Duration.WHOLE, velocity=62, bend=0.5)
theremin.add(Db, Duration.HALF, velocity=68, bend=-0.25)
theremin.add(Eb, Duration.HALF, velocity=65)

# Bars 59-60: the solo opens up — singing, bending
theremin.add(Ab, Duration.QUARTER, velocity=75, bend=0.5)
theremin.add(Gb, Duration.EIGHTH, velocity=68)
theremin.add(F, Duration.EIGHTH, velocity=65)
theremin.add(Eb, Duration.HALF, velocity=72, bend=-0.25)
theremin.add(F, Duration.QUARTER, velocity=70, bend=0.5)
theremin.add(Ab, Duration.QUARTER, velocity=78)
theremin.add(Bb, Duration.HALF, velocity=80, bend=-0.5)
theremin.add(Ab, Duration.HALF, velocity=72)

# Bars 61-62: climax — the highest, most exposed moment
theremin.add(Bb, Duration.QUARTER, velocity=82, bend=1.0)
theremin.add(Ab, Duration.QUARTER, velocity=78, bend=-0.5)
theremin.add(Gb, Duration.QUARTER, velocity=72, bend=0.5)
theremin.add(Ab, Duration.QUARTER, velocity=80, bend=1.0)
# Descending — the release
theremin.add(Gb, Duration.QUARTER, velocity=75, bend=0.25)
theremin.add(F, Duration.QUARTER, velocity=70)
theremin.add(Eb, Duration.QUARTER, velocity=65, bend=-0.25)
theremin.add(Db, Duration.QUARTER, velocity=62)

# Bars 63-64: fading — one last held note
theremin.add(Db, Duration.WHOLE, velocity=58, bend=0.15)
theremin.add(Db, Duration.WHOLE, velocity=42)

# Bars 65-80: gone
for _ in range(16):
    theremin.rest(Duration.WHOLE)

# ── SUB — enters bar 33 ──────────────────────────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.45,
                 lowpass=150, distortion=0.12, distortion_drive=2.0,
                 sub_osc=0.4, sidechain=0.3)

for _ in range(32):
    sub.rest(Duration.WHOLE)

sub_roots = [Db.add(-24), Bb.add(-24), Gb.add(-24), Ab.add(-24)]
for _ in range(8):
    for root in sub_roots:
        sub.add(root, Duration.WHOLE, velocity=35)

# Bars 65-80: just the root, fading
for vel in [32, 28, 25, 22, 18, 15, 12, 8, 5, 0, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        sub.add(Db.add(-24), Duration.WHOLE, velocity=vel)
    else:
        sub.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 90")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing TAPE MEMORY (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing TAPE MEMORY...")
    play_score(score)
