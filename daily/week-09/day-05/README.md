# Week 09 · Day 05 — Streamlit UI wired to the FastAPI backend

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Build a Streamlit chat UI that talks to yesterday's FastAPI backend over HTTP.
- [ ] Keep frontend and backend as separate layers (UI never calls the LLM directly).
- [ ] Handle loading states and backend errors gracefully in the UI.

## Learn (with resources)
- **Streamlit docs** — chat elements (`st.chat_message`, `st.chat_input`) + session state: https://docs.streamlit.io
- **FastAPI docs** — you're consuming the API you built Day 04.
- `requests`/`httpx` for calling the backend from Streamlit.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-streamlit-ui`.
2. [ ] `projects/intermediate/llm-api/ui.py`: a Streamlit app with a chat input; on submit, POST the message to your FastAPI `/chat` endpoint and render the reply.
3. [ ] Keep conversation history in `st.session_state` and render the full thread with `st.chat_message`.
4. [ ] Show a spinner while waiting, and if the backend returns an error (or is down), show a friendly message instead of a stack trace.
5. [ ] Run both together (uvicorn backend + `streamlit run ui.py`); confirm end-to-end. Add run instructions to `projects/intermediate/llm-api/README.md`.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
