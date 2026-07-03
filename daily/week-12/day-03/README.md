# Week 12 · Day 03 — Core RAG pipeline end to end

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Wire retrieval + prompt + LLM into a working question → grounded answer flow.
- [ ] Return citations/sources so answers are traceable, not trust-me.
- [ ] Confirm the pipeline refuses or hedges when the context doesn't support an answer.

## Learn (with resources)
- **DeepLearning.AI** — "Building and Evaluating Advanced RAG" (retrieval quality + grounding).
- **Anthropic docs** — prompt engineering guide (grounding a model in retrieved context, avoiding hallucination): https://docs.anthropic.com
- **LangChain docs** — retrieval / RAG chains: https://python.langchain.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week12-day03-rag-core`.
2. [ ] Write `app/rag.py`: given a question, retrieve top-k chunks, build a grounded prompt that instructs the model to answer ONLY from context and to say "I don't know" when the context is insufficient.
3. [ ] Return the answer **plus the source chunks/filenames** it used. Print them so you can eyeball grounding.
4. [ ] Run 5–8 questions by hand: some clearly answerable from the corpus, some deliberately out-of-scope. Confirm out-of-scope questions get an honest "not in the docs" answer, not a confident hallucination.
5. [ ] Jot down 3–5 of these Q/expected-A pairs in `eval/seed_questions.md` — these become seeds for the golden dataset in Week 13.
6. [ ] Push, PR with `Closes #<issue>`, self-review (check: are sources actually being returned? does it hallucinate on the trick questions?), merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
