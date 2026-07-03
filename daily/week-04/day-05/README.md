# Week 04 · Day 05 — pandas basics

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Load data into a `DataFrame` (from CSV) and inspect it (`head`, `info`, `describe`, `dtypes`).
- [ ] Select and filter rows/columns (label vs boolean indexing).
- [ ] Aggregate with `groupby` and compute basic stats.

## Learn (with resources)
- **CS50P** — no new lecture; this is toward data/AI tooling.
- **pandas docs** — "10 minutes to pandas": https://pandas.pydata.org/docs/user_guide/10min.html
- **Real Python** — "The pandas DataFrame: Make Working With Data Delightful": https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-pandas`.
2. [ ] `pip install pandas` and add it to `requirements.txt`.
3. [ ] Put a small CSV in `projects/small/pandas_intro/data.csv` (make one up, e.g. sales: `date,region,product,units,price`).
4. [ ] `projects/small/pandas_intro/explore.py`: read the CSV, print `head()`, `info()`, and `describe()`, and print the column dtypes.
5. [ ] `projects/small/pandas_intro/analyze.py`: filter rows (e.g. one region, or `units > N`), add a computed `revenue = units * price` column, and use `groupby("region")` to show total revenue per region sorted descending.
6. [ ] Run `black`/`ruff`; fix issues. Add a `projects/small/pandas_intro/README.md` with what the scripts show.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
