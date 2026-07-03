# Curriculum Design — The "Why" Behind This Planner

This document captures the reasoning behind how this curriculum is structured: who it's for, the decisions that shaped it, and the full 15-week map with the resources chosen for each phase. It's the *rationale* companion to [`README.md`](../README.md) (the roadmap) and [`GETTING_STARTED.md`](../GETTING_STARTED.md) (the quickstart).

If you're editing or extending the curriculum, read this first — it explains why things are the way they are, so changes stay coherent with the original intent.

---

## Context

A full, self-paced curriculum + tracking system for a career-changer moving into AI engineering.

**Learner profile:** MBA (Business Analytics), ~4 yrs experience across Marketing, Salesforce admin, and Manual QA. Basic Python (syntax, running scripts locally) and *some prior git exposure*. Not from a CS background. Strong domain instincts and analytical thinking; needs software-engineering fundamentals and hands-on AI depth.

**Goal:** Launch as a Junior AI/LLM Engineer who interviews *above* junior level — able to frame a problem, choose an AI approach, build it, evaluate it, deploy it on AWS, and reason about tradeoffs.

**Confirmed decisions:**
- **Pace:** Full-time, ~6-8 hrs/day.
- **Timeline:** Aggressive — 3-4 months (planned as **15 weeks**; ML/DL theory compressed to 1 week since the goal is *applied* AI, not ML depth — keep learning ML "just-in-time" on the job).
- **Tracking:** GitHub Issues + Projects (learn the real SWE workflow *while* tracking progress).
- **Project domains:** General LLM apps (RAG, agents, chatbots) **+** QA/testing-with-AI (the differentiator — LLM evals, test generation, guardrails).
- **Git approach:** No separate git phase — git/GitHub is woven into daily coding from Week 1 so confidence is rebuilt *by using it*, not by drilling it in isolation.
- **CS course:** **CS50P — "CS50's Introduction to Programming with Python"** (Harvard, free, Python-focused) instead of the C-heavy CS50x. 1-1.5 hr/day, front-loaded into Weeks 1-6. Optionally cherry-pick 2-3 CS50x lectures later for pure CS concepts (arrays/memory, algorithms) — concept only, not the C problem sets.

---

## Answers to the three founding questions

**1. Minimum time investment?** Given full-time: **min 5 focused hrs/day, 5-6 days/week** (keep 1 rest day — it prevents burnout on an aggressive track). Split: ~1-1.5 hr CS50P + ~3.5-4 hr AI/build. ~30 hrs/week min, ~35-40 target. Below ~25 hrs/week the 3-4 month goal slips toward 6 months.

**2. Progress-tracking tool?** **GitHub Issues + Projects.** Every day = an Issue with a homework checklist; work is done on a branch → Pull Request → review → merge (auto-closes the issue). A **Project board** (Kanban) is the daily dashboard. Doubles as resume-grade proof: green contribution graph, dozens of PRs, issues, reviews.

**3. How to sound "beyond junior"?** Three habits in every project:
- **Problem-framing first** — a one-page brief: who's the user, what's the problem, why AI, simplest solution, success metric, what could go wrong.
- **Always evaluate** — never "it works," always "here's how I measured it" (the QA background is the superpower).
- **Tradeoff fluency** — cost/latency/quality; RAG vs fine-tune vs prompt; when NOT to use a framework.

---

## The 15-Week Curriculum

### Phase 1 — Python + Git Foundations (Weeks 1-4) — *merged*
Real Python fluency with git/GitHub used daily from day one.
- **Week 1:** environment (terminal, VS Code, `pyenv`/`venv`, `pip`), and git/GitHub used immediately — every exercise is a branch → commit → PR → merge. `.gitignore`, README/Markdown, resolving a merge conflict on purpose.
- **Weeks 2-4:** data structures, comprehensions, functions, modules/packages, OOP basics, error handling, file/JSON I/O; type hints; REST APIs with `requests`; env vars & secrets; **`pytest`** + testing discipline (leans on the QA strength); async basics (`asyncio`); CLI apps (`typer`); `numpy` + `pandas` basics.
- CS50P Weeks 0-4 in parallel.
- **Small projects:** a `typer` CLI tool (tested), an API-consuming script with `pytest` tests, all shipped via PRs.

**Learn it here (Phase 1):**
- *Python (free):* **CS50P** — `cs50.harvard.edu/python`. YouTube: **Corey Schafer**'s "Python Tutorial for Beginners" playlist; **freeCodeCamp** 4-hr "Python for Beginners".
- *Python (paid, optional):* Udemy — *"100 Days of Code: The Complete Python Pro Bootcamp"* by **Angela Yu** (do days 1-40); or *"Python for Everybody"* (Dr. Chuck) free on `py4e.com` / Coursera.
- *Git/GitHub (free):* **Pro Git** book — `git-scm.com/book`; **Atlassian Git tutorials** — `atlassian.com/git/tutorials`; YouTube: **freeCodeCamp** "Git and GitHub for Beginners"; GitHub's own `skills.github.com`.
- *pytest (free):* official docs `docs.pytest.org`; YouTube: **ArjanCodes** and **Corey Schafer** unit-testing videos.

### Phase 2 — ML & DL Concepts (Week 5) — *compressed*, breadth-only
One focused week: enough to speak fluently and make good applied decisions — not to master ML.
- ML core: supervised/unsupervised, train/test split, overfitting, features, metrics (precision/recall/F1, RMSE).
- Hands-on `scikit-learn`: one small classification (or regression) on business/tabular data.
- DL intuition: neurons, layers, gradient descent, backprop, **embeddings**.
- **Transformers & attention** conceptually; tokenization hands-on.
- **Small project:** train + evaluate one sklearn model, write up findings. (Deeper ML is picked up just-in-time later, as needed.)

**Learn it here (Phase 2):**
- *Free:* **DeepLearning.AI + Andrew Ng** "Machine Learning Specialization" (Coursera, audit free) — watch, don't grind. YouTube: **StatQuest with Josh Starmer** (best intuitive ML/stats explainers), **3Blue1Brown** "Neural Networks" series (4 videos — essential intuition). scikit-learn docs `scikit-learn.org`.
- *Transformers intuition (free):* **3Blue1Brown** "But what is a GPT?" + **Andrej Karpathy** "Let's build GPT" (YouTube) — watch for concepts, not to reproduce.
- *Paid (optional):* Udemy — *"Machine Learning A-Z"* by **Kirill Eremenko** (concepts + sklearn).

### Phase 3 — LLM Engineering Core (Weeks 6-9) — the heart
- LLM APIs (Anthropic/OpenAI): prompt engineering in depth — system prompts, few-shot, structured/JSON output.
- Chatbots with conversation state & memory.
- **RAG end-to-end:** embeddings, chunking, vector DBs (Chroma/FAISS/pgvector), retrieval, reranking.
- Frameworks: LangChain / LlamaIndex — **and when not to use them**.
- **Agents:** tool use / function calling, ReAct, multi-step workflows.
- Guardrails & structured output.
- **LLM Evaluation & Testing (the differentiator):** eval harnesses, LLM-as-judge, prompt regression tests, golden datasets.
- App layers: `FastAPI` (backend) + `Streamlit` (quick UI).
- **Projects:** RAG document Q&A; a tool-using agent; a chatbot with memory + an eval suite.

**Learn it here (Phase 3):**
- *Free — best in class:* **DeepLearning.AI short courses** (all free) — "ChatGPT Prompt Engineering for Developers," "Building Systems with the ChatGPT API," "LangChain for LLM App Dev," "LangChain: Chat with Your Data," "Functions/Tools & Agents with LangChain," "Building & Evaluating Advanced RAG." Official docs: **Anthropic** `docs.anthropic.com` (incl. prompt engineering guide), **OpenAI** `platform.openai.com/docs`, **LangChain** `python.langchain.com`, **LlamaIndex** `docs.llamaindex.ai`. **Hugging Face** course `huggingface.co/learn`.
- *YouTube (free):* **Anthropic** channel (prompt/agent talks), **freeCodeCamp** LangChain/RAG full courses.
- *Paid (optional):* Udemy — *"LangChain — Develop LLM powered applications with LangChain"* by **Eden Marco**.

### Phase 4 — Cloud & Deployment on AWS (Weeks 10-11)
- AWS fundamentals: IAM, security groups, **EC2**, **S3**, cost awareness + tearing down resources.
- Launch EC2, SSH in, deploy a FastAPI app; deploy a **small open model** (small HF model / **Ollama**) on EC2; take an **API-backed LLM app** live.
- **Docker** basics — containerize an app.
- Secrets/env management; **GitHub Actions CI** (run `pytest` on each PR — ties QA + git + cloud together).
- Serverless & managed AI overview: Lambda, **AWS Bedrock** (concept + one small hands-on).
- **Project:** take an earlier project fully live on AWS.

**Learn it here (Phase 4):**
- *Free:* **AWS Free Tier** + official "Getting Started" tutorials `aws.amazon.com/getting-started`; YouTube: **freeCodeCamp** "AWS Certified Cloud Practitioner" course (concepts), **TechWorld with Nana** for Docker + CI/CD; **Docker** docs `docs.docker.com`; **GitHub Actions** docs `docs.github.com/actions`; **Ollama** `ollama.com`.
- *Paid (optional):* Udemy — *"Docker & Kubernetes: The Practical Guide"* by **Maximilian Schwarzmüller** (Docker portion); AWS Cloud Practitioner course by **Stephane Maarek**.

### Phase 5 — Capstone, Portfolio & Interview Prep (Weeks 12-15)
- **Capstone:** RAG + agent + eval suite, containerized and deployed on AWS. Anchor = an LLM-powered QA/testing assistant *or* a RAG assistant with a rigorous eval harness (plays to strengths).
- Architecture diagram, thorough README, cost/latency notes.
- Portfolio: GitHub profile, pinned repos, project write-ups; **resume + LinkedIn** framing the MBA + QA → AI pivot as an asset.
- **LLM system design** for interviews: designing a RAG system, hallucination mitigation, evals, cost/latency tradeoffs.
- Mock interviews + common junior AI/LLM questions; behavioral / career-pivot narrative.
- Stretch: **one real open-source PR** to an AI project.

**Learn it here (Phase 5):** GitHub profile README examples; **excalidraw.com** for architecture diagrams; DeepLearning.AI "Evaluating & Debugging Generative AI"; system-design intuition from **ByteByteGo** (YouTube) adapted to LLM apps.

*CS50P target: finish core lectures/psets by end of Week 6, then taper.*

---

## Repository Structure

```
ai-engineering-mastery/
├── README.md                     # master roadmap + how to use this repo
├── GETTING_STARTED.md            # self-contained quickstart
├── WELCOME.md                    # kickoff message for the learner
├── CLAUDE.md                     # guidance for AI sessions in this repo
├── PROGRESS.md                   # high-level phase/week progress tracker
├── RESOURCES.md                  # consolidated "learn it here" links by phase
├── .gitignore
├── docs/
│   └── CURRICULUM_DESIGN.md       # this file — the "why" behind the plan
├── curriculum/
│   ├── phase-1-python-git/README.md
│   ├── phase-2-ml-dl-concepts/README.md
│   ├── phase-3-llm-engineering/README.md
│   ├── phase-4-cloud-aws/README.md
│   └── phase-5-capstone/README.md
├── daily/
│   └── week-NN/day-NN/README.md   # objectives · resources · homework · reflection
├── projects/{small,intermediate,capstone}/
├── notes/
├── templates/
│   ├── daily-readme-template.md
│   ├── project-brief-template.md  # the problem-framing one-pager
│   └── weekly-review-template.md
└── .github/
    ├── ISSUE_TEMPLATE/{daily-plan.md,project-brief.md}
    ├── pull_request_template.md
    └── workflows/ci.yml           # pytest on every push/PR
```

## GitHub Tracking Workflow
- **Daily issue** per study day, labeled `daily` + `week-NN`, with a checkbox homework list.
- **Branch → PR → review → merge** for every homework/project (teaches the real loop; builds git confidence daily).
- **Project board (Kanban):** `Backlog · This Week · In Progress · In Review · Done`.
- **Milestones:** one per Phase (1-5).
- **Labels:** `python`, `ml`, `llm`, `cloud`, `git`, `project`, `cs50p`, `reading`, `homework`, `week-NN`.
- From Phase 4, **GitHub Actions** runs `pytest` on each PR (a green check to point to in interviews).

## Daily Rhythm
1. Warm-up 15 min (review yesterday's note). 2. CS50P 60-90 min. 3. Core AI learning + build 3-4 hr (the day's homework issue). 4. Commit via PR + self-review. 5. Reflection 10 min into the daily README. Weekly: a `weekly-review` issue.
