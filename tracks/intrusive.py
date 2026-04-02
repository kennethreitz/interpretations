"""
INTRUSIVE — the thought you can't stop thinking.
One phrase. Over and over. You try to play something else.
It comes back. It always comes back.
Until you learn to let it pass.
Bb minor, 92 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("Bb", "minor")
s = key.scale  # Bb C Db Eb F Gb Ab

Bb = s[0]; C  = s[1]; Db = s[2]; Eb = s[3]
F  = s[4]; Gb = s[5]; Ab = s[6]

score = Score("4/4", bpm=92)

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (56 bars, ~2:26):
#   Bars  1-8:   THE THOUGHT — one piano phrase, repeating
#   Bars  9-16:  TRYING — Rhodes plays something different. The thought returns.
#   Bars 17-24:  FIGHTING — drums try to drown it. The thought is louder.
#   Bars 25-32:  SPIRALING — the thought fragments, multiplies, distorts
#   Bars 33-40:  ACCEPTING — stop fighting. Let it play. Something changes.
#   Bars 41-48:  RELEASING — the thought slows down. Spaces between.
#   Bars 49-56:  PASSING — it plays once more. Quiet. And doesn't come back.
# ═══════════════════════════════════════════════════════════════════

# The intrusive thought — this exact phrase, burned into your brain
THOUGHT = [
    (Bb, Duration.EIGHTH, 72), (Db, Duration.EIGHTH, 68),
    (F, Duration.QUARTER, 75), (Eb, Duration.EIGHTH, 65),
    (Db, Duration.EIGHTH, 62), (Bb, Duration.QUARTER, 70),
]

def play_thought(part, vel_offset=0, rest_after=Duration.WHOLE):
    """The thought. Always the same. Always unwanted."""
    for note, dur, vel in THOUGHT:
        part.add(note, dur, velocity=min(127, max(15, vel + vel_offset)))
    part.rest(rest_after)


# ── THE THOUGHT — piano, the thing you can't unthink ──────────
thought = score.part("thought", synth="saw", volume=0.4,
                     lowpass=3000, distortion=0.1, distortion_drive=1.5,
                     saturation=0.4, legato=True, glide=0.03,
                     reverb=0.25, reverb_type="spring",
                     delay=0.12, delay_time=0.326, delay_feedback=0.15,
                     pan=-0.1, humanize=0.06)

# Bars 1-8: repeating. and repeating. and repeating.
for _ in range(4):
    play_thought(thought)

# Bars 9-12: it keeps going while Rhodes tries
for _ in range(2):
    play_thought(thought)

# Bars 13-16: louder — you noticed it and now it's worse
for _ in range(2):
    play_thought(thought, vel_offset=8)

# Bars 17-20: drums enter, thought persists
for _ in range(2):
    play_thought(thought, vel_offset=5)

# Bars 21-24: even louder — fighting it makes it stronger
thought.set(volume=0.6)
for _ in range(2):
    play_thought(thought, vel_offset=12)

# Bars 25-28: SPIRALING — the thought starts fragmenting, distorting
thought.set(volume=0.55, reverb=0.5)
# Fragment 1: just the first three notes, repeated
for _ in range(3):
    thought.add(Bb, Duration.EIGHTH, velocity=78)
    thought.add(Db, Duration.EIGHTH, velocity=72)
    thought.add(F, Duration.QUARTER, velocity=80)
thought.rest(Duration.QUARTER)
# Fragment 2: the ending, wrong rhythm
thought.add(Eb, Duration.SIXTEENTH, velocity=70)
thought.add(Db, Duration.SIXTEENTH, velocity=65)
thought.add(Bb, Duration.EIGHTH, velocity=72)
thought.rest(Duration.HALF)
thought.add(Eb, Duration.SIXTEENTH, velocity=72)
thought.add(Db, Duration.SIXTEENTH, velocity=68)
thought.add(Bb, Duration.EIGHTH, velocity=75)
thought.rest(Duration.QUARTER)
thought.add(F, Duration.QUARTER, velocity=78)

# Bars 29-32: the thought in wrong octaves, displaced
thought.add(Bb.add(12), Duration.EIGHTH, velocity=75)
thought.add(Db.add(12), Duration.EIGHTH, velocity=70)
thought.add(F.add(12), Duration.QUARTER, velocity=78)
thought.add(Eb, Duration.EIGHTH, velocity=62)
thought.add(Db, Duration.EIGHTH, velocity=58)
thought.add(Bb.add(-12), Duration.QUARTER, velocity=68)
thought.rest(Duration.HALF)
# Overlapping — like it's echoing inside your skull
thought.add(Bb, Duration.EIGHTH, velocity=70)
thought.add(Db, Duration.EIGHTH, velocity=65)
thought.add(F, Duration.QUARTER, velocity=72)
thought.add(Bb.add(12), Duration.EIGHTH, velocity=68)
thought.add(Db.add(12), Duration.EIGHTH, velocity=62)
thought.add(F, Duration.QUARTER, velocity=70)
thought.rest(Duration.WHOLE)

# Bars 33-40: ACCEPTING — stop fighting. The thought plays but softer.
thought.set(volume=0.4, reverb=0.3)
for _ in range(2):
    play_thought(thought, vel_offset=-5)
# Slower now — gaps between repetitions
play_thought(thought, vel_offset=-10, rest_after=Duration.WHOLE)
thought.rest(Duration.WHOLE)
play_thought(thought, vel_offset=-15, rest_after=Duration.WHOLE)
thought.rest(Duration.WHOLE)

# Bars 41-48: RELEASING — more space, softer each time
thought.set(volume=0.3)
play_thought(thought, vel_offset=-20, rest_after=Duration.WHOLE)
thought.rest(Duration.WHOLE)
thought.rest(Duration.WHOLE)
play_thought(thought, vel_offset=-28, rest_after=Duration.WHOLE)
thought.rest(Duration.WHOLE)
thought.rest(Duration.WHOLE)
thought.rest(Duration.WHOLE)

# Bars 49-52: PASSING — one last time. Barely there.
thought.set(volume=0.2)
play_thought(thought, vel_offset=-40, rest_after=Duration.WHOLE)

# Bars 53-56: silence. it passed.
for _ in range(4):
    thought.rest(Duration.WHOLE)

# ── RHODES — what you're trying to think instead ──────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.35,
                    reverb=0.45, reverb_type="taj_mahal",
                    delay=0.12, delay_time=0.326, delay_feedback=0.15,
                    tremolo_depth=0.1, tremolo_rate=2.5,
                    pan=0.2, humanize=0.1)

for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# Bars 9-12: tries to play its own melody — interrupted
rhodes.add(Db, Duration.QUARTER, velocity=60)
rhodes.add(Eb, Duration.QUARTER, velocity=55)
rhodes.add(F, Duration.HALF, velocity=62)
# interrupted — rest while thought plays
rhodes.rest(Duration.WHOLE)
rhodes.add(Ab, Duration.QUARTER, velocity=58)
rhodes.add(Gb, Duration.QUARTER, velocity=55)
rhodes.add(F, Duration.HALF, velocity=60)
rhodes.rest(Duration.WHOLE)

# Bars 13-16: tries again — longer phrases
rhodes.add(Db, Duration.QUARTER, velocity=62)
rhodes.add(Eb, Duration.QUARTER, velocity=58)
rhodes.add(F, Duration.QUARTER, velocity=65)
rhodes.add(Ab, Duration.QUARTER, velocity=60)
rhodes.add(Gb, Duration.HALF, velocity=62)
rhodes.add(F, Duration.HALF, velocity=58)
rhodes.rest(Duration.WHOLE)
rhodes.rest(Duration.WHOLE)

# Bars 17-24: keeps trying through the drums
for _ in range(2):
    rhodes.add(Db, Duration.QUARTER, velocity=58)
    rhodes.add(Eb, Duration.QUARTER, velocity=55)
    rhodes.add(F, Duration.HALF, velocity=60)
    rhodes.add(Ab, Duration.QUARTER, velocity=55)
    rhodes.add(Gb, Duration.EIGHTH, velocity=50)
    rhodes.add(F, Duration.EIGHTH, velocity=48)
    rhodes.add(Eb, Duration.HALF, velocity=55)
    rhodes.rest(Duration.WHOLE)
    rhodes.rest(Duration.WHOLE)

# Bars 25-32: gives up — sparse, defeated
for _ in range(4):
    rhodes.add(Db, Duration.QUARTER, velocity=45)
    rhodes.rest(Duration.DOTTED_HALF)
    rhodes.rest(Duration.WHOLE)

# Bars 33-40: acceptance — Rhodes and thought coexist
rhodes.set(volume=0.4)
prog_chords = key.progression("i", "VI", "iv", "v")
for _ in range(2):
    for chord in prog_chords:
        rhodes.add(chord, Duration.WHOLE, velocity=52)

# Bars 41-48: Rhodes grows — it's winning, gently
rhodes.set(volume=0.5)
rhodes.add(Db, Duration.QUARTER, velocity=65)
rhodes.add(Eb, Duration.QUARTER, velocity=60)
rhodes.add(F, Duration.HALF, velocity=68)
rhodes.add(Ab, Duration.QUARTER, velocity=62)
rhodes.add(Gb, Duration.EIGHTH, velocity=58)
rhodes.add(F, Duration.EIGHTH, velocity=55)
rhodes.add(Eb, Duration.HALF, velocity=60)
rhodes.rest(Duration.QUARTER)
rhodes.add(Bb.add(-12), Duration.QUARTER, velocity=55)
rhodes.add(Db, Duration.QUARTER, velocity=60)
rhodes.add(F, Duration.QUARTER, velocity=58)
rhodes.add(Ab, Duration.HALF, velocity=65)
rhodes.add(Gb, Duration.HALF, velocity=60)
rhodes.add(F, Duration.WHOLE, velocity=62)
rhodes.rest(Duration.WHOLE)

# Bars 49-56: Rhodes owns the space now — peaceful
rhodes.add(Db, Duration.QUARTER, velocity=62)
rhodes.add(Eb, Duration.QUARTER, velocity=58)
rhodes.add(F, Duration.HALF, velocity=65)
rhodes.add(Eb, Duration.QUARTER, velocity=58)
rhodes.add(Db, Duration.QUARTER, velocity=55)
rhodes.add(Bb.add(-12), Duration.HALF, velocity=60)
rhodes.add(Bb.add(-12), Duration.WHOLE, velocity=55)
for _ in range(5):
    rhodes.rest(Duration.WHOLE)

# ── DRUMS — trying to drown the thought, bars 17-32 ──────────
K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT

drums = score.part("drums", volume=0.35, humanize=0.06,
                   reverb=0.2, reverb_decay=0.8,
                   delay=0.08, delay_time=0.326, delay_feedback=0.12,
                   pan=-0.05)

for _ in range(16):
    drums.rest(Duration.WHOLE)

# Bars 17-24: trying to overpower it
for _ in range(8):
    drums.hit(K, Duration.QUARTER, velocity=90)
    drums.hit(CH, Duration.EIGHTH, velocity=55)
    drums.hit(CH, Duration.EIGHTH, velocity=42)
    drums.hit(S, Duration.QUARTER, velocity=88)
    drums.hit(CH, Duration.EIGHTH, velocity=50)
    drums.hit(K, Duration.EIGHTH, velocity=78)

# Bars 25-32: drums get frantic — can't overpower it
for bar in range(8):
    if bar % 4 == 3:
        # Frustrated fill
        for i in range(8):
            drums.hit(S, Duration.SIXTEENTH, velocity=min(100, 60 + i * 5))
        drums.hit(K, Duration.HALF, velocity=95)
    else:
        drums.hit(K, Duration.QUARTER, velocity=95)
        drums.hit(CH, Duration.SIXTEENTH, velocity=58)
        drums.hit(CH, Duration.SIXTEENTH, velocity=42)
        drums.hit(CH, Duration.EIGHTH, velocity=50)
        drums.hit(S, Duration.QUARTER, velocity=92)
        drums.hit(CH, Duration.EIGHTH, velocity=48)
        drums.hit(K, Duration.EIGHTH, velocity=82)

# Bars 33-40: drums soften — stop fighting
for vel in [75, 68, 60, 52, 45, 38, 30, 22]:
    drums.hit(K, Duration.QUARTER, velocity=vel)
    drums.rest(Duration.QUARTER)
    drums.hit(S, Duration.QUARTER, velocity=max(15, vel - 8))
    drums.rest(Duration.QUARTER)

# Bars 41-56: gone — no need to fight anymore
for _ in range(16):
    drums.rest(Duration.WHOLE)

# ── CELLO — enters at acceptance, warmth ───────────────────────
cello = score.part("cello", instrument="cello", volume=0.15,
                   reverb=0.4, reverb_type="cathedral",
                   delay=0.08, delay_time=0.326, delay_feedback=0.1,
                   pan=0.25, humanize=0.08)

for _ in range(32):
    cello.rest(Duration.WHOLE)

# Bars 33-48: long tones — acceptance has weight
for note, vel in [(Bb.add(-12), 38), (Bb.add(-12), 42),
                  (Db, 40), (Eb, 42),
                  (F, 45), (Eb, 42),
                  (Db, 40), (Bb.add(-12), 45),
                  (Bb.add(-12), 48), (Db, 45),
                  (F, 48), (Eb, 45),
                  (Db, 42), (Bb.add(-12), 48),
                  (Bb.add(-12), 42), (Bb.add(-12), 35)]:
    cello.add(note, Duration.WHOLE, velocity=vel)

# Bars 49-56: fading
for vel in [32, 25, 18, 12, 8, 0, 0, 0]:
    if vel > 0:
        cello.add(Bb.add(-12), Duration.WHOLE, velocity=vel)
    else:
        cello.rest(Duration.WHOLE)

# ── SUB — the weight of acceptance, bars 33 onward ────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.6,
                 lowpass=180, distortion=0.15, distortion_drive=2.5,
                 sub_osc=0.5, sidechain=0.3)

for _ in range(32):
    sub.rest(Duration.WHOLE)

# Bars 33-48: enters with acceptance — the ground beneath you
roots = [Bb.add(-24), Gb.add(-24), Eb.add(-24), F.add(-24)]
for _ in range(4):
    for root in roots:
        sub.add(root, Duration.WHOLE, velocity=35)

# Bars 49-56: one long Bb — settling
for vel in [35, 32, 28, 25, 20, 15, 10, 5]:
    sub.add(Bb.add(-24), Duration.WHOLE, velocity=vel)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 92")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing INTRUSIVE (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing INTRUSIVE...")
    play_score(score)
