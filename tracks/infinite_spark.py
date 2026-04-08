"""
BONUS: INFINITE SPARK
Composed by Grok & Claude with Kenneth Reitz's pytheory

A minor, 78 BPM. A single bowl strike in darkness. A sitar tone
finds its voice. Piano and choir breathe underneath. The spark catches —
ornaments quicken, the room fills — then slowly, silence returns.
"""

from pytheory import Key, Duration, Score, play_score
from pytheory.rhythm import DrumSound

key = Key("A", "minor")
s = key.scale

# Scale degrees (Hindustani names in comments)
A  = s[0]   # Sa
B  = s[1]   # Re
C  = s[2]   # Ga
D  = s[3]   # Ma
E  = s[4]   # Pa
F  = s[5]   # Dha
G  = s[6]   # Ni

score = Score("4/4", bpm=78)

K  = DrumSound.KICK
CH = DrumSound.CLOSED_HAT

prog = key.progression("i", "VI", "III", "VII")  # Am - F - C - G

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~3:17 at 78 BPM):
#   Bars  1-8:   Bowl alone. Sub drone fades in. Empty room.
#   Bars  9-16:  Sitar alap — Sa, Re, Ga. Slow, meditative.
#   Bars 17-24:  Piano enters. Choir breathes. Space fills.
#   Bars 25-32:  Sitar climbs. Theremin enters. The spark catches.
#   Bars 33-40:  Energy — sitar ornaments, kick arrives, supersaw.
#   Bars 41-48:  Peak — sitar shred phrase, everything converges.
#   Bars 49-56:  Dissolution — parts thin, sitar holds.
#   Bars 57-64:  Bowl alone again. One last ring.
# ═══════════════════════════════════════════════════════════════════

# ── SINGING BOWL — time-keeper, bookends everything ──────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.5,
                  reverb=1.0, reverb_type="taj_mahal",
                  delay=0.25, delay_time=0.923, delay_feedback=0.4,
                  pan=0.15)

# Section markers — sparse strikes, 4 bars apart
marker_bars = {1: 72, 5: 65, 9: 60, 17: 58, 25: 62, 33: 68, 41: 72, 49: 60, 57: 55, 61: 48}
for bar in range(1, 65):
    if bar in marker_bars:
        bowl.add(A.add(-12), Duration.WHOLE, velocity=marker_bars[bar])
    else:
        bowl.rest(Duration.WHOLE)

# ── SUB — sine pulse, the room's heartbeat ───────────────────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.25,
                 lowpass=120, sub_osc=0.3, sidechain=0.25)

# Bars 1-8: fade in from nothing
for vel in [0, 0, 8, 15, 22, 30, 38, 45]:
    if vel > 0:
        sub.add(A.add(-24), Duration.HALF, velocity=vel)
        sub.rest(Duration.HALF)
    else:
        sub.rest(Duration.WHOLE)

# Bars 9-32: steady pulse, root follows progression loosely
for _ in range(6):
    for root in [A.add(-24), A.add(-24), E.add(-24), A.add(-24)]:
        sub.add(root, Duration.HALF, velocity=55)
        sub.rest(Duration.HALF)

# Bars 33-48: stronger
for _ in range(4):
    for root in [A.add(-24), A.add(-24), E.add(-24), A.add(-24)]:
        sub.add(root, Duration.HALF, velocity=72)
        sub.rest(Duration.HALF)

# Bars 49-56: fading
for vel in [62, 55, 48, 40, 32, 24, 16, 8]:
    sub.add(A.add(-24), Duration.HALF, velocity=vel)
    sub.rest(Duration.HALF)

# Bars 57-64: silence
for _ in range(8):
    sub.rest(Duration.WHOLE)

# ── SITAR — the voice, from whisper to shred to silence ──────────
sitar = score.part("sitar", instrument="sitar", volume=0.7,
                   reverb=0.3, reverb_type="taj_mahal",
                   delay=0.2, delay_time=0.375, delay_feedback=0.22,
                   saturation=0.2, pan=-0.15, humanize=0.1)

# Bars 1-8: silence
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# Bars 9-12: alap — Sa alone, then Sa-Re
sitar.add(A, Duration.WHOLE, velocity=65, bend=-0.15)    # Sa — home
sitar.rest(Duration.WHOLE)
sitar.add(B, Duration.HALF, velocity=60)                  # Re
sitar.add(A, Duration.HALF, velocity=68, bend=-0.15)      # Sa
sitar.rest(Duration.WHOLE)

# Bars 13-16: alap expands — Ga arrives
sitar.add(C, Duration.DOTTED_HALF, velocity=72)           # Ga — first new color
sitar.rest(Duration.QUARTER)
sitar.add(D, Duration.QUARTER, velocity=68)               # Ma (passing)
sitar.add(C, Duration.QUARTER, velocity=65)               # Ga
sitar.add(B, Duration.QUARTER, velocity=60)               # Re
sitar.add(A, Duration.QUARTER, velocity=70, bend=-0.15)   # Sa
sitar.rest(Duration.DOTTED_HALF)

# Bars 17-20: melody takes shape — still patient
sitar.add(E, Duration.HALF, velocity=78)                  # Pa — the leap up
sitar.add(D, Duration.QUARTER, velocity=72)               # Ma
sitar.add(C, Duration.QUARTER, velocity=68)               # Ga
sitar.add(B, Duration.HALF, velocity=65)                  # Re
sitar.add(A, Duration.HALF, velocity=72, bend=-0.15)      # Sa
sitar.rest(Duration.WHOLE)
sitar.add(E, Duration.WHOLE, velocity=82, bend=-0.2)      # Pa held — new height

# Bars 21-24: descending from Pa, finding phrases
sitar.add(D, Duration.QUARTER, velocity=75)
sitar.add(C, Duration.QUARTER, velocity=70)
sitar.add(B, Duration.QUARTER, velocity=65)
sitar.add(A, Duration.QUARTER, velocity=72)
sitar.add(E, Duration.HALF, velocity=58)                          # Pa below — grounding
sitar.rest(Duration.HALF)
sitar.rest(Duration.WHOLE)
sitar.add(A, Duration.WHOLE, velocity=68, bend=-0.15)     # Sa — breath

# Bars 25-28: climbing higher — Dha, Ni arrive
sitar.add(E, Duration.QUARTER, velocity=82)               # Pa
sitar.add(F, Duration.QUARTER, velocity=78)               # Dha — new note
sitar.add(E, Duration.QUARTER, velocity=75)               # Pa
sitar.add(D, Duration.QUARTER, velocity=70)               # Ma
sitar.add(F, Duration.HALF, velocity=85, bend=-0.15)      # Dha held
sitar.add(G, Duration.HALF, velocity=90, bend=-0.2)       # Ni! — the spark
sitar.add(F, Duration.QUARTER, velocity=78)               # Dha
sitar.add(E, Duration.QUARTER, velocity=75)               # Pa
sitar.add(D, Duration.QUARTER, velocity=70)               # Ma
sitar.add(C, Duration.QUARTER, velocity=65)               # Ga
sitar.add(A, Duration.WHOLE, velocity=80, bend=-0.15)     # Sa — home

# Bars 29-32: the spark catches — shorter notes, wider range
sitar.add(A, Duration.HALF, velocity=95, bend=-0.15)      # High Sa!
sitar.add(G, Duration.QUARTER, velocity=85)               # Ni
sitar.add(F, Duration.QUARTER, velocity=80)               # Dha
sitar.add(E, Duration.QUARTER, velocity=88)               # Pa
sitar.add(F, Duration.QUARTER, velocity=82)               # Dha
sitar.add(G, Duration.QUARTER, velocity=90)               # Ni
sitar.add(A, Duration.QUARTER, velocity=98, bend=-0.15)   # High Sa
# Descending cascade
sitar.add(G, Duration.EIGHTH, velocity=85)
sitar.add(F, Duration.EIGHTH, velocity=80)
sitar.add(E, Duration.EIGHTH, velocity=75)
sitar.add(D, Duration.EIGHTH, velocity=70)
sitar.add(C, Duration.EIGHTH, velocity=65)
sitar.add(B, Duration.EIGHTH, velocity=60)
sitar.add(A, Duration.QUARTER, velocity=78, bend=-0.15)
sitar.rest(Duration.QUARTER)

# Bars 33-36: eighth-note energy — the fire is burning
for _ in range(2):
    sitar.add(A.add(12), Duration.EIGHTH, velocity=105)
    sitar.add(G.add(12), Duration.EIGHTH, velocity=95)
    sitar.add(E.add(12), Duration.EIGHTH, velocity=100)
    sitar.add(G.add(12), Duration.EIGHTH, velocity=92)
    sitar.add(A.add(12), Duration.EIGHTH, velocity=108)
    sitar.add(G.add(12), Duration.EIGHTH, velocity=90)
    sitar.add(F.add(12), Duration.EIGHTH, velocity=85)
    sitar.add(E.add(12), Duration.EIGHTH, velocity=95)

# Bars 37-40: building toward peak — mixed eighths and sixteenths
sitar.add(A.add(12), Duration.EIGHTH, velocity=110, bend=-0.15)
sitar.add(G.add(12), Duration.SIXTEENTH, velocity=100)
sitar.add(F.add(12), Duration.SIXTEENTH, velocity=95)
sitar.add(E.add(12), Duration.EIGHTH, velocity=105)
sitar.add(D.add(12), Duration.SIXTEENTH, velocity=92)
sitar.add(C.add(12), Duration.SIXTEENTH, velocity=88)
sitar.add(B.add(12), Duration.EIGHTH, velocity=95)
sitar.add(A.add(12), Duration.EIGHTH, velocity=100, bend=-0.15)
sitar.rest(Duration.HALF)
# ascending run
sitar.add(A.add(12), Duration.SIXTEENTH, velocity=100)
sitar.add(B.add(12), Duration.SIXTEENTH, velocity=105)
sitar.add(C.add(12), Duration.SIXTEENTH, velocity=108)
sitar.add(D.add(12), Duration.SIXTEENTH, velocity=110)
sitar.add(E.add(12), Duration.SIXTEENTH, velocity=112)
sitar.add(F.add(12), Duration.SIXTEENTH, velocity=115)
sitar.add(G.add(12), Duration.SIXTEENTH, velocity=118)
sitar.add(A.add(12), Duration.SIXTEENTH, velocity=120)
sitar.add(A.add(12), Duration.HALF, velocity=115, bend=-0.2)
sitar.rest(Duration.WHOLE)

# Bars 41-44: PEAK — full 16th-note shred, velocity at max
# ascending
sitar.add(A.add(12), Duration.SIXTEENTH, velocity=112)
sitar.add(B.add(12), Duration.SIXTEENTH, velocity=115)
sitar.add(C.add(12), Duration.SIXTEENTH, velocity=118)
sitar.add(D.add(12), Duration.SIXTEENTH, velocity=120)
sitar.add(E.add(12), Duration.SIXTEENTH, velocity=122)
sitar.add(F.add(12), Duration.SIXTEENTH, velocity=125)
sitar.add(G.add(12), Duration.SIXTEENTH, velocity=125)
sitar.add(A.add(12), Duration.SIXTEENTH, velocity=127)
# descending
sitar.add(G.add(12), Duration.SIXTEENTH, velocity=120)
sitar.add(F.add(12), Duration.SIXTEENTH, velocity=115)
sitar.add(E.add(12), Duration.SIXTEENTH, velocity=110)
sitar.add(D.add(12), Duration.SIXTEENTH, velocity=105)
sitar.add(C.add(12), Duration.SIXTEENTH, velocity=100)
sitar.add(B.add(12), Duration.SIXTEENTH, velocity=95)
sitar.add(A.add(12), Duration.SIXTEENTH, velocity=90)
sitar.add(E, Duration.SIXTEENTH, velocity=85)
# peak held note
sitar.add(A.add(12), Duration.WHOLE, velocity=127, bend=-0.25)
# resolution
sitar.add(E.add(12), Duration.HALF, velocity=100, bend=-0.2)
sitar.add(A.add(12), Duration.WHOLE, velocity=95, bend=-0.25)
sitar.rest(Duration.HALF)

# Bars 45-48: cooling — longer notes, falling velocity
sitar.add(E, Duration.HALF, velocity=82)
sitar.add(D, Duration.QUARTER, velocity=75)
sitar.add(C, Duration.QUARTER, velocity=70)
sitar.add(A, Duration.WHOLE, velocity=78, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.add(A, Duration.WHOLE, velocity=65, bend=-0.15)

# Bars 49-56: fading — sparse, widely spaced
sitar.add(E, Duration.WHOLE, velocity=58)
sitar.rest(Duration.WHOLE)
sitar.add(A, Duration.WHOLE, velocity=52, bend=-0.15)
sitar.rest(Duration.WHOLE)
sitar.add(A, Duration.WHOLE * 2, velocity=45, bend=-0.1)
sitar.rest(Duration.WHOLE)
sitar.rest(Duration.WHOLE)

# Bars 57-64: silence
for _ in range(8):
    sitar.rest(Duration.WHOLE)

# ── PIANO — harmonic grounding, enters bar 17 ────────────────────
piano = score.part("piano", instrument="piano", volume=0.6,
                   reverb=0.72, reverb_type="taj_mahal",
                   delay=0.12, delay_time=0.468, delay_feedback=0.18,
                   pan=-0.1)

# Bars 1-16: silence
for _ in range(16):
    piano.rest(Duration.WHOLE)

# Bars 17-24: slow chords, one every 2 bars
for chord in prog:
    piano.add(chord, Duration.WHOLE * 2, velocity=68)

# Bars 25-32: chords continue, slightly louder
for chord in prog:
    piano.add(chord, Duration.WHOLE * 2, velocity=75)

# Bars 33-40: more present
for chord in prog:
    piano.add(chord, Duration.WHOLE * 2, velocity=82)

# Bars 41-48: peak — stronger, whole notes for more movement
for chord in prog:
    piano.add(chord, Duration.WHOLE, velocity=88)
for chord in prog:
    piano.add(chord, Duration.WHOLE, velocity=82)

# Bars 49-56: fading
piano.add(prog[0], Duration.WHOLE * 2, velocity=68)
piano.add(prog[1], Duration.WHOLE * 2, velocity=60)
piano.add(prog[0], Duration.WHOLE * 2, velocity=52)
piano.add(prog[3], Duration.WHOLE * 2, velocity=45)

# Bars 57-64: silence
for _ in range(8):
    piano.rest(Duration.WHOLE)

# ── MELLOTRON CHOIR — atmospheric wash ────────────────────────────
choir = score.part("choir", instrument="mellotron_choir", volume=0.1,
                   reverb=0.85, reverb_type="taj_mahal",
                   delay=0.3, delay_time=0.875, delay_feedback=0.35,
                   chorus=0.3, chorus_rate=0.06, chorus_depth=0.01,
                   lowpass=2200, pan=0.25)

# Bars 1-16: silence
for _ in range(16):
    choir.rest(Duration.WHOLE)

# Bars 17-24: enters soft — one chord per 4 bars
choir.add(prog[0], Duration.WHOLE * 4, velocity=38)
choir.add(prog[1], Duration.WHOLE * 4, velocity=35)

# Bars 25-32: louder
choir.add(prog[2], Duration.WHOLE * 4, velocity=42)
choir.add(prog[3], Duration.WHOLE * 4, velocity=40)

# Bars 33-40: fuller
choir.add(prog[0], Duration.WHOLE * 4, velocity=48)
choir.add(prog[1], Duration.WHOLE * 4, velocity=45)

# Bars 41-48: peak
choir.add(prog[0], Duration.WHOLE * 4, velocity=55)
choir.add(prog[3], Duration.WHOLE * 4, velocity=52)

# Bars 49-56: fading
choir.add(prog[0], Duration.WHOLE * 4, velocity=42)
choir.add(prog[1], Duration.WHOLE * 4, velocity=32)

# Bars 57-64: silence
for _ in range(8):
    choir.rest(Duration.WHOLE)

# ── THEREMIN — ethereal countermelody, enters bar 25 ─────────────
theremin = score.part("theremin", instrument="theremin", volume=0.25,
                      reverb=0.88, reverb_type="taj_mahal",
                      delay=0.2, delay_time=0.625, delay_feedback=0.28,
                      pan=0.35, humanize=0.1)

# Bars 1-24: silence
for _ in range(24):
    theremin.rest(Duration.WHOLE)

# Bars 25-32: long tones, answering sitar
theremin.add(E.add(12), Duration.WHOLE * 2, velocity=50)
theremin.add(A.add(12), Duration.WHOLE * 2, velocity=48)
theremin.add(G.add(12), Duration.WHOLE * 2, velocity=52)
theremin.add(E.add(12), Duration.WHOLE * 2, velocity=45)

# Bars 33-40: more present
theremin.add(A.add(12), Duration.WHOLE * 2, velocity=58)
theremin.add(G.add(12), Duration.WHOLE * 2, velocity=55)
theremin.add(F.add(12), Duration.WHOLE * 2, velocity=52)
theremin.add(E.add(12), Duration.WHOLE * 2, velocity=60)

# Bars 41-48: peak — higher, brighter
theremin.add(A.add(36), Duration.WHOLE * 2, velocity=65)
theremin.add(G.add(12), Duration.WHOLE * 2, velocity=60)
theremin.add(E.add(12), Duration.WHOLE * 4, velocity=55)

# Bars 49-56: fading
theremin.add(A.add(12), Duration.WHOLE * 4, velocity=42)
theremin.add(E.add(12), Duration.WHOLE * 4, velocity=32)

# Bars 57-64: silence
for _ in range(8):
    theremin.rest(Duration.WHOLE)

# ── SUPERSAW PAD — swells at the peak, never dominates ───────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.08,
                 reverb=0.65, reverb_type="taj_mahal",
                 chorus=0.25, chorus_rate=0.08,
                 detune=5, lowpass=2500, pan=-0.25)
pad.lfo("lowpass", rate=0.008, min=800, max=3500, bars=64, shape="triangle")

# Bars 1-32: silence
for _ in range(32):
    pad.rest(Duration.WHOLE)

# Bars 33-40: enters barely audible
for chord in prog:
    pad.add(chord, Duration.WHOLE * 2, velocity=35)

# Bars 41-48: peak swell
for chord in prog:
    pad.add(chord, Duration.WHOLE * 2, velocity=48)

# Bars 49-56: fading
pad.add(prog[0], Duration.WHOLE * 4, velocity=30)
pad.add(prog[1], Duration.WHOLE * 4, velocity=20)

# Bars 57-64: silence
for _ in range(8):
    pad.rest(Duration.WHOLE)

# ── KICK — arrives bar 33, minimal, earns its place ──────────────
kick = score.part("kick", volume=0.65, humanize=0.02)

# Bars 1-32: silence
for _ in range(32):
    kick.rest(Duration.WHOLE)

# Bars 33-40: one hit per bar, on beat 1 only
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=95)
    kick.rest(Duration.DOTTED_HALF)

# Bars 41-48: beats 1 and 3
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=105)
    kick.rest(Duration.QUARTER)
    kick.hit(K, Duration.QUARTER, velocity=88)
    kick.rest(Duration.QUARTER)

# Bars 49-56: back to one per bar, fading
for vel in [90, 82, 75, 68, 58, 48, 35, 22]:
    kick.hit(K, Duration.QUARTER, velocity=vel)
    kick.rest(Duration.DOTTED_HALF)

# Bars 57-64: silence
for _ in range(8):
    kick.rest(Duration.WHOLE)

# ── HATS — ghost shimmer, bars 33-48 only ────────────────────────
hats = score.part("hats", volume=0.18, pan=0.1, humanize=0.04)

# Bars 1-32: silence
for _ in range(32):
    hats.rest(Duration.WHOLE)

# Bars 33-40: offbeat eighths, barely there
for _ in range(8):
    for _ in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=42)

# Bars 41-48: slightly more present
for _ in range(8):
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=55 if beat % 2 == 1 else 40)

# Bars 49-56: thinning
for bar in range(8):
    vel = max(20, 45 - bar * 5)
    for _ in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=vel)

# Bars 57-64: silence
for _ in range(8):
    hats.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 78")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing INFINITE SPARK (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing INFINITE SPARK...")
    play_score(score)
