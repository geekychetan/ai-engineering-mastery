# Week 15 · Day 01 — LLM system design: whiteboard a RAG system

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Design a RAG system on a whiteboard from a blank page.
- [ ] Reason out loud about chunking, retrieval, evals, and cost/latency/quality tradeoffs.
- [ ] Have a crisp story for hallucination mitigation.

## Learn (with resources)
- **ByteByteGo** (YouTube) — system-design method (requirements → components → tradeoffs); adapt it to LLM apps.
- **Excalidraw** — practice sketching the design cleanly and fast: https://excalidraw.com
- **DeepLearning.AI** — "Building and Evaluating Advanced RAG" for the tradeoff vocabulary.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week15-day01-system-design`.
2. [ ] Take a fresh prompt (e.g. "Design a RAG assistant for a company's internal docs at 10k queries/day") and whiteboard it in Excalidraw: ingestion, chunking strategy, embeddings, vector store, retriever (+ reranking), the LLM, guardrails, and the **eval loop**.
3. [ ] Annotate the tradeoffs: chunk size vs recall, top-k vs cost/latency, model choice vs quality, caching, when to fine-tune vs prompt vs RAG. Say why for each.
4. [ ] Write a dedicated **hallucination mitigation** note: grounding prompts, "I don't know" behavior, source citation, retrieval quality, and how evals *catch* hallucinations (tie back to your capstone).
5. [ ] Save the diagram + a written walkthrough to `notes/interview/system-design-rag.md`. Time yourself doing the walkthrough out loud in ~10 minutes.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
