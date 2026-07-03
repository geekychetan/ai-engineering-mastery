# Week 05 · Day 04 — Regression, over/underfitting & cross-validation

**Estimated time:** ~5 hrs (1–1.5 hr CS50P + 3.5–4 hr build)
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Train a regression model and evaluate it with RMSE/MAE and R².
- [ ] Explain overfitting vs underfitting and how the train/test gap reveals each.
- [ ] Describe what k-fold cross-validation does and why it beats a single split.

## Learn (with resources)
- **CS50P** — continue this week's problem set.
- **StatQuest** (YouTube) — "Linear Regression, Clearly Explained", "R-squared, Clearly Explained", and "Cross Validation, Clearly Explained".
- **scikit-learn docs** — `LinearRegression`, the regression metrics (`mean_squared_error`, `mean_absolute_error`, `r2_score`), and `cross_val_score`: https://scikit-learn.org

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-regression`.
2. [ ] Create `projects/small/first-regressor/train.py` using a regression dataset (e.g. `sklearn.datasets.load_diabetes` or the California housing set):
   - Split, fit a `LinearRegression`, predict on test.
   - Print RMSE, MAE, and R² on the test set.
3. [ ] Add a `cross_val_score(model, X, y, cv=5)` run and print the 5 fold scores plus their mean/std. Add a comment explaining why the spread matters.
4. [ ] Create `projects/small/ml-notes/overfitting.md`: in your own words explain overfitting vs underfitting, give the "symptom" for each (train vs test scores), and name one fix for each.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
