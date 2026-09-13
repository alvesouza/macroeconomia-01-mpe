# Manim video pipeline — measured behaviour

Everything here was measured on this machine on 2026-09-12/13. Kit: `.claude/manim_kit.py`
(source of truth in `../Video explainer/lib/`). Compile: `.claude/explainer_compile.py`.

## Toolchain

Manim CE **0.21.0** · ffmpeg/ffprobe **8.1.1** · MiKTeX (`latex`, `pdflatex`, `dvisvgm`).
Installed with Manim: `manimpango`, `pycairo`, `moderngl`, `av`, `skia-pathops`, `networkx`;
it also upgraded `click` 8.4.1 → 8.5.0 for `cloup`.
**Not installed:** ImageMagick, `sox`, `pyarrow`, `papermill`. Do not depend on them.
`PIL` and `matplotlib` are present, so `mpl_figure()` and image assets work.

## The three failures the kit prevents

| Failure | Measured | Idiom |
|---|---|---|
| Glacial motion | **15.2 s per animation** — 165 events over 2 510 s | 0.5–3 s |
| Overlapping text | *"lend, and deposits rise"* drawn across *"excess reserves, earning nothing"* | never |
| Fake table | 3 labels stacked in 1 empty box | 1 cell per value |

**Root cause of the slowness:** expressing `run_time` as a *fraction of the beat's total*. A
148 s beat with 8 steps then had to crawl at ~18 s per move. The fix inverts it — animations
run at their own natural speed and the narration's slack is spent **holding a still frame**.
`Beat.step(anims, t, hold)` enforces it and raises above `MAX_RUN_TIME = 3.0`.
**A long beat needs more steps, never slower ones. 12–20 per beat.**

## Compile: three things that desync a video

1. **Manim quantises to whole frames, and rounds per `self.play()` call.** A beat can render
   *shorter* than its narration even when fractions sum to 1.0 — measured 16.600 s rendered
   against 16.656 s of speech. Padding audio to the video length would cut speech mid-word.
   So each beat's slot is **`max(video, audio)`**: pad the audio with silence *and* freeze the
   video's last frame, whichever is short.
2. **Concatenating AAC accumulates per-clip padding** — 10.1 ms over two clips. Concatenate
   **lossless PCM** and encode AAC exactly once, at the mux.
3. **ffmpeg cannot open Git Bash's `$PWD`** — a POSIX `/tmp/claude/...` path handed to the
   native Windows binary fails with "No such file or directory". Concat entries resolve
   relative to the list file, so write **relative** paths.

Never use `-shortest`: it hides drift by truncating whichever stream is longer — which is the
speech you wrote.

Result on the 20-beat Aula 7 video: 2 515.667 s video, 2 515.667 s audio, **0.0 ms drift**.

## Render quality

`-ql` 854×480/15 for drafting, **`-qh` 1920×1080/60 is the deliverable** (`-qm` 1280×720/30,
`-qk` 4K/60). Renders land in `media/videos/<module>/<resolution>/<Scene>.mp4` — one module, or
the compile script's single-directory assumption breaks.

**MiKTeX prompts to install a missing package on first use, which hangs an unattended render.**
If a `MathTex` beat stalls, run that beat once interactively.

## Gotchas that cost time

- Heredocs in the Bash tool mangle prose containing apostrophes and quotes — write Python to a
  file and run it instead.
- `print()` of box-drawing or accented characters dies on Windows cp1252 (`UnicodeEncodeError`).
  Keep script output ASCII; the *file* content can be UTF-8.
- `Path.read_text(newline=...)` does not exist on Python 3.12 — use `open()`.
- `from manim import *` does not reliably export `np`; import numpy explicitly.


## Frame quantisation: why a beat used to end before its narration

Manim renders whole frames, so every `play()` and `wait()` is floored to a frame boundary.
A beat with 21 steps issues about 42 of those calls; at 15 fps each discards up to 67 ms,
and the losses accumulate.

Measured on the 480p draft of aula-07, before the fix:

| Beat | Steps | Narration | Rendered | Gap |
|---|---|---|---|---|
| BeatOne | 21 | 81.65 s | 80.67 s | **-0.98 s** |
| BeatSix | 23 | 147.90 s | 147.05 s | -0.85 s |
| BeatNine | 18 | 112.20 s | 112.08 s | -0.12 s |

Seven of twenty beats fell outside `GAP_OK`. The shortfall tracks step count, which is the
signature of per-call rounding rather than of any one wrong duration.

`Beat.run()` used to trust the sum of its intended durations. It now steers by the clock:
after each step it compares `self.scene.renderer.time` against where it should be and spends
the difference, then tops up to `self.total` rounding **up** to the next frame. Overshooting
by milliseconds is free -- `explainer_compile` pads the audio -- while undershooting shows as
a freeze or clips the last word. BeatOne went from -0.98 s to +0.22 s.

The compile step had been hiding this by cloning the final frame to cover the narration. The
picture was right and the timing was wrong; the gate was correct to fail it.
