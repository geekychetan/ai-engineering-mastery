# Week 06 · Day 05 — Build a chatbot with a system prompt

**Estimated time:** ~5 hrs (1 hr learn/brief + 4 hr build)
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Write a project brief before building.
- [ ] Build a working CLI or Streamlit chatbot that keeps conversation history.
- [ ] Give it a distinct persona/behavior via a strong system prompt.

## Learn (with resources)
- **DeepLearning.AI short course** — "Building Systems with the ChatGPT API": the "Chatbot" lesson (maintaining message history).
- **Anthropic docs** — Messages API: how to pass the running list of messages for multi-turn context: https://docs.anthropic.com
- **Streamlit docs** (if you go the UI route) — `st.chat_message` / `st.chat_input`: https://docs.streamlit.io

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-chatbot`.
2. [ ] **Brief first:** copy `templates/project-brief-template.md` into `projects/intermediate/chatbot/BRIEF.md` and fill it (who's the user, why an LLM, approach, success metric, risks, scope). Keep v1 tiny.
3. [ ] Build `projects/intermediate/chatbot/app.py` — a CLI loop **or** a Streamlit app that:
   - Loads the API key from `.env`.
   - Uses a **system prompt** giving the bot a clear role (e.g. "a concise study buddy that only helps with Python/ML").
   - Maintains the message history so follow-up questions have context.
   - Has a clean way to exit (`quit`) and handles empty input.
4. [ ] Reuse Day-04's retry wrapper so the chatbot doesn't crash on a rate limit.
5. [ ] Add `projects/intermediate/chatbot/README.md` with setup + run instructions and a screenshot or sample transcript.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
