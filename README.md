```
    _       _                        _        _   _
   (_)_ __ | |_ ___ _ __ _ __  _ __ | |_ __ _| |_(_) ___  _ __  ___
   | | '_ \| __/ _ \ '__| '_ \| '__/ _ \ __/ _` | __| |/ _ \| '_ \/ __|
   | | | | | ||  __/ |  | |_) | | |  __/ || (_| | |_| | (_) | | | \__ \
   |_|_| |_|\__\___|_|  | .__/|_|  \___|\__\__,_|\__|_|\___/|_| |_|___/
                         |_|          ~ written in python ~
```

# Interpretations

An album of compositions written in Python using [pytheory](https://github.com/kennethreitz/pytheory).

Each track is a `.py` file. Run it to hear it.

![](https://kennethreitz.org/static/images/interpretations-player.png)

## Tracks

1. **Raga Midnight** — D Phrygian (Bhairavi), shruti just intonation, 90 BPM. Tabla, sitar, tambura, dhol. Hand-written tabla solo with tihai cadence.
2. **Chakra** — Root to crown frequency activation journey. Shruti tuning at A=432 Hz. Ukulele opening, singing bowls, harmonium, tambura, sitar, theremin. Metric modulation tempo changes (60 → 90 → 108 → 135 BPM) ascending through seven chakras.
3. **Ghost Protocol** — F minor, 128 BPM. Portishead-style dark Rhodes intro with trip-hop beat, morphing into a Strobe-inspired hypnotic build. Saw arp emerges, kick doesn't arrive until bar 49. NES square wave melody at the emotional peak.
4. **Acid Reign** — A minor, 140 BPM. Dual 303 acid bass lines (saw + square) with resonant filter sweeps (Q up to 20). Cajon in cathedral reverb, Rhodes pad, 808 sub. Five hand-written groove patterns.
5. **Silk Road** — D minor, 95 BPM. A caravan picking up musicians along the ancient trade route. Koto solo (China) → sitar + tabla (India) → mandolin + doumbek (Persia) → guitar + cajon (Mediterranean) → all together. Nobody leaves, everyone adds their voice.
6. **Deep Time** — B minor, 40 BPM, just intonation. Ambient drone. Tingsha, rainstick, finger cymbals, singing bowls, didgeridoo, sine drones, harmonium, theremin, choir, cello. 7.5 minutes of deep listening.
7. **The Interruption** — D minor, 85 BPM. A baroque harpsichord and string quartet playing beautifully. Then at bar 33, a drum & bass breakbeat slams in with sub bass and reese. The strings keep playing like nothing happened. The beat dissolves, the quartet wins.
8. **The Temple** — A Phrygian (Bhairavi), 65 BPM, shruti just intonation, A=432 Hz. Devotional layers inside a vast stone chamber. Singing bowls, tambura drone, harmonium, sitar, bansuri, tabla. The reverb is the instrument. Everything enters slowly, sings together, then dissolves back into silence.
9. **The Dialogue** — E Phrygian (Bhairavi), 75 BPM, shruti just intonation, A=432 Hz. Sitar (human) and theremin (machine) start alone, find each other through call-and-response, and become something neither could be on their own. House beat enters when they find the groove.
10. **Voltage** — F minor, 138 BPM. Raw oscillators, nothing else. Sine sub, saw lead, pulse counter-rhythm. Rhythm is pitch. Saw arp solo, pulse arp solo, 32nd note chaos at the peak. Aggressive, monophonic, electric.
11. **The Observatory** — G minor, 112 BPM. Chapel harmonies broadcast through shortwave static. Radio hiss, singing bowl, square-wave organ, choir, saw arp, supersaw halo pad, theremin signal melody. Patient house pulse arrives at bar 33.
12. **Gravity** — C minor, 88 BPM. Sparse piano stabs, 808 sub, boom bap drums with trap hat evolution. Rhodes melody, string swell. Tambura buried underneath, singing bowl bookends, one sitar bend in the breakdown. The weight of it all.
13. **Sleight of Hand** — D minor, 100 BPM. Music box → didgeridoo → jazz piano → 808 drop → solo theremin → choir → acid 303 rips through the choir → music box returns over boom bap. You never see the next move coming.
14. **An Exception Occurred** — Eb major→minor→major, 80 BPM. Piano-driven arc: stability → spiritual seeking (tambura, sitar, om chant) → psychosis (wild theremin, chaos drums) → despair → hymn (pipe organ) → recovery. Every note by hand.
15. **Voices** — F# minor, 65 BPM. Five vocal parts multiplying across the stereo field. Piano enters as reality. One last whisper, then silence.
16. **Intrusive** — Bb minor, 92 BPM. One saw synth phrase repeating. Rhodes tries to play something else. Drums try to drown it. Stop fighting — acceptance, sub bass, cello. It passes.
17. **Waveforms** — F minor, 118 BPM. Pure synthesis showcase — percussive blips stacking, FM solo, saw/square duet in thirds, sine/triangle/PWM canon.
18. **Tape Memory** — Db minor, 90 BPM. Mellotron flute dreams surrounded by new synthesis. FM bells, drift oscillator, crotales, granular texture, hard_sync bass, PWM lead, wavefold, ring_mod. Theremin solo at the peak.
19. **Emergence** — E minor, 100 BPM. Acoustic births electronic. Singing bowls, tingsha, didgeridoo, mellotron flute, sitar 16th arps with 32nd shreds, then synths emerge. Both worlds collide at the peak.
20. **Music Box Factory** — G major, 108 BPM. Eight tuned percussion instruments only. Kalimba, vibraphone, celesta, marimba, glockenspiel, xylophone, crotales, timpani. Tubular bells mark sections. No synths, no strings — just metal and wood.
21. **Cathedral** — D minor, 60 BPM. Ancient stone. Tubular bells in taj_mahal, bagpipe drone, mellotron choir, timpani thunder, pipe organ, kick in cathedral reverb.
22. **Beast Mode** — G minor, 135 BPM. Trap drums, 808 slides, distorted saw bass, sitar hook + shred solo, mellotron flute drop, timpani war drums. The hardest track on the album.

## Usage

```bash
uv sync
```

**Interactive player** — pick a track, play/pause, seek:

```bash
uv run play.py
```

**Play a specific track:**

```bash
uv run play.py tracks/the_temple.py
```

**Playback options:**

```bash
uv run play.py tracks/acid_reign.py --from 17 --to 32       # measure range
uv run play.py tracks/the_temple.py --from-time 3:30         # seek to time
uv run play.py tracks/ghost_protocol.py --solo arp,kick       # solo parts
uv run play.py tracks/deep_time.py --mute wind                # mute parts
uv run play.py tracks/the_temple.py --pitch 440               # override tuning
uv run play.py tracks/acid_reign.py --bpm 160                 # override tempo
uv run play.py tracks/silk_road.py --loop 3                   # loop playback
```

**Export & inspect:**

```bash
uv run play.py tracks/raga_midnight.py -o raga.wav            # export WAV
uv run play.py tracks/culture_clash.py --info                  # show metadata
uv run play.py tracks/the_interruption.py --parts              # list parts
uv run play.py --list                                          # list all tracks
```

`Ctrl+C` to stop playback.

See the [changelog](CHANGELOG.md) for detailed track history.

## License

ISC
