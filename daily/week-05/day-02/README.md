# Week 05 · Day 02 — Classification hands-on with scikit-learn

**Estimated time:** ~5 hrs (1–1.5 hr CS50P + 3.5–4 hr build)
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Load a small tabular dataset and inspect features/labels with pandas.
- [ ] Train a classifier and make predictions using the sklearn fit/predict pattern.
- [ ] Explain each step of the pipeline (split → fit → predict) in a comment or docstring.

## Learn (with resources)
- **CS50P** — continue this week's problem set.
- **StatQuest** (YouTube) — "Decision Trees" (clearest first classifier) and "Naive Bayes, Clearly Explained" (pick one to match the model you train).
- **scikit-learn docs** — "An introduction to machine learning with scikit-learn" tutorial and the `train_test_split` reference: https://scikit-learn.org

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-classification`.
2. [ ] Create `projects/small/first-classifier/train.py`. Using a built-in dataset (e.g. `sklearn.datasets.load_iris` or `load_breast_cancer`):
   - Load the data into a pandas DataFrame and print its shape + `head()`.
   - Split into train/test with `train_test_split(..., test_size=0.2, random_state=42)`.
   - Train one classifier (`DecisionTreeClassifier` or `LogisticRegression`) with `.fit()`.
   - Predict on the test set with `.predict()` and print the first 10 predictions vs actual labels.
3. [ ] Print the plain `.score()` accuracy on the test set (you'll critique this number tomorrow).
4. [ ] Add a top-of-file docstring explaining what the script does and what "features" and "labels" are in this dataset.
5. [ ] Save a `projects/small/first-classifier/README.md` noting which dataset + model you used and the accuracy you got.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
