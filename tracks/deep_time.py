"""
DEEP TIME — ambient drone. No rhythm, no melody, just texture and space.
Like listening to the earth breathe through a cathedral.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("B", "minor")
s = key.scale

B  = s[0]; Cs = s[1]; D  = s[2]; E  = s[3]
Fs = s[4]; G  = s[5]; A  = s[6]

score = Score("4/4", bpm=40, temperament="just")

# ═══════════════════════════════════════════════════════════════════
# No structure. Just layers appearing and dissolving.
# 48 bars at 40 BPM = ~7.5 minutes
# ═══════════════════════════════════════════════════════════════════

# ── TINGSHA — crystalline strikes, etheric opening ──────────────
tingsha = score.part("tingsha", instrument="tingsha", volume=0.2,
                     reverb=0.5, reverb_type="taj_mahal",
                     delay=0.2, delay_time=1.5, delay_feedback=0.25,
                     pan=0.35)

# Sparse strikes in the first 8 bars — let each one ring forever
tingsha.add(B.add(12), Duration.WHOLE, velocity=65)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
tingsha.add(Fs.add(12), Duration.WHOLE, velocity=58)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
tingsha.add(B.add(12), Duration.WHOLE, velocity=52)
tingsha.rest(Duration.WHOLE)
# A few more through bars 9-16
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
tingsha.add(D.add(12), Duration.WHOLE, velocity=48)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
tingsha.add(Fs.add(12), Duration.WHOLE, velocity=42)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
# Bars 17-48: continues throughout — one strike every 4-6 bars
tingsha_strikes = {
    18: (B.add(12), 45), 22: (Fs.add(12), 40), 26: (D.add(12), 42),
    30: (B.add(12), 38), 34: (E.add(12), 35), 38: (Fs.add(12), 38),
    42: (B.add(12), 32), 46: (D.add(12), 28),
}
for bar in range(17, 49):
    if bar in tingsha_strikes:
        note, vel = tingsha_strikes[bar]
        tingsha.add(note, Duration.WHOLE, velocity=vel)
    else:
        tingsha.rest(Duration.WHOLE)

# ── RAINSTICK — slow texture wash ──────────────────────────────
rain = score.part("rain", volume=0.15, reverb=0.5, reverb_type="cathedral",
                  pan=-0.3)

RS = DrumSound.RAINSTICK_SLOW
# One slow rainstick every 4 bars in the intro
rain.hit(RS, Duration.WHOLE, velocity=60)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
rain.hit(RS, Duration.WHOLE, velocity=55)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
rain.hit(RS, Duration.WHOLE, velocity=50)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
rain.hit(RS, Duration.WHOLE, velocity=42)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
rain.rest(Duration.WHOLE)
# Rest of track
for _ in range(32):
    rain.rest(Duration.WHOLE)

# ── FINGER CYMBALS — a few gypsy accents ───────────────────────
FC = DrumSound.FINGER_CYMBAL
fingers = score.part("fingers", volume=0.12, reverb=0.4,
                     delay=0.15, delay_time=1.0, delay_feedback=0.2,
                     pan=-0.4)

fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
fingers.hit(FC, Duration.HALF, velocity=55)
fingers.rest(Duration.HALF)
fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
fingers.hit(FC, Duration.HALF, velocity=48)
fingers.rest(Duration.HALF)
fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
fingers.hit(FC, Duration.HALF, velocity=42)
fingers.rest(Duration.HALF)
fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
fingers.rest(Duration.WHOLE)
# Rest of track
for _ in range(32):
    fingers.rest(Duration.WHOLE)

# ── SINGING BOWL LOW — deep bowl in the opening ────────────────
bowl_low = score.part("bowl_low", instrument="singing_bowl_ring", volume=0.45,
                      reverb=0.85, reverb_type="taj_mahal",
                      delay=0.15, delay_time=1.5, delay_feedback=0.2,
                      pan=-0.15)

# Strike every 8 bars throughout — the deep pulse of the earth
bowl_strikes = [
    (B.add(-24), 70), (B.add(-24), 62), (Fs.add(-24), 58),
    (B.add(-24), 55), (D.add(-12), 50), (B.add(-24), 45),
]
for note, vel in bowl_strikes:
    bowl_low.add(note, Duration.WHOLE, velocity=vel)
    for _ in range(7):
        bowl_low.rest(Duration.WHOLE)

# ── DIDGERIDOO — primal opening, first voice heard ──────────────
didge = score.part("didge", instrument="didgeridoo", volume=0.08,
                   reverb=0.3, reverb_type="cathedral",
                   chorus=0.2, chorus_rate=0.05, chorus_depth=0.01,
                   lowpass=300, pan=0.1)

for _ in range(16):
    didge.add(B.add(-24), Duration.WHOLE, velocity=65)
# Fade out as other layers build
for vel in [55, 45, 35, 25, 18, 12, 8, 5]:
    didge.add(B.add(-24), Duration.WHOLE, velocity=vel)
for _ in range(24):
    didge.rest(Duration.WHOLE)

# ── DRONE 1 — deep sine, the foundation of the earth ───────────
earth = score.part("earth", synth="sine", envelope="pad", volume=0.25,
                   reverb=0.7, reverb_type="taj_mahal",
                   chorus=0.3, chorus_rate=0.03, chorus_depth=0.015,
                   lowpass=400, sub_osc=0.2)

for _ in range(48):
    earth.add(B.add(-36), Duration.WHOLE, velocity=60)

# ── DRONE 2 — fifth above, slow beating ────────────────────────
fifth = score.part("fifth", synth="sine", envelope="pad", volume=0.18,
                   reverb=0.9, reverb_type="taj_mahal",
                   chorus=0.4, chorus_rate=0.02, chorus_depth=0.02,
                   lowpass=500, pan=0.3)

for _ in range(4):
    fifth.rest(Duration.WHOLE)
for _ in range(44):
    fifth.add(Fs.add(-24), Duration.WHOLE, velocity=50)

# ── DRONE 3 — octave, barely there ─────────────────────────────
octave = score.part("octave", synth="sine", envelope="pad", volume=0.12,
                    reverb=0.9, reverb_type="taj_mahal",
                    chorus=0.5, chorus_rate=0.015, chorus_depth=0.025,
                    lowpass=600, pan=-0.3)

for _ in range(8):
    octave.rest(Duration.WHOLE)
for _ in range(40):
    octave.add(B.add(-24), Duration.WHOLE, velocity=45)

# ── HARMONIUM — breathing chords, glacial ──────────────────────
harmonium = score.part("harmonium", instrument="harmonium", volume=0.06,
                       reverb=0.6, reverb_type="taj_mahal",
                       chorus=0.3, chorus_rate=0.1, chorus_depth=0.01,
                       pan=0.15)

for _ in range(12):
    harmonium.rest(Duration.WHOLE)

# One chord every 4 bars — like breathing
chords = [
    key.progression("i")[0],
    key.progression("iv")[0],
    key.progression("i")[0],
    key.progression("v")[0],
    key.progression("i")[0],
    key.progression("VI")[0],
    key.progression("iv")[0],
    key.progression("i")[0],
    key.progression("i")[0],
]
for chord in chords:
    harmonium.add(chord, Duration.WHOLE, velocity=45)
    harmonium.rest(Duration.WHOLE)
    harmonium.rest(Duration.WHOLE)
    harmonium.rest(Duration.WHOLE)

# ── SINGING BOWL — one strike, ages apart ──────────────────────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.4,
                  reverb=0.85, reverb_type="taj_mahal",
                  delay=0.2, delay_time=1.5, delay_feedback=0.2,
                  pan=0.2)

# Strike once every 8 bars
for i in range(6):
    bowl.add(B.add(-12), Duration.WHOLE, velocity=max(35, 70 - i * 5))
    for _ in range(7):
        bowl.rest(Duration.WHOLE)

# ── HIGH TEXTURE — triangle shimmer, almost subliminal ─────────
shimmer = score.part("shimmer", synth="drift", envelope="pad", volume=0.06,
                     reverb=0.9, reverb_type="taj_mahal",
                     chorus=0.6, chorus_rate=0.05, chorus_depth=0.03,
                     lowpass=2000, pan=-0.4)
shimmer.lfo("lowpass", rate=0.01, min=800, max=3000, bars=48, shape="sine")

for _ in range(16):
    shimmer.rest(Duration.WHOLE)

# Slowly evolving — holds for 4 bars at a time
shimmer_notes = [Fs, D, E, Fs, B, A, Fs, D]
for note in shimmer_notes:
    for _ in range(4):
        shimmer.add(note.add(12), Duration.WHOLE, velocity=35)

# ── VOCAL — low "ohhh", enters bar 16 ──────────────────────────
vocal = score.part("vocal", instrument="vocal", volume=0.12,
                   reverb=0.7, reverb_type="taj_mahal",
                   chorus=0.3, chorus_rate=0.06, chorus_depth=0.012,
                   pan=-0.2)

for _ in range(16):
    vocal.rest(Duration.WHOLE)

# Low sustained notes — like a monk humming
vocal_notes = [B.add(-24), Fs.add(-24), D.add(-12), B.add(-24),
               Fs.add(-24), E.add(-12), D.add(-12), B.add(-24)]
for note in vocal_notes:
    vocal.add(note, Duration.WHOLE, velocity=40)
    vocal.add(note, Duration.WHOLE, velocity=38)
    vocal.rest(Duration.WHOLE)
    vocal.rest(Duration.WHOLE)

# ── CHOIR — voices from nowhere, enters bar 20 ─────────────────
choir = score.part("choir", instrument="choir", volume=0.1,
                   reverb=0.8, reverb_type="cathedral",
                   chorus=0.4, chorus_rate=0.08, chorus_depth=0.015,
                   pan=0.25)

for _ in range(20):
    choir.rest(Duration.WHOLE)

# Held chords, glacial — one every 4 bars
choir_notes = [
    (B.add(-12), Fs),
    (D, A),
    (E, B),
    (Fs, Cs.add(12)),
    (D, A),
    (B.add(-12), Fs),
    (B.add(-12), Fs),
]
for low, high in choir_notes:
    choir.hold(low, Duration.WHOLE * 4, velocity=40)
    choir.add(high, Duration.WHOLE, velocity=35)
    choir.rest(Duration.WHOLE)
    choir.rest(Duration.WHOLE)
    choir.rest(Duration.WHOLE)

# ── NOISE WASH — the wind ──────────────────────────────────────
wind = score.part("wind", synth="noise", envelope="pad", volume=0.03,
                  reverb=0.8, reverb_type="taj_mahal",
                  lowpass=500)
wind.lfo("lowpass", rate=0.008, min=200, max=1500, bars=48, shape="sine")
wind.lfo("volume", rate=0.015, min=0.01, max=0.05, bars=48, shape="triangle")

for _ in range(48):
    wind.add(B, Duration.WHOLE, velocity=30)

# ── GRAIN — deep granular texture, barely perceptible ──────────
grain = score.part("grain", instrument="granular_pad", volume=0.06,
                   reverb=0.5, reverb_type="taj_mahal",
                   pan=0.35)

# Bars 1-16: silence
for _ in range(16):
    grain.rest(Duration.WHOLE)

# Bars 17-40: low B drone, glacial
for _ in range(24):
    grain.add(B.add(-12), Duration.WHOLE, velocity=30)

# Bars 41-48: silence — dissolve
for _ in range(8):
    grain.rest(Duration.WHOLE)

# ── THEREMIN — emotional break, center of the piece ─────────────
theremin = score.part("theremin", instrument="theremin", volume=0.22,
                      reverb=0.5, reverb_type="taj_mahal",
                      delay=0.12, delay_time=0.75, delay_feedback=0.15,
                      pan=-0.1, humanize=0.06)

for _ in range(20):
    theremin.rest(Duration.WHOLE)

# Bars 21-32: slow, aching melody — the emotional core
theremin.add(Fs, Duration.WHOLE, velocity=45, bend=0.5)
theremin.add(Fs, Duration.WHOLE, velocity=48)
theremin.rest(Duration.WHOLE)
theremin.rest(Duration.WHOLE)
theremin.add(B, Duration.WHOLE, velocity=52, bend=-0.25)
theremin.add(A, Duration.WHOLE, velocity=50)
theremin.add(Fs, Duration.WHOLE, velocity=48, bend=0.5)
theremin.rest(Duration.WHOLE)
theremin.add(D.add(12), Duration.WHOLE, velocity=55, bend=-0.5)
theremin.add(Cs.add(12), Duration.WHOLE, velocity=50)
theremin.add(B, Duration.WHOLE, velocity=45, bend=0.25)
theremin.add(Fs, Duration.WHOLE, velocity=40)

# Bars 33-48: silent — let it dissolve
for _ in range(16):
    theremin.rest(Duration.WHOLE)

# ── CELLO — one long note, enters late, the human voice ────────
cello = score.part("cello", instrument="cello", volume=0.15,
                   reverb=0.5, reverb_type="cathedral",
                   delay=0.1, delay_time=1.0, delay_feedback=0.15,
                   pan=0.3, humanize=0.05)

for _ in range(32):
    cello.rest(Duration.WHOLE)

# Bars 33-44: one held note that slowly rises
cello.add(B.add(-12), Duration.WHOLE, velocity=40)
cello.add(B.add(-12), Duration.WHOLE, velocity=45)
cello.add(B.add(-12), Duration.WHOLE, velocity=50)
cello.add(B.add(-12), Duration.WHOLE, velocity=55)
cello.add(Cs, Duration.WHOLE, velocity=50)
cello.add(Cs, Duration.WHOLE, velocity=48)
cello.add(D, Duration.WHOLE, velocity=52)
cello.add(D, Duration.WHOLE, velocity=50)
cello.add(Cs, Duration.WHOLE, velocity=45)
cello.add(B.add(-12), Duration.WHOLE, velocity=42)
cello.add(B.add(-12), Duration.WHOLE, velocity=38)
cello.add(B.add(-12), Duration.WHOLE, velocity=30)

# Bars 45-48: silence — dissolve
for _ in range(4):
    cello.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 40 (just intonation)")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing DEEP TIME (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing DEEP TIME...")
    play_score(score)
