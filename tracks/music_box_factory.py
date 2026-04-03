"""
MUSIC BOX FACTORY — tuned percussion only.
Kalimba, vibraphone, celesta, marimba, glockenspiel, xylophone, crotales.
No synths. No strings. Just metal and wood and keys.
G major, 108 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("G", "major")
s = key.scale  # G A B C D E F#

G  = s[0]; A  = s[1]; B  = s[2]; C  = s[3]
D  = s[4]; E  = s[5]; Fs = s[6]

score = Score("4/4", bpm=108)

prog = key.progression("I", "vi", "IV", "V")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (72 bars, ~4:00):
#   Bars  1-8:   Kalimba alone — thumb piano, intimate
#   Bars  9-16:  Vibraphone joins — jazz shimmer, motor wobble
#   Bars 17-24:  Celesta — ethereal, high, Tchaikovsky's ghost
#   Bars 25-32:  Marimba — warm wood, the low end
#   Bars 33-40:  Glockenspiel — bright, cutting through
#   Bars 41-48:  All together — the factory floor
#   Bars 49-56:  Xylophone + crotales — the brightest moment
#   Bars 57-64:  Kalimba melody reprise — over everything
#   Bars 65-72:  Winding down — one by one they stop
# ═══════════════════════════════════════════════════════════════════

# ── KALIMBA — the seed, thumb piano ───────────────────────────
kalimba = score.part("kalimba", instrument="kalimba", volume=0.45,
                     reverb=0.25, reverb_type="taj_mahal",
                     delay=0.15, delay_time=0.278, delay_feedback=0.2,
                     pan=-0.15, humanize=0.1)

# Bars 1-8: alone — simple, percussive, melodic
kalimba_phrase_a = [
    (G, Duration.EIGHTH, 72), (None, Duration.EIGHTH, 0),
    (B, Duration.EIGHTH, 65), (D, Duration.EIGHTH, 68),
    (None, Duration.EIGHTH, 0), (B, Duration.EIGHTH, 62),
    (G, Duration.EIGHTH, 70), (None, Duration.EIGHTH, 0),
]
kalimba_phrase_b = [
    (E, Duration.EIGHTH, 68), (None, Duration.EIGHTH, 0),
    (G, Duration.EIGHTH, 65), (B, Duration.EIGHTH, 70),
    (A, Duration.EIGHTH, 62), (None, Duration.EIGHTH, 0),
    (G, Duration.EIGHTH, 68), (None, Duration.EIGHTH, 0),
]
for _ in range(4):
    for note, dur, vel in kalimba_phrase_a:
        if note is None:
            kalimba.rest(dur)
        else:
            kalimba.add(note, dur, velocity=vel)
    for note, dur, vel in kalimba_phrase_b:
        if note is None:
            kalimba.rest(dur)
        else:
            kalimba.add(note, dur, velocity=vel)

# Bars 9-56: continues — the constant heartbeat
for _ in range(24):
    for note, dur, vel in kalimba_phrase_a:
        if note is None:
            kalimba.rest(dur)
        else:
            kalimba.add(note, dur, velocity=vel)
    for note, dur, vel in kalimba_phrase_b:
        if note is None:
            kalimba.rest(dur)
        else:
            kalimba.add(note, dur, velocity=vel)

# Bars 57-64: REPRISE — melody sings above everything
kalimba.set(volume=0.55)
kalimba_melody = [
    (D, Duration.QUARTER, 78), (E, Duration.EIGHTH, 72),
    (D, Duration.EIGHTH, 68), (B, Duration.HALF, 75),
    (A, Duration.QUARTER, 70), (G, Duration.EIGHTH, 65),
    (Fs, Duration.EIGHTH, 62), (G, Duration.HALF, 72),
    (B, Duration.QUARTER, 75), (D, Duration.QUARTER, 72),
    (E, Duration.HALF, 78),
    (D, Duration.QUARTER, 72), (B, Duration.QUARTER, 68),
    (A, Duration.QUARTER, 65), (G, Duration.QUARTER, 70),
    (G, Duration.WHOLE, 72),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in kalimba_melody:
    if note is None:
        kalimba.rest(dur)
    else:
        kalimba.add(note, dur, velocity=vel)

# Bars 65-72: last one playing — fading
kalimba.set(volume=0.4)
for rep in range(4):
    off = rep * -12
    for note, dur, vel in kalimba_phrase_a:
        if note is None:
            kalimba.rest(dur)
        else:
            kalimba.add(note, dur, velocity=max(20, vel + off))
    for note, dur, vel in kalimba_phrase_b:
        if note is None:
            kalimba.rest(dur)
        else:
            kalimba.add(note, dur, velocity=max(20, vel + off))

# ── VIBRAPHONE — jazz shimmer, enters bar 9 ──────────────────
vib = score.part("vibraphone", instrument="vibraphone", volume=0.35,
                 reverb=0.3, reverb_type="cathedral",
                 delay=0.12, delay_time=0.556, delay_feedback=0.2,
                 pan=0.25, humanize=0.08)

for _ in range(8):
    vib.rest(Duration.WHOLE)

# Bars 9-16: sustained chords — the motor wobble gives life
for _ in range(2):
    for chord in prog:
        vib.add(chord, Duration.WHOLE, velocity=55)

# Bars 17-40: continues — warm bed under everything
for _ in range(6):
    for chord in prog:
        vib.add(chord, Duration.WHOLE, velocity=52)

# Bars 41-48: arpeggiated — the factory speeds up
vib_arp = [G, B, D, B, G, D.add(-12), B.add(-12), D.add(-12)]
for _ in range(8):
    for note in vib_arp:
        vib.add(note, Duration.EIGHTH, velocity=60)

# Bars 49-56: peak chords
for _ in range(2):
    for chord in prog:
        vib.add(chord, Duration.WHOLE, velocity=62)

# Bars 57-64: under kalimba melody
for _ in range(2):
    for chord in prog:
        vib.add(chord, Duration.WHOLE, velocity=50)

# Bars 65-72: fading
for vel in [45, 40, 35, 30, 25, 18, 10, 0]:
    if vel > 0:
        vib.add(prog[0], Duration.WHOLE, velocity=vel)
    else:
        vib.rest(Duration.WHOLE)

# ── CELESTA — ethereal, enters bar 17 ────────────────────────
celesta = score.part("celesta", instrument="celesta", volume=0.3,
                     reverb=0.35, reverb_type="taj_mahal",
                     delay=0.15, delay_time=0.278, delay_feedback=0.25,
                     pan=-0.3, humanize=0.08)

for _ in range(16):
    celesta.rest(Duration.WHOLE)

# Bars 17-24: high, sparkling countermelody
celesta_phrase = [
    (None, Duration.QUARTER, 0),
    (D, Duration.EIGHTH, 62), (E, Duration.EIGHTH, 58),
    (None, Duration.QUARTER, 0),
    (B, Duration.EIGHTH, 60), (None, Duration.EIGHTH, 0),
    (None, Duration.QUARTER, 0),
    (E, Duration.EIGHTH, 62), (D, Duration.EIGHTH, 58),
    (B, Duration.EIGHTH, 55), (None, Duration.EIGHTH, 0),
    (None, Duration.QUARTER, 0),
]
for _ in range(8):
    for note, dur, vel in celesta_phrase:
        if note is None:
            celesta.rest(dur)
        else:
            celesta.add(note, dur, velocity=vel)

# Bars 25-56: continues
for _ in range(32):
    for note, dur, vel in celesta_phrase:
        if note is None:
            celesta.rest(dur)
        else:
            celesta.add(note, dur, velocity=vel)

# Bars 57-72: fading
for rep in range(8):
    off = rep * -6
    for note, dur, vel in celesta_phrase:
        if note is None:
            celesta.rest(dur)
        else:
            celesta.add(note, dur, velocity=max(15, vel + off))
for _ in range(8):
    celesta.rest(Duration.WHOLE)

# ── MARIMBA — warm wood, the bass, enters bar 25 ─────────────
marimba = score.part("marimba", instrument="marimba", volume=0.4,
                     reverb=0.2, reverb_decay=1.0,
                     delay=0.08, delay_time=0.278, delay_feedback=0.1,
                     pan=0.1, humanize=0.08)

for _ in range(24):
    marimba.rest(Duration.WHOLE)

# Bars 25-32: low register — the warm bass of the ensemble
marimba_bass = [
    (G.add(-12), Duration.QUARTER, 72), (None, Duration.EIGHTH, 0),
    (G.add(-12), Duration.EIGHTH, 62), (B.add(-12), Duration.QUARTER, 68),
    (None, Duration.QUARTER, 0),
    (D, Duration.QUARTER, 65), (None, Duration.EIGHTH, 0),
    (B.add(-12), Duration.EIGHTH, 60), (G.add(-12), Duration.HALF, 70),
]
for _ in range(8):
    for note, dur, vel in marimba_bass:
        if note is None:
            marimba.rest(dur)
        else:
            marimba.add(note, dur, velocity=vel)

# Bars 33-56: continues — the floor
for _ in range(24):
    for note, dur, vel in marimba_bass:
        if note is None:
            marimba.rest(dur)
        else:
            marimba.add(note, dur, velocity=vel)

# Bars 57-72: fading
for rep in range(8):
    off = rep * -8
    for note, dur, vel in marimba_bass:
        if note is None:
            marimba.rest(dur)
        else:
            marimba.add(note, dur, velocity=max(20, vel + off))
for _ in range(8):
    marimba.rest(Duration.WHOLE)

# ── GLOCKENSPIEL — bright, cutting, enters bar 33 ────────────
glock = score.part("glockenspiel", instrument="glockenspiel", volume=0.2,
                   reverb=0.3, reverb_type="cathedral",
                   delay=0.12, delay_time=0.139, delay_feedback=0.15,
                   pan=-0.4, humanize=0.06)

for _ in range(32):
    glock.rest(Duration.WHOLE)

# Bars 33-40: high bright hits — sparse, like light catching metal
glock_hits = [
    (D, Duration.QUARTER, 58), (None, Duration.DOTTED_HALF, 0),
    (None, Duration.HALF, 0), (E, Duration.QUARTER, 55),
    (None, Duration.QUARTER, 0),
    (B, Duration.QUARTER, 60), (None, Duration.DOTTED_HALF, 0),
    (None, Duration.WHOLE, 0),
    (D, Duration.QUARTER, 55), (None, Duration.QUARTER, 0),
    (G, Duration.QUARTER, 58), (None, Duration.QUARTER, 0),
    (None, Duration.WHOLE, 0),
    (None, Duration.HALF, 0), (Fs, Duration.QUARTER, 52),
    (None, Duration.QUARTER, 0),
    (None, Duration.WHOLE, 0),
]
for note, dur, vel in glock_hits:
    if note is None:
        glock.rest(dur)
    else:
        glock.add(note, dur, velocity=vel)

# Bars 41-56: more active — 16th note runs
glock_run = [G, A, B, D, B, A, G, Fs, G, B, D, E, D, B, A, G]
for _ in range(4):
    for note in glock_run:
        glock.add(note, Duration.SIXTEENTH, velocity=55)
for _ in range(4):
    for note, dur, vel in glock_hits:
        if note is None:
            glock.rest(dur)
        else:
            glock.add(note, dur, velocity=vel)
for _ in range(4):
    for note in glock_run:
        glock.add(note, Duration.SIXTEENTH, velocity=58)

# Bars 57-72: fading runs
for _ in range(4):
    for note in glock_run:
        glock.add(note, Duration.SIXTEENTH, velocity=max(20, 48))
for _ in range(12):
    glock.rest(Duration.WHOLE)

# ── XYLOPHONE — bright wood, enters bar 49 ───────────────────
xylo = score.part("xylophone", instrument="xylophone", volume=0.25,
                  reverb=0.15, reverb_decay=0.6,
                  delay=0.1, delay_time=0.139, delay_feedback=0.12,
                  pan=0.35, humanize=0.06)

for _ in range(48):
    xylo.rest(Duration.WHOLE)

# Bars 49-56: rapid arps — woody brightness
xylo_arp_a = [G, B, D, G, D, B, G, D]
xylo_arp_b = [A, C, E, A, E, C, A, E]
for _ in range(4):
    for note in xylo_arp_a:
        xylo.add(note, Duration.SIXTEENTH, velocity=65)
    for note in xylo_arp_b:
        xylo.add(note, Duration.SIXTEENTH, velocity=62)

# Bars 57-64: continues under kalimba melody
for _ in range(4):
    for note in xylo_arp_a:
        xylo.add(note, Duration.SIXTEENTH, velocity=58)
    for note in xylo_arp_b:
        xylo.add(note, Duration.SIXTEENTH, velocity=55)

# Bars 65-72: fading
for vel in [50, 42, 35, 28, 22, 15, 0, 0]:
    if vel > 0:
        for note in xylo_arp_a:
            xylo.add(note, Duration.SIXTEENTH, velocity=vel)
        for note in xylo_arp_b:
            xylo.add(note, Duration.SIXTEENTH, velocity=max(15, vel - 5))
    else:
        xylo.rest(Duration.WHOLE)

# ── CROTALES — crystalline, enters bar 49 ─────────────────────
crot = score.part("crotales", instrument="crotales", volume=0.18,
                  reverb=0.35, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.556, delay_feedback=0.2,
                  pan=-0.35)

for _ in range(48):
    crot.rest(Duration.WHOLE)

# Bars 49-56: sparse strikes — like tiny church bells
crot_map = {49: (D, 52), 51: (G, 48), 53: (B, 50), 55: (E, 45)}
for bar in range(49, 73):
    if bar in crot_map:
        note, vel = crot_map[bar]
        crot.add(note, Duration.WHOLE, velocity=vel)
    elif bar > 56 and bar % 3 == 0:
        crot.add(D, Duration.WHOLE, velocity=max(20, 45 - (bar - 57) * 2))
    else:
        crot.rest(Duration.WHOLE)

# ── TUBULAR BELLS — section markers ───────────────────────────
bells = score.part("tubular_bells", instrument="tubular_bells", volume=0.2,
                   reverb=0.4, reverb_type="cathedral",
                   delay=0.15, delay_time=0.556, delay_feedback=0.15,
                   pan=0.15)

bell_bars = {1: 60, 9: 55, 17: 52, 25: 58, 33: 55, 41: 62, 49: 58, 57: 65}
for bar in range(1, 73):
    if bar in bell_bars:
        bells.add(G.add(-12), Duration.WHOLE, velocity=bell_bars[bar])
    else:
        bells.rest(Duration.WHOLE)

# ── TIMPANI — the low end, enters bar 25 ──────────────────────
timp = score.part("timpani", instrument="timpani", volume=0.3,
                  reverb=0.2, reverb_decay=1.0,
                  delay=0.06, delay_time=0.278, delay_feedback=0.08,
                  pan=0.05, humanize=0.06)

for _ in range(24):
    timp.rest(Duration.WHOLE)

# Bars 25-32: sparse — one hit per bar, like a grandfather clock
for note, vel in [(G.add(-12), 68), (D.add(-12), 62),
                  (G.add(-12), 65), (None, 0),
                  (G.add(-12), 70), (B.add(-12), 60),
                  (G.add(-12), 68), (D.add(-12), 62)]:
    if note is None:
        timp.rest(Duration.WHOLE)
    else:
        timp.add(note, Duration.QUARTER, velocity=vel)
        timp.rest(Duration.DOTTED_HALF)

# Bars 33-48: more active — rhythmic pulse
for _ in range(16):
    timp.add(G.add(-12), Duration.QUARTER, velocity=65)
    timp.rest(Duration.QUARTER)
    timp.add(D.add(-12), Duration.QUARTER, velocity=58)
    timp.rest(Duration.QUARTER)

# Bars 49-56: peak — 8th note rolls
for bar in range(8):
    if bar % 4 == 3:
        for i in range(16):
            timp.add(G.add(-12), Duration.SIXTEENTH, velocity=min(82, 48 + i * 2))
    else:
        timp.add(G.add(-12), Duration.QUARTER, velocity=68)
        timp.rest(Duration.QUARTER)
        timp.add(D.add(-12), Duration.QUARTER, velocity=60)
        timp.rest(Duration.QUARTER)

# Bars 57-72: fading
for vel in [58, 52, 45, 38, 32, 25, 18, 10, 0, 0, 0, 0, 0, 0, 0, 0]:
    if vel > 0:
        timp.add(G.add(-12), Duration.QUARTER, velocity=vel)
        timp.rest(Duration.DOTTED_HALF)
    else:
        timp.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 108")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing MUSIC BOX FACTORY (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing MUSIC BOX FACTORY...")
    play_score(score)
