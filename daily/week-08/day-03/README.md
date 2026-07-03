# Week 08 · Day 03 — LangChain basics (and when NOT to use a framework)

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Use LangChain building blocks: prompt templates, an LLM, and a simple chain (LCEL / `prompt | model | parser`).
- [ ] Rebuild something you already wrote raw, now with LangChain, and compare the two.
- [ ] Articulate **when a framework helps vs when the raw API is simpler** (a real engineering judgment call).

## Learn (with resources)
- **DeepLearning.AI short course** — "LangChain for LLM Application Development".
- **LangChain (Python) docs** — quickstart, prompt templates, LCEL: https://python.langchain.com
- Optional: **freeCodeCamp** — a LangChain crash course on YouTube.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-langchain-basics`.
2. [ ] `projects/intermediate/langchain-basics/summarize_chain.py`: build a chain with a `ChatPromptTemplate` (a summarizer with a system message + a `{text}` variable), pipe it through the model and an output parser, and run it on a paragraph.
3. [ ] `projects/intermediate/langchain-basics/raw_vs_framework.py`: implement the *same* summarizer using the raw provider SDK (no LangChain). Keep both so you can diff them.
4. [ ] `projects/intermediate/langchain-basics/README.md`: write a short "When NOT to use a framework" note — e.g., raw API is often clearer for a single call, easier to debug, fewer dependencies; frameworks earn their keep for multi-step chains, swappable components, and built-in integrations. Give your honest take after building both.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
