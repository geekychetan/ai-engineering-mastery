# Week 07 · Day 05 — PROJECT: RAG document Q&A app end-to-end

**Estimated time:** ~5 hrs (0.5 hr brief + 4.5 hr build)
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Write a project brief before building.
- [ ] Ship a working RAG doc Q&A app that ingests, retrieves, and answers with citations.
- [ ] Package it so a teammate can run it from your README.

## Learn (with resources)
- **DeepLearning.AI short course** — "LangChain: Chat with Your Data": the final "Chat" lesson (tying the pipeline together).
- **Streamlit docs** (if adding a UI) — `st.chat_input`, file display: https://docs.streamlit.io
- Reuse everything from Days 1–4 this week — today is assembly + polish, not new concepts.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-rag-app`.
2. [ ] **Brief first:** copy `templates/project-brief-template.md` into `projects/intermediate/rag-qa/BRIEF.md` and fill it — including a concrete **success metric** (e.g. "answers 8/10 questions from my golden list correctly with a correct citation").
3. [ ] Build `projects/intermediate/rag-qa/` combining your week's pieces:
   - `ingest.py` — load `docs/`, chunk, embed, store in Chroma.
   - `app.py` — a CLI loop or Streamlit UI: take a question → retrieve → answer with `[source]` citations → handle "not in docs".
   - Reuse the Week-6 retry wrapper so API hiccups don't crash it.
4. [ ] Create a small `golden_questions.md` (5–8 Q&A pairs you know the docs can answer) — this is your eval seed, leaning on your QA strength.
5. [ ] Write `projects/intermediate/rag-qa/README.md`: what it does, setup, how to run, an example question + cited answer.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
