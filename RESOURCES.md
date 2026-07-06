# AI Engineer Resources — Complete Reference
# 150-Day Advanced Plan | Free Only

---

## CONTENTS
1. [Section A — Claude-Researched Resources](#section-a)
2. [Section B — Your Provided Resources](#section-b)
3. [Section C — Comparison & Recommendation](#section-c)
4. [Quick Install Commands](#quick-install)

---

---

# SECTION A — CLAUDE-RESEARCHED RESOURCES

*Researched and curated by Claude, mapped to each phase of the 150-day plan.*

---

## A1 — PHASE 1: ADVANCED PYTHON

### Courses & Videos
| Resource | URL | What it covers |
|----------|-----|----------------|
| **CS50P — Harvard** | https://cs50.harvard.edu/python/ | Clean code, OOP, decorators, testing — free audit |
| **Corey Schafer — YouTube** | https://www.youtube.com/@coreyms | Decorators, generators, async, OOP, design patterns |
| **mCoding — YouTube** | https://www.youtube.com/@mCoding | Decorators, async/await, dataclasses, Python internals |
| **ArjanCodes — YouTube** | https://www.youtube.com/@ArjanCodes | SOLID principles, design patterns, clean architecture |

### Books (Free)
| Resource | URL |
|----------|-----|
| **Automate the Boring Stuff** (Al Sweigart) | https://automatetheboringstuff.com |
| **Think Python** (Allen Downey) | https://greenteapress.com/wp/think-python-2e/ |
| **Fluent Python — code notebooks** | https://github.com/fluentpython/example-code-2e |

### Tools
| Tool | Install | Use |
|------|---------|-----|
| **ruff** | `pip install ruff` | Linting + formatting (replaces black + flake8) |
| **mypy** | `pip install mypy` | Static type checking |
| **pytest** | `pip install pytest pytest-cov` | Testing |
| **poetry** | `pip install poetry` | Package + dependency management |
| **uv** | `pip install uv` | Ultra-fast pip replacement (Rust-based) |

---

## A2 — PHASE 2: DATA SCIENCE

### Courses & Videos
| Resource | URL | What it covers |
|----------|-----|----------------|
| **Kaggle Learn** | https://www.kaggle.com/learn | Pandas, SQL, visualization, feature engineering, EDA — fully free |
| **StatQuest — YouTube** | https://www.youtube.com/@statquest | Statistics, probability, ML intuition — essential for interviews |
| **Google Data Analytics (audit)** | https://www.coursera.org/professional-certificates/google-data-analytics | EDA, SQL, data cleaning |
| **Plotly/Dash official tutorials** | https://dash.plotly.com/tutorial | Dash apps, Plotly charts |

### Books (Free)
| Resource | URL |
|----------|-----|
| **Python Data Science Handbook** (Jake VanderPlas) | https://jakevdp.github.io/PythonDataScienceHandbook/ |

### Datasets
| Dataset | URL | Use |
|---------|-----|-----|
| **Titanic** | https://www.kaggle.com/c/titanic | CSV basics, missing values, EDA |
| **House Prices** | https://www.kaggle.com/c/house-prices-advanced-regression-techniques | Regression, many features |
| **Ames Housing** | https://www.kaggle.com/datasets/prevek18/ames-housing-dataset | 80 features, EDA practice |
| **Google Play Store Apps** | https://www.kaggle.com/datasets/lava18/google-play-store-apps | Mixed text + numeric, cleaning |
| **Rossmann Store Sales** | https://www.kaggle.com/c/rossmann-store-sales | Time series, retail forecasting |
| **Store Item Demand** | https://www.kaggle.com/c/demand-forecasting-kernels-only | Multiple time series |

---

## A3 — PHASE 3: MACHINE LEARNING

### Courses & Videos
| Resource | URL | What it covers |
|----------|-----|----------------|
| **Stanford CS229 (YouTube)** | https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU | Full ML — regression, SVMs, neural nets, math |
| **Google ML Crash Course** | https://developers.google.com/machine-learning/crash-course | Scikit-learn, feature engineering, neural net basics |
| **Kaggle: Intro + Intermediate ML** | https://www.kaggle.com/learn | XGBoost, cross-validation, pipelines |
| **StatQuest — YouTube** | https://www.youtube.com/@statquest | Random forest, XGBoost, PCA, SHAP — visual |

### Books (Free)
| Resource | URL |
|----------|-----|
| **Hands-On ML notebooks** (Géron) | https://github.com/ageron/handson-ml3 |
| **ML Engineering** (Andriy Burkov) | http://www.mlebook.com/wiki/doku.php |
| **ML Interviews Book** (Chip Huyen) | https://huyenchip.com/ml-interviews-book/ |

### Datasets
| Dataset | URL | Use |
|---------|-----|-----|
| **Credit Card Fraud** | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud | Imbalanced classification |
| **UCI Adult Income** | https://archive.ics.uci.edu/dataset/2/adult | Binary classification |
| **Heart Disease UCI** | https://archive.ics.uci.edu/dataset/45/heart+disease | Medical classification |
| **Porto Seguro Safe Driver** | https://www.kaggle.com/c/porto-seguro-safe-driver-prediction | Imbalanced, XGBoost |
| **Bike Sharing Demand** | https://www.kaggle.com/c/bike-sharing-demand | Regression with time features |

### Tools
| Tool | Install | Notes |
|------|---------|-------|
| **scikit-learn** | `pip install scikit-learn` | Core ML library |
| **xgboost** | `pip install xgboost` | Gradient boosting |
| **lightgbm** | `pip install lightgbm` | Faster boosting for large data |
| **optuna** | `pip install optuna` | Hyperparameter tuning, free |
| **mlflow** | `pip install mlflow` | Experiment tracking — self-hosted, no limits |
| **shap** | `pip install shap` | Model explainability |
| **lime** | `pip install lime` | Local model explanations |

---

## A4 — PHASE 4: DEEP LEARNING + GENAI

### Courses & Videos
| Resource | URL | What it covers |
|----------|-----|----------------|
| **Karpathy — Zero to Hero (YouTube)** | https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ | Backprop from scratch, RNNs, GPT in PyTorch |
| **fast.ai — Practical Deep Learning** | https://course.fast.ai/ | PyTorch, CNNs, NLP, top-down practical |
| **Stanford CS231N — CNNs (YouTube)** | https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv | Convolution, pooling, backprop, attention |
| **Stanford CS224N — NLP + LLMs (YouTube)** | https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6zgCd4CO2iZ4Cr | Embeddings, transformers, LLMs, RLHF |
| **DeepLearning.AI Specialization (audit)** | https://www.coursera.org/specializations/deep-learning | Neural nets, CNNs, RNNs, transformers — Andrew Ng |
| **DeepLearning.AI Short Courses (free)** | https://www.deeplearning.ai/short-courses/ | RAG, LangChain, agents, LangGraph — 1-2 hrs each |
| **CS50AI — Harvard** | https://cs50.harvard.edu/ai/ | AI foundations, search, NLP, neural nets |
| **LangChain Academy — LangGraph** | https://academy.langchain.com/courses/intro-to-langgraph | LangGraph, agents, memory, multi-agent |
| **Anthropic MCP Docs** | https://modelcontextprotocol.io/introduction | MCP protocol, building servers/clients |

### Books (Free)
| Resource | URL |
|----------|-----|
| **Deep Learning** (Goodfellow) | https://www.deeplearningbook.org |
| **Dive into Deep Learning (d2l.ai)** | https://d2l.ai |
| **Speech & Language Processing** (Jurafsky & Martin) | https://web.stanford.edu/~jurafsky/slpdraft/ |
| **LLM Engineer's Handbook notebooks** | https://github.com/PacktPublishing/LLM-Engineers-Handbook |
| **LLM Patterns** (Eugene Yan blog) | https://eugeneyan.com/writing/llm-patterns/ |

### Datasets
| Dataset | URL | Use |
|---------|-----|-----|
| **MNIST** | http://yann.lecun.com/exdb/mnist/ | CNN intro, digit classification |
| **Fashion-MNIST** | https://github.com/zalandoresearch/fashion-mnist | Better MNIST alternative |
| **CIFAR-10** | https://www.cs.toronto.edu/~kriz/cifar.html | Color image classification |
| **Dogs vs Cats** | https://www.kaggle.com/c/dogs-vs-cats | Transfer learning |
| **IMDB Sentiment** | https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews | Sentiment classification |
| **SQuAD 2.0** | https://rajpurkar.github.io/SQuAD-explorer/ | RAG evaluation, extractive QA |
| **MS MARCO** | https://huggingface.co/datasets/ms_marco | Passage retrieval, RAG |
| **Wikipedia (HuggingFace)** | https://huggingface.co/datasets/wikipedia | RAG document corpus |

### Tools
| Tool | Install | Free? |
|------|---------|-------|
| **torch** (CPU) | `pip install torch torchvision torchaudio` | Yes, unlimited |
| **transformers** | `pip install transformers` | Yes, public models free |
| **langchain** | `pip install langchain langchain-google-genai` | Yes, open source |
| **langgraph** | `pip install langgraph` | Yes, open source |
| **chromadb** | `pip install chromadb` | Yes, self-hosted, no limits |
| **faiss-cpu** | `pip install faiss-cpu` | Yes, Facebook open source |
| **google-generativeai** | `pip install google-generativeai` | Free tier (Flash: 1,500 req/day) |
| **mcp** | `pip install mcp` | Yes, open source |

### Gemini Free Tier (verify at https://ai.google.dev/pricing)
| Model | Req/min | Req/day | Tokens/min |
|-------|---------|---------|-----------|
| Gemini 2.0 Flash | 15 | 1,500 | 1,000,000 |
| Gemini 1.5 Flash | 15 | 1,500 | 1,000,000 |
| Gemini 1.5 Pro | 2 | 50 | 32,000 |

---

## A5 — PHASE 5: PRODUCTION AI SYSTEMS

### Courses & Videos
| Resource | URL | What it covers |
|----------|-----|----------------|
| **FastAPI official tutorial** | https://fastapi.tiangolo.com/tutorial/ | Complete FastAPI to production |
| **Docker official Get Started** | https://docs.docker.com/get-started/ | Containers, images, Compose |
| **DeepLearning.AI MLOps Spec (audit)** | https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops | ML pipelines, monitoring, CI/CD |
| **Microsoft Learn — Azure AI** | https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/ | Cloud ML, Azure ML Studio |

### Tools
| Tool | Install | Free Limits |
|------|---------|------------|
| **fastapi + uvicorn** | `pip install fastapi "uvicorn[standard]"` | Fully free |
| **redis** | `pip install redis` | Self-hosted = free |
| **Docker Desktop** | https://docs.docker.com/get-docker/ | Free for personal use |
| **GitHub Actions** | Built into GitHub | Unlimited for public repos |
| **GCP Cloud Run** | gcloud CLI | 2M requests/month free |

---

## A6 — PHASE 7: INTERVIEW MASTERY

| Resource | URL | What it covers |
|----------|-----|----------------|
| **ML Interviews Book** (Chip Huyen) | https://huyenchip.com/ml-interviews-book/ | 200+ ML interview Q&A — free |
| **CS329S slides** (Stanford) | https://stanford-cs329s.github.io | ML system design |

---

## A7 — FREE COMPUTE

| Platform | GPU | Limit | Best for |
|----------|-----|-------|----------|
| **Google Colab** | T4 | ~12 hrs/session | HuggingFace, GenAI experiments |
| **Kaggle Notebooks** | T4 x2 | 30 hrs/week GPU | ML training, competitions |
| **Oracle Cloud Always Free** | None | 4 CPU + 24 GB RAM permanent | FastAPI hosting, MLflow server |
| **GitHub Codespaces** | None | 60 hrs/month | Dev environment |
| **Render.com** | None | Free (spins down idle) | FastAPI deployment |

---

---

# SECTION B — YOUR PROVIDED RESOURCES

*Resources you shared, organized by topic.*

---

## B1 — ROADMAPS & GUIDES

| Resource | URL | What it is |
|----------|-----|------------|
| **AI Engineer Roadmap (Whimsical)** | https://whimsical.com/coden1/ai-engineer-B5bFoXoFpGB3kMQL8Y3Qzv | Visual AI Engineer roadmap diagram |
| **Agentic AI Labs Roadmap** | https://github.com/AgenticAiLabs/Ai-Engineering-Roadmap | 7-phase open-source curriculum: Programming → Math → ML → DL → LLMs → Agents → Projects |
| **AI Engineering from Scratch** | https://aiengineeringfromscratch.com | 503 lessons, 20 phases — every algorithm built from raw math. Free (MIT). |
| **How to Pivot into AI/ML 2026 (PDF)** | https://drive.google.com/file/d/14aV1wmdaC3woFubcWJic1BINc5J19B6A/view | Career pivot guide for 2026 AI roles |
| **Personal Playbook (Reddit PDF)** | https://drive.google.com/file/d/1luC0rnrET4tDYtS7xe5jUxMDZA-4qNf-/view | Community AI career playbook |

---

## B2 — PYTHON

| Resource | URL | What it covers |
|----------|-----|----------------|
| **JPMorgan Python Training** | https://github.com/jpmorganchase/python-training | Python fundamentals, numerical computing, data viz — real finance data, beginner friendly |
| **CampusX — 100 Days of Python** | https://youtube.com/playlist?list=PLKnIA16_Rmvb1RYR-iTA_hzckhdONtSW4 | Full Python from scratch, 100 videos |

---

## B3 — MATH FOUNDATIONS

| Resource | URL | What it covers |
|----------|-----|----------------|
| **Harvard Intro to Probability** | https://pll.harvard.edu/course/introduction-probability | Probability, distributions, conditional probability — free audit |
| **3Blue1Brown — Linear Algebra** | https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab | Visual linear algebra — best free intuition resource |
| **Khan Academy — Calculus** | https://www.khanacademy.org/math/calculus-1 | Calculus 1 — derivatives, integrals (needed for backprop) |

---

## B4 — MACHINE LEARNING

| Resource | URL | What it covers |
|----------|-----|----------------|
| **CampusX — 100 Days of ML** | https://youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH | Full ML curriculum, 100 videos |
| **ML From Scratch (GitHub)** | https://github.com/eriklindernoren/ML-From-Scratch | Every ML algorithm in NumPy — no frameworks. Regression → GANs → DQN |
| **ML Playlist — Sentdex** | https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v | Practical ML in Python |
| **500 AI/ML/DL/CV/NLP Projects** | https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code | Meta-repo of 500+ projects with code — use as inspiration |

---

## B5 — DEEP LEARNING & GENAI

| Resource | URL | What it covers |
|----------|-----|----------------|
| **CampusX — 100 Days of DL** | https://youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn | Full deep learning curriculum, 100 videos |
| **LLM Explained (YouTube)** | https://www.youtube.com/watch?v=Q86qzJ1K1Ss | LLM internals explained |
| **LLM Ops (YouTube)** | https://www.youtube.com/watch?v=1jvxxa7tdjw | Deploying and monitoring LLMs |
| **CampusX — GenAI with LangChain** | https://youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0 | GenAI using LangChain end-to-end |

---

## B6 — AGENTS & LANGGRAPH

| Resource | URL | What it covers |
|----------|-----|----------------|
| **LangGraph Full Course (YouTube)** | https://www.youtube.com/watch?v=5h-JBkySK34&list=PLfaIDFEXuae16n2TWUkKq5PgJ0w6Pkwtg | LangGraph deep dive playlist |
| **CampusX — Agentic AI with LangGraph** | https://youtube.com/playlist?list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL | Agentic AI using LangGraph |
| **CampusX — MCP** | https://youtube.com/playlist?list=PLKnIA16_Rmva_oZ9F4ayUu9qcWgF7Fyc0 | Full MCP course |
| **Agent Evaluation (YouTube)** | https://www.youtube.com/watch?v=WZZLtwnZ4w0 | How to evaluate AI agents |
| **Agent Swarms (agentswarms.fyi)** | https://agentswarms.fyi | 50+ runnable agents — ReAct, Reflexion, Graph RAG. Free in beta. Interactive broken-agent debugging labs. |
| **500 AI Agents Projects** | https://github.com/ashishpatel26/500-AI-Agents-Projects | 500+ real agent projects — CrewAI, AutoGen, LangGraph, LlamaIndex |

---

## B7 — PRODUCTION & FASTAPI

| Resource | URL | What it covers |
|----------|-----|----------------|
| **CampusX — FastAPI for ML** | https://youtube.com/playlist?list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ | FastAPI specifically for ML deployments |

---

## B8 — CLAUDE & ANTHROPIC

| Resource | URL | What it covers |
|----------|-----|----------------|
| **Anthropic Academy** | https://anthropic.skilljar.com/ | 20+ free courses: Claude API, MCP, agents, Claude Code, AWS Bedrock, Vertex AI |
| **Anthropic Cookbook (GitHub)** | https://github.com/anthropics/anthropic-cookbook | Code examples: RAG, tool use, agents, sub-agents, PDF, prompt caching, evals — 46k stars |
| **Claude Code Playlist** | https://www.youtube.com/playlist?list=PL4cUxeGkcC9g4YJeBqChhFJwKQ9TRiivY | Claude Code workflows for developers |
| **Agent Skills (YouTube)** | https://www.youtube.com/watch?v=CEvIs9y1uog | Building agent skills with Claude |
| **Claude Certified Architect Exam** | https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request | Free Anthropic certification — add to resume |

---

---

# SECTION C — COMPARISON & RECOMMENDATION

*Where Claude's list and your list overlap, differ, and which to use for each phase.*

---

## C1 — OVERLAP (Both lists have it)

| Topic | Claude Found | You Provided | Verdict |
|-------|-------------|--------------|---------|
| ML courses | Stanford CS229, Google ML Crash Course | CampusX 100 Days of ML, Sentdex | Use both — CS229 for depth, CampusX for pace |
| LangGraph | LangChain Academy | CampusX LangGraph + YouTube playlist | Your list is better here — more options |
| MCP | Anthropic MCP docs | CampusX MCP playlist + Anthropic Academy | Your list wins — CampusX has a full dedicated course |
| Agent projects | — | 500 AI Agents repo | Unique to your list — excellent |
| FastAPI | Official FastAPI docs | CampusX FastAPI for ML | Use both — official docs for reference, CampusX for ML-specific context |

---

## C2 — ONLY IN CLAUDE'S LIST (gaps in your list)

| Resource | Why it matters |
|----------|----------------|
| **Karpathy — Zero to Hero** | Best free DL content — builds GPT from scratch. Must use for Phase 4. |
| **fast.ai** | Top-down PyTorch, great for CNNs. Complements CampusX DL. |
| **Stanford CS231N, CS224N** | Rigorous academic depth for interviews — system design questions often draw from these |
| **DeepLearning.AI Short Courses** | Free 1-2 hr focused courses on RAG, agents, LangChain — fastest way to cover GenAI topics |
| **Goodfellow Deep Learning book** | Free online — theory reference for interview questions |
| **d2l.ai** | Best free book combining PyTorch code + theory for transformers |
| **Jurafsky & Martin NLP book** | NLP bible — free draft, essential for LLM interview questions |
| **Kaggle Learn** | Fastest hands-on practice — no setup required |
| **StatQuest** | Best channel for statistics + ML intuition, interview-critical |
| **ML Interviews Book (Chip Huyen)** | 200+ interview questions with answers — free online |
| **Hands-On ML notebooks (Géron)** | Free GitHub code for one of the best ML books |
| **Free datasets** (Kaggle, UCI, HuggingFace) | 40+ curated datasets mapped to each phase |
| **Free compute guide** | Kaggle GPU (30 hrs/week) vs Colab vs Oracle free tier |

---

## C3 — ONLY IN YOUR LIST (gaps in Claude's list)

| Resource | Why it matters |
|----------|----------------|
| **JPMorgan Python Training** | Real-world finance data + Jupyter notebooks — good for Python + data viz basics |
| **ML From Scratch (GitHub)** | Implements every algorithm in NumPy — excellent for interview prep (understand internals) |
| **AI Engineering from Scratch** | 503 lessons, builds from raw math — very deep if you want fundamentals |
| **Agentic AI Labs Roadmap** | Good structured alternative roadmap to compare with your plan |
| **3Blue1Brown — Linear Algebra** | Best visual linear algebra — essential math for understanding ML |
| **Khan Academy — Calculus** | Free calculus — needed for understanding backprop |
| **Harvard Intro to Probability** | Best free probability course — important for ML interviews |
| **CampusX (all playlists)** | 6 dedicated playlists: Python → ML → DL → GenAI → LangGraph → MCP → FastAPI. One channel covering the entire plan. |
| **Agent Swarms (agentswarms.fyi)** | Interactive broken-agent labs — unique hands-on debugging practice |
| **500 AI Agents Projects** | 500+ agent projects with code — best reference library for Phase 4 |
| **Anthropic Academy + Cookbook** | Official Claude/MCP courses and code examples — directly relevant to your Phase 4 MCP project |
| **Claude Certified Architect Exam** | Free Anthropic cert — good resume addition |
| **Career PDFs** (2026 pivot guide + playbook) | Practical career guidance specific to 2026 AI job market |

---

## C4 — FINAL RECOMMENDATION: WHICH TO USE PER PHASE

| Phase | Primary (use this) | Supplement (add this) |
|-------|-------------------|----------------------|
| **Phase 1 — Python** | CampusX 100 Days of Python | ArjanCodes (design patterns), CS50P (clean code) |
| **Math** | 3Blue1Brown Linear Algebra + Khan Calculus | Harvard Probability |
| **Phase 2 — Data Science** | Kaggle Learn (hands-on) | Python DS Handbook (reference) |
| **Phase 3 — ML** | CampusX 100 Days of ML | Stanford CS229 (depth), ML From Scratch (internals) |
| **Phase 4 — Deep Learning** | CampusX 100 Days of DL | Karpathy Zero to Hero (must watch), fast.ai |
| **Phase 4 — GenAI/RAG** | DeepLearning.AI Short Courses | CampusX LangChain, Anthropic Cookbook |
| **Phase 4 — Agents** | CampusX LangGraph + Agent Swarms | 500 AI Agents repo |
| **Phase 4 — MCP** | CampusX MCP playlist | Anthropic Academy + MCP Docs |
| **Phase 5 — Production** | CampusX FastAPI for ML | FastAPI official docs + Docker official docs |
| **Phase 5 — MLOps** | DeepLearning.AI MLOps Specialization | ML Engineering book (Burkov) |
| **Phase 7 — Interview** | ML Interviews Book (Chip Huyen) | CS229 + CS231N for system design |

---

## C5 — OVERALL VERDICT

| Dimension | Claude's List | Your List | Winner |
|-----------|--------------|-----------|--------|
| Academic depth | Stanford CS229, CS224N, CS231N | CampusX series | **Claude** |
| Practical hands-on | Kaggle Learn, fast.ai | CampusX, Agent Swarms | **Tie** |
| Agent/MCP specific | Anthropic MCP docs | CampusX MCP, Anthropic Academy, 500 Agents | **Your list** |
| Math foundations | — | 3Blue1Brown, Khan, Harvard | **Your list** |
| Free books | 8 free books mapped per phase | ML From Scratch code | **Claude** |
| Free datasets | 40+ datasets mapped per phase | — | **Claude** |
| Career guidance | — | 2026 pivot guide, playbook, cert | **Your list** |
| Tools & install cmds | Full install guide per phase | — | **Claude** |
| Free compute | Kaggle/Colab/Oracle guide | — | **Claude** |

**Bottom line:** Use both lists together. Claude's list fills the academic depth, datasets, books, and tools gaps. Your list fills the agents/MCP, math foundations, career guidance, and CampusX structured playlists gaps. Together they cover everything in the 150-day plan with zero paid resources needed.

---

---

# QUICK INSTALL — All phases

```bash
# Phase 1 — Python tooling
pip install ruff black mypy pytest pytest-cov poetry uv

# Phase 2 — Data Science
pip install numpy pandas polars plotly dash matplotlib seaborn jupyterlab

# Phase 3 — Machine Learning
pip install scikit-learn xgboost lightgbm optuna mlflow shap lime

# Phase 4 — Deep Learning + GenAI (CPU)
pip install torch torchvision torchaudio
pip install transformers datasets accelerate huggingface_hub
pip install langchain langchain-google-genai langgraph
pip install chromadb faiss-cpu
pip install google-generativeai mcp

# Phase 5 — Production
pip install fastapi "uvicorn[standard]" redis
# Docker: https://docs.docker.com/get-docker/

# Start MLflow dashboard
mlflow ui   # http://localhost:5000
```

---

## NOTE ON COURSERA AUDIT (access lectures for free)
1. Open any Coursera course → click **"Enroll for Free"**
2. In the popup → choose **"Audit"** at the bottom
3. You get all video lectures and readings — no certificate, no cost
4. Works for: Stanford CS229, DeepLearning.AI Specialization, Google Data Analytics, MLOps Specialization
