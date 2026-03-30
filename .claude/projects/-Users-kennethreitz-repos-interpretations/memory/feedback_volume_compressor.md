---
name: Volume and compressor behavior
description: part.volume doesn't always work as expected due to master compressor — use velocity for fading, rests for silence
type: feedback
---

Don't use volume=0.0 on parts and then .set(volume=X) to fade in — the renderer may not handle this correctly. Instead:
- Start parts at their real volume
- Use .rest() for silent sections
- Fade dynamics via velocity, not volume
- The master compressor normalizes sparse arrangements to full volume — more parts playing simultaneously keeps relative levels sane

**Why:** We discovered volume=0.0 parts produced silence even after .set() changes, and the compressor over-amplified solo instruments.
**How to apply:** Always set non-zero starting volume. Use velocity for dynamics. For drum parts, volume param requires the pytheory fix (drum_part.volume multiplication in play.py).
