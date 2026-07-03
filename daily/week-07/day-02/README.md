# Week 07 · Day 02 — Vector databases with Chroma

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Explain what a vector database does and why you need one beyond a list of vectors.
- [ ] Store embeddings in Chroma with metadata and persist them to disk.
- [ ] Run a similarity query and get back the top-k nearest chunks.

## Learn (with resources)
- **DeepLearning.AI short course** — "LangChain: Chat with Your Data": the "Vectorstores and Embedding" lesson.
- **Chroma docs** — getting started, collections, `add`, and `query`: https://docs.trychroma.com
- Optional context: **RESOURCES.md → Phase 3** mentions Chroma / FAISS / pgvector — you're starting with Chroma because it's the simplest to run locally.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-chroma`.
2. [ ] `pip install chromadb`; append to `requirements.txt`.
3. [ ] Create `projects/intermediate/rag/vector_store.py` that:
   - Creates a **persistent** Chroma collection.
   - Adds ~10 short text snippets with an `id` and simple `metadata` (e.g. `source`).
   - Runs a `query` for a natural-language question and prints the top-3 results with their distances/metadata.
4. [ ] Prove persistence: run once to add, run again in "query-only" mode and confirm the data is still there.
5. [ ] Add `projects/intermediate/rag/vector_store_notes.md`: what a vector DB adds over your Day-01 numpy loop (scale, persistence, metadata filtering, ANN search).
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
