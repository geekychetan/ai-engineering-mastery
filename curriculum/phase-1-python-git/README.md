# Phase 1 — Python + Git Foundations (Weeks 1-4)

**Goal:** real Python fluency (not just syntax) with git/GitHub used *daily* from day one, so git confidence is rebuilt by doing. By the end you can write clean, tested Python, consume APIs, and ship every change through a branch → PR → review → merge loop.

Runs in parallel with **CS50P** (Weeks 0–4), 1–1.5 hr/day.

---

## Week 1 — Environment + the daily git loop
- Terminal/shell basics; VS Code; install Python via `pyenv`; virtual environments (`venv`); `pip`.
- Project structure, `README.md`, Markdown.
- **Git used immediately:** every exercise is a branch → commit → PR → merge. Practice `.gitignore`, and deliberately create + resolve a merge conflict.
- Write and run your first small scripts.

## Week 2 — Python core
- Data types, strings, f-strings; lists/tuples/sets/dicts; comprehensions.
- Control flow, functions, arguments/return values, scope.
- Modules & packages; the standard library; `import`.
- Reading errors/tracebacks and debugging.

## Week 3 — Python for real programs
- OOP basics: classes, methods, `__init__`, dunder methods (light).
- Error handling (`try/except`, raising, custom exceptions).
- File I/O and **JSON**; working with the filesystem (`pathlib`).
- **REST APIs** with `requests`; parsing JSON; environment variables & secrets (`.env`, never commit secrets).
- **`pytest`** — write your first tests (your QA background makes this a strength).
- **Small project:** a tested `typer` CLI tool.

## Week 4 — Toward data & AI tooling
- Type hints and why they matter; `mypy` (light).
- `asyncio` basics (needed for LLM apps).
- CLI apps with `typer`; packaging a small tool.
- `numpy` + `pandas` basics (arrays, DataFrames, load/filter/aggregate).
- **Small project:** a script that calls a public REST API, processes the data with pandas, and has `pytest` tests. Shipped via PR.

---

## Exit criteria (you can do all of these)
- [ ] Create a venv, install packages, and run a script from the terminal.
- [ ] Explain lists vs dicts vs sets and when to use each.
- [ ] Write a function with type hints and a docstring, and test it with `pytest`.
- [ ] Read a traceback and fix the bug it points to.
- [ ] Call a REST API, handle errors, and parse the JSON response.
- [ ] Do the full git loop unaided: branch → commit → push → PR → review → merge.
- [ ] Keep secrets out of git using `.env` + `.gitignore`.

## Resources
See [RESOURCES.md → Phase 1](../../RESOURCES.md#phase-1--python--git-foundations). Primary: **CS50P**, **Corey Schafer** (Python), **Pro Git** + **Atlassian** (git), **pytest docs**.

## Projects this phase
- `projects/small/` — tested `typer` CLI tool (Week 3).
- `projects/small/` — API + pandas script with tests (Week 4).
