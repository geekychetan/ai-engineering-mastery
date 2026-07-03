# Week 10 · Day 06 — Run a small open model / Ollama on EC2 · tear down · weekly review

**Estimated time:** ~4 hrs (lighter day)

**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Run a small open model (via **Ollama** or a small Hugging Face model) on an EC2 instance and query it.
- [ ] Feel the cost/latency reality of self-hosting a model vs calling a managed API.
- [ ] Write the Week 10 review and plan Week 11.

## Learn (with resources)
- **Ollama** — install + run a small model (e.g., a 1–3B model): https://ollama.com
- **AWS Getting Started** — EC2 (reuse your runbook): https://aws.amazon.com/getting-started
- Hugging Face course (optional, for a `transformers` pipeline alternative): https://huggingface.co/learn

> **Cost discipline:** Free Tier `t2.micro` is small — pick a **tiny** model or expect it to be slow; that's the lesson. **Terminate the instance the moment you're done.** Keep the billing alarm on.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-open-model-ec2`.
2. [ ] Launch a Free Tier EC2 instance, install Ollama (or a small HF model), pull a tiny model, and send it a prompt from the instance.
3. [ ] `projects/intermediate/aws-open-model/notes.md`: record the model size, response time, and rough resource use; compare to your managed-API app (latency, cost, control, privacy tradeoffs).
4. [ ] **Tear down** the instance immediately after; confirm nothing is running and note it in the runbook.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.
6. [ ] **Weekly review:** copy `templates/weekly-review-template.md` into a new GitHub issue titled "Weekly Review — Week 10", fill it in, and update `PROGRESS.md` (mark Week 10 status + days done).

## Reflection
- **Biggest win this week:**
- **What I want to be faster at:**
- **Confidence (1–5): AWS/EC2 __ · S3/IAM __ · Cost discipline __**
- **Time actually spent:**
