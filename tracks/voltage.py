"""
VOLTAGE — raw oscillators, nothing else.
Rhythm is pitch. Pitch is rhythm. Aggressive, monophonic, electric.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("F", "minor")
s = key.scale  # F G Ab Bb C Db Eb

F  = s[0]; G  = s[1]; Ab = s[2]; Bb = s[3]
C  = s[4]; Db = s[5]; Eb = s[6]

score = Score("4/4", bpm=138)

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (96 bars, ~4.5 min):
#   Bars  1-8:   Sine sub — pulsing root, the heartbeat
#   Bars  9-16:  Saw enters — aggressive mono line, rhythmic pitch
#   Bars 17-24:  Pulse wave — counter-rhythm, interlocking
#   Bars 25-32:  All three locked — machine groove
#   Bars 33-40:  BREAKDOWN 1 — sine bends, tension, silence
#   Bars 41-48:  THE DROP — everything + kick
#   Bars 49-56:  SAW ARP SOLO — 16th note arps going wild
#   Bars 57-64:  PULSE ARP SOLO — square wave takes over
#   Bars 65-72:  BREAKDOWN 2 — stripped back, bends, rebuilding
#   Bars 73-80:  FINAL DROP — all three arping together
#   Bars 81-88:  PEAK — 32nd note chaos, maximum aggression
#   Bars 89-96:  Collapse — oscillators die one by one
# ═══════════════════════════════════════════════════════════════════

# ── Reusable patterns ──────────────────────────────────────────
saw_line_a = [
    (F, Duration.SIXTEENTH, 105), (None, Duration.SIXTEENTH, 0),
    (F, Duration.SIXTEENTH, 100), (Ab, Duration.SIXTEENTH, 95),
    (F, Duration.SIXTEENTH, 108), (None, Duration.SIXTEENTH, 0),
    (Eb, Duration.EIGHTH, 92),
    (F, Duration.SIXTEENTH, 110), (C, Duration.SIXTEENTH, 95),
    (F, Duration.SIXTEENTH, 105), (None, Duration.SIXTEENTH, 0),
    (Db, Duration.EIGHTH, 98),
    (F, Duration.EIGHTH, 112),
]

saw_line_b = [
    (F, Duration.SIXTEENTH, 110), (C.add(12), Duration.SIXTEENTH, 100),
    (F, Duration.SIXTEENTH, 108), (None, Duration.SIXTEENTH, 0),
    (Ab, Duration.SIXTEENTH, 102), (F, Duration.SIXTEENTH, 112),
    (Db, Duration.EIGHTH, 95),
    (F, Duration.SIXTEENTH, 115), (Eb, Duration.SIXTEENTH, 98),
    (C, Duration.SIXTEENTH, 105), (F, Duration.SIXTEENTH, 110),
    (None, Duration.EIGHTH, 0),
    (F, Duration.EIGHTH, 118),
]

pulse_line = [
    (None, Duration.SIXTEENTH, 0), (C.add(12), Duration.SIXTEENTH, 88),
    (None, Duration.EIGHTH, 0),
    (Ab, Duration.SIXTEENTH, 85), (None, Duration.SIXTEENTH, 0),
    (C.add(12), Duration.EIGHTH, 90),
    (None, Duration.SIXTEENTH, 0), (Db.add(12), Duration.SIXTEENTH, 82),
    (C.add(12), Duration.SIXTEENTH, 88), (None, Duration.SIXTEENTH, 0),
    (Ab, Duration.EIGHTH, 85),
    (C.add(12), Duration.EIGHTH, 92),
]

pulse_line_b = [
    (C.add(12), Duration.SIXTEENTH, 92), (None, Duration.SIXTEENTH, 0),
    (Ab, Duration.SIXTEENTH, 85), (C.add(12), Duration.SIXTEENTH, 90),
    (None, Duration.EIGHTH, 0),
    (Eb.add(12), Duration.EIGHTH, 88),
    (C.add(12), Duration.SIXTEENTH, 95), (Ab, Duration.SIXTEENTH, 82),
    (None, Duration.SIXTEENTH, 0), (C.add(12), Duration.SIXTEENTH, 90),
    (Db.add(12), Duration.EIGHTH, 85),
    (C.add(12), Duration.EIGHTH, 95),
]

def play_pattern(part, pattern, reps=1, vel_offset=0):
    for _ in range(reps):
        for note, dur, vel in pattern:
            if note is None:
                part.rest(dur)
            else:
                part.add(note, dur, velocity=min(127, max(20, vel + vel_offset)))


# ── SINE — the sub, the foundation, the pulse ──────────────────
sine = score.part("sine", synth="sine", volume=0.8,
                  lowpass=200, distortion=0.2, distortion_drive=2.5,
                  sub_osc=0.5, reverb=0.12, reverb_decay=0.6,
                  pan=0.05)

# Bars 1-8: pulsing root
for _ in range(8):
    sine.add(F.add(-24), Duration.EIGHTH, velocity=110)
    sine.rest(Duration.EIGHTH)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=95)
    sine.rest(Duration.EIGHTH)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=110)
    sine.add(F.add(-24), Duration.SIXTEENTH, velocity=85)
    sine.rest(Duration.SIXTEENTH)
    sine.add(F.add(-24), Duration.QUARTER, velocity=105)

# Bars 9-16: pitch movement
for _ in range(4):
    sine.add(F.add(-24), Duration.EIGHTH, velocity=110)
    sine.rest(Duration.EIGHTH)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=95)
    sine.add(Ab.add(-24), Duration.EIGHTH, velocity=100)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=110)
    sine.add(Eb.add(-24), Duration.SIXTEENTH, velocity=90)
    sine.rest(Duration.SIXTEENTH)
    sine.add(F.add(-24), Duration.QUARTER, velocity=105)
for _ in range(4):
    sine.add(F.add(-24), Duration.EIGHTH, velocity=110)
    sine.rest(Duration.EIGHTH)
    sine.add(Db.add(-24), Duration.EIGHTH, velocity=100)
    sine.add(C.add(-24), Duration.EIGHTH, velocity=95)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=112)
    sine.add(Ab.add(-24), Duration.SIXTEENTH, velocity=88)
    sine.rest(Duration.SIXTEENTH)
    sine.add(F.add(-24), Duration.QUARTER, velocity=108)

# Bars 17-32: locked groove
for _ in range(16):
    sine.add(F.add(-24), Duration.EIGHTH, velocity=112)
    sine.rest(Duration.EIGHTH)
    sine.add(Ab.add(-24), Duration.EIGHTH, velocity=98)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=108)
    sine.add(Db.add(-24), Duration.SIXTEENTH, velocity=95)
    sine.add(C.add(-24), Duration.SIXTEENTH, velocity=92)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=115)
    sine.add(Eb.add(-24), Duration.EIGHTH, velocity=100)

# Bars 33-40: BREAKDOWN 1 — long bends
sine.set(volume=0.9)
sine.add(F.add(-24), Duration.WHOLE, velocity=115, bend=-2.0)
sine.add(F.add(-24), Duration.WHOLE, velocity=110, bend=3.0)
sine.rest(Duration.WHOLE)
sine.add(C.add(-24), Duration.HALF, velocity=108, bend=-1.5)
sine.rest(Duration.HALF)
sine.add(F.add(-24), Duration.WHOLE, velocity=118, bend=2.0)
sine.rest(Duration.WHOLE)
sine.add(Db.add(-24), Duration.HALF, velocity=105, bend=-3.0)
sine.add(F.add(-24), Duration.HALF, velocity=120, bend=1.0)

# Bars 41-64: DROP + arp solos — locked groove under the solos
sine.set(volume=0.85)
for _ in range(24):
    sine.add(F.add(-24), Duration.EIGHTH, velocity=118)
    sine.add(Ab.add(-24), Duration.SIXTEENTH, velocity=100)
    sine.add(F.add(-24), Duration.SIXTEENTH, velocity=112)
    sine.add(Db.add(-24), Duration.EIGHTH, velocity=105)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=115)
    sine.add(C.add(-24), Duration.SIXTEENTH, velocity=98)
    sine.add(Eb.add(-24), Duration.SIXTEENTH, velocity=95)
    sine.add(F.add(-24), Duration.QUARTER, velocity=120)

# Bars 65-72: BREAKDOWN 2 — bends again, rebuilding
sine.set(volume=0.9)
sine.add(F.add(-24), Duration.WHOLE, velocity=120, bend=3.0)
sine.add(C.add(-24), Duration.WHOLE, velocity=115, bend=-2.0)
sine.add(F.add(-24), Duration.HALF, velocity=118, bend=1.5)
sine.add(Ab.add(-24), Duration.HALF, velocity=110, bend=-1.0)
sine.rest(Duration.WHOLE)
# Rebuilding
for _ in range(4):
    sine.add(F.add(-24), Duration.EIGHTH, velocity=112)
    sine.rest(Duration.EIGHTH)
    sine.add(Ab.add(-24), Duration.EIGHTH, velocity=100)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=115)
    sine.add(C.add(-24), Duration.SIXTEENTH, velocity=98)
    sine.add(Db.add(-24), Duration.SIXTEENTH, velocity=95)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=118)
    sine.add(Eb.add(-24), Duration.EIGHTH, velocity=102)

# Bars 73-88: FINAL DROP + PEAK
sine.set(volume=0.85)
for _ in range(16):
    sine.add(F.add(-24), Duration.EIGHTH, velocity=120)
    sine.add(Ab.add(-24), Duration.SIXTEENTH, velocity=105)
    sine.add(F.add(-24), Duration.SIXTEENTH, velocity=115)
    sine.add(Db.add(-24), Duration.EIGHTH, velocity=108)
    sine.add(F.add(-24), Duration.EIGHTH, velocity=118)
    sine.add(C.add(-24), Duration.SIXTEENTH, velocity=102)
    sine.add(Eb.add(-24), Duration.SIXTEENTH, velocity=98)
    sine.add(F.add(-24), Duration.QUARTER, velocity=122)

# Bars 89-96: dying
for bar in range(8):
    vel = max(30, 115 - bar * 12)
    sine.add(F.add(-24), Duration.HALF, velocity=vel, bend=-0.5 * bar)
    sine.rest(Duration.HALF)

# ── SAW — aggressive, cutting, the main voice ──────────────────
saw = score.part("saw", synth="saw", volume=0.55,
                 lowpass=4000, distortion=0.3, distortion_drive=3.5,
                 saturation=0.7, legato=True, glide=0.03,
                 reverb=0.25, reverb_type="spring",
                 delay=0.35, delay_time=0.326, delay_feedback=0.4,
                 pan=-0.25)
saw.lfo("lowpass", rate=0.015, min=1500, max=8000, bars=96, shape="saw")

# Bars 1-8: silent
for _ in range(8):
    saw.rest(Duration.WHOLE)

# Bars 9-16: enters
play_pattern(saw, saw_line_a, 8)

# Bars 17-24: wider intervals
play_pattern(saw, saw_line_b, 8)

# Bars 25-32: patterns alternate
for _ in range(4):
    play_pattern(saw, saw_line_a)
    play_pattern(saw, saw_line_b)

# Bars 33-40: BREAKDOWN 1 — screaming bends
saw.set(volume=0.65)
saw.add(F.add(12), Duration.WHOLE, velocity=105, bend=2.0)
saw.add(Eb.add(12), Duration.WHOLE, velocity=100, bend=-1.5)
saw.rest(Duration.WHOLE)
saw.add(Ab.add(12), Duration.HALF, velocity=108, bend=3.0)
saw.add(F.add(12), Duration.HALF, velocity=102, bend=-1.0)
saw.add(C.add(12), Duration.WHOLE, velocity=110, bend=-2.0)
saw.rest(Duration.WHOLE)
saw.add(F.add(12), Duration.HALF, velocity=115, bend=1.5)
saw.add(Db.add(12), Duration.HALF, velocity=100, bend=-2.5)

# Bars 41-48: DROP — pattern A full power
saw.set(volume=0.7)
play_pattern(saw, saw_line_a, 8, vel_offset=10)

# ═══════════════════════════════════════════════════════════════════
# Bars 49-56: SAW ARP SOLO — the saw goes absolutely nuts
# ═══════════════════════════════════════════════════════════════════
saw.set(volume=0.75)

# Arp 1: minor triad arps — 16ths, climbing through inversions
arp_i  = [F, Ab, C.add(12), Ab, F, C, Ab.add(-12), C]
arp_iv = [Bb, Db.add(12), F.add(12), Db.add(12), Bb, F, Db, F]
arp_v  = [C, Eb, G, Eb, C, G.add(-12), Eb.add(-12), G.add(-12)]
arp_vi = [Db, F, Ab, F, Db, Ab.add(-12), F.add(-12), Ab.add(-12)]

for _ in range(2):
    for note in arp_i:
        saw.add(note, Duration.SIXTEENTH, velocity=115)
    for note in arp_iv:
        saw.add(note, Duration.SIXTEENTH, velocity=112)
    for note in arp_v:
        saw.add(note, Duration.SIXTEENTH, velocity=118)
    for note in arp_vi:
        saw.add(note, Duration.SIXTEENTH, velocity=110)

# Arp 2: wide crazy arps — octave jumps
arp_wild = [F, F.add(12), Ab, Ab.add(12), C, C.add(12), Eb, Eb.add(12)]
arp_wild_down = [Eb.add(12), C.add(12), Ab, F, Eb, C.add(-12), Ab.add(-12), F.add(-12)]
for _ in range(2):
    for note in arp_wild:
        saw.add(note, Duration.SIXTEENTH, velocity=120)
    for note in arp_wild_down:
        saw.add(note, Duration.SIXTEENTH, velocity=118)

# Arp 3: 32nd note burst — chromatic-ish madness
saw_solo_32 = [F, G, Ab, Bb, C, Db, Eb, F.add(12),
               Eb, Db, C, Bb, Ab, G, F, G,
               Ab, C, Eb, Ab.add(12), Eb, C, Ab, F,
               C.add(12), Ab, F, C, Ab.add(-12), F.add(-12), Ab.add(-12), C.add(-12)]
for note in saw_solo_32:
    saw.add(note, 0.125, velocity=125)

# ═══════════════════════════════════════════════════════════════════
# Bars 57-64: PULSE ARP SOLO — square wave takes the lead
# ═══════════════════════════════════════════════════════════════════
# Saw drops to support
saw.set(volume=0.4)
play_pattern(saw, saw_line_a, 8)

# Bars 65-72: BREAKDOWN 2
saw.set(volume=0.6)
saw.add(F.add(12), Duration.WHOLE, velocity=108, bend=-2.5)
saw.add(C.add(12), Duration.WHOLE, velocity=105, bend=2.0)
saw.rest(Duration.WHOLE)
saw.add(Ab.add(12), Duration.WHOLE, velocity=110, bend=3.0)
# Rebuild
saw.set(volume=0.65)
play_pattern(saw, saw_line_b, 4, vel_offset=5)

# Bars 73-80: FINAL DROP
saw.set(volume=0.75)
play_pattern(saw, saw_line_a, 4, vel_offset=12)
play_pattern(saw, saw_line_b, 4, vel_offset=12)

# Bars 81-88: PEAK — 32nd note chaos
saw.set(volume=0.8)
shred_up = [F, G, Ab, Bb, C, Db, Eb, F.add(12)]
shred_down = [F.add(12), Eb, Db, C, Bb, Ab, G, F]
shred_wide = [F, C.add(12), Ab, F.add(12), Db, Eb.add(12), Bb, F.add(12)]

for _ in range(2):
    for note in shred_up:
        saw.add(note, 0.125, velocity=122)
    for note in shred_down:
        saw.add(note, 0.125, velocity=120)
for _ in range(2):
    for note in shred_wide:
        saw.add(note, 0.125, velocity=127)
    for note in reversed(shred_wide):
        saw.add(note, 0.125, velocity=125)
# Final ascending scream
for note in [F, Ab, C, Eb, F.add(12), Ab.add(12), C.add(12), Eb.add(12),
             F.add(24), Eb.add(12), C.add(12), Ab.add(12), F.add(12), Eb, C, F]:
    saw.add(note, 0.125, velocity=127)
# Held scream
saw.add(F.add(12), Duration.WHOLE, velocity=125, bend=3.0)

# Bars 89-96: dying
saw.set(volume=0.35)
play_pattern(saw, saw_line_a, 4, vel_offset=-20)
for _ in range(4):
    saw.rest(Duration.WHOLE)

# ── PULSE — square wave, digital, counter-rhythm ───────────────
pulse = score.part("pulse", synth="square", volume=0.35,
                   lowpass=3000, distortion=0.15, distortion_drive=2.0,
                   saturation=0.5, reverb=0.15, reverb_type="taj_mahal",
                   delay=0.3, delay_time=0.435, delay_feedback=0.5,
                   pan=0.3)
pulse.lfo("lowpass", rate=0.03, min=800, max=5000, bars=96, shape="triangle")

# Bars 1-16: silent
for _ in range(16):
    pulse.rest(Duration.WHOLE)

# Bars 17-24: enters syncopated
play_pattern(pulse, pulse_line, 8)

# Bars 25-32: tighter
play_pattern(pulse, pulse_line_b, 8)

# Bars 33-40: BREAKDOWN 1 — stuttering
pulse.set(volume=0.4)
for _ in range(4):
    pulse.add(C.add(12), Duration.SIXTEENTH, velocity=95)
    pulse.rest(Duration.SIXTEENTH)
    pulse.add(C.add(12), Duration.SIXTEENTH, velocity=88)
    pulse.rest(Duration.SIXTEENTH)
    pulse.rest(Duration.HALF)
for _ in range(4):
    pulse.rest(Duration.WHOLE)

# Bars 41-48: DROP
pulse.set(volume=0.45)
play_pattern(pulse, pulse_line_b, 8, vel_offset=8)

# Bars 49-56: support under saw solo
pulse.set(volume=0.3)
play_pattern(pulse, pulse_line, 8)

# ═══════════════════════════════════════════════════════════════════
# Bars 57-64: PULSE ARP SOLO — square wave goes crazy
# ═══════════════════════════════════════════════════════════════════
pulse.set(volume=0.55)

# Arp 1: bouncing octaves — hypnotic
p_arp1 = [C.add(12), C, C.add(12), Ab, C.add(12), Eb.add(12), C.add(12), F.add(12)]
for _ in range(4):
    for note in p_arp1:
        pulse.add(note, Duration.SIXTEENTH, velocity=105)
    for note in reversed(p_arp1):
        pulse.add(note, Duration.SIXTEENTH, velocity=100)

# Arp 2: staccato — rapid fire with rests
p_arp2 = [
    (C.add(12), 108), (None, 0), (Ab, 95), (C.add(12), 105),
    (Eb.add(12), 110), (None, 0), (C.add(12), 102), (None, 0),
    (F.add(12), 112), (Db.add(12), 98), (None, 0), (C.add(12), 108),
    (Ab, 95), (None, 0), (C.add(12), 105), (Eb.add(12), 110),
]
for _ in range(4):
    for note, vel in p_arp2:
        if note is None:
            pulse.rest(Duration.SIXTEENTH)
        else:
            pulse.add(note, Duration.SIXTEENTH, velocity=vel)

# Arp 3: 32nd notes — the fastest moment for pulse
p_solo_32 = [C.add(12), Ab, F, Ab, C.add(12), Eb.add(12), F.add(12), Eb.add(12),
             C.add(12), Ab, F, C, Ab.add(-12), F.add(-12), Ab.add(-12), C,
             F, Ab, C.add(12), F.add(12), Ab.add(12), F.add(12), C.add(12), Ab,
             F, C, Ab.add(-12), C, F, Ab, C.add(12), F.add(12)]
for note in p_solo_32:
    pulse.add(note, 0.125, velocity=118)

# Bars 65-72: BREAKDOWN 2 — drops out
pulse.set(volume=0.35)
for _ in range(4):
    pulse.add(C.add(12), Duration.SIXTEENTH, velocity=90)
    pulse.rest(Duration.SIXTEENTH)
    pulse.add(C.add(12), Duration.SIXTEENTH, velocity=82)
    pulse.rest(Duration.SIXTEENTH)
    pulse.rest(Duration.HALF)
for _ in range(4):
    pulse.rest(Duration.WHOLE)

# Bars 73-80: FINAL DROP — both patterns
pulse.set(volume=0.5)
play_pattern(pulse, pulse_line_b, 4, vel_offset=10)
play_pattern(pulse, pulse_line, 4, vel_offset=10)

# Bars 81-88: PEAK — rapid arps
pulse.set(volume=0.55)
pulse_arp = [C.add(12), Ab, F, Ab, C.add(12), Eb.add(12), C.add(12), Ab]
for _ in range(8):
    for note in pulse_arp:
        pulse.add(note, Duration.SIXTEENTH, velocity=105)
    for note in reversed(pulse_arp):
        pulse.add(note, Duration.SIXTEENTH, velocity=100)

# Bars 89-96: dies first
pulse.set(volume=0.2)
play_pattern(pulse, pulse_line, 4, vel_offset=-25)
for _ in range(4):
    pulse.rest(Duration.WHOLE)

# ── SYNC — hard sync oscillator, enters late ───────────────────
sync = score.part("sync", synth="hard_sync", volume=0.25,
                  lowpass=4000, distortion=0.2, distortion_drive=2.5,
                  reverb=0.15, reverb_type="spring",
                  delay=0.15, delay_time=0.234, delay_feedback=0.2,
                  pan=-0.15)

# Bars 1-48: silence
for _ in range(48):
    sync.rest(Duration.WHOLE)

# Bars 49-72: plays saw_line_a pattern
play_pattern(sync, saw_line_a, 24)

# Bars 73-96: silence
for _ in range(24):
    sync.rest(Duration.WHOLE)

# ── KICK — enters at bar 41 ───────────────────────────────────
K = DrumSound.KICK
kick = score.part("kick", volume=1.0, humanize=0.02,
                  distortion=0.15, distortion_drive=2.0)

for _ in range(40):
    kick.rest(Duration.WHOLE)

# Bars 41-64: four on the floor through both solos
for _ in range(24):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=120)

# Bars 65-72: breakdown — just beat 1
for _ in range(8):
    kick.hit(K, Duration.QUARTER, velocity=105)
    kick.rest(Duration.DOTTED_HALF)

# Bars 73-88: FINAL DROP + PEAK
for _ in range(16):
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=122)

# Bars 89-96: fading
for bar in range(8):
    vel = max(25, 118 - bar * 12)
    for beat in range(4):
        kick.hit(K, Duration.QUARTER, velocity=vel)

# ── NOISE HIT — percussive bursts ─────────────────────────────
noise = score.part("noise", synth="noise", envelope="pluck", volume=0.2,
                   lowpass=6000, highpass=2000,
                   distortion=0.5, distortion_drive=4.0,
                   pan=-0.15)

for _ in range(24):
    noise.rest(Duration.WHOLE)

# Bars 25-32: offbeat stabs
for _ in range(8):
    noise.rest(Duration.EIGHTH)
    noise.add(F, Duration.SIXTEENTH, velocity=80)
    noise.rest(Duration.SIXTEENTH)
    noise.rest(Duration.QUARTER)
    noise.rest(Duration.EIGHTH)
    noise.add(F, Duration.SIXTEENTH, velocity=75)
    noise.rest(Duration.SIXTEENTH)
    noise.rest(Duration.QUARTER)

# Bars 33-40: silent
for _ in range(8):
    noise.rest(Duration.WHOLE)

# Bars 41-64: snare position hits
for _ in range(24):
    noise.rest(Duration.QUARTER)
    noise.add(F, Duration.SIXTEENTH, velocity=90)
    noise.rest(Duration.EIGHTH)
    noise.rest(Duration.SIXTEENTH)
    noise.rest(Duration.QUARTER)
    noise.add(F, Duration.SIXTEENTH, velocity=92)
    noise.rest(Duration.EIGHTH)
    noise.rest(Duration.SIXTEENTH)

# Bars 65-72: silent
for _ in range(8):
    noise.rest(Duration.WHOLE)

# Bars 73-88: back full
for _ in range(16):
    noise.rest(Duration.QUARTER)
    noise.add(F, Duration.SIXTEENTH, velocity=95)
    noise.rest(Duration.EIGHTH)
    noise.rest(Duration.SIXTEENTH)
    noise.rest(Duration.QUARTER)
    noise.add(F, Duration.SIXTEENTH, velocity=98)
    noise.rest(Duration.EIGHTH)
    noise.rest(Duration.SIXTEENTH)

# Bars 89-96: fading
for bar in range(8):
    vel = max(20, 90 - bar * 10)
    noise.rest(Duration.QUARTER)
    noise.add(F, Duration.SIXTEENTH, velocity=vel)
    noise.rest(Duration.EIGHTH)
    noise.rest(Duration.SIXTEENTH)
    noise.rest(Duration.HALF)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: {key}")
print(f"BPM: 138")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing VOLTAGE (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing VOLTAGE...")
    play_score(score)
