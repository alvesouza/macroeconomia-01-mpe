# Provenance — Aula 7, Money and Inflation

Built 2026-09-12 with `/explainer`.

## What it is

**Thesis.** One number that no central bank can observe — the income elasticity of money
demand — decides whether it hits its inflation target. The rest of the lecture is the
derivation of that number, the equation it sits in, and the machinery assumed to get there.

**Length uncapped by request.** 20 beats, five acts, the whole lecture rather than a slice.

| Output | Value |
|---|---|
| Final video | `aula-07-money-and-inflation.mp4` — 2,515.667 s (**41 min 56 s**), 854×480, 15 fps, h264 + aac, 69.8 MB |
| Subtitles | `aula-07-money-and-inflation.srt`, accumulated from measured beat durations |
| Script | `script.md` — 8,256 words |
| Timing contract | `beats.json` — measured durations plus word-level speech marks |
| Scenes | `scenes.py` — 949 lines, 20 `Scene` subclasses |
| Data | `data/` — 5 cached series plus `registry.json` |

**Render quality: draft.** This is the `-ql` pass (854×480, 15 fps). The `-qh` pass
(1920×1080, 60 fps) has **not** been run; it is the expensive step and was deliberately left
until the draft was checked.

## Sources cited in the narration

| Claim | Source |
|---|---|
| Three functions of money, five properties, the M0–M2 ladder | Kurlat §10.1, printed pp. 191–192 |
| Bank balance sheet, why banks hold reserves, open market operation | Kurlat §§10.2–10.3, pp. 192–195 |
| The money multiplier, one over theta plus gamma minus theta gamma | Kurlat §10.3, eq. 10.3.1, p. 197 |
| Multiplier collapse at zero rates; US late 2008, base up ~5×, multiplier 2 → below 1 | Kurlat §10.3 and Fig. 10.3.1, p. 198 |
| Baumol-Tobin: sawtooth, average balance, first-order condition, real balances | Kurlat §10.4, eqs. 10.4.1–10.4.4, pp. 199–200 |
| Income elasticity one half | Kurlat ex. 11.1, p. 218 |
| GDP deflator and CPI worked examples (73 and −27 per cent; 300 → 330, index 110) | Kurlat §11.1, pp. 205–206 |
| Fisher, exact and approximate; the 100 → 111 → 1.088 baskets example | Kurlat §11.1, eq. 11.1.1, pp. 207–208 |
| Money market equilibrium, three channels, the classical view | Kurlat §11.2, eq. 11.2.1, pp. 208–209 |
| Inflation equals money growth minus elasticity times output growth | Kurlat §11.2, eq. 11.2.3, p. 211 |
| The level jump, and the growth-rate change that also makes prices jump | Kurlat §11.2, pp. 212–213 |
| Quantity equation as a definition; velocity as output over money demand | Kurlat §11.2, eqs. 11.2.4–11.2.5, pp. 213–215 |
| Seigniorage, the government budget constraint, the inflation tax, the Laffer limit | Kurlat §11.3, eq. 11.3.1, pp. 215–217 |
| Shoe leather with its formula, Friedman rule, menu costs, relative prices, bank seigniorage | Kurlat §11.4, eq. 11.4.1, pp. 217–218 |
| The Argentina anecdote (the author's father, twice a day) | Kurlat §11.4, p. 217 |
| The calibrated miss: 2, 3, 3.5, 0.5 per cent | Lista 6, Q2(b) |
| Lecture framing, notation, the three steady states | `Aula/MPE_Macro1_SlidesAula7_2026.pdf` |
| Reading plan and the lecture-versus-book diff | `Map/leituras-aula-07.md` |

Kurlat's offset is 0, so every printed page above is also the PDF page.
**No exercise statement is reproduced** — exercises are cited by number and page only.

## Data

Full detail in `data/registry.json`, including how each code was confirmed.

| Series | Source | Rows | Confirmation |
|---|---|---|---|
| Broad money growth (annual %) | WDI `FM.LBL.BMNY.ZG` | 5,110 | **Self-naming** — the API payload carries the indicator's own name |
| Inflation, consumer prices (annual %) | WDI `FP.CPI.TOTL.ZG` | 7,418 | Self-naming, same way |
| Country averages, 1990–2023 | derived | 159 | Countries with ≥15 years of both |
| IPCA, 12-month accumulated | BCB SGS `13522` | 320 | Magnitude: 4.22 per cent Aug 2026; SGS 433 matched published monthly prints for Jan–Jun 2024 |
| Meta Selic | BCB SGS `432` | 9,756 | Magnitude and shape: 2.0 to 26.5 per cent over 2000–2026, discrete Copom steps |

### What was deliberately omitted, and why

**No Brazilian monetary aggregate.** Codes 27791, 27841, 1788, 27810 and 1833 all return
plausible magnitudes and cannot be told apart: the SGS JSON endpoint returns no series names,
and the SGS metadata endpoint returns HTTP 400. Naming one "M1" would have been a guess
presented as a fact. Beat 17 says this out loud on screen rather than omitting it silently,
and the cross-country evidence in Beat 16 uses a source that names its own series.

### A finding that changed the video

Beat 16 was designed as "plot the data, confirm the theory". The data refused. All 159
countries give **slope 0.061, correlation 0.171** — apparently refuting the lecture. The cause
is one observation: Sierra Leone at 3,879 per cent average money growth, whose annual series
runs 7–76 per cent every year *except* **2001 at 131,119 per cent** and **2015 at −99.89 per
cent** — the signature of a redenomination or a units break, not an economy; its median year
is 23 per cent. Dropping averages above 100 per cent gives **slope 1.064, correlation 0.746**
across 148 countries, which is Kurlat's Fig. 11.2.1. The beat now carries that reversal,
which is both better exposition and a more honest use of the data.

## Toolchain

| Component | Version / setting |
|---|---|
| Manim Community Edition | 0.21.0 |
| Render | `-ql` → 854×480, 15 fps, h264 |
| ffmpeg / ffprobe | 8.1.1 |
| LaTeX | MiKTeX (`MathTex` throughout; no package prompts hit) |
| Narration | Speechify API, `https://api.speechify.ai`, `POST /v1/audio/speech` |
| Voice | `george` (en-US) |
| Model | `simba-3.2` |
| Audio | mp3, loudness normalisation on |

The API key lives in the repo's gitignored `.env` as `SPEECHIFY_API_KEY` and is **not
recorded here**. Billing for this build: **46,112 characters** in one pass, reported by
Speechify's own `billable_characters_count` field. Beats are cached against a text hash, so
re-rendering costs nothing and only edited beats would re-synthesise.

## Timing and verification

Compiled with `.claude/explainer_compile.py`. Per beat the slot is `max(video, audio)`; every
beat's render came out 50–450 ms **longer** than its narration, so audio was padded with
silence and no speech was truncated. No video needed freezing.

- Video total: **2,515.667 s**
- Audio total: **2,515.667 s**
- **Measured drift: 0.0 ms** (tolerance 40 ms, about one frame at 25 fps)
- Streams: `h264, 854×480` + `aac`

## Not versioned

`media/`, `audio/`, `build/` and `*.mp4` under `Videos/` are gitignored — render trees, the
narration clips and the 70 MB output. Versioned: `plan.md`, `script.md`, `beats.json`,
`scenes.py`, `companion.html`, `provenance.md`, the `.srt`, and `data/`.

## Open items

1. **The `-qh` pass** (1920×1080, 60 fps) has not been run. Expect well over an hour for
   ~42 minutes of animation.
2. **The interactive companion** (`companion.html`) — one slider on the elasticity, showing
   realised inflation and the miss against the 2 per cent target.
3. Beats 6 and 7 carry the most on-screen text of any in the video; if the draft reads
   crowded at 480p they are the two to re-cut before the high-quality render.
