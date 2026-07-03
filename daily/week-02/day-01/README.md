# Week 02 · Day 01 — Strings deep dive

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Use core string methods confidently (`.strip()`, `.split()`, `.join()`, `.replace()`, `.find()`, `.startswith()`, case methods).
- [ ] Slice strings (including negative indices and step) and reason about immutability.
- [ ] Format output cleanly with f-strings (padding, alignment, number/precision specifiers).

## Learn (with resources)
- **CS50P** — Week 1 (Conditionals) recap + Week 2 (Loops), focusing on string handling in the problem sets.
- **Corey Schafer** — "Python Tutorial: Strings" video (YouTube).
- **Real Python** — "Python String Formatting Best Practices": https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-strings`.
2. [ ] `projects/small/strings/string_toolkit.py`: write functions `normalize(text)` (strip + collapse inner whitespace + lowercase), `title_case(text)`, and `reverse_words(text)`. Each with a docstring.
3. [ ] `projects/small/strings/slicing_demo.py`: given a string, print the first 3 chars, last 3 chars, every other char (step slice), and the reversed string using `[::-1]`.
4. [ ] `projects/small/strings/receipt.py`: use f-strings to print a small aligned "receipt" — item names left-aligned in a 20-char column, prices right-aligned to 2 decimals (e.g. `{price:>8.2f}`).
5. [ ] CS50P Week 1–2 problem set: complete at least one string-heavy exercise (e.g. `deep`, `playback`, or `vanity plates`).
6. [ ] Push, PR with `Closes #<issue>`, self-review the diff, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
