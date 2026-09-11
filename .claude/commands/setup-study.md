---
description: Scaffold a new study project with directory structure, CLAUDE.md, rules files, quiz template, README, and local copies of all commands.
argument-hint: <course-name>
allowed-tools: Read Grep Glob Bash PowerShell Write Edit AskUserQuestion
---

Create a new study project for the course `$ARGUMENTS`.

## Instructions

### Step 0: Auto-discover project structure

**CRITICAL — Do NOT assume fixed directory names.** Before anything else, scan the project root (or target directory) and identify what already exists:

1. List all directories and files in the project root.
2. Identify each directory's **purpose** by its name pattern AND contents — not by matching an exact name:
   - **Lectures**: slide PDFs, .html presentations, .R/.py scripts from class (e.g., `Aula`, `Aulas`, `Lectures`, `Slides`)
   - **Exercise lists**: problem sets, homework PDFs (e.g., `Listas`, `Lista`, `Exercises`, `Lists`)
   - **Books/Textbooks**: textbook PDFs, solution manuals (e.g., `Livros`, `Books`, `Textos`, `Bibliografia`)
   - **Tutorials/Office hours**: supplementary review materials (e.g., `Monitoria`, `Tutoria`, `Tutorial`)
   - **Exams/Tests**: exam papers and solutions (e.g., `Prova`, `Provas`, `Exams`, `Tests`)
   - **Quizzes**: quiz MD files for quiz.html (e.g., `Simulados`, `Quizzes`, `Quiz`)
   - **Rules**: topic rule files (e.g., `rules`, `regras`)
   - **Maps**: cross-reference files (e.g., `Map`, `Maps`)
   - **Solutions**: generated exercise solutions (e.g., `Resolucao`, `Resolução`, `Solutions`)
   - **NotebookLM prompts**: prompt files (e.g., `NotebookLM`)
3. **Preserve existing names** — if the user already has `Aula/` (singular), do NOT create `Aulas/` (plural). Adapt to their convention.
4. Store the discovered mapping (purpose → actual directory name) and use it throughout all subsequent steps.
5. Only create directories that don't already exist, using the user's naming convention (language, singular/plural).

### Step 1: Gather information

Ask the user for:
- **Course name** (full name and abbreviation)
- **Professor** name
- **Institution / program** (e.g., "Insper — Mestrado Profissional em Economia")
- **Bibliography**: main textbook + complementary references (title, author, edition) — or say "look at the files" to auto-detect from existing book PDFs and lecture slides
- **Topics list**: each topic with its corresponding lecture number and textbook chapters — or say "look at the files" to auto-extract from lecture filenames/contents and match to book TOCs
- **Language**: for content output (default: Portuguese Brazil)
- **Code language**: R, Python, or both (default: R)

**If the user says "look at the files" for bibliography or topics:**
1. Read the first few pages of each lecture PDF to extract topic titles, chapter references, and bibliography slides
2. Read the TOC pages of each textbook PDF in the books directory
3. Cross-reference lecture topics with book chapters to build the mapping automatically
4. Present the extracted mapping to the user for confirmation before proceeding

### Step 2: Create directory structure

Create only the directories that don't already exist. Use the discovered naming convention. The required purposes (with example names) are:

```
<course-name>/
├── CLAUDE.md
├── README.md
├── .claude/
│   ├── settings.json
│   └── commands/          ← copies of all global commands
├── <lectures-dir>/        ← existing or new (e.g., Aula, Aulas)
├── <lists-dir>/           ← existing or new (e.g., Listas, Lista)
├── <tutorials-dir>/       ← existing or new (e.g., Monitoria)
├── <quizzes-dir>/         ← existing or new (e.g., Simulados)
├── <books-dir>/           ← existing or new (e.g., Livros)
├── rules/
├── <solutions-dir>/       ← existing or new (e.g., Resolucao)
├── Map/
├── NotebookLM/
│   ├── slides/
│   └── audio/
└── quiz.html
```

### Step 3: Generate CLAUDE.md

Follow the Econometria project pattern:
- Course scope (which topics, which lectures)
- "NAO extrapolar" restriction
- Topic × textbook reference table (Aula | Tópico | Livro principal | Outros)
- Lists covered
- Bibliography section with usage guidelines
- Language and format restrictions
- Rules index table linking to each `rules/*.md` file

### Step 4: Generate rules/ files

One file per topic (e.g., `rules/01_topicname.md`), each with:
```markdown
# Topico N - Topic Title

> **Aula N** - Topic subtitle
> **Main Book** - Chapter X, Sections Y-Z
> **Other refs** - ...

---

## Key Concept 1
[placeholder for formulas, definitions]

## Key Concept 2
[placeholder]

## Code Patterns
[placeholder for R/Python code templates]
```

### Step 5: Copy global commands and shared templates

1. Copy all `.md` files from `C:\Users\pedro\.claude\commands\` into the project's `.claude\commands\` directory (local copies the user can customize). This includes `exam-gen.md` and `exam-grade.md`.
2. Set up the **exam/list tooling** (used by `/exam-gen` and `/exam-grade`):
   - Copy `~/.claude/commands/templates/lista-exam.tex` into the project (e.g., `<lists-dir>/lista-exam.tex`) — the LaTeX template for lists/simulados (single source, `\ifsolucoes` toggle for blank list vs. gabarito+rubrica; preamble already follows the global lmodern+cmap copyable-PDF rule).
   - Copy `~/.claude/commands/templates/estilo-avaliacao.md` into `rules/00_estilo_avaliacao.md` — the exam-style rules (taxonomy, contextualization, solution/rubric format, bibliography usage). Adapt the institution/bibliography names to this course.

### Step 6: Generate quiz.html

Copy the canonical quiz player from `~/.claude/commands/templates/quiz.html` into the project root as `quiz.html` (verbatim — it has the perfect standalone-export feature). See `/quiz-gen` for the MD format the player consumes.

Also copy the quiz validator `~/.claude/commands/templates/quiz-validate.py` into the project's `.claude/` directory — `/quiz-gen` runs it to gate every generated quiz (parse integrity + anti-cheat length/style checks). Do not hand-write one-off checks; this script is the single source of truth.

### Step 7: Generate README.md

Include:
- Project structure explanation (what each directory is for)
- Available slash commands with usage examples (use the actual directory names from the project):
  - `/convert <lectures-dir>/` — convert lecture PDFs to markdown
  - `/summarize <lectures-dir>/` — summarize all lectures
  - `/list-exercises <lists-dir>/` — extract all exercises
  - `/solution <lists-dir>/list-file.md` — solve exercises from a list
  - `/exam-gen <topics>` — generate an exam-style exercise list + solution key & rubric (LaTeX, simulado style); asks depth / tangential topics / math complexity first
  - `/exam-grade <lists-dir>/lista-X.tex <my-resolution>` — grade and analyze your own resolution against the rubric, with book references
  - `/exercise-plan <topics>` — curated practice plan referencing real exercises in the source books (number + page), weighted by subtopic and distributed across knowledge levels
  - `/quiz-gen <quizzes-dir>/` — generate quiz from MD question files
  - `/quiz-analyze <paste results>` — analyze quiz performance
  - `/study-map .` — generate Obsidian cross-reference maps
  - `/notebooklm <lectures-dir>/` — generate NotebookLM prompts (slides + audio) for all lectures
  - `/speechify <topic-or-file>` — narrated plain-text script for Speechify or any TTS app (math spoken in words, no tables, no code); `--split` for one file per part, `--short` for a revision-only pass
- How to run quizzes:
  1. `cd <project-dir>`
  2. `python -m http.server`
  3. Open `http://localhost:8000/quiz.html` in browser
  4. Select the quiz MD file to load
- How to navigate the project in Obsidian (open the root as a vault)
- NotebookLM workflow (use actual directory names):
  1. Upload all course materials (lectures, books, lists, quizzes) to NotebookLM
  2. Run `/notebooklm <lectures-dir>/` to generate prompts
  3. Open each prompt file → Ctrl+A → Ctrl+C → paste into NotebookLM

### Step 8: Auto-convert all materials

Scan the entire project for convertible files (HTML, PDF, PPTX, DOCX, EPUB, TXT, etc.) in **all discovered directories** and root.

**For the books directory:** Ask the user before converting:
> "Found N book PDFs in <books-dir>/. Converting large textbooks can take several minutes and produce very large MD files. Convert books now?"
>
> Options: **Yes, convert all books** / **No, skip books for now** / **Let me pick which books**

Run `/convert` on the selected files. This is the entry point for the rest of the ecosystem:
- Converted lectures feed `/summarize` and `/quiz-gen`
- Converted books feed `/study-map` cross-references (more precise chapter-level linking)
- Converted exercise lists feed `/list-exercises` and `/solution`
- Any converted reading feeds `/speechify` when the user wants to study by listening

If existing `.md` files are found, ask the user once (overwrite all / skip all / let me pick).

### Step 9: Generate initial study map

**Before generating:** Check if books in the books directory have been converted to MD. If not, warn:
> "Books are not yet converted to MD. The study map will use chapter references from CLAUDE.md and rules/ only. For precise chapter-level cross-references, run `/convert <books-dir>/` first."

After conversion (or warning), run `/study-map .` to create the `Map/` cross-reference files linking books to lectures to exercises.

### Step 9.5: Copy original sources for NotebookLM upload

Create a `NotebookLM/sources/` directory and copy **all original source files** into it as a flat collection ready for bulk upload to NotebookLM. This saves the user from hunting across subdirectories.

**What to copy:**
1. All files from `<lectures-dir>/` (slides, scripts, articles)
2. All files from `<lists-dir>/` (including subdirectories)
3. All files from `<books-dir>/`
4. All files from `<tutorials-dir>/`
5. All files from `<exams-dir>/`

**NotebookLM supported formats:**
pdf, txt, md, docx, csv, pptx, epub, 3g2, 3gp, aac, aif, aifc, aiff, amr, au, avi, cda, m4a, mid, mp3, mp4, mpeg, ogg, opus, ra, ram, snd, wav, wma, avif, bmp, gif, ico, jp2, png, webp, tif, tiff, heic, heif, jpeg, jpg, jpe

**Conversion rule:** For each file, check its extension against the supported list above.
- **If supported** → copy as-is to `NotebookLM/sources/` with the category prefix.
- **If NOT supported** → convert to `.txt` (cheapest for AI) before copying:
  - **Code files** (.R, .py, .jl, .m, .do, .sas, .sql, .js, .ts, etc.) → copy as `.txt` (just change the extension — the content is already plain text)
  - **HTML files** (.html, .htm) → convert to `.md` via `markitdown`, then copy the `.md`
  - **Other text-based files** (.json, .xml, .yaml, .yml, .toml, .ini, .cfg, .log, .tex, .bib, .sty) → copy as `.txt`
  - **Binary files with no supported equivalent** → skip and warn the user

**Naming convention:** Prefix each copied file with its source category:
- `Aula_<filename>.ext` (or `.txt` / `.md` if converted)
- `Lista_<filename>.ext`
- `Livro_<filename>.ext`
- `Monitoria_<filename>.ext`
- `Prova_<filename>.ext`

**After copying:** List all filenames in `NotebookLM/sources/` so the `/notebooklm` command can reference them by exact name when generating prompts.

### Step 10: Show summary

Print what was created and list available commands with examples. Include:
- Directory structure created
- Number of rules files generated
- Number of files converted
- Number of cross-references in Map/
- Reminder about `/notebooklm` for generating study prompts
