# AI Engineer 28-Day Interview Prep

A structured 30-day plan to go from Python basics to a job-ready AI Engineer — covering ML, Pandas, LLMs, FastAPI, Docker, Cloud, and Interview Prep.

---

## Projects Built

| Day | Project | Tech |
|-----|---------|------|
| Day 7 | Iris Classifier CLI Tool | scikit-learn, argparse |
| Day 13 | Iris Model API | FastAPI, joblib, scikit-learn |
| Day 14 | AI Resume Analyzer API | FastAPI, Groq API (LLaMA 3.3), Pandas |
| Day 21 | Sentiment Dashboard API | sklearn, FastAPI, Docker, Cloud Run |

---

## Tech Stack

- **Language:** Python 3.10+
- **ML:** scikit-learn, NumPy, Pandas
- **LLM API:** Groq (LLaMA 3.3 70B), Sentence Transformers
- **API Framework:** FastAPI + Pydantic + Uvicorn
- **Embeddings:** sentence-transformers (all-MiniLM-L6-v2)
- **Deployment:** Docker, Google Cloud Run, GitHub Actions
- **Tools:** joblib, python-dotenv, requests

---

## Progress Log

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Python Refresher — variables, lists, comprehensions | Done |
| Day 2 | Functions, Modules, Error Handling | Done |
| Day 3 | File I/O, JSON, APIs | Done |
| Day 4 | OOP — classes, inheritance, all 4 pillars | Done |
| Day 5 | NumPy Crash Course | Done |
| Day 6 | ML Fundamentals + scikit-learn Intro | Done |
| Day 7 | Project: Iris Classifier CLI Tool | Done |
| Day 8 | Pandas Part 1 — read, explore, groupby | Done |
| Day 9 | Pandas Part 2 — cleaning, fillna, apply+lambda | Done |
| Day 10 | Groq API Basics — summarizer.py | Done |
| Day 11 | Prompt Engineering + Embeddings + Cosine Similarity | Done |
| Day 12 | FastAPI Part 1 — GET, POST, Pydantic | Done |
| Day 13 | FastAPI Part 2 — Wrap ML Model | Done |
| Day 14 | Project: AI Resume Analyzer API + CSV Logging | Done |
| Day 15 | Git + GitHub — init, push, .gitignore, branches | Done |
| Day 16 | Docker Part 1 | Pending |
| Day 17 | Docker Part 2 — Containerize FastAPI | Pending |
| Day 18 | Cloud Deployment — Google Cloud Run | Pending |
| Day 19 | CI/CD with GitHub Actions | Pending |
| Day 20 | Project A: AI Document Q&A (RAG-lite) | Pending |
| Day 21 | Project: Sentiment Dashboard API | Pending |
| Day 22 | Python + Data Structures Interview Q&A | Pending |
| Day 23 | ML Interview Q&A | Pending |
| Day 24 | GenAI / LLM Interview Q&A | Pending |
| Day 25 | System Design for AI Apps | Pending |
| Day 26 | Fine-Tuning Concepts | Pending |
| Day 27 | Mock Interview Day | Pending |
| Day 28 | AI Agents + MCP Basics | Pending |
| Day 29 | Vector Databases + Advanced RAG | Pending |
| Day 30 | Final Polish + Launch | Pending |

---

## How to Run

### Resume Analyzer API (Day 14)
```bash
# Install dependencies
pip install fastapi uvicorn groq pandas python-dotenv

# Add your Groq API key to day14/.env
# GROQ_API_KEY=your_key_here

# Run
python -m uvicorn day14.main:app --reload

# Test at http://localhost:8000/docs
```

### Iris Classifier (Day 7)
```bash
pip install scikit-learn

python day07/predict.py --sepal-length 5.1 --sepal-width 3.5 --petal-length 1.4 --petal-width 0.2
```

---

## Key Concepts Covered

- Python OOP (4 pillars: encapsulation, abstraction, inheritance, polymorphism)
- NumPy vectorization and broadcasting
- Pandas data cleaning and aggregation
- ML: train/test split, LogisticRegression, accuracy/precision/recall
- LLM API: prompt engineering, few-shot, chain-of-thought, structured JSON output
- Embeddings and cosine similarity
- REST APIs with FastAPI and Pydantic
- Saving/loading ML models with joblib
- Git, .gitignore, branching, PRs

---

## Final Deliverables (End of Day 30)
- [ ] 3 GitHub projects (Iris, Resume Analyzer, Sentiment Dashboard)
- [ ] At least 1 deployed live URL
- [ ] CI/CD on at least 1 repo
- [ ] Basic RAG system built
- [ ] MCP concept understood
- [ ] LinkedIn updated
- [ ] 2-min self-intro memorized
