# Rebuild the 20 Manim scenes of aula-07 against the kit idiom and ship one 1080p60 cut, working sequentially and resumably

## Context

- `Videos/aula-07-money-and-inflation/scenes.py:1` — the OLD cut, 949 lines, 20 `Scene`
  classes, its own private `steps()`/`heading()`/`ols()` helpers at lines 30-66. Averages
  8.3 steps/beat and 15.2 s/animation. This file is the artifact being replaced.
- **15 of 20 beats are already rewritten against the kit.** The parallel attempt died
  after group 4, not before group 1:
  - `Videos/aula-07-money-and-inflation/scenes_g1.py:14` — BeatOne..BeatFive (21, 19, 24, 20, 26 steps)
  - `Videos/aula-07-money-and-inflation/scenes_g2.py:14` — BeatSix..BeatTen (23, 20, 26, 18, 25 steps)
  - `Videos/aula-07-money-and-inflation/scenes_g3.py:14` — BeatEleven..BeatFifteen (24, 28, 24, 28, 20 steps)
  - All three carry an **identical import header** (`scenes_g2.py:6-11`) and define **no
    module-level names** beyond it — every helper is a `@staticmethod` inside its class
    (`scenes_g3.py:394`). Concatenation therefore cannot collide.
  - Missing: **BeatSixteen..BeatTwenty**. That is the only scene code still to write.
- `.claude/manim_kit.py:76` — `Beat.step(anims, t=NORMAL, hold=1.0)`; `t > MAX_RUN_TIME =
  3.0` raises (`:83`), and `motion > narration` raises at `run()` (`:97`). Both failures
  are compile-time, not visual.
- `.claude/manim_kit.py:117` — `SLOTS = title | main | left | right | aside | note`, one
  occupant each; `Stage.show()` (`:148`) emits `FadeOut(old) + FadeIn(new)`, which is the
  mechanism that makes the BeatSix overlap impossible.
- `.claude/manim_kit.py:208` / `:261` — `table(columns, rows, ...)` and
  `balance_sheet(assets, liabilities)`: one cell per value. The "3 labels in 1 box"
  balance sheet in the old BeatSix is what these replace.
- `.claude/manim_kit.py:334` — `mpl_figure(draw, name, width, cache_dir="figures",
  regenerate=False)`; caches to `figures/<name>.png` and **reuses the PNG unless
  `regenerate=True`**, so re-rendering a beat does not redraw.
- `Videos/aula-07-money-and-inflation/mpltest.py:1` — a working `mpl_figure` call against
  the 148-country scatter; `figures/scatter_clean.png` already exists and is committed.
  This is the template for BeatSixteen, not something to invent.
- `Videos/aula-07-money-and-inflation/manim_kit.py` — byte-identical to `.claude/manim_kit.py`
  (verified with `diff -q`). Scenes import `manim_kit` locally, so **renders must run with
  cwd = the project directory** (also required by `load_beats()`'s `Path.cwd()/beats.json`
  at `.claude/manim_kit.py:55` and by the relative `data/` and `figures/` paths).
- `beats.json` — 20 beats, `total_seconds = 2510.328`, each beat carrying `seconds`,
  `text_sha256` and `speech_marks` (per-word timings). Durations, longest first:
  BeatSixteen 163.920 · BeatEighteen 155.880 · BeatNineteen 154.416 · BeatTwenty 153.696 ·
  BeatSix 147.912 · BeatTen 146.040 · BeatFive 138.960 · BeatThirteen 133.416 ·
  BeatTwelve 131.856 · BeatFourteen 128.472 · BeatSeven 124.080 · BeatFifteen 114.840 ·
  BeatSixteen-adjacents BeatEleven 107.928 · BeatSeventeen 111.816 · BeatEight 112.056 ·
  BeatNine 112.248 · BeatThree 113.280 · BeatFour 90.600 · BeatTwo 87.264 · BeatOne 81.648.
  **Narration is final — `beats.json`, `audio/*.mp3` and `script.md` are read-only in this plan.**
- `.claude/explainer_compile.py:63` — `find_render_dir` globs `media/videos/*/*`, filters
  by `--quality` and takes the highest resolution. `media/videos/` currently holds four
  modules: `scenes`, `scenes_g3`, `kittest`, `mpltest` — all at `480p15`. The single-render-
  directory assumption survives only because the new render will be the sole `1080p60` dir;
  prune the rest anyway.
- `.claude/explainer_compile.py:120` — compile aborts if any beat's `<BeatId>.mp4` is
  missing ("Never compile a partial video"), and pads with `max(video, audio)` per beat.
- `.gitignore:57-60` — `Videos/*/media/`, `Videos/*/audio/`, `Videos/*/build/` and
  `Videos/*/*.mp4` are untracked. The current 480p deliverable exists **only on disk**;
  `scenes.py`, `scenes_g1..g3.py`, `beats.json`, `figures/` and `data/` are committed.
- `.agent/notes/manim-video-pipeline.md` — pacing/compile/toolchain facts; not re-derived here.
- `.agent/notes/aula-07-data.md` — Sierra Leone: 3 879 % average from 2001 (131 118.96 %) and
  2015 (-99.89 %); 159 countries → slope 0.061 / r 0.171; drop averages > 100 % → 148
  countries, slope 1.064 / r 0.746. "Do not clean this silently."

## Approach

Treat the rebuild as a **resume**, not a restart: keep `scenes_g1..g3.py` as written, add a
fourth group for BeatSixteen..BeatTwenty, gate every beat through one check script, then
concatenate the four groups into a single `scenes.py` and render once at `-qh`.

Rejected: rewriting all 20 beats from `scenes.py` again — it discards 15 beats of finished,
kit-conformant work whose step counts (18-28) already clear the floor, and doubles the render
budget for no visual gain.

Rejected: rendering directly from four `scenes_g*.py` modules and pointing the compiler at
one of them — Manim writes `media/videos/<module>/<quality>/`, so four modules produce four
render directories and `find_render_dir` (`.claude/explainer_compile.py:63`) picks exactly
one, silently compiling a partial video.

## Chunking and resume

Six chunks, each ending in a durable on-disk artifact. **The artifact, not the transcript,
is the resume signal** — on restart, re-run the check of the last completed chunk and
continue at the first beat whose check JSON is absent or failing.

| Chunk | Scope | Resume signal |
|---|---|---|
| C0 | Backup + prune + check harness | `build/_backup_480p/` exists; `tools/beatcheck.py` runs |
| C1 | Audit BeatOne..BeatFifteen (already written) at `-ql` | `build/checks/<Beat>.json` with `"pass": true`, 15 files |
| C2 | Write + check BeatSixteen..BeatTwenty (`scenes_g4.py`) | `build/checks/<Beat>.json`, 20 files |
| C3 | Merge four groups into `scenes.py` | `python -c "import scenes"` clean; 20 classes |
| C4 | Render all 20 at `-qh` | `media/videos/scenes/1080p60/<Beat>.mp4`, 20 files |
| C5 | Compile + drift + cleanup | `aula-07-money-and-inflation.mp4` at 1080p60, drift 0 ms |

Beats inside C1, C2 and C4 are independently resumable: one beat, one command, one artifact.

## Pacing rule (applies to every beat, C1 audit and C2 authoring alike)

1. **Step floor:** `steps >= max(12, ceil(seconds / 9))`. BeatSixteen (163.9 s) needs >= 19;
   BeatOne (81.6 s) needs >= 12. Target band 14-24. C1's measured counts (18-28) all pass.
2. **Motion budget:** `sum(t) <= 0.30 * seconds`. At 150 s that is 45 s of motion across
   ~20 steps — an average `t` near 1.0 s, which is the idiom. The kit's `MAX_RUN_TIME`
   catches only the single worst step; this rule catches the aggregate.
3. **`t` by kind:** `FAST` (0.6) for a text/slot swap, `NORMAL` (1.0) for building a
   diagram or table, `SLOW` (1.8) only for a curve or graph being drawn. Never a literal
   above 2.0; never a value computed from `beat.total`. *Expressing `run_time` as a fraction
   of the beat total is the exact defect being removed — see the note's root-cause section.*
4. **`hold` by narration weight:** one step tracks one sentence group of `script.md`. Set
   `hold` to that group's word count divided by 20, rounded to 0.5, floor 1.0 — so a step
   covering 60 words of speech holds three times as long as one covering 20. Weights are
   relative; the kit normalises them against the measured slack (`.claude/manim_kit.py:100`).
   Give the beat's punchline frame (the result, the reversal, the final identity) the
   largest weight in its beat.
5. **One slot, one occupant.** Every visual enters through `Stage.show(slot, mob)`. Use
   `Stage.add_to` only for marks that are positioned relative to an existing mobject
   (a dot on an axis, an arrow between two cells).
6. **Every number in a grid is a cell.** `table()` or `balance_sheet()` — never labels
   arranged inside a rectangle.

## Rendering medium, per beat

| Beats | Medium | Why |
|---|---|---|
| 1-15, 18-20 | Pure Manim (`table`, `balance_sheet`, `axes_panel`, `sawtooth`, `eq`, `bullets`) | The argument is constructed: a ledger changed a line at a time, a sawtooth, a hump-shaped Laffer curve, a chain of four claims. Manim builds; matplotlib cannot. |
| **16** | `mpl_figure` for the three clouds; Manim for the annotation | 159 scatter points twice, plus a 34-point Sierra Leone series with two outliers off-scale. Dense data — the kit's own stated dividing line (`.claude/manim_kit.py:340`). |
| **17** | `mpl_figure` for the dual series; Manim for the callouts | Two ~320-point monthly series (IPCA 12 m, Meta Selic) over 26 years on shared axes. |

BeatSixteen needs **four** cached figures, named so the cache keys are stable:
`scatter_raw159` (full range, axis out to ~4 000 %, the apparent refutation),
`scatter_raw159_zoom` (same data, corner detail showing the crush),
`sierraleone_series` (annual broad-money growth, log axis, 2001 and 2015 annotated),
`scatter_clean` (**already built and committed** — reuse, do not regenerate).
BeatSeventeen needs one: `brazil_ipca_selic`.
Slope/correlation labels must be **computed from the CSVs at figure-draw time**, not typed
in — the numbers in `.agent/notes/aula-07-data.md` are the expected output of that
computation and the check for it, not the source.

BeatSeventeen must keep the on-screen statement that no Brazilian monetary aggregate is
shown and why (`script.md`, BeatSeventeen, final paragraph). Do not quietly drop it to
simplify the visual.

## Steps

### C0 — Backup, prune, harness

1. [ ] Copy the current deliverable out of the render path:
   `mkdir -p build/_backup_480p && cp aula-07-money-and-inflation.mp4 aula-07-money-and-inflation.srt build/_backup_480p/ && cp -r media/videos/scenes/480p15 build/_backup_480p/renders`
   — verify: `ls build/_backup_480p/renders/*.mp4 | wc -l` prints `20` and
   `ffprobe -v error -show_entries format=duration -of csv=p=0 build/_backup_480p/aula-07-money-and-inflation.mp4`
   prints ~`2515.667`. **`build/` is gitignored — this backup is the only copy. Do not skip.**
2. [ ] Record the old cut's git identity so it can be restored: `git log -1 --format=%H -- Videos/aula-07-money-and-inflation/scenes.py`
   — verify: a commit hash is printed and written into the Rollback section below.
3. [ ] Prune stale render modules so one directory remains:
   `rm -rf media/videos/kittest media/videos/mpltest media/videos/scenes_g3 media/images/kittest media/images/mpltest media/images/scenes_g3`
   — verify: `ls media/videos` lists only `scenes`.
4. [ ] Write `tools/beatcheck.py` (project-local, committed) taking a beat id and a
   quality dir. It must, in one run: (a) count `Beat.step(` calls in the beat's class via
   `ast`; (b) sum the literal `t` arguments; (c) read `seconds` from `beats.json`;
   (d) `ffprobe` the rendered mp4; (e) write `build/checks/<Beat>.json` with
   `steps, motion, seconds, video, shortfall, pass`. Pass condition, all four:
   `steps >= max(12, ceil(seconds/9))`, `motion <= 0.30*seconds`, `max(t) <= 2.0`,
   `0 <= seconds - video <= 0.6`.
   — verify: `python tools/beatcheck.py BeatEleven --quality 480p15` exits 0 and prints a
   JSON line (BeatEleven already has a 480p render at `media/videos/scenes_g3/480p15` —
   run this step *before* step 3, or re-render it).
   *Keep script output ASCII: `print()` of box-drawing or accented characters dies on
   Windows cp1252 (see the pipeline note).*

### C1 — Audit the fifteen written beats

5. [ ] For each of BeatOne..BeatFifteen, in order, render a draft from its group module
   with cwd = the project dir:
   `python -m manim render -ql --media_dir media scenes_g1.py BeatOne`
   — verify: exit 0, and `python tools/beatcheck.py BeatOne --module scenes_g1 --quality 480p15`
   writes `"pass": true`. A beat that fails is edited **in its group file** and re-checked;
   do not defer failures to after the merge.
   *First run of a beat containing new `MathTex` can hang on a MiKTeX package prompt — run
   the first beat of each group interactively before backgrounding the rest.*
6. [ ] Screenshot-audit the three beats the old cut was caught on plus a sample: for
   `BeatSix`, `BeatSeven`, `BeatThirteen` and one more of choice, extract three frames
   (`ffmpeg -v error -ss <t> -i media/videos/scenes_g*/480p15/<Beat>.mp4 -frames:v 1 build/frames/<Beat>_<t>.png -y`
   at 25 %, 55 %, 85 % of duration) and read them.
   — verify: no two text mobjects share pixels; every balance sheet and table shows ruled
   cells with one value each. Record the four filenames checked in the beat's check JSON.

### C2 — Write BeatSixteen..BeatTwenty

7. [ ] Create `scenes_g4.py` with the **same import header as `scenes_g2.py:6-11`** plus
   `mpl_figure`. Import `numpy` explicitly — `from manim import *` does not reliably
   export `np`.
   — verify: `python -c "import ast,sys; ast.parse(open('scenes_g4.py').read())"` exits 0.
8. [ ] **BeatSixteen** (163.9 s, floor 19 steps). The dramatic shape is fixed by the data
   note and must be preserved in this order: pose the test → raw 159 cloud → flat fit,
   slope 0.061 / r 0.171, "appears refuted" → shape of the cloud, axis out to 4 000 % →
   the single dot named → Sierra Leone's own annual series, median 23 % → the two
   impossible years (2001, 2015) as highlighted cells → the redenomination reading →
   filtered cloud → slope 1.064 / r 0.746 → the two lessons → the qualification that the
   fit is tight at high inflation and loose at low. Figures via `mpl_figure`; slope,
   correlation and n computed in the draw callable and asserted against the note's values.
   — verify: `python -m manim render -ql --media_dir media scenes_g4.py BeatSixteen` exits
   0; `python tools/beatcheck.py BeatSixteen --module scenes_g4 --quality 480p15` passes;
   `ls figures/` contains the four scatter/series PNGs.
9. [ ] **BeatSeventeen** (111.8 s, floor 13 steps). One `mpl_figure` dual-axis series
   (IPCA blue, Selic yellow, from `data/bcb_sgs_13522.csv` and `data/bcb_sgs_432.csv`,
   parsed `dayfirst=True`), then Manim callouts: co-movement, the 2 %-26.5 % range, Fisher
   as the reading of it, the link back to the trip-cost model, and the stated omission of
   any Brazilian monetary aggregate with its reason.
   — verify: as step 8, for BeatSeventeen.
10. [ ] **BeatEighteen** (155.9 s, floor 18 steps). Pure Manim: `balance_sheet` for the
    base expansion (interest-bearing assets against non-interest liabilities), the
    government budget constraint built term by term with `eq`, the incidence argument, the
    tax framed as base × rate in a `table`, then an `axes_panel` hump — revenue against
    inflation — drawn as a curve with the peak marked, closing on the growth footnote.
    — verify: as step 8, for BeatEighteen.
11. [ ] **BeatNineteen** (154.4 s, floor 18 steps). Pure Manim: the four costs as four
    `table` rows revealed one at a time (shoe leather with its back-reference to the
    square root, menu costs, relative-price uncertainty, bank over-entry), plus the
    Friedman-rule remedy as its own frame.
    — verify: as step 8, for BeatNineteen.
12. [ ] **BeatTwenty** (153.7 s, floor 18 steps). Pure Manim: neutrality against
    superneutrality as two columns; the derived chain (money growth → inflation → nominal
    rate → real balances → real resources) built one link at a time so the contradiction
    resolves visually; then the flexible-price assumption named and removed, and the final
    frame carrying the identity, the one-half elasticity, and the explicit statement that
    the chapter has no mechanism for fixed prices.
    — verify: as step 8, for BeatTwenty.
13. [ ] Gate: `ls build/checks/*.json | wc -l` prints `20` and
    `python -c "import json,glob; print(all(json.load(open(f))['pass'] for f in glob.glob('build/checks/*.json')))"`
    prints `True`. Do not enter C3 otherwise.

### C3 — Merge into one module

14. [ ] Replace `scenes.py` with the concatenation: one shared docstring, the single import
    header (`scenes_g2.py:6-11` plus `mpl_figure`), then the 20 classes in beat order from
    g1, g2, g3, g4. No module-level helpers survive from the old file — `steps()`,
    `heading()`, `load_csv()`, `scatter_data()`, `ols()` (`scenes.py:30-66`) are all
    superseded by the kit.
    — verify: `python -c "import ast;m=ast.parse(open('scenes.py').read());c=[n.name for n in m.body if isinstance(n,ast.ClassDef)];print(len(c),c)"`
    prints 20 names matching `beats.json` ids in order; and
    `grep -c "def steps\|def heading\|def load_csv\|def scatter_data" scenes.py` prints `0`.
15. [ ] Delete the group files and the scratch modules now that they are merged:
    `git rm scenes_g1.py scenes_g2.py scenes_g3.py kittest.py mpltest.py` and `rm scenes_g4.py`
    (add `scenes_g4.py`'s content only via `scenes.py`).
    — verify: `git status --short` shows the deletions and the modified `scenes.py`;
    `python -c "import scenes"` still exits 0.
    Rollback: `git checkout HEAD -- Videos/aula-07-money-and-inflation/` restores all five.
16. [ ] Commit the source state before the long render, so C4 can be resumed from a clean
    tree: `git add -A Videos/aula-07-money-and-inflation tools/beatcheck.py && git commit`.
    — verify: `git status --short Videos/aula-07-money-and-inflation` is empty apart from
    ignored paths.

### C4 — Render at 1080p60

17. [ ] Render one beat interactively first to clear any MiKTeX package prompt:
    `python -m manim render -qh --media_dir media scenes.py BeatOne`
    — verify: `media/videos/scenes/1080p60/BeatOne.mp4` exists and
    `ffprobe ... -show_entries stream=width,height,r_frame_rate` reports `1920 1080 60/1`.
18. [ ] Render the remaining 19 beats sequentially, one command per beat, each followed by
    its check: `python -m manim render -qh --media_dir media scenes.py <Beat> && python tools/beatcheck.py <Beat> --quality 1080p60`
    — verify per beat: check JSON `"pass": true` with `shortfall` in `[0, 0.6]`.
    Resume rule: skip a beat whose `media/videos/scenes/1080p60/<Beat>.mp4` exists **and**
    whose 1080p60 check JSON passes; re-render otherwise.
19. [ ] Gate: `ls media/videos/scenes/1080p60/*.mp4 | wc -l` prints `20`, and the sum of
    probed durations is within 20 s below `2510.328` (per-beat quantisation only ever
    shortens, and the compiler pads).

### C5 — Compile, verify, clean up

20. [ ] `python ../../.claude/explainer_compile.py . --quality 1080p60`
    — verify: exit 0 (exit 3 = drift over tolerance), the printed drift is **0.0 ms**, and
    the report shows video and audio both at ~2 515.7 s.
    Rollback: restore `build/_backup_480p/aula-07-money-and-inflation.mp4` over the output.
21. [ ] Probe the deliverable:
    `ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 aula-07-money-and-inflation.mp4`
    — verify: 1920×1080, 60/1, duration 2515.6-2515.7 s.
22. [ ] Spot-check sync by ear/eye at three points — 00:04:00 (BeatThree), 00:28:00
    (around BeatFourteen/Fifteen) and 00:36:00 (BeatSixteen's reversal): extract a frame
    and confirm the visual matches the narration at that timestamp in `aula-07-money-and-inflation.srt`.
    — verify: the Sierra Leone reversal frame is on screen while the narration says the
    correlation goes to 0.75.
23. [ ] Update `provenance.md` with the new figure cache keys, the computed slope/correlation
    values, and the render quality; append a line to `.agent/notes/manim-video-pipeline.md`
    only if a *new* measured behaviour was observed.
    — verify: `git diff --stat` shows both files; no narration file (`script.md`,
    `beats.json`, `audio/`) appears in the diff.
24. [ ] Commit. Keep `build/_backup_480p/` on disk until step 22 has passed.

## Risks

- **Long `-qh` render dies midway (power, OOM, hang).** → C4 is per-beat with a per-beat
  artifact and an explicit skip rule; nothing before C4 is re-done.
- **MiKTeX package prompt hangs an unattended batch.** → steps 5 and 17 render one beat
  interactively first; if a later beat stalls >10 min with no frame progress, kill it and
  re-run that single beat in the foreground.
- **A rewritten beat's animations exceed its narration.** → `Beat.run()` raises at
  `.claude/manim_kit.py:97` before any frame is written, so this surfaces at `-ql` in C1/C2,
  not after the 1080p render.
- **`find_render_dir` picks the wrong module.** → C0 step 3 prunes to one module and every
  compile/check command passes `--quality 1080p60` explicitly.
- **Figure cache serves a stale PNG after the draw code changes.** → figure names are
  version-free but the cache is small; when a draw callable changes, delete
  `figures/<name>.png` (or pass `regenerate=True` once) and confirm the file mtime moved.
- **Silently "cleaning" the Sierra Leone outlier.** → step 8 fixes the on-screen order:
  the failed fit is shown *before* the filter, and the filter's effect is stated. The data
  note calls this out explicitly; treat a beat that skips the failure as failing review.
- **ffmpeg given a Git Bash POSIX path.** → run all ffmpeg/ffprobe from the project dir
  with relative paths; never hand it `$PWD`.
- **Heredoc mangles prose containing apostrophes.** → write any generated Python to a file
  with the Write tool and run it; do not pipe scene text through a shell heredoc.

## Rollback

- **Source:** `git checkout <hash from C0 step 2> -- Videos/aula-07-money-and-inflation/scenes.py`
  restores the old 949-line cut; `git checkout HEAD~1 -- Videos/aula-07-money-and-inflation/`
  restores `scenes_g1..g3.py`, `kittest.py`, `mpltest.py` after the C3 deletions.
- **Deliverable:** `cp build/_backup_480p/aula-07-money-and-inflation.mp4 build/_backup_480p/aula-07-money-and-inflation.srt .`
  restores the working 480p video. Untracked and gitignored — recoverable from nowhere else,
  which is why C0 step 1 precedes every other action.
- **Renders:** `cp -r build/_backup_480p/renders media/videos/scenes/480p15` restores the
  20 old per-beat mp4s, enough to re-compile the old cut with
  `python ../../.claude/explainer_compile.py . --quality 480p15`.
- **Not changed, so nothing to roll back:** `beats.json`, `audio/*.mp3`, `script.md`,
  `data/*.csv`. No re-synthesis is triggered by anything in this plan, so no spend is at risk.
- Irreversible on disk only: the C0 step 3 pruning of `media/videos/{kittest,mpltest,scenes_g3}`
  — draft 480p test renders, reproducible in under a minute from the committed sources.
