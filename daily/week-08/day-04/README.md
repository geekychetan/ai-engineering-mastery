# Week 08 · Day 04 — Structured outputs with pydantic

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Define a `pydantic` model that describes the exact shape you want back from the LLM.
- [ ] Get the model to return that structure and **validate/parse** it reliably.
- [ ] Handle the case where the model returns malformed output (retry / repair) instead of crashing.

## Learn (with resources)
- **DeepLearning.AI short course** — "Functions, Tools and Agents with LangChain" (structured output / extraction lessons).
- **Anthropic docs** — structured / JSON output and tool-based extraction: https://docs.anthropic.com
- **LangChain docs** — structured output / output parsers (`with_structured_output`): https://python.langchain.com
- pydantic docs (skim `BaseModel`, `ValidationError`): search "pydantic BaseModel".

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-structured-output`.
2. [ ] `projects/intermediate/structured-output/models.py`: a `pydantic` model `ContactCard` with fields like `name: str`, `email: str`, `company: str | None`, `priority: Literal["low","medium","high"]`.
3. [ ] `projects/intermediate/structured-output/extract.py`: send an unstructured email/blurb to the model, ask for output matching the schema, then `ContactCard.model_validate(...)` the result. On `ValidationError`, retry once with the error message fed back to the model; if it still fails, raise a clean error.
4. [ ] Test on 3 inputs, including one messy/incomplete one, and confirm you get validated objects (or a graceful failure).
5. [ ] `projects/intermediate/structured-output/README.md`: note *why* structured + validated output matters (downstream code can trust the shape). Connect this to your QA instinct: validation is a contract test on the model.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
