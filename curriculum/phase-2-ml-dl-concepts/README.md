# Phase 2 — ML & DL Concepts (Week 5)

**Goal (breadth-only):** enough machine-learning and deep-learning intuition to speak fluently, read a model card, and make good *applied* decisions — **not** to master ML. Deeper ML is picked up just-in-time later, as needed. One focused week.

> Why so short? This path targets an **applied AI/LLM engineer**. You need to know what a model does, how it's evaluated, and where it fits — not how to derive backpropagation.

---

## What to cover this week
- **ML core:** supervised vs unsupervised; training vs test data; features/labels; overfitting & why we split data.
- **Metrics (this is your edge — QA background):** accuracy, precision, recall, F1, confusion matrix (classification); RMSE/MAE (regression). *When is accuracy misleading?*
- **Hands-on `scikit-learn`:** load a small tabular/business dataset, train ONE model (classification or regression), evaluate it properly, interpret results.
- **DL intuition:** what a neuron/layer is; weights; gradient descent; backprop (concept only); what **embeddings** are and why they matter for LLMs.
- **Transformers & attention (conceptual):** the "why" behind modern LLMs; tokenization hands-on (tokenize some text, count tokens).

---

## Exit criteria
- [ ] Explain supervised vs unsupervised with an example each.
- [ ] Explain why we split train/test and what overfitting looks like.
- [ ] Pick the right metric for a given problem and justify it (e.g., why recall matters for fraud detection).
- [ ] Train + evaluate one sklearn model end to end and write up findings.
- [ ] Explain, in plain English, what an embedding is and what attention does.
- [ ] Tokenize text and explain why token count matters (cost/context limits).

## Resources
See [RESOURCES.md → Phase 2](../../RESOURCES.md#phase-2--ml--dl-concepts-breadth-only). Primary: **StatQuest** (intuition), **3Blue1Brown** neural-net + GPT videos, **scikit-learn docs**, **Andrew Ng ML Specialization** (audit, watch selectively).

## Project this phase
- `projects/small/` — train + evaluate one sklearn model on a business dataset; short write-up of the metric choice and results.
