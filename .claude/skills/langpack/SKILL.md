---
name: langpack
description: Language-specific conventions and toolchain setup for C, C++, C#/.NET, Python, Rust, JavaScript/TypeScript, React, Angular, and Flutter/Dart. Use when writing or reviewing code in any of these, when setting up a new project or its lint/CI configuration, or when asked "what's idiomatic here".
---

# Language pack

Load **only** the pack for the language you are touching. Loading all of them defeats
the purpose.

| Language | Pack | Also read |
|---|---|---|
| C, C++ | `rules/lang-c-cpp.md` | `rules/memory-safety.md` |
| C#, .NET | `rules/lang-csharp.md` | `rules/memory-safety.md` if P/Invoke |
| Python | `rules/lang-python.md` | `rules/quant-research.md` if numerical |
| Rust | `rules/lang-rust.md` | `rules/memory-safety.md` if `unsafe` |
| JavaScript, TypeScript | `rules/lang-js-ts.md` | |
| React | `rules/lang-react.md` | `rules/lang-js-ts.md` first |
| Angular | `rules/lang-angular.md` | `rules/lang-js-ts.md` first |
| Flutter, Dart | `rules/lang-flutter.md` | `rules/memory-safety.md` if `dart:ffi` |

## Toolchain baseline

Every language gets the same three things, and a project without them is not
"lightweight", it is unverified.

1. **A formatter, enforced in CI.** Formatting never appears in a diff.
2. **A linter at error level, enforced in CI.** Warnings that do not fail are warnings
   nobody reads.
3. **A type check where the language has one.**

| Language | Format | Lint | Types |
|---|---|---|---|
| C / C++ | `clang-format` | `clang-tidy` (`bugprone-*`, `cppcoreguidelines-*`) | `-Wall -Wextra -Wpedantic -Werror` |
| C# | `dotnet format` | NetAnalyzers, Meziantou, AsyncFixer | `<Nullable>enable</Nullable>`, warnings as errors |
| Python | `ruff format` | `ruff check` | `mypy --strict` or `pyright` |
| Rust | `cargo fmt` | `cargo clippy -- -D warnings` | (compiler) |
| TS / JS | Prettier / Biome | ESLint + `@typescript-eslint` | `"strict": true` |
| Dart | `dart format` | `very_good_analysis` | (sound null safety) |

## Cross-language invariants

These hold everywhere and are the ones most often violated in polyglot repos:

- **Validate at the boundary, trust inside.** Parse untrusted input into a typed value
  once, at the edge. Do not re-check the same thing at every layer, and do not skip the
  edge check because "the caller validates".
- **Errors carry cause.** Preserve the chain (`raise ... from e`, `throw new Error(msg,
  {cause})`, `?` with `thiserror`, bare `throw;`). A rethrow that resets the stack trace
  destroys the only evidence of the failure.
- **No wall-clock in business logic.** Inject a clock. Tests that depend on the system
  clock fail at midnight, in another time zone, and on someone else's machine.
- **Structured logging.** Message template plus fields, never string interpolation —
  interpolation formats eagerly even at a disabled level, and destroys queryability.
- **Cancellation is a parameter.** `CancellationToken`, `AbortSignal`, `context.Context`,
  `asyncio` task cancellation — accepted *and* propagated, not accepted and dropped.
- **Config parsed once at startup** into a typed object, with validation. Not
  `os.environ[...]` scattered through the codebase.

## New project checklist

- [ ] Formatter + linter + type checker wired into CI on day one
- [ ] Dependency lockfile committed; CI installs frozen
- [ ] `.gitignore` and `.graphifyignore` cover build output and generated code
- [ ] Test framework with one real test that exercises the wiring
- [ ] `Dockerfile` per `rules/containers-docker.md` if it ships as a container
- [ ] `applyTo` glob in the language pack actually matches this project's layout
