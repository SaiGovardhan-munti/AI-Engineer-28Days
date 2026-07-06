# 30-Day AI Engineer Interview Prep Plan

**Start date:** 2026-06-02 (Day 1)
**End date:** 2026-07-01 (Day 30)
**Daily commitment:** 3 hours
**Study folder:** `C:\Users\I756813\OneDrive - SAP SE\Desktop\Vibecoding\AI-Engineer-28Days\`

## Daily Structure
- **Hour 1:** Learn concept (challenge-first style — try first, then I teach)
- **Hour 2:** Hands-on coding
- **Hour 3:** Revise + explain out loud + end-of-day quiz

## Tools
- **Editor:** VS Code
- **Language:** Python 3.10+
- **GenAI API:** Free Gemini API key (Week 2 onwards)
- **Free model alternatives:** Groq, Hugging Face, Ollama

---

## WEEK 1: Python + ML Fundamentals

### Day 1 — Python Refresher (Core Syntax)
- Variables, data types, f-strings, type hints basics
- Lists, tuples, dicts, sets
- List/dict comprehensions
- if/else, for, while, enumerate, zip
- **Practice:** Student scores script (avg, max, min, count above avg)
- **Resource:** Corey Schafer Python Basics Playlist (Videos 1–5)

### Day 2 — Functions, Modules, Error Handling
- def, default args, *args, **kwargs
- Importing modules, `if __name__ == "__main__"`
- try/except/finally, raising exceptions
- Lambda, map, filter
- **Practice:** Build calculator.py module with error handling
- **Resource:** Python Functions — Corey Schafer

### Day 3 — File I/O + JSON + APIs
- Reading/writing txt and CSV files
- JSON: json.load, json.dumps
- HTTP basics + requests library
- Status codes
- **Practice:** Call GitHub API, parse JSON, save to file
- **Resource:** Python Requests — Corey Schafer

### Day 4 — Object-Oriented Python
- Classes, __init__, self
- Methods, __str__, __repr__
- Inheritance basics
- Why OOP matters for ML pipelines
- **Practice:** BankAccount + SavingsAccount classes
- **Resource:** Python OOP — Tech With Tim

### Day 5 — NumPy Crash Course
- np.array, shape, dtype, reshape
- Slicing, broadcasting, vectorization
- np.mean, np.std, np.dot, np.where
- **Practice:** 5x5 random matrix operations with broadcasting
- **Resource:** NumPy Tutorial — Keith Galli

### Day 6 — ML Fundamentals + scikit-learn Intro
- Supervised vs unsupervised; classification vs regression
- Train/test split, overfitting/underfitting
- fit/predict API
- Metrics: accuracy, precision, recall, RMSE
- **Practice:** Iris dataset + LogisticRegression
- **Resource:** scikit-learn in 15 minutes — StatQuest

### Day 7 — 🏁 PROJECT: Iris Classifier CLI Tool
- Train Decision Tree + Logistic Regression
- Compare accuracy
- CLI: `python predict.py --sepal-length 5.1 ...`
- Push to GitHub with README
- **Resource:** Build Your First ML Model — Ken Jee

---

## WEEK 2: Pandas + Gemini API + FastAPI

### Day 8 — Pandas Part 1
- Series vs DataFrame
- pd.read_csv, df.to_csv
- head, tail, info, describe
- loc vs iloc
- **Practice:** Titanic CSV — rows, missing data, mean fare per class
- **Resource:** Pandas Tutorial — Corey Schafer

### Day 9 — Pandas Part 2 (Cleaning)
- fillna, dropna
- Boolean filtering
- groupby, agg, value_counts
- apply with lambda
- **Practice:** Titanic — fill ages, group by Sex+Pclass, survival rate
- **Resource:** Pandas Data Cleaning — Alex The Analyst

### Day 10 — Gemini API Basics
- Tokens, context window, temperature
- Gemini chat API: roles, system instructions
- API keys + .env files
- Prompt structure
- **Practice:** Build summarizer.py with Gemini
- **Resource:** Google AI Studio Gemini API docs

### Day 11 — Prompt Engineering + Embeddings
- Zero-shot, few-shot, chain-of-thought
- Structured output (JSON mode)
- Embeddings (vector basics)
- Cosine similarity
- **Practice:** Sentiment classifier with few-shot prompting (JSON output)
- **Resource:** Google Prompt Engineering Guide

### Day 12 — FastAPI Part 1
- REST basics: GET/POST/PUT/DELETE
- @app.get, @app.post, params
- Pydantic models
- Auto docs at /docs
- **Practice:** API with `/` and `POST /add` endpoints
- **Resource:** FastAPI Crash Course — Patrick Loeber

### Day 13 — FastAPI Part 2 (Wrap ML Model)
- joblib/pickle for saving models
- JSON input → predictions
- Background tasks, dependency injection
- CORS
- **Practice:** Wrap Iris model in `POST /predict` endpoint
- **Resource:** FastAPI Official Tutorial

### Day 14 — 🏁 PROJECT: AI Resume Analyzer API
- POST /analyze takes resume text
- Calls Gemini to extract: skills, years exp, top 3 strengths
- Returns structured JSON
- Pandas logs to CSV
- Test with /docs UI
- **Resource:** FastAPI + LLM tutorials — freeCodeCamp

---

## WEEK 3: Docker + Cloud + Build Two Projects

### Day 15 — Git + GitHub Mastery
- init, add, commit, push, pull, clone
- Branching, merge, conflicts
- .gitignore, semantic commits
- PRs and code review
- **Practice:** Feature branch + PR on Week 2 project
- **Resource:** Git & GitHub — freeCodeCamp

### Day 16 — Docker Part 1
- Containers vs VMs
- Image vs container, Dockerfile, build, run
- Layers and caching
- ps, logs, exec
- **Practice:** Dockerize hello-world Python script
- **Resource:** Docker Tutorial — TechWorld with Nana

### Day 17 — Docker Part 2 (Containerize FastAPI)
- requirements.txt in Dockerfile
- EXPOSE, CMD, ENTRYPOINT
- Port mapping
- docker-compose basics
- **Practice:** Containerize Resume Analyzer
- **Resource:** Dockerize FastAPI — Bek Brace

### Day 18 — Cloud Deployment (Google Cloud Run)
- What Cloud Run is
- gcloud CLI basics
- Env vars in cloud
- HTTPS + logs
- **Practice:** Deploy Resume Analyzer to Cloud Run
- **Resource:** Deploy FastAPI to Cloud Run

### Day 19 — CI/CD with GitHub Actions
- What CI/CD is
- .github/workflows/main.yml
- Run tests on push
- Auto-deploy to Cloud Run
- **Practice:** Add pytest GitHub Action
- **Resource:** GitHub Actions for Python — ArjanCodes

### Day 20 — Project A: AI Document Q&A (RAG-lite)
- POST /ask endpoint
- PDF/text + question input
- Chunking, Gemini embeddings, cosine search
- Answer from gemini-pro
- Containerize
- **Resource:** Simple RAG tutorials

### Day 21 — 🏁 PROJECT: Sentiment Dashboard API
- Train sklearn sentiment model on IMDB sample
- /predict endpoint (sklearn model)
- /explain endpoint (Gemini explanation)
- Dockerize, deploy to Cloud Run, GitHub Actions CI

---

## WEEK 4: Interview Prep + Mock + Polish

### Day 22 — Python + Data Structures Q&A
- Mutable vs immutable
- is vs ==, shallow vs deep copy
- Generators, iterators
- Decorators
- **Practice:** 10 Python interview questions + timing decorator
- **Resource:** Python Interview Questions — Edureka

### Day 23 — ML Q&A
- Bias/variance, overfitting fixes
- Cross-validation
- Train/val/test, data leakage
- LR vs RF vs XGBoost
- **Practice:** 8 ML concepts in 90 sec each (recorded)
- **Resource:** ML Interview Questions — Krish Naik

### Day 24 — GenAI / LLM Q&A
- Tokens, context, temperature, top_p
- Hallucinations + RAG
- Fine-tuning vs RAG vs prompting
- Embeddings + vector DBs
- **Practice:** 1-paragraph answers to 3 LLM questions
- **Resource:** LLM Interview Questions — AssemblyAI

### Day 25 — System Design for AI Apps
- Architecture: client → API → model → DB
- Caching, rate limiting
- Cost considerations
- Monitoring
- **Practice:** Design "Customer Support AI" on paper
- **Resource:** Design an LLM App — ByteByteGo

### Day 26 — Fine-Tuning Concepts
- When fine-tuning is worth it
- Data prep: JSONL format
- LoRA / PEFT basics
- Why RAG before fine-tuning
- **Practice:** Write JSONL with 10 prompt/completion examples
- **Resource:** Gemini fine-tuning docs

### Day 27 — Mock Interview Day
- STAR format for project questions
- Live-code: FizzBuzz, reverse string, word count
- Walk through Day 21 project line by line
- **Practice:** 3 LeetCode easy + 3 project walkthroughs + roleplay interview
- **Resource:** Mock AI Engineer Interview — Exponent

### Day 28 — AI Agents + MCP Basics
- What are AI Agents? (autonomous task execution)
- Tools, memory, planning in agents
- MCP (Model Context Protocol) — what it is and why it matters
- How MCP connects AI models to external tools/data sources
- MCP vs traditional API calls
- **Practice:** Build a simple agent loop — LLM + tool call + response
- **Resource:** Anthropic MCP docs, LangChain agents intro

### Day 29 — Vector Databases + Advanced RAG
- What is a vector database? (Chroma, FAISS, Pinecone)
- Embeddings recap — turning text into numbers
- Semantic search vs keyword search
- Chunking strategies for documents
- Full RAG pipeline: embed → store → retrieve → generate
- **Practice:** Build a simple RAG system — load a text file, embed it, answer questions
- **Resource:** LangChain RAG tutorial, Chroma docs

### Day 30 — 🏁 FINAL POLISH + LAUNCH
- Polish all 3 README files + Day 28-29 projects
- Pin top 3 GitHub repos, profile README
- LinkedIn: title, projects in Featured
- 2-min "tell me about yourself" pitch (rehearse 5x)

**Final deliverables:**
- [ ] 3 GitHub projects (Iris, Resume Analyzer, Sentiment Dashboard)
- [ ] At least 1 deployed live URL
- [ ] CI/CD on at least 1 repo
- [ ] Basic RAG system built
- [ ] MCP concept understood
- [ ] LinkedIn updated
- [ ] 2-min self-intro memorized

---

## Daily Habits
1. **Hour 3 = explain out loud** — record on phone. If you can teach it, you know it.
2. **Commit code daily** — recruiters look at green squares.
3. **Keep notes.md** — one-line answers to every concept = your final cheat sheet.
4. **Don't skip a day** — but don't double up either. Pick up where you left off.
