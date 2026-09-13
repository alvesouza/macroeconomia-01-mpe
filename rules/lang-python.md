---
id: lang-python
title: Python
tier: 2
applyTo: "**/*.{py,pyi}, **/pyproject.toml, **/requirements*.txt"
skills: [langpack]
owner: repo-owner
---

## Non-negotiable

1. `pyproject.toml` with pinned direct dependencies and a lockfile (`uv.lock`,
   `poetry.lock`, or `requirements.txt` compiled by `uv pip compile`). Never an
   unpinned `pip install` in a Dockerfile.

2. Type hints on every public function and every module boundary. `mypy --strict` or
   `pyright` in CI on `src/`.
   *Why:* Python's failure mode is a `TypeError` in production on a rarely-taken branch;
   static checking is the only thing that finds those before users do.

3. `ruff check` and `ruff format` in CI. One formatter, no debate, no formatting in diffs.

4. No mutable default arguments (`def f(x=[])`). Use `None` and construct inside.
   *Check:* ruff `B006`.

5. No bare `except:` and no `except Exception: pass`. Catch the specific exception, or
   re-raise with context (`raise X from e`).

6. Every file operation, socket, and DB connection acquired via a context manager.

## Prefer

7. `pathlib.Path` over `os.path`; `dataclasses`/`pydantic` over dicts for structured
   data; `enum` over string constants.

8. Pydantic v2 (or `attrs` + `cattrs`) for anything crossing a boundary — API payloads,
   config, message envelopes. Validate at the edge, then trust the type inside.

9. `structlog` or stdlib logging with `extra={}`, always structured. Never f-strings in
   log calls — they format eagerly, even at a disabled level.

10. `asyncio` for I/O-bound concurrency; `multiprocessing`/`joblib` for CPU-bound.
    Threads only for blocking C extensions that release the GIL.

11. Vectorize before you parallelize: NumPy/Polars operations over Python loops, and
    Polars or DuckDB over pandas for anything large.
    *Why:* a vectorized NumPy expression is typically 10–100× a Python loop, with no new
    failure modes; parallelism adds failure modes and is often slower than vectorizing.

12. `numpy.random.default_rng(seed)` — never the legacy global `np.random.*`, which is
    process-global mutable state and makes reproducibility a lie.

13. `functools.cache` / `lru_cache` for pure functions only. Caching an impure function
    is a correctness bug that presents as a heisenbug.

14. `uv` for environment and dependency management. It is materially faster and the
    lockfile is honest.

## Avoid

15. `from module import *`, and wildcard re-exports in `__init__.py`.

16. `pickle` for anything crossing a trust or version boundary. It executes arbitrary
    code on load and is not a serialization format.

17. `pandas.DataFrame.append` / `iterrows` / `applymap` in loops, and chained assignment
    (`df[a][b] = x`) — silently a no-op or a copy warning depending on version.

18. Module-level side effects: I/O, network calls, or expensive computation at import
    time. It makes imports slow, order-dependent, and untestable.

19. `time.time()` for measuring elapsed time. `time.monotonic()` / `perf_counter()`.

20. Catching `Exception` around an entire request handler and returning 200.

21. `sys.path` manipulation. Use a real package layout (`src/` + editable install).
