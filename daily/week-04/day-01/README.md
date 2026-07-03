# Week 04 · Day 01 — Type hints, docstrings & code style

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Add type hints to function signatures (including `list`, `dict`, `Optional`) and understand they're not enforced at runtime.
- [ ] Write clear docstrings (a consistent style, e.g. Google or NumPy) for functions and classes.
- [ ] Run `black`, `ruff`, and `mypy` (light) and clean up what they flag.

## Learn (with resources)
- **CS50P** — no new lecture; this builds on all prior weeks' functions/OOP work.
- **Real Python** — "Python Type Checking (Guide)" and "Documenting Python Code": https://realpython.com
- Tool docs: `black` (https://black.readthedocs.io), `ruff` (https://docs.astral.sh/ruff), `mypy` (https://mypy.readthedocs.io).

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-type-hints-style`.
2. [ ] `pip install black ruff mypy` and add them to `requirements.txt` (or a `requirements-dev.txt`).
3. [ ] `projects/small/typed/geometry.py`: rewrite a few earlier functions (e.g. area/perimeter helpers) with full type hints and docstrings. Include one function returning `Optional[float]`.
4. [ ] Run `black .`, then `ruff check .`, then `mypy projects/small/typed/geometry.py`. Fix every issue and note in the PR what each tool caught.
5. [ ] Add a short `projects/small/typed/README.md` recording the exact commands you ran and their output.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
