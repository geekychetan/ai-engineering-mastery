# Week 12 · Day 02 — Repo skeleton + data ingestion pipeline

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Stand up a clean, production-shaped repo skeleton for the capstone.
- [ ] Build the ingestion pipeline: load → chunk → embed → store.
- [ ] Verify documents actually land in the vector store.

## Learn (with resources)
- **DeepLearning.AI** — "LangChain: Chat with Your Data" (loaders, splitting, vector stores) or "Building and Evaluating Advanced RAG".
- **LangChain docs** — document loaders + text splitters: https://python.langchain.com
- **LlamaIndex docs** (if you prefer it for ingestion): https://docs.llamaindex.ai

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week12-day02-ingestion`.
2. [ ] Scaffold `projects/capstone/` with a sane layout, e.g. `app/` (ingestion, retrieval, agent, api), `data/` (source docs), `eval/` (empty for now), `tests/`, `requirements.txt`, and a stub `README.md`. Pin your dependencies.
3. [ ] Drop a small, realistic corpus into `data/` — e.g. requirements docs / test-plan docs / product docs relevant to your chosen domain (5–15 files is plenty for v1).
4. [ ] Write `app/ingest.py`: load the docs, chunk with a chosen `chunk_size`/`overlap` (write a one-line comment on *why* you picked those), embed, and persist to a local vector store (Chroma or FAISS).
5. [ ] Add a tiny sanity check: after ingestion, run a similarity search for a known term and print the top-k chunks to confirm retrieval hits sensible content.
6. [ ] Note your embedding model + dimensions and rough ingestion cost/time in a comment or the stub README.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
