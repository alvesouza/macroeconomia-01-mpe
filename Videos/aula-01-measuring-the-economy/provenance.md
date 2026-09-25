---
tags: [video, aula-01, explainer, provenance]
date: 2026-09-18
slug: aula-01-measuring-the-economy
---

# Provenance — Aula 1: Measuring the Economy

## Topic and thesis

Kurlat (2020), chapters **1–2**, printed pages 15–44 (offset 0: printed page = PDF page).

> Every macroeconomic number is the output of a construction, and every construction is a
> choice. Learning macro measurement is learning which choice was made, and in which
> direction it bends the answer.

Purpose *first exposure*; math *textbook derivation*; examples *calibrated case + the course's
own exercises + Brazilian data* (scoping answers, 2026-09-17). Narration **English**, per the
global rule, while the course itself runs in pt-BR.

## Sources cited, by beat

| Beat | Source | Printed page |
|---|---|---|
| BeatFirmIdentity | Kurlat §1.1, Table 1.1 | 15–17 |
| BeatTelescope | Kurlat Example 1.2 | 17 |
| BeatExpenditure | Kurlat Example 1.6; inventory rule | 18–19 |
| BeatConventions | Kurlat Examples 1.5, 1.7, 1.8, 1.11 | 18–22 |
| BeatGNP | Kurlat §1.1 (GDP vs GNP), stock–flow | 21 |
| BeatExpandia | Kurlat Example 1.13 (Expandia), eq. 1.2.1 | 23 |
| BeatCovariance | Kurlat's one-sentence claim, proved | 24 |
| BeatFisher | Kurlat Alternative 3, Fisher chain | 24 |
| BeatBias | Substitution bias; Boskin Commission (1996) | 25 |
| BeatDeflatorCPI | Kurlat deflator vs CPI; exporter mirror | 24 |
| BeatLogs–BeatLogScale | growth arithmetic, formalised in `Map/aula-01-mensuracao/03` | — |
| BeatPPPproblem | Kurlat Example 1.14 | 25 |
| BeatPPPconstruct | Kurlat PPP construction; Big Mac footnote 2 | 25–27 |
| BeatBalassaSetup/Prediction | Balassa–Samuelson, derived in `Map/aula-01-mensuracao/04` | — |
| BeatDenominator | Kurlat §1.2; France–US decomposition | 27 |
| BeatHDI | Kurlat §2.1, Figure 2.1.1 | 31–33 |
| BeatRawls / BeatJensen | Kurlat §2.2, eqs. 2.2.1–2.2.6; quote p. 35 | 33–35 |
| BeatLambdaDerive/Brazil | Jones–Klenow decomposition, derived in `Map/aula-01-mensuracao/05` | 33–40 |

**Exercises are cited by number and page only; no statement is reproduced or animated.**
1.1–1.2 (p. 26), 1.3, 1.4–1.5 (p. 27), 2.1–2.4 (pp. 42–43), 2.10 (p. 44), 3.1–3.2 (pp. 52–53),
11.6 (Cagan, named in BeatLogs).

## Data

Nine World Bank WDI indicators, retrieved **2026-09-18** via `data/fetch_wdi.py`, registered
with row counts and hashes in `data/registry.json`. Every indicator is **self-confirming**: the
API payload carries its own name, which the fetcher prints and the registry quotes verbatim.

Python's TLS stack fails against `api.worldbank.org` in this environment (`SSLEOFError`), so the
fetcher shells out to `curl`. Recorded because it will recur in the other eight videos.

**Not used, deliberately:** BCB SGS series 433 and 13522 (IPCA). The Brazilian CPI is already in
the set as `FP.CPI.TOTL.ZG`, from the same source and vintage as the GDP deflator it is compared
against; mixing a BCB series with a WDI series would put a source difference inside a wedge the
video attributes to basket composition.

### λ is computed, never quoted

`data/check_lambda.py` evaluates the Jones–Klenow decomposition for Brazil against the US at
σ = 1. Four caveats, all stated out loud in the narration:

1. household consumption per head, not the paper's C+G;
2. the **leisure term is omitted** — no verified hours series was fetched for both countries;
3. ū has no market price, so the mortality term is reported at ū ∈ {0, 5, 10};
4. σ = 1 is Jones and Klenow's own conservative choice, which *minimises* the inequality penalty.

Verification: the closed-form `E[ln c] − ln E[c] = −s²/2` is checked against a 400,000-draw
Monte Carlo for both countries (agreement within 0.01 nats). Result at ū = 5: **λ ≈ 0.119**,
against a PPP consumption ratio of 0.227.

## Narration

- Voice: `george` (en-US), model `simba-3.2`, Speechify. **The API key is never recorded here,
  printed, or placed in any file that is not `.env`.**
- 26 beats, 8,649 words, 49,706 characters synthesised.
- Every duration measured with `ffprobe`; none estimated.

**Pauses.** The script marks 62 `[pause]` points. Speechify ignores intra-clip silence —
verified live: a passage with and without ellipses measured **identically at 3.648 s** — so a
pause cannot be bought inside a clip. Each one is realised instead as held frame time in
`scenes.py` (`PAUSE_S = 2.5 s`, added to the beat's budget), which `explainer-compile` pads with
silence because it slots every beat at `max(video, audio)`.

**Rate.** `george` speaks at roughly **197 words per minute**, not the 150 wpm the command's
budgeting assumes. The beat budgets in `plan.md` were rebuilt from measured audio rather than
from the word count; this is worth carrying into the other eight videos.

## Toolchain

| Component | Version / setting |
|---|---|
| Manim Community Edition | 0.21.0 |
| ffmpeg / ffprobe | 8.1.1 |
| `video_explainer` kit | 0.2.0, imported (never vendored) |
| Draft render | `-ql`, 854×480, 15 fps |

### One fix made to the shared kit

`speechify_tts.py` honoured the server's `Retry-After` header alone, which this plan pins at
**1.0 s** against a *concurrency* limit ("your plan allows 1 simultaneous request") that does not
clear in a second — so all four retries fired into the same wall and the run died. The module's
own escalating `delay` existed but was never used. Changed to:

```python
wait = max(float(r.headers.get("Retry-After", delay)), delay)
```

so the backoff runs 1.5 → 3 → 6 s. The limit is strict enough that synthesis of a 26-beat script
still needs repeated invocations; the client's text-hash cache makes each one resume for free.

## Deliverables

| File | Kept in git? |
|---|---|
| `plan.md`, `script.md`, `beats.json`, `scenes.py`, `provenance.md` | yes |
| `data/*.csv`, `data/registry.json`, `data/fetch_wdi.py`, `data/check_lambda.py` | yes |
| `figures/*.png` | yes (cached, cheap) |
| `audio/`, `media/`, concat lists | no — gitignored render artefacts |

## Results -- 480p draft, compiled 2026-09-20

| | |
|---|---|
| File | `aula-01-measuring-the-economy-480p.mp4` |
| Runtime | **2855.2 s = 47.6 min** |
| Resolution | 854x480, h264 + aac |
| Size | 79.8 MB |
| **Measured drift** | **0.0 ms** (tolerance 40 ms) |
| Subtitles | `aula-01-measuring-the-economy.srt`, built from the same measurements |

Per-beat narration, render and slot lengths agree exactly for all 26 beats: every beat's
render is its narration plus its scripted holds, and the compiler slots each at
`max(video, audio)`.

## Faults found and fixed during the draft pass

The draft exists to be watched before the expensive pass. Three real defects surfaced:

1. **The derivation stack grew out of its slot** into the caption strip. The kit refused to
   render the frame -- correctly -- rather than write a caption across the algebra.
2. **The first fix did not work, for an instructive reason.** `Stage.show()` runs its overlap
   check when a step is *built*, not when it plays, so a deferred `.animate` rescale is
   invisible to it. Geometry corrections in a scene must mutate the mobject immediately.
3. **Lines rendered on top of each other.** Re-fitting the whole stack on every line meant
   each new line was sized against an already-shrunken predecessor until the spacing
   collapsed. Caught only by pulling a frame out of the rendered beat and looking at it --
   no gate reported it, because every individual `Stage` slot was legal.
   Fixed by laying each stack on a fixed grid sized to that scene's own line count.

The lesson for the remaining eight videos: **`beatcheck` and `layoutcheck` passing is not
evidence that the frames are right.** Extract a frame from each derivation beat and look.

### Render-time outlier

`BeatBias` took **4,352 s** against 20-70 s for every other beat in the same pass -- a 60x
outlier, consistent with MiKTeX fetching a package on first use mid-render. Output was
correct. Budget for it in the 1080p pass rather than treating a stalled beat as a hang.

### layoutcheck

Not used for this video. Its dry run had consumed hours without emitting a line, while the
real render enforces the same guards (`Stage.show`'s overlap assertion and `check_ink` on
every step) *and* produces frames. The render is strictly the more informative gate.
