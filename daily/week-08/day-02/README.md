# Week 08 · Day 02 — Multi-tool agent + the ReAct loop

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Explain the ReAct pattern: **Reason → Act (call a tool) → Observe (result) → repeat** until done.
- [ ] Register more than one tool and let the model pick the right one.
- [ ] Build a small agent loop by hand (no framework yet) that runs until the model stops calling tools.

## Learn (with resources)
- **DeepLearning.AI short course** — "Functions, Tools and Agents with LangChain" (the agents/ReAct lessons).
- **Anthropic docs** — agents & tool use best practices: https://docs.anthropic.com
- Optional intuition: **Anthropic** YouTube channel — an agents/tool-use talk.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-react-agent`.
2. [ ] `projects/intermediate/react-agent/tools.py`: define **two** tools — `calculator(expression: str)` (safe eval of basic math) and `get_time(timezone: str)` (return current time). Type hints + docstrings on both.
3. [ ] `projects/intermediate/react-agent/agent.py`: write a `while` loop that (a) sends messages to the model, (b) if the model requests a tool, dispatches to the right Python function by name, (c) appends the observation, (d) loops until the model returns a final answer or a max-steps cap is hit.
4. [ ] Add a `MAX_STEPS = 5` guard so the loop can never run forever. Log each Reason/Act/Observe step to the console.
5. [ ] Test it with a prompt that needs both tools (e.g., "What time is it in UTC, and what's 18% of 240?").
6. [ ] `projects/intermediate/react-agent/README.md`: a short diagram/notes of the ReAct loop in your own words.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
