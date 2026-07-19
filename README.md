# 🚀 AskGenAI AI Research Digest Service

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Vercel](https://img.shields.io/badge/Deployment-Vercel-black)
![License](https://img.shields.io/badge/License-Apache%202.0-orange)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

> An AI research aggregation service that collects the latest and trending Artificial Intelligence papers from multiple sources and exposes them through a unified API.

🌐 **Live Website:** https://askgenai.in  
⚡ **API Service:** https://ai-news-service.vercel.app

---

# 📌 Overview

AskGenAI Research Digest Service is a lightweight and extensible AI content aggregation platform built using **FastAPI**.

The goal is simple:

> Provide AI engineers, researchers, and enthusiasts a single place to discover the latest AI research papers.

The service collects information from multiple AI knowledge sources through a pluggable adapter architecture.

Currently supported sources:

- 📚 arXiv AI Research Papers
- 🤗 Hugging Face Trending Papers


Future integrations:

- AWS AI Blogs
- Microsoft AI Research
- Meta AI Engineering
- Google DeepMind
- OpenAI Research
- GitHub Trending AI Projects
- NVIDIA Research

---

# 🏗️ Architecture


```
                    WordPress
                       |
                       |
                       |
              AskGenAI Research Digest
                       |
                       |
                  FastAPI Service
                       |
        +--------------+--------------+
        |                             |
        |                             |
   arXiv Adapter              Hugging Face Adapter
        |                             |
        |                             |
     RSS Feed                    HuggingFace API


```


The system follows an adapter-based architecture:

```
External Source
       |
       |
 Adapter
       |
       |
 Article Model
       |
       |
 Research API
```

Adding a new source does not require changing existing integrations.

---

# ✨ Features

## 🔎 Multi Source AI Research Aggregation

Collect AI research content from different platforms.

Current sources:

### 📚 arXiv

Source:

```
https://rss.arxiv.org/rss/cs.AI
```

Provides:

- Research papers
- Authors
- Categories
- Publication dates


---

### 🤗 Hugging Face Papers API

Source:

```
https://huggingface.co/api/daily_papers
```

Provides:

- Trending papers
- Community popularity
- AI summaries
- Keywords
- GitHub references


---

# 🚀 API Endpoints

## Health Check

```
GET /
```

Response:

```json
{
 "message":"AI News Service is running."
}
```

---

## arXiv Articles

```
GET /api/v1/articles?limit=5
```

Example response:

```json
[
 {
   "title":"AI Research Paper",
   "source":"arXiv"
 }
]
```

---

## Hugging Face Papers

```
GET /api/v1/huggingface/articles?limit=5
```

Example response:

```json
[
 {
   "title":"Trending AI Paper",
   "source":"Hugging Face"
 }
]
```

---

## Unified Research Digest API ⭐

Recommended endpoint:

```
GET /api/v1/research?limit=5
```

Response:

```json
{
 "latest":[
   {
    "title":"Latest AI Paper",
    "source":"arXiv"
   }
 ],

 "trending":[
   {
    "title":"Trending AI Paper",
    "source":"Hugging Face"
   }
 ]
}
```

---

# 📂 Project Structure

```
ai-news-service
│
├── app
│   │
│   ├── adapters
│   │   │
│   │   ├── rss
│   │   │   └── arxiv_adapter.py
│   │   │
│   │   └── api
│   │       └── huggingface_adapter.py
│   │
│   ├── models
│   │   └── article.py
│   │
│   ├── routers
│   │   ├── articles.py
│   │   ├── huggingface.py
│   │   └── research.py
│   │
│   ├── services
│   │   └── research_service.py
│   │
│   └── main.py
│
├── requirements.txt
├── vercel.json
├── .env
└── README.md

```

---

# 🛠️ Running Locally

## 1. Clone Repository

```bash
git clone https://github.com/<your-user>/ai-news-service.git

cd ai-news-service
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables


Create:

```
.env
```


Add:

```properties
HF_TOKEN=<your_huggingface_token>
```

The Hugging Face token is required for accessing Hugging Face APIs.

---

## 5. Start Application

Run:

```bash
uvicorn app.main:app --reload
```


Service starts:

```
http://localhost:8000
```


Swagger documentation:

```
http://localhost:8000/docs
```

---

# 🚢 Deployment

## Deploy to Vercel

Install Vercel CLI:

```bash
npm install -g vercel
```

Login:

```bash
vercel login
```

Deploy:

```bash
vercel
```

Production deployment:

```bash
vercel --prod
```

---

## Environment Variables

Configure:

```
HF_TOKEN
```

inside:

```
Vercel Dashboard
      |
      |
Project Settings
      |
      |
Environment Variables
```

---

# ☁️ Deploying to Other Cloud Platforms

The service is a standard FastAPI application.

It can be deployed to:

- AWS Lambda + API Gateway
- AWS ECS
- Google Cloud Run
- Azure Container Apps
- Railway
- Render
- Fly.io
- Docker/Kubernetes


Example:

```
FastAPI Application
        |
        |
Container
        |
        |
Cloud Platform
```

---

# 🔌 WordPress Integration

AskGenAI WordPress plugin consumes:

```
/api/v1/research
```

and renders:

```
📚 Latest AI Research Papers

🔥 Trending AI Papers
```

The WordPress layer does not know about individual sources.

All source management happens inside FastAPI.

---

# 🤝 Contributing

Contributions are welcome!

You can contribute by:

✨ Adding new AI sources

Examples:

- AWS AI Blog Adapter
- Microsoft AI Adapter
- Meta AI Adapter
- GitHub Trending Adapter


✨ Improving ranking algorithms

✨ Adding caching support

✨ Adding AI summarization

✨ Improving frontend experience


## Contribution Steps

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/new-source
```

3. Commit changes

```bash
git commit -m "Add new AI source adapter"
```

4. Push branch

```bash
git push origin feature/new-source
```

5. Open Pull Request

---

# 🗺️ Roadmap


## Phase 1 ✅

- FastAPI foundation
- arXiv integration
- REST APIs


## Phase 2 ✅

- Vercel deployment
- WordPress integration


## Phase 3 ✅

- Hugging Face Papers integration
- Research aggregation API


## Future

- 🧠 AI generated summaries
- 🔥 Personalized AI feeds
- 🗄️ Database persistence
- ⚡ Redis caching
- 🔍 Semantic search
- 🤖 Agent-based research assistant


---

# 📜 License

Licensed under Apache License 2.0.

You are free to use, modify, and distribute this project.

---

# 🙌 Acknowledgements

Built with:

- FastAPI
- Python
- arXiv
- Hugging Face
- WordPress
- Vercel

---

⭐ If you find this project useful, consider starring the repository!
