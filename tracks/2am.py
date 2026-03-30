"""
2AM — lo-fi hip hop study beats. Late night, rain on the window.
Rhodes, vinyl crackle, lazy drums, upright bass, saxophone.
Just vibes.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("Eb", "minor")
s = key.scale
prog = key.progression("i", "VI", "iv", "VII")

# Eb minor: Eb F Gb Ab Bb Cb Db
Eb = s[0]; F  = s[1]; Gb = s[2]; Ab = s[3]
Bb = s[4]; Cb = s[5]; Db = s[6]

score = Score("4/4", bpm=72, swing=0.15)

K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~5.5 min at 72 BPM):
#   Bars  1-8:   Rhodes alone, establishing the vibe
#   Bars  9-16:  Drums enter, lazy boom-bap
#   Bars 17-32:  Bass enters, the groove settles
#   Bars 33-48:  Sax melody — the heart
#   Bars 49-56:  Sax + rhodes trading, peak warmth
#   Bars 57-64:  Stripping back, rhodes alone again
# ═══════════════════════════════════════════════════════════════════

# ── RHODES — the soul of lo-fi ──────────────────────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.35,
                    reverb=0.5, reverb_type="taj_mahal",
                    tremolo_depth=0.12, tremolo_rate=2.5,
                    chorus=0.2, chorus_rate=0.3, chorus_depth=0.005,
                    humanize=0.12, saturation=0.15)

# Full 64 bars — chords throughout, the anchor
for _ in range(16):
    for chord in prog:
        rhodes.add(chord, Duration.WHOLE, velocity=65)

# ── VINYL CRACKLE — noise texture, always on ───────────────────
vinyl = score.part("vinyl", synth="noise", envelope="pad", volume=0.04,
                   lowpass=3000)

for _ in range(64):
    vinyl.add(Eb, Duration.WHOLE, velocity=40)

# ── DRUMS — lazy boom-bap, enters bar 9 ────────────────────────
drums = score.part("drums", volume=0.35, humanize=0.12)

for _ in range(8):
    drums.rest(Duration.WHOLE)

# Bars 9-56: the laziest beat alive
for bar in range(48):
    # Kick on 1, ghost kick on the & of 2
    drums.hit(K, Duration.QUARTER, velocity=90)
    drums.hit(CH, Duration.EIGHTH, velocity=45)
    drums.hit(K, Duration.EIGHTH, velocity=55)
    # Snare on 2
    drums.hit(S, Duration.QUARTER, velocity=82)
    # Kick ghost on & of 3
    drums.hit(K, Duration.EIGHTH, velocity=50)
    drums.hit(CH, Duration.EIGHTH, velocity=42)
    drums.hit(S, Duration.QUARTER, velocity=78)

# Bars 57-64: fading out
for bar in range(8):
    vel = max(25, 85 - bar * 7)
    drums.hit(K, Duration.QUARTER, velocity=vel)
    drums.hit(CH, Duration.EIGHTH, velocity=max(15, vel - 40))
    drums.hit(K, Duration.EIGHTH, velocity=max(15, vel - 35))
    drums.hit(S, Duration.QUARTER, velocity=max(20, vel - 8))
    drums.hit(K, Duration.EIGHTH, velocity=max(15, vel - 38))
    drums.hit(CH, Duration.EIGHTH, velocity=max(15, vel - 42))
    drums.hit(S, Duration.QUARTER, velocity=max(20, vel - 10))

# ── UPRIGHT BASS — warm, round, enters bar 17 ──────────────────
bass = score.part("bass", instrument="upright_bass", volume=0.35,
                  reverb=0.2, lowpass=800, humanize=0.1)

for _ in range(16):
    bass.rest(Duration.WHOLE)

# Bars 17-56: walking bass following the roots
bass_lines = [
    # i — Ebm
    [(Eb.add(-24), Duration.QUARTER, 85),
     (Gb.add(-24), Duration.QUARTER, 72),
     (Bb.add(-24), Duration.QUARTER, 78),
     (Ab.add(-24), Duration.QUARTER, 70)],
    # VI — Cb
    [(Cb.add(-24), Duration.QUARTER, 82),
     (Eb.add(-12), Duration.QUARTER, 70),
     (Db.add(-24), Duration.QUARTER, 75),
     (Cb.add(-24), Duration.QUARTER, 68)],
    # iv — Abm
    [(Ab.add(-24), Duration.QUARTER, 85),
     (Cb.add(-24), Duration.QUARTER, 72),
     (Bb.add(-24), Duration.QUARTER, 78),
     (Ab.add(-24), Duration.QUARTER, 70)],
    # VII — Db
    [(Db.add(-24), Duration.QUARTER, 82),
     (F.add(-24), Duration.QUARTER, 70),
     (Ab.add(-24), Duration.QUARTER, 75),
     (Db.add(-12), Duration.QUARTER, 68)],
]
for _ in range(10):
    for bass_bar in bass_lines:
        for note, dur, vel in bass_bar:
            bass.add(note, dur, velocity=vel)

# Bars 57-64: fading
for _ in range(2):
    for bass_bar in bass_lines:
        for note, dur, vel in bass_bar:
            bass.add(note, dur, velocity=max(30, vel - 25))

# ── SAXOPHONE — the melody, enters bar 33 ──────────────────────
sax = score.part("sax", instrument="saxophone", volume=0.35,
                 reverb=0.45, reverb_type="taj_mahal",
                 delay=0.15, delay_time=0.417, delay_feedback=0.25,
                 humanize=0.1)

for _ in range(32):
    sax.rest(Duration.WHOLE)

# Bars 33-48: lazy, bluesy melody — lots of space
sax_phrases = [
    # Phrase 1: opening statement
    [(Bb, Duration.HALF, 82), (Ab, Duration.QUARTER, 75),
     (Gb, Duration.QUARTER, 70)],
    [(Eb, Duration.HALF, 78), (None, Duration.HALF, 0)],
    # Phrase 2: climbing
    [(None, Duration.QUARTER, 0), (Gb, Duration.QUARTER, 72),
     (Ab, Duration.QUARTER, 78), (Bb, Duration.QUARTER, 82)],
    [(Db.add(12), Duration.HALF, 85), (Cb, Duration.QUARTER, 75),
     (Bb, Duration.QUARTER, 72)],
    # Phrase 3: the cry
    [(Bb, Duration.DOTTED_HALF, 88),
     (Ab, Duration.QUARTER, 78)],
    [(Gb, Duration.QUARTER, 72), (Eb, Duration.QUARTER, 68),
     (None, Duration.HALF, 0)],
    # Phrase 4: resolution
    [(Eb, Duration.QUARTER, 75), (F, Duration.QUARTER, 72),
     (Gb, Duration.QUARTER, 78), (Ab, Duration.QUARTER, 75)],
    [(Eb, Duration.WHOLE, 80)],
]
for _ in range(2):
    for phrase in sax_phrases:
        for note, dur, vel in phrase:
            if note is None:
                sax.rest(dur)
            else:
                sax.add(note, dur, velocity=vel)

# Bars 49-56: higher, more expressive
sax_high = [
    [(Eb.add(12), Duration.HALF, 90), (Db.add(12), Duration.QUARTER, 82),
     (Cb, Duration.QUARTER, 78)],
    [(Bb, Duration.HALF, 85), (None, Duration.QUARTER, 0),
     (Ab, Duration.QUARTER, 75)],
    [(Bb, Duration.QUARTER, 80), (Db.add(12), Duration.QUARTER, 85),
     (Eb.add(12), Duration.HALF, 92)],
    [(Db.add(12), Duration.QUARTER, 82), (Bb, Duration.QUARTER, 78),
     (Ab, Duration.HALF, 75)],
]
for _ in range(2):
    for phrase in sax_high:
        for note, dur, vel in phrase:
            if note is None:
                sax.rest(dur)
            else:
                sax.add(note, dur, velocity=vel)

# Bars 57-64: one last phrase, fading
for phrase in sax_phrases[:4]:
    for note, dur, vel in phrase:
        if note is None:
            sax.rest(dur)
        else:
            sax.add(note, dur, velocity=max(35, vel - 20))
for _ in range(4):
    sax.rest(Duration.WHOLE)

# ── PAD — warmth underneath ─────────────────────────────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.08,
                 reverb=0.6, reverb_type="taj_mahal",
                 chorus=0.3, chorus_rate=0.15, chorus_depth=0.008,
                 lowpass=1200)

for _ in range(16):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=45)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 72 (swing 0.15)")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing 2AM (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing 2AM...")
    play_score(score)
