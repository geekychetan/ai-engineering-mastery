# Week 08 · Day 01 — Function/tool calling basics

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Explain what "tool calling" (a.k.a. function calling) is and why a model needs it.
- [ ] Define a Python function as a tool the model can request.
- [ ] Run the full loop: model asks for a tool → you execute it → you pass the result back → model answers.

## Learn (with resources)
- **DeepLearning.AI short course** — "Functions, Tools and Agents with LangChain" (watch the tool-calling lessons only today): https://www.deeplearning.ai/short-courses
- **Anthropic docs** — Tool use / function calling guide: https://docs.anthropic.com
- Skim [Phase 3 README → Week 8](../../../curriculum/phase-3-llm-engineering/README.md) so you know where this week is headed.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-tool-calling`.
2. [ ] `projects/intermediate/tool-basics/tools.py`: write one plain Python function `get_weather(city: str) -> dict` that returns a hard-coded/fake response (no external API yet). Give it a clear docstring and type hints.
3. [ ] `projects/intermediate/tool-basics/tool_call.py`: describe the tool as a JSON schema, send a user question ("What's the weather in Pune?") to the LLM, detect when the model requests the tool, execute your Python function, feed the result back, and print the model's final natural-language answer.
4. [ ] Print each step (model's tool request → your function output → final answer) so you can *see* the loop. Note in the reflection who decides to call the tool (the model) vs who runs it (your code).
5. [ ] `projects/intermediate/tool-basics/README.md`: a few lines on what tool calling is, in your own words.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
