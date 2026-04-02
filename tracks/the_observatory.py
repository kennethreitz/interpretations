"""
THE OBSERVATORY — chapel harmonies broadcast through shortwave static.
An organ learns to levitate. By the time the kick arrives,
the room is already in orbit.

G minor, 112 BPM. Radio hiss, bell, organ, choir, arp,
sub bass, and a patient house pulse.
"""

from pytheory import Key, Duration, Score, play_score
from pytheory.rhythm import DrumSound

key = Key("G", "minor")
s = key.scale  # G A Bb C D Eb F

G  = s[0]
A  = s[1]
Bb = s[2]
C  = s[3]
D  = s[4]
Eb = s[5]
F  = s[6]

score = Score("4/4", bpm=112)

K  = DrumSound.KICK
CL = DrumSound.CLAP
CH = DrumSound.CLOSED_HAT
OH = DrumSound.OPEN_HAT

prog = key.progression("i", "VI", "III", "VII")  # Gm - Eb - Bb - F
roots = [G.add(-24), Eb.add(-24), Bb.add(-24), F.add(-24)]

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (96 bars, ~5.1 minutes at 112 BPM):
#   Bars  1-8:   Shortwave hiss + bell. Empty room, open sky.
#   Bars  9-16:  Organ enters — first human architecture.
#   Bars 17-32:  Arp appears, still no drums. The orbit begins.
#   Bars 33-48:  Kick/sub/clap enter — lift.
#   Bars 49-64:  Choir + signal melody — the windows open.
#   Bars 65-80:  Peak — full transmission, bright and weightless.
#   Bars 81-88:  Drums thin out. Organ and choir suspend.
#   Bars 89-96:  Static, bell, and one last heartbeat.
# ═══════════════════════════════════════════════════════════════════

# ── RADIO HISS — the sky itself ───────────────────────────────────
radio = score.part("radio", synth="noise", envelope="pad", volume=0.04,
                   reverb=0.85, reverb_type="taj_mahal",
                   lowpass=900, pan=-0.35)
radio.lfo("lowpass", rate=0.012, min=300, max=1800, bars=96, shape="sine")
radio.lfo("volume", rate=0.02, min=0.02, max=0.06, bars=96, shape="triangle")

for _ in range(96):
    radio.add(G, Duration.WHOLE, velocity=25)

# ── BOWL — section markers, like light reflecting off metal ──────
bowl = score.part("bowl", instrument="singing_bowl", volume=0.42,
                  reverb=1.0, reverb_type="taj_mahal",
                  delay=0.25, delay_time=0.875, delay_feedback=0.35,
                  pan=0.2)

marker_bars = {1: 78, 9: 72, 17: 68, 33: 75, 49: 72, 65: 76, 81: 60, 89: 54}
for bar in range(1, 97):
    if bar in marker_bars:
        note = G.add(-24) if bar < 65 else D.add(-12)
        bowl.add(note, Duration.WHOLE, velocity=marker_bars[bar])
    else:
        bowl.rest(Duration.WHOLE)

# ── ORGAN — square-wave chapel, warm but slightly unreal ──────────
organ = score.part("organ", synth="square", envelope="organ", volume=0.14,
                   reverb=0.78, reverb_type="taj_mahal",
                   chorus=0.25, chorus_rate=0.18, chorus_depth=0.01,
                   lowpass=1800, pan=-0.15)

low_prog = [c.transpose(-12) for c in prog]
mid_prog = prog
high_prog = [c.transpose(12) for c in prog]

# Bars 1-8: silence
for _ in range(8):
    organ.rest(Duration.WHOLE)

# Bars 9-16: first statement, low and slow
for _ in range(2):
    for chord in low_prog:
        organ.add(chord, Duration.WHOLE, velocity=52)

# Bars 17-32: stronger, still no pulse beneath it
for _ in range(4):
    for chord in low_prog:
        organ.add(chord, Duration.WHOLE, velocity=60)

# Bars 33-64: fully present
for _ in range(8):
    for chord in mid_prog:
        organ.add(chord, Duration.WHOLE, velocity=72)

# Bars 65-80: brighter voicings at the peak
for _ in range(4):
    for chord in high_prog:
        organ.add(chord, Duration.WHOLE, velocity=66)

# Bars 81-88: suspended, looking down at the earth
for _ in range(2):
    for chord in [mid_prog[0], mid_prog[1], mid_prog[0], mid_prog[3]]:
        organ.add(chord, Duration.WHOLE, velocity=54)

# Bars 89-96: fading architecture
for chord, vel in zip(low_prog * 2, [50, 44, 40, 36, 30, 24, 16, 8]):
    organ.add(chord, Duration.WHOLE, velocity=vel)

# ── CHOIR — the air inside the room starts singing ────────────────
choir = score.part("choir", instrument="choir", volume=0.11,
                   reverb=0.95, reverb_type="taj_mahal",
                   chorus=0.35, chorus_rate=0.08, chorus_depth=0.012,
                   pan=0.25)

# Bars 1-32: silence
for _ in range(32):
    choir.rest(Duration.WHOLE)

# Bars 33-48: arrives behind the drums, soft
for _ in range(4):
    for chord in prog:
        choir.add(chord, Duration.WHOLE, velocity=38)

# Bars 49-80: fully open
for _ in range(8):
    for chord in prog:
        choir.add(chord, Duration.WHOLE, velocity=48)

# Bars 81-88: held breath
for _ in range(2):
    for chord in [prog[0], prog[1], prog[0], prog[3]]:
        choir.add(chord, Duration.WHOLE, velocity=36)

# Bars 89-96: gone
for _ in range(8):
    choir.rest(Duration.WHOLE)

# ── HALO PAD — the light around the chord, not the chord itself ──
halo = score.part("halo", synth="supersaw", envelope="pad", volume=0.08,
                  reverb=0.65, reverb_type="taj_mahal",
                  chorus=0.45, chorus_rate=0.2, chorus_depth=0.008,
                  lowpass=1200, pan=-0.25)
halo.lfo("lowpass", rate=0.01, min=500, max=2800, bars=96, shape="triangle")

# Bars 1-48: silence
for _ in range(48):
    halo.rest(Duration.WHOLE)

# Bars 49-80: glow at the peak
for _ in range(8):
    for chord in prog:
        halo.add(chord, Duration.WHOLE, velocity=42)

# Bars 81-96: silence
for _ in range(16):
    halo.rest(Duration.WHOLE)

# ── ARP — the signal lock, patient and inevitable ────────────────
arp = score.part("arp", synth="saw", envelope="pluck", volume=0.35,
                 reverb=0.3, delay=0.35, delay_time=0.234,
                 delay_feedback=0.42, lowpass=1300, detune=5,
                 pan=0.15, humanize=0.03)
arp.lfo("lowpass", rate=0.009, min=900, max=5200, bars=96, shape="saw")

P1 = [
    G.add(12), None, D.add(12), None,
    Bb, None, F.add(12), None,
    G.add(12), None, D.add(12), None,
    C.add(12), Bb, F, D,
]

P2 = [
    G.add(12), D.add(12), F.add(12), D.add(12),
    Eb.add(12), D.add(12), Bb, D.add(12),
    G.add(12), D.add(12), F.add(12), D.add(12),
    C.add(12), Bb, F, D,
]


def arp_bar(notes, vel):
    for note in notes:
        if note is None:
            arp.rest(Duration.SIXTEENTH)
        else:
            arp.add(note, Duration.SIXTEENTH, velocity=vel)


# Bars 1-16: silence
for _ in range(16):
    arp.rest(Duration.WHOLE)

# Bars 17-32: emerges quietly
for _ in range(8):
    arp_bar(P1, 50)
    arp_bar(P2, 54)

# Bars 33-48: steady and confident
for _ in range(8):
    arp_bar(P1, 64)
    arp_bar(P2, 68)

# Bars 49-64: brighter
for _ in range(8):
    arp_bar(P1, 76)
    arp_bar(P2, 80)

# Bars 65-80: peak — no more hesitation
for _ in range(8):
    arp_bar(P2, 88)
    arp_bar(P1, 92)

# Bars 81-88: thinning out
for _ in range(4):
    arp_bar(P1, 62)
    arp_bar(P2, 58)

# Bars 89-96: silence
for _ in range(8):
    arp.rest(Duration.WHOLE)

# ── SUB — the floor finally arrives beneath the chapel ───────────
sub = score.part("sub", synth="sine", envelope="pad", volume=0.28,
                 lowpass=120, distortion=0.12, distortion_drive=2.5,
                 sub_osc=0.4, sidechain=0.25)

# Bars 1-32: silence
for _ in range(32):
    sub.rest(Duration.WHOLE)

# Bars 33-80: root motion, simple and physical
for _ in range(12):
    for root in roots:
        sub.add(root, Duration.HALF, velocity=92)
        sub.rest(Duration.HALF)

# Bars 81-88: just the home note, held
for _ in range(8):
    sub.add(G.add(-24), Duration.HALF, velocity=72)
    sub.rest(Duration.HALF)

# Bars 89-96: fading heartbeat
for vel in [66, 58, 50, 42, 34, 26, 16, 0]:
    if vel > 0:
        sub.add(G.add(-24), Duration.HALF, velocity=vel)
        sub.rest(Duration.HALF)
    else:
        sub.rest(Duration.WHOLE)

# ── KICK — the patient release ────────────────────────────────────
kick = score.part("kick", volume=0.55, humanize=0.03)

# Bars 1-32: none
for _ in range(32):
    kick.rest(Duration.WHOLE)

# Bars 33-80: four on the floor
for _ in range(48):
    for _beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=114)

# Bars 81-88: still there, but more human now
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=95)
    kick.rest(Duration.QUARTER)
    kick.hit(K, Duration.QUARTER, velocity=88)
    kick.rest(Duration.QUARTER)

# Bars 89-96: last pulses
for vel in [88, 82, 76, 68, 58, 46, 32, 18]:
    kick.hit(K, Duration.QUARTER, velocity=vel)
    kick.rest(Duration.DOTTED_HALF)

# ── CLAP — 2 and 4, but never aggressive ─────────────────────────
clap = score.part("clap", volume=0.28, reverb=0.18,
                  delay=0.1, delay_time=0.268, delay_feedback=0.15,
                  pan=-0.1, humanize=0.04)

# Bars 1-32: silence
for _ in range(32):
    clap.rest(Duration.WHOLE)

# Bars 33-80: standard house backbeat
for _ in range(48):
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=96)
    clap.rest(Duration.QUARTER)
    clap.hit(CL, Duration.QUARTER, velocity=98)

# Bars 81-96: silence
for _ in range(16):
    clap.rest(Duration.WHOLE)

# ── HATS — offbeat shimmer ────────────────────────────────────────
hats = score.part("hats", volume=0.22, pan=0.1, humanize=0.04)

# Bars 1-32: silence
for _ in range(32):
    hats.rest(Duration.WHOLE)

# Bars 33-80: offbeat 8ths, occasional open hat on the turn
for bar in range(48):
    for beat in range(4):
        hats.rest(Duration.EIGHTH)
        sound = OH if beat == 3 and bar % 4 == 3 else CH
        vel = 74 if sound == CH else 68
        hats.hit(sound, Duration.EIGHTH, velocity=vel)

# Bars 81-88: thinner
for _ in range(8):
    for _beat in range(4):
        hats.rest(Duration.EIGHTH)
        hats.hit(CH, Duration.EIGHTH, velocity=52)

# Bars 89-96: silence
for _ in range(8):
    hats.rest(Duration.WHOLE)

# ── SIGNAL — the melody finally resolves the transmission ────────
signal = score.part("signal", instrument="theremin", volume=0.3,
                    reverb=0.35, reverb_type="taj_mahal",
                    delay=0.2, delay_time=0.375, delay_feedback=0.25,
                    pan=0.35, humanize=0.05)

# Bars 1-48: silence
for _ in range(48):
    signal.rest(Duration.WHOLE)

phrase_a = [
    (D.add(12), Duration.HALF, 70, 0.2),
    (F.add(12), Duration.QUARTER, 74, 0.0),
    (G.add(12), Duration.QUARTER, 78, 0.35),
    (Bb.add(12), Duration.HALF, 80, -0.2),
    (A.add(12), Duration.QUARTER, 68, 0.0),
    (G.add(12), Duration.QUARTER, 72, 0.0),
    (F.add(12), Duration.HALF, 70, 0.15),
    (Eb.add(12), Duration.QUARTER, 68, 0.0),
    (D.add(12), Duration.QUARTER, 66, -0.1),
    (G.add(12), Duration.WHOLE, 78, 0.0),
]

phrase_b = [
    (G.add(12), Duration.QUARTER, 78, 0.0),
    (Bb.add(12), Duration.QUARTER, 82, 0.15),
    (D.add(24), Duration.HALF, 86, -0.2),
    (F.add(24), Duration.HALF, 84, 0.0),
    (Eb.add(24), Duration.QUARTER, 78, 0.0),
    (D.add(24), Duration.QUARTER, 76, 0.0),
    (Bb.add(12), Duration.HALF, 72, -0.15),
    (A.add(12), Duration.QUARTER, 68, 0.0),
    (G.add(12), Duration.QUARTER, 66, 0.0),
    (F.add(12), Duration.WHOLE, 74, 0.0),
]

# Bars 49-64: first message
for _ in range(4):
    for note, dur, vel, bend in phrase_a:
        signal.add(note, dur, velocity=vel, bend=bend)

# Bars 65-80: stronger reply
for _ in range(4):
    for note, dur, vel, bend in phrase_b:
        signal.add(note, dur, velocity=vel, bend=bend)

# Bars 81-96: silence
for _ in range(16):
    signal.rest(Duration.WHOLE)

# ═══════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 112")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing THE OBSERVATORY (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing THE OBSERVATORY...")
    play_score(score)
