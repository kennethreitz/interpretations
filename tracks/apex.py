"""
APEX — beast mode's meaner sibling.
Koto hook instead of sitar. Wavefold bass. Faster. Harder.
Eb minor, 140 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("Eb", "minor")
s = key.scale  # Eb F Gb Ab Bb Cb Db

Eb = s[0]; F  = s[1]; Gb = s[2]; Ab = s[3]
Bb = s[4]; Cb = s[5]; Db = s[6]

score = Score("4/4", bpm=140)

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT
CL = DrumSound.CLAP

prog = key.progression("i", "VII", "VI", "iv")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (80 bars, ~3:26):
#   Bars  1-4:   808 + timpani hit — the warning
#   Bars  5-8:   Koto hook drops — you weren't ready
#   Bars  9-16:  Drums slam in — full trap
#   Bars 17-24:  Wavefold bass — the grind underneath
#   Bars 25-32:  Mellotron strings — the dark beauty
#   Bars 33-40:  Breakdown — 808 slides, half time, tension
#   Bars 41-48:  BUILD — timpani rolls, hats accelerate
#   Bars 49-56:  APEX — everything maxed, koto shreds
#   Bars 57-64:  Second hook — different melody, harder
#   Bars 65-72:  Last drop — mellotron + timpani + all
#   Bars 73-80:  Outro — 808 alone, descending
# ═══════════════════════════════════════════════════════════════════

# ── 808 — massive, pitch slides ───────────────────────────────
sub = score.part("808", synth="sine", envelope="pad", volume=0.6,
                 lowpass=220, distortion=0.25, distortion_drive=3.5,
                 sub_osc=0.5, saturation=0.4, sidechain=0.45)

# Bars 1-4: alone — announces itself
sub.add(Eb.add(-24), Duration.WHOLE, velocity=38)
sub.add(Eb.add(-24), Duration.HALF, velocity=40)
sub.add(Db.add(-24), Duration.HALF, velocity=38)
sub.add(Eb.add(-24), Duration.WHOLE, velocity=42)
sub.add(Cb.add(-24), Duration.HALF, velocity=40)
sub.add(Eb.add(-24), Duration.HALF, velocity=42)

# Bars 5-72: pattern
bass_pattern = [
    (Eb.add(-24), 40), (Db.add(-24), 38),
    (Cb.add(-24), 40), (Eb.add(-24), 42),
]
for _ in range(17):
    for root, vel in bass_pattern:
        sub.add(root, Duration.WHOLE, velocity=vel)

# Bars 73-80: descending slide out
for root, vel in [(Eb.add(-24), 38), (Db.add(-24), 35),
                  (Cb.add(-24), 32), (Bb.add(-24), 28),
                  (Ab.add(-24), 25), (Gb.add(-24), 22),
                  (F.add(-24), 18), (Eb.add(-36), 12)]:
    sub.add(root, Duration.WHOLE, velocity=vel)

# ── TIMPANI — the war drum ───────────────────────────────────
timp = score.part("timpani", instrument="timpani", volume=0.4,
                  reverb=0.25, reverb_type="cathedral",
                  delay=0.06, delay_time=0.214, delay_feedback=0.08,
                  pan=-0.05)

# Bar 1: massive hit with 808
timp.add(Eb.add(-12), Duration.WHOLE, velocity=85)
for _ in range(7):
    timp.rest(Duration.WHOLE)

# Bars 9-32: sparse accents
for bar in range(24):
    if bar % 4 == 0:
        timp.add(Eb.add(-12), Duration.QUARTER, velocity=75)
        timp.rest(Duration.DOTTED_HALF)
    else:
        timp.rest(Duration.WHOLE)

# Bars 33-40: breakdown — half time hits
for _ in range(8):
    timp.add(Eb.add(-12), Duration.HALF, velocity=78)
    timp.rest(Duration.HALF)

# Bars 41-48: BUILD — 16th note rolls crescendo
for bar in range(8):
    if bar < 4:
        for i in range(16):
            timp.add(Eb.add(-12), Duration.SIXTEENTH, velocity=min(92, 50 + bar * 5 + i * 2))
    else:
        for i in range(16):
            timp.add(Eb.add(-12), Duration.SIXTEENTH, velocity=min(100, 65 + i * 2))

# Bars 49-72: accents on 1 + rolls every 4
for bar in range(24):
    if bar % 4 == 3:
        for i in range(16):
            timp.add(Eb.add(-12), Duration.SIXTEENTH, velocity=min(95, 55 + i * 3))
    else:
        timp.add(Eb.add(-12), Duration.QUARTER, velocity=72)
        timp.rest(Duration.DOTTED_HALF)

# Bars 73-80: fading
for vel in [62, 50, 38, 28, 18, 0, 0, 0]:
    if vel > 0:
        timp.add(Eb.add(-12), Duration.QUARTER, velocity=vel)
        timp.rest(Duration.DOTTED_HALF)
    else:
        timp.rest(Duration.WHOLE)

# ── KOTO — the hook, enters bar 5 ────────────────────────────
koto = score.part("koto", instrument="koto", volume=0.5,
                  reverb=0.2, reverb_type="taj_mahal",
                  delay=0.12, delay_time=0.214, delay_feedback=0.2,
                  pan=-0.25, humanize=0.08)

for _ in range(4):
    koto.rest(Duration.WHOLE)

# The hook — dark, pentatonic, catchy
hook = [
    (Eb, Duration.EIGHTH, 82), (Gb, Duration.EIGHTH, 75),
    (Ab, Duration.QUARTER, 85), (Bb, Duration.EIGHTH, 72),
    (Ab, Duration.EIGHTH, 70), (Gb, Duration.QUARTER, 78),
    (Eb, Duration.EIGHTH, 80), (None, Duration.EIGHTH, 0),
    (Db, Duration.EIGHTH, 70), (Eb, Duration.EIGHTH, 78),
    (None, Duration.QUARTER, 0),
    (Gb, Duration.EIGHTH, 72), (F, Duration.EIGHTH, 68),
    (Eb, Duration.HALF, 80),
]

# Bars 5-8: hook alone over 808
for _ in range(2):
    for note, dur, vel in hook:
        if note is None:
            koto.rest(dur)
        else:
            koto.add(note, dur, velocity=vel)

# Bars 9-24: hook continues under drums
for _ in range(8):
    for note, dur, vel in hook:
        if note is None:
            koto.rest(dur)
        else:
            koto.add(note, dur, velocity=max(40, vel - 5))

# Bars 25-32: quieter under mellotron
koto.set(volume=0.35)
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            koto.rest(dur)
        else:
            koto.add(note, dur, velocity=max(35, vel - 15))

# Bars 33-40: silent — breakdown
for _ in range(8):
    koto.rest(Duration.WHOLE)

# Bars 41-48: builds back
koto.set(volume=0.4)
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            koto.rest(dur)
        else:
            koto.add(note, dur, velocity=vel)

# Bars 49-56: APEX — koto shreds, 16th arps + 32nd fills
koto.set(volume=0.6)
arp_i = [Eb, Gb, Bb, Gb, Eb, Bb.add(-12), Gb.add(-12), Bb.add(-12)]
arp_vi = [Cb.add(-12), Eb, Gb, Eb, Cb.add(-12), Gb.add(-12), Eb.add(-12), Gb.add(-12)]

def koto_arp(notes, base_vel):
    vels = [base_vel, base_vel-12, base_vel-8, base_vel+5,
            base_vel-5, base_vel-15, base_vel-18, base_vel-10]
    for note, vel in zip(notes, vels):
        koto.add(note, Duration.SIXTEENTH, velocity=max(35, vel))

for bar in range(8):
    if bar % 4 == 3:
        # 32nd shred
        for note in [Eb, F, Gb, Ab, Bb, Cb, Db, Eb.add(12),
                     Db, Cb, Bb, Ab, Gb, F, Eb, F]:
            koto.add(note, 0.125, velocity=105)
    else:
        koto_arp(arp_i if bar % 2 == 0 else arp_vi, 90)
        koto_arp(arp_i if bar % 2 == 0 else arp_vi, 85)

# Bars 57-64: second hook — different melody, higher
hook2 = [
    (Bb, Duration.EIGHTH, 85), (Ab, Duration.EIGHTH, 78),
    (Gb, Duration.QUARTER, 82), (Ab, Duration.EIGHTH, 75),
    (Bb, Duration.EIGHTH, 80), (Cb, Duration.QUARTER, 85),
    (Bb, Duration.EIGHTH, 78), (None, Duration.EIGHTH, 0),
    (Ab, Duration.EIGHTH, 72), (Gb, Duration.EIGHTH, 75),
    (None, Duration.QUARTER, 0),
    (Eb, Duration.QUARTER, 80),
    (Eb, Duration.HALF, 78),
]
koto.set(volume=0.55)
for _ in range(4):
    for note, dur, vel in hook2:
        if note is None:
            koto.rest(dur)
        else:
            koto.add(note, dur, velocity=vel)

# Bars 65-72: hook 1 returns
koto.set(volume=0.5)
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            koto.rest(dur)
        else:
            koto.add(note, dur, velocity=vel)

# Bars 73-80: fading
for _ in range(4):
    for note, dur, vel in hook:
        if note is None:
            koto.rest(dur)
        else:
            koto.add(note, dur, velocity=max(20, vel - 30))
for _ in range(4):
    koto.rest(Duration.WHOLE)

# ── KICK — hard ──────────────────────────────────────────────
kick = score.part("kick", volume=0.9, humanize=0.02,
                  distortion=0.12, distortion_drive=2.0)

for _ in range(8):
    kick.rest(Duration.WHOLE)

# Bars 9-32: trap kick
for _ in range(24):
    kick.hit(K, Duration.QUARTER, velocity=120)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=100)
    kick.hit(K, Duration.QUARTER, velocity=115)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=98)

# Bars 33-40: half time
for _ in range(8):
    kick.hit(K, Duration.HALF, velocity=118)
    kick.rest(Duration.HALF)

# Bars 41-48: builds back
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=118)
    kick.hit(K, Duration.EIGHTH, velocity=102)
    kick.hit(K, Duration.EIGHTH, velocity=95)
    kick.hit(K, Duration.QUARTER, velocity=115)
    kick.hit(K, Duration.EIGHTH, velocity=105)
    kick.hit(K, Duration.EIGHTH, velocity=110)

# Bars 49-72: full power
for _ in range(24):
    kick.hit(K, Duration.QUARTER, velocity=122)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=105)
    kick.hit(K, Duration.QUARTER, velocity=118)
    kick.rest(Duration.EIGHTH)
    kick.hit(K, Duration.EIGHTH, velocity=102)

# Bars 73-80: fading
for vel in [112, 98, 82, 65, 48, 32, 18, 0]:
    if vel > 0:
        kick.hit(K, Duration.QUARTER, velocity=vel)
        kick.rest(Duration.DOTTED_HALF)
    else:
        kick.rest(Duration.WHOLE)

# ── SNARE — crack + clap layer ────────────────────────────────
snare = score.part("snare", volume=0.5, humanize=0.03,
                   reverb=0.1, distortion=0.08,
                   delay=0.04, delay_time=0.214, delay_feedback=0.06,
                   pan=0.05)
clap = score.part("clap", volume=0.2, reverb=0.12,
                  delay=0.05, delay_time=0.214, delay_feedback=0.08,
                  pan=-0.08)

for _ in range(8):
    snare.rest(Duration.WHOLE)
    clap.rest(Duration.WHOLE)

for _ in range(24):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=110)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=112)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=82)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=85)

# Breakdown
for _ in range(8):
    snare.rest(Duration.HALF)
    snare.hit(S, Duration.HALF, velocity=108)
    clap.rest(Duration.WHOLE)

# Build — snare rolls
for bar in range(8):
    if bar >= 6:
        for i in range(16):
            snare.hit(S, Duration.SIXTEENTH, velocity=min(118, 72 + i * 3))
        clap.rest(Duration.WHOLE)
    else:
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=110)
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=112)
        clap.rest(Duration.QUARTER)
        clap.hit(CL, Duration.QUARTER, velocity=82)
        clap.rest(Duration.QUARTER)
        clap.hit(CL, Duration.QUARTER, velocity=85)

# Full power
for _ in range(24):
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=115)
    snare.rest(Duration.QUARTER)
    snare.hit(S, Duration.QUARTER, velocity=118)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=85)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=88)

# Fading
for vel in [105, 90, 72, 55, 38, 22, 0, 0]:
    if vel > 0:
        snare.rest(Duration.QUARTER)
        snare.hit(S, Duration.QUARTER, velocity=vel)
        snare.rest(Duration.HALF)
        clap.rest(Duration.WHOLE)
    else:
        snare.rest(Duration.WHOLE)
        clap.rest(Duration.WHOLE)

# ── HATS — trap ──────────────────────────────────────────────
hats = score.part("hats", volume=0.28, pan=0.25, humanize=0.04)

for _ in range(8):
    hats.rest(Duration.WHOLE)

# 16ths with evolving patterns
for _ in range(24):
    hats.hit(CH, Duration.SIXTEENTH, velocity=75)
    hats.hit(CH, Duration.SIXTEENTH, velocity=40)
    hats.hit(OH, Duration.SIXTEENTH, velocity=62)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(CH, Duration.SIXTEENTH, velocity=72)
    hats.hit(CH, Duration.SIXTEENTH, velocity=42)
    hats.hit(CH, Duration.SIXTEENTH, velocity=58)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(CH, Duration.SIXTEENTH, velocity=75)
    hats.hit(CH, Duration.SIXTEENTH, velocity=40)
    hats.hit(CH, Duration.SIXTEENTH, velocity=55)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)
    hats.hit(OH, Duration.SIXTEENTH, velocity=60)
    hats.hit(CH, Duration.SIXTEENTH, velocity=38)
    hats.hit(CH, Duration.SIXTEENTH, velocity=52)
    hats.hit(CH, Duration.SIXTEENTH, velocity=35)

# Breakdown — sparse
for _ in range(8):
    hats.hit(CH, Duration.QUARTER, velocity=48)
    hats.rest(Duration.DOTTED_HALF)

# Build — 32nd rolls
for bar in range(8):
    if bar % 2 == 1:
        for i in range(32):
            hats.hit(CH, 0.125, velocity=min(82, 38 + i * 2))
    else:
        for beat in range(4):
            hats.hit(CH, Duration.SIXTEENTH, velocity=72)
            hats.hit(CH, Duration.SIXTEENTH, velocity=40)
            hats.hit(CH, Duration.SIXTEENTH, velocity=58)
            hats.hit(CH, Duration.SIXTEENTH, velocity=35)

# Peak
for bar in range(24):
    if bar % 4 == 3:
        for i in range(32):
            hats.hit(CH, 0.125, velocity=min(85, 40 + i * 2))
    else:
        hats.hit(CH, Duration.SIXTEENTH, velocity=78)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(OH, Duration.SIXTEENTH, velocity=65)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(CH, Duration.SIXTEENTH, velocity=75)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)
        hats.hit(CH, Duration.SIXTEENTH, velocity=58)
        hats.hit(CH, Duration.SIXTEENTH, velocity=42)
        hats.hit(CH, Duration.SIXTEENTH, velocity=78)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=35)
        hats.hit(OH, Duration.SIXTEENTH, velocity=62)
        hats.hit(CH, Duration.SIXTEENTH, velocity=38)
        hats.hit(CH, Duration.SIXTEENTH, velocity=55)
        hats.hit(CH, Duration.SIXTEENTH, velocity=40)

# Fading
for vel in [62, 52, 42, 32, 22, 12, 0, 0]:
    if vel > 0:
        for beat in range(4):
            hats.hit(CH, Duration.EIGHTH, velocity=vel)
            hats.hit(CH, Duration.EIGHTH, velocity=max(12, vel - 25))
    else:
        hats.rest(Duration.WHOLE)

# ── WAVEFOLD BASS — the grind, enters bar 17 ──────────────────
wf = score.part("wavefold_bass", synth="wavefold", volume=0.35,
                lowpass=1500,
                distortion=0.2, distortion_drive=3.0,
                saturation=0.5, legato=True, glide=0.01,
                reverb=0.1, reverb_type="spring",
                delay=0.08, delay_time=0.214, delay_feedback=0.1,
                sidechain=0.35, pan=0.2)

for _ in range(16):
    wf.rest(Duration.WHOLE)

wf_line = [
    (Eb.add(-12), Duration.SIXTEENTH, 95), (None, Duration.SIXTEENTH, 0),
    (Eb.add(-12), Duration.SIXTEENTH, 65), (Gb.add(-12), Duration.SIXTEENTH, 60),
    (Eb.add(-12), Duration.SIXTEENTH, 92), (None, Duration.SIXTEENTH, 0),
    (Db.add(-12), Duration.EIGHTH, 58),
    (Eb.add(-12), Duration.SIXTEENTH, 98), (Bb.add(-24), Duration.SIXTEENTH, 62),
    (Eb.add(-12), Duration.SIXTEENTH, 68), (None, Duration.SIXTEENTH, 0),
    (Cb.add(-12), Duration.EIGHTH, 55),
    (Eb.add(-12), Duration.EIGHTH, 90),
]

# Bars 17-32
for _ in range(16):
    for note, dur, vel in wf_line:
        if note is None:
            wf.rest(dur)
        else:
            wf.add(note, dur, velocity=vel)

# Breakdown — silent
for _ in range(8):
    wf.rest(Duration.WHOLE)

# Build + peak
for _ in range(32):
    for note, dur, vel in wf_line:
        if note is None:
            wf.rest(dur)
        else:
            wf.add(note, dur, velocity=min(110, vel + 5))

# Fading
for _ in range(4):
    for note, dur, vel in wf_line:
        if note is None:
            wf.rest(dur)
        else:
            wf.add(note, dur, velocity=max(25, vel - 25))
for _ in range(4):
    wf.rest(Duration.WHOLE)

# ── MELLOTRON STRINGS — dark beauty, enters bar 25 ────────────
mello = score.part("mellotron", instrument="mellotron_strings", volume=0.22,
                   reverb=0.35, reverb_type="taj_mahal",
                   pan=-0.15)

for _ in range(24):
    mello.rest(Duration.WHOLE)

# Bars 25-32: dark pad
for _ in range(2):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=52)

# Bars 33-48: continues through breakdown and build
for _ in range(4):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=48)

# Bars 49-72: peak + drops
mello.set(volume=0.28)
for _ in range(6):
    for chord in prog:
        mello.add(chord, Duration.WHOLE, velocity=55)

# Fading
for vel in [48, 40, 32, 25, 18, 12, 0, 0]:
    if vel > 0:
        mello.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        mello.rest(Duration.WHOLE)

# ── SINGING BOWL — marks sections ─────────────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.22,
                  reverb=0.45, reverb_type="taj_mahal",
                  delay=0.12, delay_time=0.428, delay_feedback=0.15,
                  pan=0.15)

markers = {1: 62, 5: 55, 9: 58, 25: 60, 33: 52, 41: 58, 49: 65, 57: 58, 65: 62}
for bar in range(1, 81):
    if bar in markers:
        bowl.add(Eb.add(-24), Duration.WHOLE, velocity=markers[bar])
    else:
        bowl.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 140")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing APEX (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing APEX...")
    play_score(score)
