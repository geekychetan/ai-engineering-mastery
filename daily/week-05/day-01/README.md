# Week 05 · Day 01 — The ML landscape (what ML actually is)

**Estimated time:** ~5 hrs (1–1.5 hr CS50P + 3.5–4 hr learn/notes)
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Explain supervised vs unsupervised learning with a concrete example of each.
- [ ] Define features, labels, and the train/test split — and why we split.
- [ ] Describe overfitting in plain English and how you'd spot it.

## Learn (with resources)
- **CS50P** — continue this week's problem set (runs in parallel).
- **StatQuest with Josh Starmer** (YouTube) — "Machine Learning Fundamentals: Bias and Variance", "The Main Ideas of Fitting a Line to Data", and the intro "A Gentle Introduction to Machine Learning".
- **Andrew Ng / DeepLearning.AI — Machine Learning Specialization** (Coursera, audit free) — Week 1 intro videos only, for the supervised/unsupervised framing. *Watch for intuition, don't grind.*
- **scikit-learn docs** — skim the "Getting Started" page: https://scikit-learn.org

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-ml-landscape`.
2. [ ] Create `projects/small/ml-notes/ml_landscape.md`. In it, write in your own words (short paragraphs, not copied):
   - Supervised vs unsupervised, with one real example each (tie one to your QA/business background, e.g. "predict which support tickets are urgent").
   - What features and labels are, using a tiny table example (3–4 rows).
   - Why we hold out a test set, and what overfitting looks like on train vs test scores.
3. [ ] Add a `projects/small/ml-notes/glossary.md` with 8–10 terms you met today (feature, label, model, training, generalization, overfitting, etc.), one line each.
4. [ ] Install the tools you'll use this week into your venv and pin them:
   ```bash
   pip install scikit-learn pandas matplotlib
   pip freeze | grep -Ei "scikit-learn|pandas|matplotlib" >> requirements.txt
   ```
5. [ ] Push, PR with `Closes #<issue>`, self-review the diff, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
