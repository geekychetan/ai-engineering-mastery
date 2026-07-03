# Week 07 · Day 03 — Chunking + an ingestion pipeline over real docs

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Explain why we chunk documents and the size/overlap tradeoff.
- [ ] Load real documents (PDF/txt/markdown), split them, and embed the chunks.
- [ ] Build a repeatable ingestion pipeline that populates your vector store.

## Learn (with resources)
- **DeepLearning.AI short course** — "LangChain: Chat with Your Data": the "Document Loading" and "Document Splitting" lessons.
- **LangChain docs (Python)** — text splitters (`RecursiveCharacterTextSplitter`) and document loaders: https://python.langchain.com
- **Chroma docs** — adding many documents efficiently: https://docs.trychroma.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-chunking`.
2. [ ] Put 2–4 real documents you care about in `projects/intermediate/rag/docs/` (e.g. a PDF manual, a few markdown notes, an article you saved).
3. [ ] Create `projects/intermediate/rag/ingest.py` that:
   - Loads each doc's text.
   - Splits into chunks with a chosen size + overlap (start ~500–1000 chars, ~100 overlap).
   - Embeds and stores each chunk in Chroma with metadata `{source, chunk_index}`.
   - Prints how many chunks were created per document.
4. [ ] Make the script idempotent-ish (re-running doesn't silently duplicate everything — e.g. reset or use stable ids).
5. [ ] Add `projects/intermediate/rag/chunking_notes.md`: why chunk at all, what happens if chunks are too big vs too small, and what overlap buys you.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
