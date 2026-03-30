"""
ECHO CHAMBER — deep dub. Spring reverb, delay throws, space between the hits.
King Tubby meets the studio at midnight. Every note echoes into infinity.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("E", "minor")
s = key.scale
prog = key.progression("i", "iv", "VII", "i")

E  = s[0]; Fs = s[1]; G  = s[2]; A  = s[3]
B  = s[4]; C  = s[5]; D  = s[6]

score = Score("4/4", bpm=72)

K  = DrumSound.KICK
S  = DrumSound.SNARE
RS = DrumSound.RIMSHOT
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~5.5 min at 72 BPM):
#   Bars  1-8:   Bass + kick, sparse, establishing the weight
#   Bars  9-16:  Skank guitar enters, rimshots
#   Bars 17-32:  Melodica melody, delay throws on everything
#   Bars 33-48:  Peak — horns, full groove, spring reverb madness
#   Bars 49-56:  Breakdown — just bass and delay echoes
#   Bars 57-64:  Outro — everything dissolving into reverb
# ═══════════════════════════════════════════════════════════════════

# ── KICK + SNARE — the one drop ─────────────────────────────────
drums = score.part("drums", volume=0.4, humanize=0.1)

# Bars 1-8: just kick on 1 and 3, sparse
for _ in range(8):
    drums.hit(K, Duration.QUARTER, velocity=105)
    drums.rest(Duration.QUARTER)
    drums.hit(K, Duration.QUARTER, velocity=95)
    drums.rest(Duration.QUARTER)

# Bars 9-48: one drop — kick on 1, rimshot on 3
for _ in range(40):
    drums.hit(K, Duration.QUARTER, velocity=108)
    drums.rest(Duration.QUARTER)
    drums.hit(RS, Duration.QUARTER, velocity=88)
    drums.rest(Duration.QUARTER)

# Bars 49-56: stripped back
for _ in range(8):
    drums.hit(K, Duration.QUARTER, velocity=90)
    drums.rest(Duration.DOTTED_HALF)

# Bars 57-64: fading
for bar in range(8):
    vel = max(25, 85 - bar * 8)
    drums.hit(K, Duration.QUARTER, velocity=vel)
    drums.rest(Duration.DOTTED_HALF)

# ── BASS — deep, round, the foundation ─────────────────────────
bass = score.part("bass", instrument="upright_bass", volume=0.45,
                  reverb=0.15, lowpass=600, humanize=0.1)

# The bass line — simple, heavy, lots of space
bass_a = [
    (E.add(-24), Duration.QUARTER, 90),
    (None, Duration.QUARTER, 0),
    (G.add(-24), Duration.QUARTER, 82),
    (E.add(-24), Duration.QUARTER, 85),
]
bass_b = [
    (A.add(-24), Duration.QUARTER, 88),
    (None, Duration.QUARTER, 0),
    (B.add(-24), Duration.QUARTER, 80),
    (A.add(-24), Duration.QUARTER, 82),
]
bass_c = [
    (D.add(-12), Duration.QUARTER, 85),
    (None, Duration.QUARTER, 0),
    (C.add(-12), Duration.QUARTER, 78),
    (B.add(-24), Duration.QUARTER, 80),
]
bass_d = [
    (E.add(-24), Duration.HALF, 90),
    (None, Duration.HALF, 0),
]

for _ in range(16):
    for note, dur, vel in bass_a:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=vel)
    for note, dur, vel in bass_b:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=vel)
    for note, dur, vel in bass_c:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=vel)
    for note, dur, vel in bass_d:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=vel)

# ── SKANK GUITAR — offbeat chops, enters bar 9 ─────────────────
skank = score.part("skank", instrument="acoustic_guitar", volume=0.2,
                   reverb=0.3, reverb_type="cathedral",
                   humanize=0.12)

for _ in range(8):
    skank.rest(Duration.WHOLE)

# Offbeat chops — the heartbeat of dub
for _ in range(10):
    for chord in prog:
        skank.rest(Duration.EIGHTH)
        skank.add(chord, Duration.EIGHTH, velocity=62)
        skank.rest(Duration.EIGHTH)
        skank.add(chord, Duration.EIGHTH, velocity=58)
        skank.rest(Duration.EIGHTH)
        skank.add(chord, Duration.EIGHTH, velocity=60)
        skank.rest(Duration.EIGHTH)
        skank.add(chord, Duration.EIGHTH, velocity=55)

# Bars 49-56: stripped
for _ in range(4):
    for chord in prog:
        skank.rest(Duration.QUARTER)
        skank.add(chord, Duration.QUARTER, velocity=45)
        skank.rest(Duration.HALF)

# Bars 57-64: dissolving
for _ in range(2):
    for chord in prog:
        skank.rest(Duration.HALF)
        skank.add(chord, Duration.QUARTER, velocity=35)
        skank.rest(Duration.QUARTER)

# ── MELODICA — the melody, drenched in delay, enters bar 17 ────
melodica = score.part("melodica", instrument="flute", volume=0.3,
                      reverb=0.4, reverb_type="cathedral",
                      delay=0.5, delay_time=0.417, delay_feedback=0.5,
                      humanize=0.1)

for _ in range(16):
    melodica.rest(Duration.WHOLE)

# Bars 17-32: simple melody — the delay does the work
mel_phrases = [
    [(B, Duration.HALF, 78), (None, Duration.HALF, 0)],
    [(A, Duration.QUARTER, 72), (G, Duration.QUARTER, 68),
     (E, Duration.HALF, 75)],
    [(None, Duration.QUARTER, 0), (G, Duration.QUARTER, 70),
     (A, Duration.QUARTER, 75), (B, Duration.QUARTER, 72)],
    [(E.add(12), Duration.HALF, 80), (None, Duration.HALF, 0)],
]
for _ in range(4):
    for phrase in mel_phrases:
        for note, dur, vel in phrase:
            if note is None:
                melodica.rest(dur)
            else:
                melodica.add(note, dur, velocity=vel)

# Bars 33-48: higher, more expressive
mel_high = [
    [(E.add(12), Duration.QUARTER, 82), (D.add(12), Duration.QUARTER, 78),
     (B, Duration.HALF, 80)],
    [(None, Duration.QUARTER, 0), (A, Duration.QUARTER, 75),
     (B, Duration.HALF, 78)],
    [(D.add(12), Duration.HALF, 82), (C.add(12), Duration.QUARTER, 78),
     (B, Duration.QUARTER, 75)],
    [(A, Duration.HALF, 78), (None, Duration.HALF, 0)],
]
for _ in range(4):
    for phrase in mel_high:
        for note, dur, vel in phrase:
            if note is None:
                melodica.rest(dur)
            else:
                melodica.add(note, dur, velocity=vel)

# Bars 49-64: sparse echoes, then gone
melodica.add(B, Duration.WHOLE, velocity=65)
melodica.rest(Duration.WHOLE)
melodica.add(E, Duration.WHOLE, velocity=55)
melodica.rest(Duration.WHOLE)
for _ in range(12):
    melodica.rest(Duration.WHOLE)

# ── HORNS — trumpet stabs, delay throws, bars 33-48 ────────────
horn = score.part("horn", instrument="trumpet", volume=0.25,
                  reverb=0.35, reverb_type="cathedral",
                  delay=0.45, delay_time=0.833, delay_feedback=0.45,
                  humanize=0.08)

for _ in range(32):
    horn.rest(Duration.WHOLE)

# Bars 33-48: stabs that echo forever
horn_stabs = [
    (B, Duration.QUARTER, 85), (None, Duration.DOTTED_HALF, 0),
    (None, Duration.WHOLE, 0),
    (E.add(12), Duration.QUARTER, 80), (None, Duration.DOTTED_HALF, 0),
    (None, Duration.WHOLE, 0),
]
for _ in range(4):
    for note, dur, vel in horn_stabs:
        if note is None:
            horn.rest(dur)
        else:
            horn.add(note, dur, velocity=vel)

# Rest of track: the delay echoes are the music
for _ in range(32):
    horn.rest(Duration.WHOLE)

# ── SPRING REVERB PAD — the space itself ────────────────────────
spring = score.part("spring", synth="sine", envelope="pad", volume=0.1,
                    reverb=0.7, reverb_type="cathedral",
                    chorus=0.4, chorus_rate=0.1, chorus_depth=0.015,
                    lowpass=800)

for _ in range(16):
    for chord in prog:
        spring.add(chord, Duration.WHOLE, velocity=40)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 72")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing ECHO CHAMBER (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing ECHO CHAMBER...")
    play_score(score)
