# Aula 7 data — what is verified, what is not

Cached in `Videos/aula-07-money-and-inflation/data/` with `registry.json`. Fetched 2026-09-12.

## Confirmed, and how

| Series | Source | Rows | How it was confirmed |
|---|---|---|---|
| Broad money growth (annual %) | WDI `FM.LBL.BMNY.ZG` | 5 110 | **Self-naming** — the payload carries the indicator's own name |
| Inflation, consumer prices (annual %) | WDI `FP.CPI.TOTL.ZG` | 7 418 | Self-naming, same way |
| Country averages 1990–2023 | derived | 159 | Countries with ≥15 years of both |
| IPCA, 12-month accumulated | BCB SGS `13522` | 320 | Magnitude: 4.22 % Aug 2026; and SGS `433` returned the exact published monthly prints for Jan–Jun 2024 |
| Meta Selic | BCB SGS `432` | 9 756 | Magnitude and shape: 2.0 → 26.5 % over 2000–2026, discrete Copom steps |

**Prefer World Bank WDI when a series must be named**: the API returns the indicator's own
name in the payload, so the code is self-confirming. BCB SGS does not.

## Not used, deliberately

**No Brazilian monetary aggregate.** Codes `27791`, `27841`, `1788`, `27810`, `1833` all return
plausible magnitudes (~R$ 650 bn, ~R$ 432 bn, ~R$ 7.6 tn …) and **cannot be told apart**:

- the SGS JSON data endpoint returns values with **no series name**;
- the SGS metadata endpoint `www3.bcb.gov.br/sgspub/localizarseries/localizarSeriesJSON.do`
  is **dead — HTTP 400 "Invalid path"**.

Calling one of them "M1" would be a guess presented as a fact. The video says this out loud
on screen rather than omitting it silently.

## API traps

- **SGS row cap**: a 26-year *daily* pull (series `432`) returns **HTTP 406**. Page it in
  five-year windows and dedupe on date.
- **SGS dates are `dd/MM/yyyy`** in both the query (`dataInicial`/`dataFinal`) and the
  response. Parse with `dayfirst=True` or every day/month pair under 13 silently transposes.
- **WDI response is a two-element envelope** `[metadata, rows]` — the rows are element 1 — and
  it **pages**: read `pages` from the metadata and loop, or you silently get the first page.

## The finding that changed the video

Plotting all 159 countries gives **slope 0.061, correlation 0.171** — the theory appears
refuted. The cause is a single observation: **Sierra Leone at 3 879 % average money growth**.
Its annual series runs 7–76 % every year *except* **2001 at 131 118.96 %** and
**2015 at −99.89 %** — a redenomination or a units break, not an economy. Its median year is
23.0 %; the mean without those two years is 23.4 %.

Dropping averages above 100 % leaves 148 countries at **slope 1.064, correlation 0.746** —
which is Kurlat's Figure 11.2.1 (p. 211), earned from the raw data rather than asserted.

**Do not "clean" this silently in a future cut.** The reversal is the strongest beat in the
video precisely because the failure is shown first.
