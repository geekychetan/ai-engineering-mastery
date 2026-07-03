# Week 12 · Day 04 — Add the agent / tool-use layer

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Add an agent layer that can decide when to use tools vs answer directly.
- [ ] Expose the RAG retriever as one tool, plus at least one domain-specific tool.
- [ ] Make the agent's tool calls observable (log which tool ran and with what args).

## Learn (with resources)
- **DeepLearning.AI** — "Functions, Tools and Agents with LangChain".
- **Anthropic docs** — tool use / function calling: https://docs.anthropic.com
- **LangChain docs** — agents & tools: https://python.langchain.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week12-day04-agent`.
2. [ ] Write `app/agent.py`: an agent that has access to a `search_docs` tool (your RAG retriever from Day 03) plus one domain tool. For a QA assistant that could be `generate_test_cases(requirement)` or `parse_bug_report(text)`; for a doc assistant it could be a `lookup` or a lightweight `calculator`/`date` tool.
3. [ ] Give the agent a clear system prompt: when to search docs, when to call the domain tool, when to just answer. Keep the tool set small — an agent with 2–3 good tools beats one with 10 vague ones.
4. [ ] Log every tool invocation (tool name + arguments + short result) so you can trace the agent's reasoning path. Save a couple of example traces to `projects/capstone/docs/` for your README/build-notes later.
5. [ ] Test with prompts that force each path: one that should search, one that should use the domain tool, one that needs both.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
