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

## Tracks

1. **Raga Midnight** — D Phrygian (Bhairavi), shruti just intonation, 90 BPM. Tabla, sitar, tambura, dhol. Hand-written tabla solo with tihai cadence.
2. **Culture Clash** — D minor, 95 BPM. Didgeridoo drone, Rhodes, tabla with fills, sitar arps, NES Mario theme, Hotline Bling on steel drum, theremin solo, marching snare military finale with DCI cadence. 808 sub bass throughout.
3. **Chakra** — Root to crown frequency activation journey. Shruti tuning at A=432 Hz. Ukulele opening, singing bowls, harmonium, tambura, sitar, theremin. Metric modulation tempo changes (60 → 90 → 108 → 135 BPM) ascending through seven chakras.
4. **Ghost Protocol** — F minor, 128 BPM. Portishead-style dark Rhodes intro with trip-hop beat, morphing into a Strobe-inspired hypnotic build. Saw arp emerges, kick doesn't arrive until bar 49. NES square wave melody at the emotional peak.
5. **Acid Reign** — A minor, 140 BPM. Dual 303 acid bass lines (saw + square) with resonant filter sweeps (Q up to 20). Cajon in cathedral reverb, Rhodes pad, 808 sub. Five hand-written groove patterns.
6. **Silk Road** — D minor, 95 BPM. A caravan picking up musicians along the ancient trade route. Koto solo (China) → sitar + tabla (India) → mandolin + doumbek (Persia) → guitar + cajon (Mediterranean) → all together. Nobody leaves, everyone adds their voice.
7. **Deep Time** — B minor, 40 BPM, just intonation. Ambient drone. Tingsha, rainstick, finger cymbals, singing bowls, didgeridoo, sine drones, harmonium, theremin, choir, cello. 7.5 minutes of deep listening.
8. **The Interruption** — D minor, 85 BPM. A baroque harpsichord and string quartet playing beautifully. Then at bar 33, a drum & bass breakbeat slams in with sub bass and reese. The strings keep playing like nothing happened. The beat dissolves, the quartet wins.
9. **The Temple** — A Phrygian (Bhairavi), 65 BPM, shruti just intonation, A=432 Hz. Devotional layers inside a vast stone chamber. Singing bowls, tambura drone, harmonium, sitar, bansuri, tabla. The reverb is the instrument. Everything enters slowly, sings together, then dissolves back into silence.

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

## License

ISC
