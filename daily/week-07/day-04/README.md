# Week 07 · Day 04 — Retrieval + prompt assembly (grounded, cited answers)

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Retrieve the top-k relevant chunks for a question and assemble them into a prompt.
- [ ] Instruct the model to answer only from the context and cite its sources.
- [ ] Explain how grounding reduces hallucination and how to handle "not in the docs".

## Learn (with resources)
- **DeepLearning.AI short course** — "LangChain: Chat with Your Data": the "Retrieval" and "Question Answering" lessons.
- **DeepLearning.AI short course** — "Building and Evaluating Advanced RAG": the intro to the retrieve→augment→generate flow.
- **Anthropic docs** — grounding / long-context tips and asking the model to cite: https://docs.anthropic.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-retrieval`.
2. [ ] Create `projects/intermediate/rag/answer.py` that, given a question:
   - Retrieves top-k chunks from Chroma (from Day-03's store).
   - Builds a prompt that puts the retrieved chunks (with their `source`) in the context, delimited clearly.
   - Uses a **system prompt** telling the model: answer only from the provided context, cite sources like `[source: filename]`, and say "I don't know based on the provided documents" when the answer isn't there.
   - Prints the answer + which chunks were used.
3. [ ] Test the "I don't know" path: ask something the docs can't answer and confirm it refuses to make things up.
4. [ ] Add `projects/intermediate/rag/grounding_notes.md`: why grounding + citations reduce hallucination, and one failure you observed.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
