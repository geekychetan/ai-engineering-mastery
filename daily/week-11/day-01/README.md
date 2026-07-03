# Week 11 · Day 01 — Docker basics

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Explain images vs containers, and why "works on my machine" stops being a problem with Docker.
- [ ] Write a Dockerfile, build an image, and run a container with a mapped port.
- [ ] Use the core commands: `build`, `run`, `ps`, `logs`, `stop`, `rm`.

## Learn (with resources)
- YouTube — **TechWorld with Nana**, "Docker Tutorial for Beginners" (full crash course).
- **Docker docs** — get started / Dockerfile reference: https://docs.docker.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-docker-basics`.
2. [ ] Install Docker Desktop; run `docker run hello-world` to confirm it works.
3. [ ] `projects/intermediate/docker-basics/app.py`: a tiny Flask/FastAPI (or even `http.server`) app that returns "hello from a container" on a port.
4. [ ] `projects/intermediate/docker-basics/Dockerfile`: base off a slim Python image, copy the app, install deps, expose the port, set the run command.
5. [ ] Build and run: `docker build -t hello-container .` then `docker run -p 8000:8000 hello-container`; hit it in the browser. Practice `docker ps`, `docker logs`, `docker stop`.
6. [ ] `projects/intermediate/docker-basics/README.md`: define image vs container in your own words + the commands you used.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
