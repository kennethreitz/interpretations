---
name: Taj mahal reverb creates choir sound on drums
description: Convolution reverb (taj_mahal) on percussive hits creates unwanted harmonic/choral artifacts
type: feedback
---

Don't use reverb_type="taj_mahal" on drum/percussion parts — the long IR creates harmonic resonances that sound like a choir. Use algorithmic reverb (reverb=0.35, reverb_decay=1.5) for drums instead.

**Why:** Discovered during Raga Midnight — tabla with taj_mahal reverb sounded like a choir was singing. Cathedral reverb is OK for cajon. Taj mahal works great on sustained instruments (tambura, sitar, Rhodes, pad, singing bowl).
**How to apply:** Reserve taj_mahal for melodic/sustained instruments. Use algorithmic or cathedral reverb for percussion.
