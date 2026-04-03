"""
AN EXCEPTION OCCURRED — the mind shifts underneath you.
Beautiful, then disorienting, then bare, then whole again.
Piano-driven. Human. Every note placed by hand.
Eb major → minor → resolution. 80 BPM.
"""

from pytheory import Key, Duration, Score, Tone, play_score
from pytheory.rhythm import DrumSound

key = Key("Eb", "major")
key_major = key
key_minor = Key("Eb", "minor")
sm = key_major.scale  # Eb F G Ab Bb C D
sn = key_minor.scale  # Eb F Gb Ab Bb Cb Db

score = Score("4/4", bpm=80)

# Major scale tones
Eb = sm[0]; F = sm[1]; G = sm[2]; Ab = sm[3]
Bb = sm[4]; C = sm[5]; D = sm[6]

# Minor scale tones (for the shift)
Gb = sn[2]; Cb = sn[5]; Db = sn[6]

# ═══════════════════════════════════════════════════════════════════
# STRUCTURE (64 bars, ~3:12):
#   Bars  1-8:   STABLE — warm piano, everything's fine
#   Bars  9-16:  REACHING — exploring higher, spiritual, beautiful
#   Bars 17-24:  THE SHIFT — something's off. Octave jumps. Wrong notes.
#   Bars 25-32:  FALLING — the key changes, rhythm stumbles, disorienting
#   Bars 33-40:  THE ROOM — stripped to almost nothing. Bare. Quiet.
#   Bars 41-48:  FINDING GROUND — melody returns, tentative, changed
#   Bars 49-56:  RECOVERY — warmth comes back, but different. Wiser.
#   Bars 57-64:  GRATITUDE — full, resolved, the melody you remember
# ═══════════════════════════════════════════════════════════════════

# ── DEEP TAMBURA — washing bass, the ground you stand on ───────
deep = score.part("deep_tambura", synth="sine", envelope="pad", volume=0.2,
                  reverb=0.6, reverb_type="taj_mahal",
                  chorus=0.5, chorus_rate=0.04, chorus_depth=0.015,
                  lowpass=500, sub_osc=0.3, pan=-0.1)

# Bars 1-8: present from the start — you feel it before you hear it
for vel in [25, 30, 35, 38, 40, 40, 38, 35]:
    deep.add(Eb.add(-24), Duration.HALF, velocity=vel)
    deep.add(Bb.add(-24), Duration.HALF, velocity=max(10, vel - 8))

# Bars 9-16: grows with the spiritual seeking
for _ in range(8):
    deep.add(Eb.add(-24), Duration.HALF, velocity=42)
    deep.add(Bb.add(-24), Duration.HALF, velocity=35)

# Bars 17-24: darkens with the shift
for vel in [40, 38, 35, 32, 28, 25, 20, 15]:
    deep.add(Eb.add(-24), Duration.HALF, velocity=vel)
    deep.add(Gb.add(-24), Duration.HALF, velocity=max(8, vel - 10))

# Bars 25-32: swallowed by psychosis bass
for _ in range(8):
    deep.rest(Duration.WHOLE)

# Bars 33-40: returns in despair — just the root, nothing else
for vel in [15, 18, 20, 22, 25, 28, 30, 32]:
    deep.add(Eb.add(-24), Duration.WHOLE, velocity=vel)

# Bars 41-56: recovery — Sa-Pa returns, stable
for _ in range(16):
    deep.add(Eb.add(-24), Duration.HALF, velocity=35)
    deep.add(Bb.add(-24), Duration.HALF, velocity=28)

# Bars 57-64: gratitude — warm and full
for vel in [38, 40, 42, 42, 40, 35, 28, 18]:
    deep.add(Eb.add(-24), Duration.HALF, velocity=vel)
    deep.add(Bb.add(-24), Duration.HALF, velocity=max(10, vel - 8))

# ── PIANO — the whole story, every note by hand ────────────────
piano = score.part("piano", instrument="piano", volume=0.55,
                   reverb=0.4, reverb_type="taj_mahal",
                   delay=0.1, delay_time=0.375, delay_feedback=0.15,
                   pan=-0.1, humanize=0.12)

# ── 1. STABLE (bars 1-8) — warm, grounded, life is good ────────
# Simple melody in Eb major — nothing fancy, just human
piano.add(Eb, Duration.QUARTER, velocity=68)
piano.add(G, Duration.QUARTER, velocity=62)
piano.add(Bb, Duration.HALF, velocity=70)
piano.add(Ab, Duration.QUARTER, velocity=65)
piano.add(G, Duration.EIGHTH, velocity=58)
piano.add(F, Duration.EIGHTH, velocity=55)
piano.add(Eb, Duration.HALF, velocity=62)

piano.rest(Duration.QUARTER)
piano.add(Bb.add(-12), Duration.QUARTER, velocity=58)
piano.add(Eb, Duration.QUARTER, velocity=65)
piano.add(G, Duration.QUARTER, velocity=60)
piano.add(Ab, Duration.HALF, velocity=68)
piano.add(G, Duration.HALF, velocity=62)

piano.add(F, Duration.QUARTER, velocity=58)
piano.add(Eb, Duration.QUARTER, velocity=55)
piano.add(D.add(-12), Duration.QUARTER, velocity=52)
piano.add(Eb, Duration.QUARTER, velocity=60)
piano.rest(Duration.WHOLE)

piano.add(Eb.add(-12), Duration.QUARTER, velocity=55)
piano.rest(Duration.QUARTER)
piano.add(Bb.add(-12), Duration.QUARTER, velocity=50)
piano.rest(Duration.QUARTER)
piano.add(Eb, Duration.HALF, velocity=62)
piano.rest(Duration.HALF)

# ── 2. REACHING (bars 9-16) — climbing higher, exploring ───────
# The melody stretches upward — spiritual seeking
piano.add(Eb.add(12), Duration.QUARTER, velocity=72)
piano.add(D.add(12), Duration.EIGHTH, velocity=65)
piano.add(C.add(12), Duration.EIGHTH, velocity=62)
piano.add(Bb, Duration.HALF, velocity=70)
piano.add(C.add(12), Duration.QUARTER, velocity=68)
piano.add(D.add(12), Duration.QUARTER, velocity=72)
piano.add(Eb.add(12), Duration.HALF, velocity=78)
piano.rest(Duration.HALF)

# Higher still — it feels good, transcendent
piano.add(G.add(12), Duration.QUARTER, velocity=75)
piano.add(Ab.add(12), Duration.QUARTER, velocity=72)
piano.add(Bb.add(12), Duration.HALF, velocity=80)
piano.add(Ab.add(12), Duration.QUARTER, velocity=72)
piano.add(G.add(12), Duration.EIGHTH, velocity=68)
piano.add(F.add(12), Duration.EIGHTH, velocity=65)
piano.add(Eb.add(12), Duration.HALF, velocity=72)

# A moment of beauty at the peak
piano.add(Bb.add(12), Duration.QUARTER, velocity=82)
piano.rest(Duration.QUARTER)
piano.add(G.add(12), Duration.QUARTER, velocity=75)
piano.rest(Duration.QUARTER)
piano.add(Eb.add(12), Duration.WHOLE, velocity=78)

piano.rest(Duration.HALF)
piano.add(D.add(12), Duration.QUARTER, velocity=68)
piano.add(Eb.add(12), Duration.QUARTER, velocity=72)

# ── 3. THE SHIFT (bars 17-24) — something's wrong ──────────────
# Octave jumps where they shouldn't be. Notes slightly off.
# The melody you knew but... displaced.
piano.add(Eb, Duration.QUARTER, velocity=70)
piano.add(G.add(12), Duration.QUARTER, velocity=65)  # too high suddenly
piano.add(Bb.add(-12), Duration.HALF, velocity=68)   # too low
piano.add(Ab.add(12), Duration.QUARTER, velocity=72)  # jump
piano.rest(Duration.EIGHTH)
piano.add(F, Duration.EIGHTH, velocity=55)
piano.add(Eb.add(12), Duration.HALF, velocity=60)     # displaced

# The rhythm starts stumbling
piano.add(G, Duration.QUARTER, velocity=62)
piano.rest(Duration.EIGHTH)
piano.add(Bb.add(12), Duration.EIGHTH, velocity=68)   # wrong octave
piano.rest(Duration.QUARTER)
piano.add(Ab, Duration.QUARTER, velocity=58)
piano.add(Eb.add(-12), Duration.QUARTER, velocity=52)  # dropped low
piano.rest(Duration.QUARTER)
piano.add(D.add(12), Duration.QUARTER, velocity=70)    # reaching
piano.add(Eb, Duration.QUARTER, velocity=55)

# Gb creeps in — the key is shifting underneath
piano.add(Gb, Duration.HALF, velocity=65)              # first minor note
piano.add(Eb, Duration.QUARTER, velocity=58)
piano.add(Bb.add(12), Duration.QUARTER, velocity=72)   # too high
piano.add(Db, Duration.HALF, velocity=62)              # another minor note
piano.rest(Duration.QUARTER)
piano.add(Ab.add(-12), Duration.QUARTER, velocity=50)  # low, unsettled

piano.add(Eb.add(12), Duration.EIGHTH, velocity=75)   # flash
piano.add(Eb.add(-12), Duration.EIGHTH, velocity=48)  # two octave drop
piano.rest(Duration.QUARTER)
piano.add(Gb, Duration.QUARTER, velocity=60)
piano.add(Bb, Duration.QUARTER, velocity=58)
piano.rest(Duration.QUARTER)
piano.add(Cb, Duration.QUARTER, velocity=55)           # fully minor now

# ── 4. FALLING (bars 25-32) — disorienting, the key has changed ─
# Eb minor now. The same melody but in a darker mirror.
piano.add(Eb, Duration.QUARTER, velocity=55)
piano.add(Gb, Duration.QUARTER, velocity=52)
piano.add(Bb, Duration.HALF, velocity=58)
piano.add(Ab, Duration.QUARTER, velocity=52)
piano.add(Gb, Duration.EIGHTH, velocity=48)
piano.add(F, Duration.EIGHTH, velocity=45)
piano.add(Eb, Duration.HALF, velocity=50)

# Rhythm breaking apart
piano.rest(Duration.HALF)
piano.add(Db, Duration.EIGHTH, velocity=48)
piano.rest(Duration.EIGHTH)
piano.add(Eb.add(12), Duration.EIGHTH, velocity=52)   # flash of height
piano.rest(Duration.QUARTER)
piano.rest(Duration.EIGHTH)
piano.add(Cb, Duration.QUARTER, velocity=45)
piano.rest(Duration.QUARTER)

# Getting quieter, more confused
piano.add(Eb.add(-12), Duration.QUARTER, velocity=42)
piano.rest(Duration.HALF)
piano.add(Bb.add(-12), Duration.QUARTER, velocity=38)
piano.add(Gb, Duration.HALF, velocity=42)
piano.rest(Duration.HALF)
piano.add(Eb, Duration.QUARTER, velocity=40)
piano.rest(Duration.DOTTED_HALF)

# ── 5a. DESPAIR (bars 33-40) — the bottom. Nothing left. ────────
# The lowest, saddest notes. Eb minor. Barely alive.
piano.add(Eb.add(-24), Duration.WHOLE, velocity=28)
piano.rest(Duration.WHOLE)
piano.add(Gb.add(-12), Duration.HALF, velocity=22)
piano.add(Eb.add(-12), Duration.HALF, velocity=25)
piano.rest(Duration.WHOLE)
# The melody tries to come back — in minor. Broken.
piano.add(Eb, Duration.QUARTER, velocity=30)
piano.add(Gb, Duration.QUARTER, velocity=25)
piano.add(Bb, Duration.HALF, velocity=32)
piano.add(Ab, Duration.QUARTER, velocity=28)
piano.add(Gb, Duration.EIGHTH, velocity=22)
piano.add(F, Duration.EIGHTH, velocity=20)
piano.add(Eb, Duration.HALF, velocity=25)
# Lowest note of the whole piece
piano.add(Eb.add(-24), Duration.WHOLE, velocity=22)
piano.rest(Duration.WHOLE)

# ── 5b. THE ROOM (bars 41-44) — the hymn finds you ─────────────
# A single note. Then another. The major key returns.
piano.rest(Duration.WHOLE)
piano.add(Eb, Duration.QUARTER, velocity=30)
piano.rest(Duration.DOTTED_HALF)
piano.rest(Duration.WHOLE)
piano.add(G, Duration.QUARTER, velocity=32)           # G natural — light
piano.rest(Duration.DOTTED_HALF)

# ── 6. FINDING GROUND (bars 41-48) — tentative, reaching back ──
# The original melody tries to come back. Hesitant. Careful.
piano.add(Eb, Duration.QUARTER, velocity=45)
piano.rest(Duration.QUARTER)
piano.add(G, Duration.QUARTER, velocity=42)            # G natural — major!
piano.rest(Duration.QUARTER)
piano.add(Bb, Duration.HALF, velocity=48)
piano.rest(Duration.HALF)

piano.add(Ab, Duration.QUARTER, velocity=45)
piano.add(G, Duration.QUARTER, velocity=48)
piano.add(F, Duration.QUARTER, velocity=45)
piano.add(Eb, Duration.QUARTER, velocity=50)
piano.rest(Duration.WHOLE)

piano.add(Eb, Duration.QUARTER, velocity=52)
piano.add(G, Duration.QUARTER, velocity=50)
piano.add(Bb, Duration.HALF, velocity=55)
piano.add(Ab, Duration.QUARTER, velocity=52)
piano.add(G, Duration.EIGHTH, velocity=48)
piano.add(F, Duration.EIGHTH, velocity=45)
piano.add(Eb, Duration.HALF, velocity=52)

piano.rest(Duration.HALF)
piano.add(Bb.add(-12), Duration.QUARTER, velocity=48)
piano.add(Eb, Duration.QUARTER, velocity=52)

# ── 7. RECOVERY (bars 49-56) — warmth returns, but changed ─────
# The melody is back in Eb major. Stronger. You can hear what it cost.
piano.add(Eb, Duration.QUARTER, velocity=62)
piano.add(G, Duration.QUARTER, velocity=58)
piano.add(Bb, Duration.HALF, velocity=65)
piano.add(Ab, Duration.QUARTER, velocity=60)
piano.add(G, Duration.EIGHTH, velocity=55)
piano.add(F, Duration.EIGHTH, velocity=52)
piano.add(Eb, Duration.HALF, velocity=58)

piano.rest(Duration.QUARTER)
piano.add(Bb.add(-12), Duration.QUARTER, velocity=55)
piano.add(Eb, Duration.QUARTER, velocity=60)
piano.add(G, Duration.QUARTER, velocity=58)
piano.add(Ab, Duration.HALF, velocity=65)
piano.add(G, Duration.HALF, velocity=60)

# Climbing again — but this time grounded
piano.add(Eb.add(12), Duration.QUARTER, velocity=68)
piano.add(D.add(12), Duration.EIGHTH, velocity=62)
piano.add(C.add(12), Duration.EIGHTH, velocity=58)
piano.add(Bb, Duration.HALF, velocity=65)
piano.add(Ab, Duration.QUARTER, velocity=60)
piano.add(G, Duration.QUARTER, velocity=62)
piano.add(Eb, Duration.WHOLE, velocity=65)

# ── 8. GRATITUDE (bars 57-64) — full, resolved, home ───────────
# The melody you remember from the opening. Whole. Grateful.
piano.set(volume=0.6)
piano.add(Eb, Duration.QUARTER, velocity=72)
piano.add(G, Duration.QUARTER, velocity=68)
piano.add(Bb, Duration.HALF, velocity=75)
piano.add(Ab, Duration.QUARTER, velocity=70)
piano.add(G, Duration.EIGHTH, velocity=65)
piano.add(F, Duration.EIGHTH, velocity=62)
piano.add(Eb, Duration.HALF, velocity=68)

piano.rest(Duration.QUARTER)
piano.add(Bb.add(-12), Duration.QUARTER, velocity=62)
piano.add(Eb, Duration.QUARTER, velocity=68)
piano.add(G, Duration.QUARTER, velocity=65)
piano.add(Ab, Duration.HALF, velocity=72)
piano.add(Bb, Duration.HALF, velocity=70)

# Final phrase — higher than the opening, but settled
piano.add(Eb.add(12), Duration.HALF, velocity=72)
piano.add(D.add(12), Duration.QUARTER, velocity=65)
piano.add(Eb.add(12), Duration.QUARTER, velocity=70)
piano.add(Bb, Duration.HALF, velocity=65)
piano.add(G, Duration.HALF, velocity=62)

# Last notes — home
piano.add(Eb, Duration.QUARTER, velocity=60)
piano.add(Bb.add(-12), Duration.QUARTER, velocity=55)
piano.add(Eb.add(-12), Duration.HALF, velocity=58)
piano.rest(Duration.WHOLE)

# ── TAMBURA — the spiritual seeking, bars 9-24 ─────────────────
# Ram Dass. Meditation. The eastern path that opened the door.
tambura = score.part("tambura", synth="sine", envelope="pad", volume=0.12,
                     reverb=0.5, reverb_type="taj_mahal",
                     chorus=0.4, chorus_rate=0.06, chorus_depth=0.01,
                     lowpass=900, pan=-0.25)

for _ in range(8):
    tambura.rest(Duration.WHOLE)

# Bars 9-12: enters with the reaching — spiritual warmth, Sa-Pa
for vel in [18, 28, 38, 42]:
    tambura.add(Eb.add(-24), Duration.HALF, velocity=vel)
    tambura.add(Bb.add(-24), Duration.HALF, velocity=max(10, vel - 8))

# Bars 13-16: the drone shifts — Sa-Ma, subtly wrong
tambura.add(Eb.add(-24), Duration.HALF, velocity=45)
tambura.add(Ab.add(-24), Duration.HALF, velocity=38)  # fourth instead of fifth
tambura.add(Eb.add(-24), Duration.HALF, velocity=42)
tambura.add(Ab.add(-24), Duration.HALF, velocity=40)
tambura.add(Eb.add(-24), Duration.HALF, velocity=40)
tambura.add(Bb.add(-24), Duration.HALF, velocity=35)  # back to fifth
tambura.add(Eb.add(-24), Duration.HALF, velocity=38)
tambura.add(Gb.add(-24), Duration.HALF, velocity=32)  # minor third — darker

# Bars 17-20: unstable, the drone wobbles between intervals
tambura.add(Eb.add(-24), Duration.HALF, velocity=35)
tambura.add(Gb.add(-24), Duration.HALF, velocity=30)
tambura.add(Eb.add(-24), Duration.HALF, velocity=32)
tambura.add(Bb.add(-24), Duration.HALF, velocity=28)
tambura.add(Eb.add(-24), Duration.HALF, velocity=25)
tambura.add(Ab.add(-24), Duration.HALF, velocity=22)
tambura.add(Eb.add(-24), Duration.HALF, velocity=18)
tambura.add(Db.add(-24), Duration.HALF, velocity=15)  # tritone area — wrong

# Bars 21-24: dying
for vel in [12, 8, 5, 0]:
    if vel > 0:
        tambura.add(Eb.add(-24), Duration.WHOLE, velocity=vel)
    else:
        tambura.rest(Duration.WHOLE)

# Rest of track: gone
for _ in range(40):
    tambura.rest(Duration.WHOLE)

# ── VOCAL OM — the meditation, bars 9-20 ───────────────────────
om = score.part("om", instrument="vocal", volume=0.15,
                reverb=0.6, reverb_type="taj_mahal",
                chorus=0.3, chorus_rate=0.05, chorus_depth=0.01,
                pan=0.1)

for _ in range(8):
    om.rest(Duration.WHOLE)

# Bars 9-16: om drone — low, sustained, centering
for vel in [25, 32, 38, 42, 45, 45, 42, 40]:
    om.add(Eb.add(-12), Duration.WHOLE, velocity=vel, lyric="om")

# Bars 17-20: om gets unstable — pitch drifts
om.add(Eb.add(-12), Duration.WHOLE, velocity=38, bend=0.15, lyric="om")
om.add(Eb.add(-12), Duration.WHOLE, velocity=35, bend=-0.2, lyric="om")
om.add(Eb.add(-12), Duration.WHOLE, velocity=30, bend=0.3, lyric="om")
om.add(Eb.add(-12), Duration.WHOLE, velocity=22, bend=-0.4, lyric="om")

# Gone
for _ in range(44):
    om.rest(Duration.WHOLE)

# ── SITAR — spiritual exploration, bars 11-20 ──────────────────
sitar = score.part("sitar", instrument="sitar", volume=0.4,
                   reverb=0.3, reverb_type="taj_mahal",
                   delay=0.15, delay_time=0.375, delay_feedback=0.2,
                   pan=0.2, humanize=0.1)

for _ in range(10):
    sitar.rest(Duration.WHOLE)

# Bars 11-14: beautiful raga phrases — the meditation working
sitar.add(Eb, Duration.HALF, velocity=60, bend=-0.15)
sitar.add(G, Duration.HALF, velocity=55)
sitar.add(Bb, Duration.QUARTER, velocity=65, bend=-0.1)
sitar.add(Ab, Duration.QUARTER, velocity=58)
sitar.add(G, Duration.QUARTER, velocity=55)
sitar.add(Eb, Duration.QUARTER, velocity=52)
sitar.rest(Duration.WHOLE)
sitar.add(Bb, Duration.HALF, velocity=62, bend=-0.15)
sitar.add(Ab, Duration.HALF, velocity=58)

# Bars 15-20: gets more agitated — the seeking intensifies
sitar.add(Eb.add(12), Duration.QUARTER, velocity=72, bend=0.25)
sitar.add(D.add(12), Duration.EIGHTH, velocity=65)
sitar.add(C.add(12), Duration.EIGHTH, velocity=62)
sitar.add(Bb, Duration.HALF, velocity=68, bend=-0.2)
sitar.add(Ab, Duration.QUARTER, velocity=70, bend=0.3)
sitar.add(Bb, Duration.QUARTER, velocity=72, bend=-0.25)
sitar.add(Eb.add(12), Duration.HALF, velocity=78, bend=0.5)
sitar.rest(Duration.HALF)
# Getting frantic
sitar.add(Bb.add(12), Duration.EIGHTH, velocity=80, bend=0.5)
sitar.add(Ab.add(12), Duration.EIGHTH, velocity=75)
sitar.add(G.add(12), Duration.EIGHTH, velocity=72, bend=-0.3)
sitar.add(F.add(12), Duration.EIGHTH, velocity=68)
sitar.add(Eb.add(12), Duration.QUARTER, velocity=75, bend=0.5)
sitar.rest(Duration.QUARTER)
sitar.rest(Duration.WHOLE)

# Gone — the door has opened to something else
for _ in range(44):
    sitar.rest(Duration.WHOLE)

# ── THEREMIN — psychosis, bars 21-32 ───────────────────────────
# The mind unmoored. Wild bends. Beautiful and terrifying.
theremin = score.part("theremin", instrument="theremin", volume=0.25,
                      reverb=0.25, reverb_decay=1.0,
                      delay=0.12, delay_time=0.375, delay_feedback=0.2,
                      pan=-0.15, humanize=0.04)

for _ in range(18):
    theremin.rest(Duration.WHOLE)

# Bars 19-20: first whisper — barely there, just a hint of wrongness
theremin.add(Bb, Duration.WHOLE, velocity=35, bend=0.5)
theremin.rest(Duration.WHOLE)

# Bars 21-22: creeping in — something's not right
theremin.add(Bb.add(12), Duration.HALF, velocity=60, bend=1.5)
theremin.rest(Duration.HALF)
theremin.add(Eb.add(12), Duration.QUARTER, velocity=65, bend=-2.0)
theremin.add(G.add(12), Duration.QUARTER, velocity=62, bend=1.0)
theremin.rest(Duration.HALF)
theremin.add(Db.add(12), Duration.HALF, velocity=68, bend=2.5)

# Bars 23-24: intensifying — the bends get wider, faster
theremin.set(volume=0.35)
theremin.add(Eb.add(12), Duration.QUARTER, velocity=78, bend=3.0)
theremin.add(Bb.add(12), Duration.EIGHTH, velocity=72, bend=-2.5)
theremin.add(Eb.add(12), Duration.EIGHTH, velocity=80, bend=2.0)
theremin.add(Gb.add(12), Duration.QUARTER, velocity=70, bend=-3.0)
theremin.add(Eb.add(12), Duration.QUARTER, velocity=82, bend=4.0)
theremin.add(Db.add(12), Duration.EIGHTH, velocity=68, bend=-2.0)
theremin.add(Bb.add(12), Duration.EIGHTH, velocity=72, bend=3.0)
theremin.add(Eb.add(12), Duration.HALF, velocity=85, bend=-3.5)

# Bars 25-26: FULL PSYCHOSIS — screaming, octave leaps, max bends
theremin.set(volume=0.32)
theremin.add(Eb.add(12), Duration.EIGHTH, velocity=78, bend=5.0)
theremin.add(Eb, Duration.EIGHTH, velocity=58, bend=-3.0)
theremin.add(Eb.add(12), Duration.EIGHTH, velocity=80, bend=-4.0)
theremin.add(Gb.add(12), Duration.EIGHTH, velocity=65, bend=3.0)
theremin.add(Bb.add(12), Duration.QUARTER, velocity=82, bend=5.0)
theremin.add(Cb, Duration.QUARTER, velocity=55, bend=-4.0)
theremin.add(Eb.add(12), Duration.EIGHTH, velocity=78, bend=4.0)
theremin.add(Bb, Duration.EIGHTH, velocity=60, bend=-3.0)
theremin.add(Eb.add(12), Duration.EIGHTH, velocity=82, bend=-5.0)
theremin.add(Db.add(12), Duration.EIGHTH, velocity=68, bend=4.0)
theremin.add(Ab.add(12), Duration.QUARTER, velocity=85, bend=5.0)
theremin.add(Gb, Duration.QUARTER, velocity=58, bend=-5.0)

# Bars 27-28: the voices — rapid, fragmented
theremin.add(Eb.add(12), Duration.SIXTEENTH, velocity=72, bend=2.0)
theremin.add(Bb.add(12), Duration.SIXTEENTH, velocity=78, bend=-3.0)
theremin.add(Gb, Duration.SIXTEENTH, velocity=58, bend=4.0)
theremin.add(Eb.add(12), Duration.SIXTEENTH, velocity=80, bend=-4.0)
theremin.add(Db.add(12), Duration.EIGHTH, velocity=68, bend=3.0)
theremin.add(Ab.add(12), Duration.EIGHTH, velocity=82, bend=-5.0)
theremin.add(Eb, Duration.QUARTER, velocity=60, bend=5.0)
theremin.add(Bb.add(12), Duration.QUARTER, velocity=85, bend=-4.0)
# Sustained scream
theremin.add(Eb.add(12), Duration.HALF, velocity=85, bend=5.0)
theremin.add(Eb.add(12), Duration.EIGHTH, velocity=80, bend=-5.0)
theremin.add(Bb.add(12), Duration.EIGHTH, velocity=70, bend=3.0)
theremin.add(Gb.add(12), Duration.EIGHTH, velocity=65, bend=-2.0)
theremin.add(Db.add(12), Duration.EIGHTH, velocity=60, bend=2.0)

# Bars 29-30: sustained madness — the peak holds
theremin.add(Eb.add(12), Duration.QUARTER, velocity=82, bend=-5.0)
theremin.add(Bb.add(12), Duration.QUARTER, velocity=85, bend=4.0)
theremin.add(Gb, Duration.QUARTER, velocity=60, bend=-3.0)
theremin.add(Eb.add(12), Duration.QUARTER, velocity=85, bend=5.0)
theremin.add(Db.add(12), Duration.HALF, velocity=72, bend=-4.0)
theremin.add(Ab.add(12), Duration.HALF, velocity=82, bend=5.0)

# Bars 31-32: the descent — falling, falling, slower
theremin.set(volume=0.35)
theremin.add(Eb.add(12), Duration.HALF, velocity=82, bend=-3.0)
theremin.add(Bb, Duration.HALF, velocity=72, bend=-2.0)
theremin.add(Gb, Duration.HALF, velocity=62, bend=-1.5)
theremin.add(Eb, Duration.HALF, velocity=52, bend=-1.0)

# Bars 33-34: barely there — last gasps into despair
theremin.set(volume=0.25)
theremin.add(Bb.add(-12), Duration.WHOLE, velocity=35, bend=-0.5)
theremin.add(Eb.add(-12), Duration.WHOLE, velocity=20, bend=-0.25)

# Gone
for _ in range(30):
    theremin.rest(Duration.WHOLE)

# ── RING — sparse ring mod hits, spectral accents ──────────────
ring = score.part("ring", synth="ring_mod", envelope="pluck", volume=0.12,
                  reverb=0.2, reverb_type="cathedral",
                  delay=0.1, delay_time=0.375, delay_feedback=0.15,
                  pan=0.35)

# Bars 1-24: silence
for _ in range(24):
    ring.rest(Duration.WHOLE)

# Bars 25-32: sparse hits — every other bar
for _ in range(4):
    ring.add(Eb.add(12), Duration.QUARTER, velocity=55)
    ring.rest(Duration.DOTTED_HALF)
    ring.rest(Duration.WHOLE)

# Bars 33-68: silence — let it dissolve (remaining bars)
for _ in range(32):
    ring.rest(Duration.WHOLE)

# ── ORGAN — the hospital, the hymn, bars 33-40 ─────────────────
# Christian hymn on a pipe organ. Institutional. But grounding.
# "Be still and know."
organ = score.part("organ", instrument="pipe_organ", volume=0.22,
                   reverb=0.6, reverb_type="cathedral",
                   chorus=0.15, chorus_rate=0.12, chorus_depth=0.006,
                   pan=0.1)

for _ in range(40):
    organ.rest(Duration.WHOLE)

# Bars 41-44: the hymn emerges from the despair — barely there, then swells
hymn_a = key_major.progression("IV", "V", "vi", "IV")
organ.add(hymn_a[0], Duration.WHOLE, velocity=22)
organ.add(hymn_a[1], Duration.HALF, velocity=28)
organ.rest(Duration.HALF)
organ.add(hymn_a[2], Duration.WHOLE, velocity=32)
organ.add(hymn_a[3], Duration.HALF, velocity=30)
organ.add(hymn_a[0], Duration.HALF, velocity=35)

# Bars 37-40: fuller — the hymn takes shape, breathing rhythm
organ.add(key_major.progression("I")[0], Duration.DOTTED_HALF, velocity=40)
organ.rest(Duration.QUARTER)
organ.add(key_major.progression("IV")[0], Duration.HALF, velocity=38)
organ.add(key_major.progression("V")[0], Duration.HALF, velocity=42)
organ.add(key_major.progression("I")[0], Duration.WHOLE, velocity=45)
organ.add(key_major.progression("vi")[0], Duration.HALF, velocity=38)
organ.rest(Duration.HALF)

# Bars 41-48: organ continues, stronger, the hymn lifts
organ.add(key_major.progression("I")[0], Duration.DOTTED_HALF, velocity=48)
organ.rest(Duration.QUARTER)
organ.add(key_major.progression("vi")[0], Duration.WHOLE, velocity=42)
organ.add(key_major.progression("IV")[0], Duration.HALF, velocity=45)
organ.add(key_major.progression("V")[0], Duration.HALF, velocity=48)
organ.add(key_major.progression("I")[0], Duration.WHOLE, velocity=52)
organ.add(key_major.progression("IV")[0], Duration.DOTTED_HALF, velocity=48)
organ.rest(Duration.QUARTER)
organ.add(key_major.progression("V")[0], Duration.HALF, velocity=50)
organ.add(key_major.progression("I")[0], Duration.HALF, velocity=52)
organ.add(key_major.progression("I")[0], Duration.WHOLE, velocity=55)

# Bars 49-56: fading — the hymn letting go as piano takes over
for vel in [48, 42, 38, 32, 25, 18, 10, 0]:
    if vel > 0:
        organ.add(key_major.progression("I")[0], Duration.DOTTED_HALF, velocity=vel)
        organ.rest(Duration.QUARTER)
    else:
        organ.rest(Duration.WHOLE)

# Gone
for _ in range(8):
    organ.rest(Duration.WHOLE)

# ── PSYCHOSIS BASS — deep, menacing, bars 23-32 ────────────────
psycho_bass = score.part("psycho_bass", synth="sine", envelope="pad", volume=0.3,
                         lowpass=180, distortion=0.25, distortion_drive=3.5,
                         sub_osc=0.6, saturation=0.4)

for _ in range(22):
    psycho_bass.rest(Duration.WHOLE)

# Bars 23-24: creeping in — low rumble
psycho_bass.add(Eb.add(-36), Duration.WHOLE, velocity=20)
psycho_bass.add(Eb.add(-36), Duration.WHOLE, velocity=28)

# Bars 25-28: full weight — the floor is vibrating
for vel in [38, 42, 48, 52]:
    psycho_bass.add(Eb.add(-36), Duration.HALF, velocity=vel)
    psycho_bass.add(Db.add(-36), Duration.HALF, velocity=max(15, vel - 8))

# Bars 29-32: slides down as the crash comes
psycho_bass.add(Eb.add(-36), Duration.WHOLE, velocity=48)
psycho_bass.add(Db.add(-36), Duration.WHOLE, velocity=40)
psycho_bass.add(Cb.add(-36), Duration.WHOLE, velocity=30)
psycho_bass.add(Bb.add(-48), Duration.WHOLE, velocity=20)

# Rest of track: gone
for _ in range(32):
    psycho_bass.rest(Duration.WHOLE)

# ── CHAOS DRUMS — the mind racing, bars 25-30 ──────────────────
K  = DrumSound.KICK
S  = DrumSound.SNARE
CH = DrumSound.CLOSED_HAT

chaos = score.part("chaos", volume=0.35, humanize=0.08,
                   reverb=0.3, reverb_decay=1.5,
                   delay=0.2, delay_time=0.375, delay_feedback=0.3,
                   pan=-0.2)

for _ in range(24):
    chaos.rest(Duration.WHOLE)

# Bars 25-26: racing heartbeat — kick pulse with erratic snare
chaos.hit(K, Duration.QUARTER, velocity=88)
chaos.hit(S, Duration.EIGHTH, velocity=65)
chaos.hit(CH, Duration.EIGHTH, velocity=48)
chaos.hit(K, Duration.QUARTER, velocity=85)
chaos.hit(S, Duration.SIXTEENTH, velocity=72)
chaos.hit(CH, Duration.SIXTEENTH, velocity=45)
chaos.hit(K, Duration.EIGHTH, velocity=90)

chaos.hit(K, Duration.QUARTER, velocity=92)
chaos.hit(CH, Duration.EIGHTH, velocity=50)
chaos.hit(S, Duration.EIGHTH, velocity=78)
chaos.hit(K, Duration.EIGHTH, velocity=88)
chaos.hit(K, Duration.EIGHTH, velocity=85)
chaos.hit(S, Duration.QUARTER, velocity=82)

# Bars 27-28: the pulse is there but everything else is chaotic
chaos.hit(K, Duration.QUARTER, velocity=95)
chaos.hit(S, Duration.SIXTEENTH, velocity=80)
chaos.hit(CH, Duration.SIXTEENTH, velocity=55)
chaos.hit(S, Duration.SIXTEENTH, velocity=72)
chaos.hit(CH, Duration.SIXTEENTH, velocity=48)
chaos.hit(K, Duration.QUARTER, velocity=92)
chaos.hit(S, Duration.EIGHTH, velocity=85)
chaos.hit(K, Duration.EIGHTH, velocity=90)

chaos.hit(K, Duration.QUARTER, velocity=98)
# 32nd note snare roll
for i in range(8):
    chaos.hit(S, 0.125, velocity=min(105, 65 + i * 5))
chaos.hit(K, Duration.QUARTER, velocity=100)
chaos.hit(S, Duration.QUARTER, velocity=88)
chaos.hit(K, Duration.QUARTER, velocity=95)

# Bars 29-30: the pulse staggers — still there but losing it
chaos.hit(K, Duration.QUARTER, velocity=80)
chaos.rest(Duration.EIGHTH)
chaos.hit(S, Duration.EIGHTH, velocity=60)
chaos.hit(K, Duration.QUARTER, velocity=72)
chaos.rest(Duration.QUARTER)
chaos.hit(K, Duration.QUARTER, velocity=65)
chaos.rest(Duration.QUARTER)
chaos.rest(Duration.EIGHTH)
chaos.hit(S, Duration.EIGHTH, velocity=50)
chaos.hit(K, Duration.QUARTER, velocity=55)
chaos.rest(Duration.QUARTER)

# Bars 31-32: silence — the gap before the room
chaos.rest(Duration.WHOLE)
chaos.rest(Duration.WHOLE)

# Bars 33-40: sparse kick through the hymn — a heartbeat stabilizing
for vel in [30, 32, 35, 35, 38, 38, 40, 42]:
    chaos.hit(K, Duration.QUARTER, velocity=vel)
    chaos.rest(Duration.DOTTED_HALF)

# Bars 41-48: kick continues, slightly fuller — finding ground
for _ in range(8):
    chaos.hit(K, Duration.QUARTER, velocity=45)
    chaos.rest(Duration.QUARTER)
    chaos.rest(Duration.QUARTER)
    chaos.hit(K, Duration.QUARTER, velocity=35)

# Bars 49-56: steady, gentle
for _ in range(8):
    chaos.hit(K, Duration.QUARTER, velocity=42)
    chaos.rest(Duration.DOTTED_HALF)

# Bars 57-64: fading with the ending
for vel in [40, 35, 30, 25, 20, 15, 10, 0]:
    if vel > 0:
        chaos.hit(K, Duration.QUARTER, velocity=vel)
        chaos.rest(Duration.DOTTED_HALF)
    else:
        chaos.rest(Duration.WHOLE)

# ── TABLA — gentle meditation rhythm, bars 11-20 ──────────────
NA  = DrumSound.TABLA_NA
tDHA = DrumSound.TABLA_DHA
TIT = DrumSound.TABLA_TIT
GE  = DrumSound.TABLA_GE
GEB = DrumSound.TABLA_GE_BEND

tabla = score.part("tabla", volume=0.38,
                   reverb=0.25, reverb_type="cathedral", reverb_decay=1.5,
                   pan=-0.15, humanize=0.1)

for _ in range(10):
    tabla.rest(Duration.WHOLE)

# Bars 11-16: gentle keherwa — the meditation has a pulse
for vel_base in [55, 60, 65, 68, 70, 70]:
    tabla.hit(tDHA, Duration.EIGHTH, velocity=vel_base, articulation="accent")
    tabla.hit(GE, Duration.EIGHTH, velocity=max(20, vel_base - 30))
    tabla.hit(NA, Duration.EIGHTH, velocity=max(25, vel_base - 20))
    tabla.hit(TIT, Duration.EIGHTH, velocity=max(15, vel_base - 35))
    tabla.hit(NA, Duration.EIGHTH, velocity=max(22, vel_base - 22))
    tabla.hit(TIT, Duration.EIGHTH, velocity=max(15, vel_base - 38))
    tabla.hit(tDHA, Duration.EIGHTH, velocity=max(30, vel_base - 8))
    tabla.hit(NA, Duration.EIGHTH, velocity=max(22, vel_base - 18))

# Bars 17-20: rhythm destabilizes — fills get erratic
tabla.hit(tDHA, Duration.EIGHTH, velocity=72, articulation="accent")
tabla.hit(GEB, Duration.EIGHTH, velocity=80)
tabla.hit(NA, Duration.SIXTEENTH, velocity=55)
tabla.hit(TIT, Duration.SIXTEENTH, velocity=40)
tabla.hit(GEB, Duration.EIGHTH, velocity=75)
tabla.hit(tDHA, Duration.EIGHTH, velocity=68)
tabla.hit(NA, Duration.EIGHTH, velocity=52)
tabla.hit(GEB, Duration.QUARTER, velocity=82)

tabla.hit(tDHA, Duration.SIXTEENTH, velocity=70)
tabla.hit(NA, Duration.SIXTEENTH, velocity=55)
tabla.hit(GEB, Duration.SIXTEENTH, velocity=78)
tabla.hit(TIT, Duration.SIXTEENTH, velocity=38)
tabla.rest(Duration.QUARTER)
tabla.hit(tDHA, Duration.EIGHTH, velocity=65)
tabla.hit(GEB, Duration.EIGHTH, velocity=72)
tabla.rest(Duration.QUARTER)

tabla.hit(tDHA, Duration.QUARTER, velocity=58)
tabla.rest(Duration.HALF)
tabla.hit(GEB, Duration.QUARTER, velocity=55)

tabla.rest(Duration.HALF)
tabla.hit(tDHA, Duration.QUARTER, velocity=42)
tabla.rest(Duration.QUARTER)

# Gone — swallowed by the psychosis
for _ in range(44):
    tabla.rest(Duration.WHOLE)

# ── TINGSHA — crystalline, marks the meditation opening ────────
tingsha = score.part("tingsha", instrument="tingsha", volume=0.2,
                     reverb=0.5, reverb_type="taj_mahal",
                     delay=0.2, delay_time=0.75, delay_feedback=0.25,
                     pan=0.3)

# Bar 1: announces the beginning
tingsha.add(Eb.add(12), Duration.WHOLE, velocity=55)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
# Bar 5: second strike
tingsha.add(Bb.add(12), Duration.WHOLE, velocity=50)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
tingsha.rest(Duration.WHOLE)
# Bar 9: the seeking begins
tingsha.add(Eb.add(12), Duration.WHOLE, velocity=52)
# Rest of track
for _ in range(55):
    tingsha.rest(Duration.WHOLE)

# ── SINGING BOWL — the thread between worlds ──────────────────
# Strike at bar 1 (before), bar 17 (the shift), bar 33 (the room),
# bar 41 (finding ground), bar 57 (gratitude)
bowl = score.part("bowl", instrument="singing_bowl", volume=0.25,
                  reverb=0.7, reverb_type="taj_mahal",
                  delay=0.15, delay_time=0.75, delay_feedback=0.2,
                  pan=0.15)

section_bars = {1: 60, 17: 55, 33: 45, 41: 50, 57: 62}
for bar in range(1, 65):
    if bar in section_bars:
        bowl.add(Eb.add(-24), Duration.WHOLE, velocity=section_bars[bar])
    else:
        bowl.rest(Duration.WHOLE)

# ── CELLO — enters at recovery, the human warmth returning ─────
cello = score.part("cello", instrument="cello", volume=0.18,
                   reverb=0.45, reverb_type="cathedral",
                   delay=0.08, delay_time=0.375, delay_feedback=0.1,
                   pan=0.2, humanize=0.08)

for _ in range(48):
    cello.rest(Duration.WHOLE)

# Bars 49-52: tentative — one note rising slowly, like learning to breathe
cello.add(Eb.add(-12), Duration.WHOLE, velocity=35)
cello.add(Eb.add(-12), Duration.WHOLE, velocity=40)
cello.add(F.add(-12), Duration.HALF, velocity=42, bend=0.1)
cello.add(G.add(-12), Duration.HALF, velocity=45)
cello.add(Ab.add(-12), Duration.DOTTED_HALF, velocity=48, bend=-0.08)
cello.rest(Duration.QUARTER)

# Bars 53-56: gaining confidence — the line moves
cello.add(Bb.add(-12), Duration.HALF, velocity=50)
cello.add(Ab.add(-12), Duration.HALF, velocity=48)
cello.add(G.add(-12), Duration.WHOLE, velocity=52, bend=0.1)
cello.add(F.add(-12), Duration.HALF, velocity=48)
cello.add(Eb.add(-12), Duration.HALF, velocity=52)
cello.add(Bb.add(-24), Duration.DOTTED_HALF, velocity=48)
cello.rest(Duration.QUARTER)

# Bars 57-60: gratitude — singing now, not just holding
cello.add(Eb.add(-12), Duration.QUARTER, velocity=55)
cello.add(G.add(-12), Duration.QUARTER, velocity=52)
cello.add(Bb.add(-12), Duration.HALF, velocity=58, bend=0.08)
cello.add(Ab.add(-12), Duration.QUARTER, velocity=52)
cello.add(G.add(-12), Duration.QUARTER, velocity=50)
cello.add(F.add(-12), Duration.HALF, velocity=48)
cello.add(Eb.add(-12), Duration.HALF, velocity=52)
cello.add(Bb.add(-24), Duration.HALF, velocity=48)
cello.add(Eb.add(-12), Duration.HALF, velocity=55, bend=0.1)
cello.add(G.add(-12), Duration.WHOLE, velocity=52)

# Bars 61-64: settling — last long tones fading
cello.add(Eb.add(-12), Duration.WHOLE, velocity=48)
cello.add(Bb.add(-24), Duration.WHOLE, velocity=42)
cello.add(Eb.add(-12), Duration.WHOLE, velocity=35)
cello.rest(Duration.WHOLE)

# ── SINGING BOWL CHORUS — surrounds you in the despair ─────────
bowl_lo = score.part("bowl_lo", instrument="singing_bowl", volume=0.3,
                     reverb=0.8, reverb_type="taj_mahal",
                     delay=0.15, delay_time=1.5, delay_feedback=0.2,
                     pan=-0.35)

bowl_mid = score.part("bowl_mid", instrument="singing_bowl_ring", volume=0.25,
                      reverb=0.75, reverb_type="taj_mahal",
                      delay=0.12, delay_time=1.0, delay_feedback=0.18,
                      pan=0.3)

bowl_hi = score.part("bowl_hi", instrument="singing_bowl_ring", volume=0.2,
                     reverb=0.7, reverb_type="taj_mahal",
                     delay=0.1, delay_time=0.75, delay_feedback=0.15,
                     pan=-0.15)

# Silent until despair
for _ in range(33):
    bowl_lo.rest(Duration.WHOLE)
    bowl_mid.rest(Duration.WHOLE)
    bowl_hi.rest(Duration.WHOLE)

# Bars 34-40: the chorus rings — each bowl at different intervals
# Low bowl: every 2 bars
# Mid bowl: offset, every 3 bars
# High bowl: every 2 bars, different offset
for bar in range(34, 41):
    # Low
    if bar % 2 == 0:
        bowl_lo.add(Eb.add(-24), Duration.WHOLE, velocity=55)
    else:
        bowl_lo.rest(Duration.WHOLE)
    # Mid
    if bar in [34, 37, 40]:
        bowl_mid.add(Bb.add(-12), Duration.WHOLE, velocity=48)
    else:
        bowl_mid.rest(Duration.WHOLE)
    # High
    if bar % 2 == 1:
        bowl_hi.add(Eb, Duration.WHOLE, velocity=42)
    else:
        bowl_hi.rest(Duration.WHOLE)

# Bars 41-48: continues through finding ground, fading
for vel in [50, 45, 40, 35, 28, 22, 15, 8]:
    bowl_lo.add(Eb.add(-24), Duration.WHOLE, velocity=vel)
for vel in [42, 38, 32, 25, 18, 12, 0, 0]:
    if vel > 0:
        bowl_mid.add(Bb.add(-12), Duration.WHOLE, velocity=vel)
    else:
        bowl_mid.rest(Duration.WHOLE)
for vel in [38, 32, 25, 18, 12, 0, 0, 0]:
    if vel > 0:
        bowl_hi.add(Eb, Duration.WHOLE, velocity=vel)
    else:
        bowl_hi.rest(Duration.WHOLE)

# Rest of track
for _ in range(16):
    bowl_lo.rest(Duration.WHOLE)
    bowl_mid.rest(Duration.WHOLE)
    bowl_hi.rest(Duration.WHOLE)

# ── Rhodes — gentle pad, only in gratitude ─────────────────────
rhodes = score.part("rhodes", instrument="electric_piano", volume=0.15,
                    reverb=0.5, reverb_type="taj_mahal",
                    tremolo_depth=0.08, tremolo_rate=2.0,
                    pan=0.25, humanize=0.08)

for _ in range(56):
    rhodes.rest(Duration.WHOLE)

# Bars 57-64: warm chords underneath the final statement
prog_final = key_major.progression("I", "vi", "IV", "V")
for _ in range(2):
    for chord in prog_final:
        rhodes.add(chord, Duration.WHOLE, velocity=42)

# ═════════════════════════════════════════════════════════════════
import sys

print(f"Key: Eb major → minor → major")
print(f"BPM: 80")
print(f"Parts: {list(score.parts.keys())}")
print(f"Duration: {score.duration_ms / 1000:.1f}s | {score.measures} measures")

if "--live" in sys.argv:
    print("Playing AN EXCEPTION OCCURRED (live engine)...")
    from pytheory_live.live import LiveEngine
    engine = LiveEngine(buffer_size=1024)
    engine.play_score(score)
else:
    print("Playing AN EXCEPTION OCCURRED...")
    play_score(score)
