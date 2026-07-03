# Week 02 · Day 04 — Functions deeper

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Use default arguments, keyword arguments, and variable-length args (`*args`, `**kwargs`).
- [ ] Write and read `lambda` functions and use `map()` / `filter()`.
- [ ] Explain when a named function beats a lambda/comprehension for readability.

## Learn (with resources)
- **CS50P** — Week 3 (Exceptions) lecture, plus review of Week 0's Functions material for argument handling.
- **Corey Schafer** — "Python Tutorial: *args and **kwargs" video (YouTube).
- **Real Python** — "Python's map() / filter()" and lambda articles: https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-functions`.
2. [ ] `projects/small/functions/greet.py`: `greet(name, greeting="Hello", *, punctuation="!")` demonstrating a default arg and a keyword-only arg. Call it several ways.
3. [ ] `projects/small/functions/summarize.py`: `summarize(*numbers, **options)` that returns count/sum/mean, where `**options` can toggle rounding (e.g. `round_to=2`). Document behavior in the docstring.
4. [ ] `projects/small/functions/functional.py`: given a list of numbers, use `map()` to square them and `filter()` to keep evens, with `lambda`. Then rewrite the same logic as list comprehensions and add a comment on which you find clearer.
5. [ ] CS50P Week 3 problem set: complete at least one exercise (e.g. `Fuel Gauge` or `Grocery List`).
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
