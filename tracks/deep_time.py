"""
DEEP TIME — ambient drone. No rhythm, no melody, just texture and space.
Like listening to the earth breathe through a cathedral.
"""

from pytheory import Key, Duration, Score, Tone, play_score

key = Key("B", "minor")
s = key.scale

B  = s[0]; Cs = s[1]; D  = s[2]; E  = s[3]
Fs = s[4]; G  = s[5]; A  = s[6]

score = Score("4/4", bpm=40, temperament="just")

# ═══════════════════════════════════════════════════════════════════
# No structure. Just layers appearing and dissolving.
# 48 bars at 40 BPM = ~7.5 minutes
# ═══════════════════════════════════════════════════════════════════

# ── DRONE 1 — deep sine, the foundation of the earth ───────────
earth = score.part("earth", synth="sine", envelope="pad", volume=0.25,
                   reverb=0.9, reverb_type="taj_mahal",
                   chorus=0.3, chorus_rate=0.03, chorus_depth=0.015,
                   lowpass=400)

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
harmonium = score.part("harmonium", instrument="harmonium", volume=0.1,
                       reverb=0.8, reverb_type="taj_mahal",
                       chorus=0.3, chorus_rate=0.1, chorus_depth=0.01)

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
bowl = score.part("bowl", instrument="singing_bowl", volume=0.25,
                  reverb=0.95, reverb_type="taj_mahal")

# Strike once every 8 bars
for i in range(6):
    bowl.add(B.add(-12), Duration.WHOLE, velocity=max(35, 70 - i * 5))
    for _ in range(7):
        bowl.rest(Duration.WHOLE)

# ── HIGH TEXTURE — triangle shimmer, almost subliminal ─────────
shimmer = score.part("shimmer", synth="triangle", envelope="pad", volume=0.06,
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

# ── CHOIR — voices from nowhere, enters bar 20 ─────────────────
choir = score.part("choir", instrument="choir", volume=0.1,
                   reverb=0.9, reverb_type="taj_mahal",
                   chorus=0.4, chorus_rate=0.08, chorus_depth=0.015)

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

# ── CELLO — one long note, enters late, the human voice ────────
cello = score.part("cello", instrument="cello", volume=0.15,
                   reverb=0.7, reverb_type="taj_mahal",
                   humanize=0.05)

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
