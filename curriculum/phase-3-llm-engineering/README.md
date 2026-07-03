# Phase 3 — LLM Engineering Core (Weeks 6-9)

**The heart of the program.** This is where you become an *LLM engineer*: building real apps with LLM APIs, RAG, agents, and — the differentiator — **evaluation & testing**.

Every project here starts with a **problem brief** (`templates/project-brief-template.md`) and ends with **how you measured it**.

---

## Week 6 — LLM APIs + prompt engineering
- Calling LLM APIs (Anthropic/OpenAI); messages, system prompts, temperature, tokens/cost.
- Prompt engineering in depth: clear instructions, few-shot examples, **structured/JSON output**, role prompting.
- Handling failures: retries, timeouts, rate limits.
- Build: a small CLI/Streamlit chatbot with a system prompt.

## Week 7 — RAG end-to-end
- Embeddings; what a **vector database** is (Chroma / FAISS / pgvector).
- **Chunking strategies**; ingestion pipeline; retrieval; (re)ranking.
- Grounding answers in sources; citing retrieved chunks; reducing hallucination.
- **Project:** RAG document Q&A over a real doc set, with source citations.

## Week 8 — Agents + tool use
- Function/tool calling; letting the model call your Python functions.
- ReAct-style multi-step reasoning; simple agent loops.
- Frameworks: **LangChain / LlamaIndex** basics — *and when NOT to use them* (raw API is often simpler).
- **Project:** a tool-using agent (e.g., calls an API + does a calculation + returns a structured answer).

## Week 9 — Evaluation, testing & app layers (your differentiator)
- **LLM evaluation:** golden datasets, LLM-as-judge, rubric scoring.
- **Prompt regression testing:** treat prompts like code — tests that catch quality drops.
- Guardrails & structured-output validation (e.g., pydantic).
- App layers: **FastAPI** backend + **Streamlit** UI.
- **Project:** a chatbot with memory **+ an eval suite** that scores its answers and catches regressions.

---

## Exit criteria
- [ ] Build a chatbot that maintains conversation state.
- [ ] Explain and build a RAG pipeline; explain chunking/retrieval tradeoffs.
- [ ] Build an agent that calls tools and reasons over multiple steps.
- [ ] Write an eval suite (golden set + LLM-as-judge) and interpret its scores.
- [ ] Explain when RAG vs fine-tuning vs a better prompt is the right tool.
- [ ] Talk fluently about cost, latency, and hallucination mitigation.

## Resources
See [RESOURCES.md → Phase 3](../../RESOURCES.md#phase-3--llm-engineering-core). Primary: **DeepLearning.AI short courses**, **Anthropic docs**, **LangChain/LlamaIndex docs**, **Hugging Face course**.

## Projects this phase
- `projects/intermediate/` — RAG doc Q&A (Week 7).
- `projects/intermediate/` — tool-using agent (Week 8).
- `projects/intermediate/` — chatbot + eval suite (Week 9).
