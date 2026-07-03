# Week 09 · Day 06 — Project: chatbot with memory + eval suite · Phase 3 retro · weekly review

**Estimated time:** ~4 hrs (lighter day)

**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Ship a chatbot with conversation memory **plus** an eval suite that scores its answers and catches regressions.
- [ ] Close out Phase 3 with an honest retro.
- [ ] Write the Week 9 review and preview Phase 4 (AWS).

## Learn (with resources)
- This is a build + reflect day — lean on your Week 6–9 work.
- Skim [Phase 4 README](../../../curriculum/phase-4-cloud-aws/README.md) to preview cloud + deployment.
- **Anthropic docs** — reference as needed: https://docs.anthropic.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-chatbot-eval`.
2. [ ] **Brief first:** copy `templates/project-brief-template.md` to `projects/intermediate/chatbot-eval/BRIEF.md` and fill it in (be explicit in the "how will I measure good" section).
3. [ ] `projects/intermediate/chatbot-eval/app.py`: extend your FastAPI + Streamlit chatbot to keep multi-turn **memory** across a session.
4. [ ] `projects/intermediate/chatbot-eval/eval/` : bring in a `golden.jsonl`, `run_eval.py`, and `judge.py` (reuse Week 9 Days 2–3) so you can score the chatbot and flag regressions against a threshold.
5. [ ] `projects/intermediate/chatbot-eval/README.md`: what it does, how to run app + evals, and your latest eval scores.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.
7. [ ] **Phase 3 retro:** in the weekly-review issue (or a linked comment), reflect on Phase 3 exit criteria — can you build a memory chatbot, a RAG pipeline, a tool agent, and an eval suite, and talk about cost/latency/hallucination?
8. [ ] **Weekly review:** copy `templates/weekly-review-template.md` into a new GitHub issue titled "Weekly Review — Week 09", fill it in, and update `PROGRESS.md` (mark Week 09 + Phase 3 complete).

## Reflection
- **Biggest win this phase:**
- **What I want to be faster at:**
- **Confidence (1–5): Evaluation __ · App layers (FastAPI/Streamlit) __ · Shipping __**
- **Time actually spent:**
