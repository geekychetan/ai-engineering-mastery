# Week 02 · Day 05 — Scope, modules, packages & the standard library

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Explain local vs global scope and why `import` brings names into your namespace.
- [ ] Split code into your own module and import from it (`from mymodule import fn`).
- [ ] Use useful standard-library modules: `datetime`, `random`, `math`, `collections`.

## Learn (with resources)
- **CS50P** — Week 4 (Libraries) — importing modules and using the standard library.
- **Corey Schafer** — "Python Tutorial: Modules and Packages" video (YouTube).
- **Python docs** — The Python Standard Library (skim `datetime`, `random`, `math`, `collections`): https://docs.python.org/3/library/

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-modules-stdlib`.
2. [ ] `projects/small/stdlib/helpers.py`: a module with two functions (e.g. `slugify(text)` and `clamp(n, lo, hi)`), each with a docstring, and a `main.py` that imports and uses them via `from helpers import slugify, clamp`.
3. [ ] `projects/small/stdlib/dates.py`: use `datetime` to print today's date formatted, compute the number of days until a chosen future date, and print the weekday name.
4. [ ] `projects/small/stdlib/rolls.py`: use `random` to simulate rolling two dice 1,000 times, then use `collections.Counter` to report how often each total (2–12) appeared.
5. [ ] `projects/small/stdlib/math_demo.py`: use `math` for a few computations (e.g. `sqrt`, `factorial`, `ceil`/`floor`) and print the results with f-strings.
6. [ ] CS50P Week 4 problem set: complete at least one library-based exercise (e.g. `Emojize` or `Little Professor`).
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
