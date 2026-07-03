# Week 05 · Day 03 — Metrics deep dive (your QA edge)

**Estimated time:** ~5 hrs (1–1.5 hr CS50P + 3.5–4 hr build)
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Compute accuracy, precision, recall, F1, and a confusion matrix on your classifier.
- [ ] Explain when accuracy is misleading (class imbalance) with a concrete scenario.
- [ ] Pick the right metric for a given problem and justify it (recall vs precision tradeoff).

## Learn (with resources)
- **CS50P** — continue this week's problem set.
- **StatQuest** (YouTube) — "Confusion Matrix, Clearly Explained", "Precision and Recall", and "ROC and AUC, Clearly Explained".
- **scikit-learn docs** — `classification_report`, `confusion_matrix`, and the "Metrics and scoring" user guide: https://scikit-learn.org
- This is your **QA/testing strength**: metrics are just structured ways of asking "how wrong is it, and wrong in which direction?"

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-metrics`.
2. [ ] Create `projects/small/first-classifier/evaluate.py` that reuses yesterday's model and:
   - Prints `confusion_matrix(y_test, y_pred)` and labels which cell is TP/FP/TN/FN.
   - Prints `classification_report(y_test, y_pred)` (precision/recall/F1 per class).
3. [ ] Create `projects/small/ml-notes/when_accuracy_lies.md`: describe a realistic imbalanced scenario (e.g. "99% of transactions are legit") and show why 99% accuracy could still be a useless model. State which metric you'd optimize instead and why.
4. [ ] Add a small "metric chooser" cheat sheet to that file: for 3 problems (fraud detection, spam filter, medical screening) name the metric to prioritize and one sentence why.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
