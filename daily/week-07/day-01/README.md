# Week 07 · Day 01 — Embeddings hands-on + cosine similarity

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Turn sentences into embedding vectors via an API or a local model.
- [ ] Compute cosine similarity and rank sentences by semantic closeness.
- [ ] Explain, in plain English, what an embedding captures and why it enables search.

## Learn (with resources)
- **DeepLearning.AI short course** — "LangChain: Chat with Your Data": the embeddings lesson (concept + why they power retrieval).
- **Anthropic / OpenAI docs** — the embeddings endpoint you'll use (or use `sentence-transformers` locally): https://docs.anthropic.com / https://platform.openai.com/docs
- **Hugging Face course** — sentence embeddings intro: https://huggingface.co/learn
- Callback to Week 5, Day 5: this is the "vector that captures meaning" idea made real.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-embeddings`.
2. [ ] Create `projects/intermediate/rag/embeddings_demo.py` that:
   - Embeds ~6 sentences (mix a few related, a few unrelated, e.g. "I love pizza" / "Pasta is delicious" / "The stock market fell").
   - Computes pairwise **cosine similarity** (write the function with numpy, or use a library) and prints a ranked list for one query sentence.
3. [ ] Confirm the semantically similar sentences score highest and note it in a comment.
4. [ ] Add `projects/intermediate/rag/embeddings_notes.md`: what an embedding is, what cosine similarity measures, and why "similar meaning ≈ close vectors" is the whole basis of semantic search.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
