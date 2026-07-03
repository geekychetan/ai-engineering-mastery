# Week 04 · Day 04 — numpy basics

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Create numpy arrays and explain how they differ from Python lists (dtype, fixed size, vectorization).
- [ ] Do vectorized arithmetic and use aggregations (`sum`, `mean`, `std`, `min`/`max`, `axis=`).
- [ ] Index and slice arrays, including boolean masking.

## Learn (with resources)
- **CS50P** — no new lecture; this is toward data/AI tooling.
- **numpy docs** — "NumPy: the absolute basics for beginners": https://numpy.org/doc/stable/user/absolute_beginners.html
- **Real Python** — "NumPy Tutorial: Your First Steps": https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-numpy`.
2. [ ] `pip install numpy` and add it to `requirements.txt`.
3. [ ] `projects/small/numpy_intro/vectors.py`: create two arrays, add/multiply them element-wise, and compare timing of a vectorized square vs a Python-loop square over a large array (`time.perf_counter()`).
4. [ ] `projects/small/numpy_intro/stats.py`: build a 2D array (e.g. rows = students, cols = test scores) and compute per-student and per-test means with `axis=`, plus overall `mean`/`std`/`max`.
5. [ ] `projects/small/numpy_intro/masking.py`: use a boolean mask to select all values above a threshold and to replace negatives with 0.
6. [ ] Add a one-line comment connecting arrays/vectors to embeddings you'll meet later in the LLM phase.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
