"""
GHOST PROTOCOL — dark, patient, hypnotic.
Trip-hop intro dissolves into a slow-building trance arp.
One pluck line that IS the track.
The kick doesn't arrive until you've forgotten you're waiting for it.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("F", "minor")
s = key.scale

F  = s[0]; G  = s[1]; Ab = s[2]; Bb = s[3]
C  = s[4]; Db = s[5]; Eb = s[6]

score = Score("4/4", bpm=128)

K  = DrumSound.KICK
CL = DrumSound.CLAP
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

prog = key.progression("i", "VI", "VII", "i")

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (128 bars, ~6 min at 128 BPM):
#   Bars   1-16:  Portishead — dark, downtempo feel, scratchy
#   Bars  17-32:  The arp emerges from the darkness
#   Bars  33-48:  Pad swells, arp grows, still no kick
#   Bars  49-64:  Kick arrives — release, the Strobe moment
#   Bars  65-80:  Full energy, filter wide open
#   Bars  81-96:  Peak — everything singing
#   Bars  97-112: Filtering down, layers drop
#   Bars 113-128: Just the arp and pad, dissolving
# ═══════════════════════════════════════════════════════════════════

# ── RHODES — Portishead dark chords, sparse, tremolo ────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.25,
                    reverb=0.6, reverb_type="taj_mahal",
                    delay=0.2, delay_time=0.468, delay_feedback=0.3,
                    tremolo_depth=0.2, tremolo_rate=2.5,
                    pan=-0.2, humanize=0.1)

# Bars 1-16: dark sparse chords — Portishead vibe
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.HALF, velocity=70)
        rhodes.rest(Duration.HALF)

# Bars 17-32: thinner, making room for the arp
for _ in range(4):
    for chord in prog:
        rhodes.add(chord, Duration.QUARTER, velocity=55)
        rhodes.rest(Duration.DOTTED_HALF)

# Bars 33-48: fading out
for _ in range(2):
    for chord in prog:
        rhodes.add(chord, Duration.QUARTER, velocity=40)
        rhodes.rest(Duration.DOTTED_HALF)
for _ in range(8):
    rhodes.rest(Duration.WHOLE)

# Bars 49-128: gone
for _ in range(80):
    rhodes.rest(Duration.WHOLE)

# ── TRIP-HOP BEAT — Portishead style, bars 5-32 ────────────────
trip = score.part("trip_hop", volume=0.3, humanize=0.08,
                  reverb=0.25, reverb_decay=1.2,
                  delay=0.3, delay_time=0.468, delay_feedback=0.35)

# Bars 1-4: silence — let rhodes breathe
for _ in range(4):
    trip.rest(Duration.WHOLE)

# Bars 5-16: slow, lazy breakbeat — Portishead pocket
S = DrumSound.SNARE
for _ in range(12):
    trip.hit(K, Duration.QUARTER, velocity=90)
    trip.rest(Duration.EIGHTH)
    trip.hit(CH, Duration.EIGHTH, velocity=50)
    trip.hit(S, Duration.QUARTER, velocity=85)
    trip.hit(CH, Duration.EIGHTH, velocity=48)
    trip.hit(K, Duration.EIGHTH, velocity=75)

# Bars 17-24: beat thins out
for _ in range(8):
    trip.hit(K, Duration.QUARTER, velocity=70)
    trip.rest(Duration.QUARTER)
    trip.hit(S, Duration.QUARTER, velocity=60)
    trip.rest(Duration.QUARTER)

# Bars 25-32: just ghost hits, disappearing
for bar in range(8):
    vel = max(20, 60 - bar * 5)
    trip.hit(K, Duration.QUARTER, velocity=vel)
    trip.rest(Duration.DOTTED_HALF)

# Bars 33-128: gone
for _ in range(96):
    trip.rest(Duration.WHOLE)

# ── THE ARP — the soul of the track, enters quietly bar 17 ─────
arp = score.part("arp", synth="saw", envelope="pluck", volume=0.22,
                 reverb=0.35, delay=0.4, delay_time=0.234,
                 delay_feedback=0.45, lowpass=1200, detune=6,
                 pan=0.15, humanize=0.04)
# Slow filter open over the entire track
arp.lfo("lowpass", rate=0.008, min=800, max=6000, bars=128, shape="saw")

# Bars 1-16: silence
for _ in range(16):
    arp.rest(Duration.WHOLE)

# The pattern — hypnotic, never changes, just grows
arp_pattern = [
    F, None, C.add(12), None,
    Eb, None, C.add(12), Ab,
    F, None, C.add(12), None,
    Ab, None, Eb, C.add(12),
]

# Bars 17-32: arp emerges, barely audible
for _ in range(4):
    for note in arp_pattern:
        if note is None:
            arp.rest(Duration.SIXTEENTH)
        else:
            arp.add(note, Duration.SIXTEENTH, velocity=50)

# Bars 33-48: arp grows
for _ in range(4):
    for note in arp_pattern:
        if note is None:
            arp.rest(Duration.SIXTEENTH)
        else:
            arp.add(note, Duration.SIXTEENTH, velocity=65)

# Bars 49-64: kick arrives, arp confident
for _ in range(4):
    for note in arp_pattern:
        if note is None:
            arp.rest(Duration.SIXTEENTH)
        else:
            arp.add(note, Duration.SIXTEENTH, velocity=80)

# Bars 65-96: full energy, arp singing
for _ in range(8):
    for note in arp_pattern:
        if note is None:
            arp.rest(Duration.SIXTEENTH)
        else:
            arp.add(note, Duration.SIXTEENTH, velocity=90)

# Bars 97-112: filtering down
for _ in range(4):
    for note in arp_pattern:
        if note is None:
            arp.rest(Duration.SIXTEENTH)
        else:
            arp.add(note, Duration.SIXTEENTH, velocity=70)

# Bars 113-128: dissolving
for rep in range(4):
    vel = max(25, 60 - rep * 10)
    for note in arp_pattern:
        if note is None:
            arp.rest(Duration.SIXTEENTH)
        else:
            arp.add(note, Duration.SIXTEENTH, velocity=vel)

# ── PAD — supersaw atmosphere, builds imperceptibly ─────────────
pad = score.part("pad", synth="supersaw", envelope="pad", volume=0.12,
                 reverb=0.75, reverb_type="taj_mahal",
                 chorus=0.4, chorus_rate=0.2,
                 chorus_depth=0.01, lowpass=600)
pad.lfo("lowpass", rate=0.008, min=400, max=5000, bars=128, shape="triangle")

# Bars 1-16: dark, barely there
for _ in range(4):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=40)

# Bars 17-48: slowly swelling
for _ in range(8):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=55)

# Bars 49-96: full, warm
for _ in range(12):
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=70)

# Bars 97-128: fading
for rep in range(8):
    vel = max(20, 65 - rep * 6)
    for chord in prog:
        pad.add(chord, Duration.WHOLE, velocity=vel)

# ── BASS — enters with the kick, bar 49 ────────────────────────
bass = score.part("bass", synth="saw", envelope="pluck", volume=0.35,
                  lowpass=250, distortion=0.15, distortion_drive=2.5,
                  sub_osc=0.5, sidechain=0.3)

# Bars 1-48: silence
for _ in range(48):
    bass.rest(Duration.WHOLE)

# Bars 49-96: the groove
bass_line = [
    (F.add(-24), Duration.EIGHTH), (None, Duration.EIGHTH),
    (F.add(-24), Duration.EIGHTH), (None, Duration.EIGHTH),
    (F.add(-24), Duration.EIGHTH), (None, Duration.QUARTER),
    (Ab.add(-24), Duration.EIGHTH),
]
for _ in range(12):
    for note, dur in bass_line:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=100)

# Bars 97-128: fading
for rep in range(8):
    vel = max(20, 90 - rep * 10)
    for note, dur in bass_line:
        if note is None:
            bass.rest(dur)
        else:
            bass.add(note, dur, velocity=vel)

# ── KICK — the Strobe moment, enters bar 49 ────────────────────
kick = score.part("kick", volume=0.6, humanize=0.03)

# Bars 1-48: no kick — this IS the point
for _ in range(48):
    kick.rest(Duration.WHOLE)

# Bars 49-96: four on the floor — the release
for _ in range(48):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=115)

# Bars 97-112: kick continues, stable
for _ in range(16):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=108)

# Bars 113-128: kick fades last — the final heartbeat
for bar in range(16):
    vel = max(25, 105 - bar * 5)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# ── CLAP — with the kick ───────────────────────────────────────
clap = score.part("clap", volume=0.3, reverb=0.15, humanize=0.04)

# Bars 1-48: silence
for _ in range(48):
    clap.rest(Duration.WHOLE)

# Bars 49-96: 2 and 4
for _ in range(48):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=95)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=98)

# Bars 97-128: fading
for bar in range(32):
    vel = max(20, 95 - bar * 2)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=vel)

# ── HATS — offbeat, with the kick ──────────────────────────────
hats = score.part("hats", volume=0.25, humanize=0.04)

# Bars 1-48: silence
for _ in range(48):
    hats.rest(Duration.WHOLE)

# Bars 49-96: offbeat 8ths
for _ in range(48):
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=70)

# Bars 97-128: fading
for bar in range(32):
    vel = max(20, 70 - bar * 2)
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=vel)

# ── NES MELODY — emotional square wave, the heart of the peak ───
nes = score.part("nes", synth="square", envelope="organ", volume=0.28,
                 reverb=0.5, reverb_type="taj_mahal",
                 delay=0.35, delay_time=0.234, delay_feedback=0.45,
                 lowpass=4000, pan=-0.1, humanize=0.05)

# Bars 1-64: silence
for _ in range(64):
    nes.rest(Duration.WHOLE)

# Bars 65-80: the emotional peak — simple, singing melody
nes_melody = [
    (F.add(12), Duration.HALF, 85),
    (Eb.add(12), Duration.QUARTER, 80),
    (C.add(12), Duration.QUARTER, 78),
    (Db.add(12), Duration.HALF, 82),
    (C.add(12), Duration.HALF, 80),
    (Ab, Duration.HALF, 78),
    (Bb, Duration.QUARTER, 75),
    (C.add(12), Duration.QUARTER, 80),
    (F.add(12), Duration.WHOLE, 88),
]
for _ in range(4):
    for note, dur, vel in nes_melody:
        nes.add(note, dur, velocity=vel)

# Bars 81-96: melody fades
for rep in range(2):
    vel_off = rep * 15
    for note, dur, vel in nes_melody:
        nes.add(note, dur, velocity=max(25, vel - vel_off))
for _ in range(8):
    nes.rest(Duration.WHOLE)

# Bars 97-128: silence
for _ in range(32):
    nes.rest(Duration.WHOLE)

# ── PLUCK STABS — offbeat chords, bars 65-96 ───────────────────
pluck = score.part("pluck", synth="saw", envelope="pluck", volume=0.18,
                   reverb=0.25, delay=0.25, delay_time=0.234,
                   delay_feedback=0.35, lowpass=2500, detune=8,
                   pan=0.25)

# Bars 1-64: silence
for _ in range(64):
    pluck.rest(Duration.WHOLE)

# Bars 65-96: the peak — offbeat stabs
for _ in range(8):
    for chord in prog:
        pluck.rest(Duration.EIGHTH)
        pluck.add(chord, Duration.EIGHTH, velocity=85)
        pluck.rest(Duration.QUARTER)
        pluck.rest(Duration.EIGHTH)
        pluck.add(chord, Duration.EIGHTH, velocity=80)
        pluck.rest(Duration.QUARTER)

# Bars 97-128: silence
for _ in range(32):
    pluck.rest(Duration.WHOLE)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 128")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing GHOST PROTOCOL (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing GHOST PROTOCOL...")
    play_score(score)
