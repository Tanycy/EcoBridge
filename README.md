# 🌱 EcoBridge
### Energy-Efficient AI Routing Platform

EcoBridge is an intelligent AI routing platform that automatically classifies user prompts and routes them to the most appropriate Large Language Model (LLM). By directing simple requests to lightweight models and complex requests to more capable models, EcoBridge helps reduce API costs and improve computational efficiency while maintaining response quality.

---

## 📌 Project Overview

Most AI applications send every user request to the same language model regardless of task complexity. This results in unnecessary computational resource usage, higher API costs, and longer response times.

EcoBridge introduces an intelligent routing layer that:

- Classifies prompts into **Simple** or **Complex**
- Routes simple prompts to **GPT-4o Mini**
- Routes complex prompts to **GPT-4o**
- Estimates API cost
- Calculates relative energy score
- Tracks usage analytics through an interactive dashboard

---

# ✨ Features

- 🤖 Intelligent Prompt Classification
- 🔀 Automatic AI Model Routing
- ⚡ Relative Energy Score Estimation
- 💰 API Cost Estimation
- 📊 Interactive Analytics Dashboard
- 💬 Gradio Chat Interface
- 🚀 FastAPI REST API
- 💾 SQLite Request Logging

---

# 🏗 System Architecture

```
                    User
                     │
                     ▼
              Gradio Chat UI
                     │
                     ▼
               FastAPI Backend
                     │
                     ▼
            Prompt Classifier
                     │
          ┌──────────┴──────────┐
          │                     │
      Simple                Complex
          │                     │
          ▼                     ▼
     GPT-4o Mini            GPT-4o
          │                     │
          └──────────┬──────────┘
                     │
                     ▼
        Energy & Cost Calculator
                     │
                     ▼
             SQLite Database
                     │
                     ▼
          Streamlit Dashboard
```

---

# 🧠 Prompt Classification

EcoBridge uses a lightweight rule-based classifier.

A prompt is evaluated using:

- Prompt length
- Technical keywords
- Code detection
- Mathematical expressions
- Multiple questions
- Word count

If the complexity score is:

```
Score < 2
```

➡ Route to **GPT-4o Mini**

If

```
Score ≥ 2
```

➡ Route to **GPT-4o**

---

# 🤖 AI Models

| Task Type | Model |
|------------|-------|
| Simple | GPT-4o Mini |
| Complex | GPT-4o |

Examples

Simple

- What is Docker?
- Translate this sentence.
- Explain HTTP.

Complex

- Compare Docker and Kubernetes.
- Design a microservice architecture.
- Write a Python function.
- Research cloud security.

---

# ⚡ Energy Estimation

EcoBridge does not measure actual electricity usage.

Instead, it estimates the relative computational intensity of each request using model weights.

| Model | Relative Energy Score |
|--------|----------------------:|
| GPT-4o Mini | 1 |
| GPT-4o | 8 |

These scores allow EcoBridge to compare routing decisions and estimate computational savings.

---

# 💰 Cost Estimation

Estimated API cost is calculated using the official model pricing.

Formula

```
Estimated Cost

=

(Tokens / 1000)

×

Model Price
```

EcoBridge records:

- Estimated Tokens
- Estimated API Cost
- Estimated Cost Saved

---

# 📊 Dashboard

The Streamlit dashboard provides:

- Total Requests
- Model Usage
- Prompt Classification
- Average Energy Score
- Estimated API Cost
- Estimated Cost Savings
- Response Time
- Request History

---

# 📂 Project Structure

```
EcoBridge
│
├── app
│   ├── classifier.py
│   ├── config.py
│   ├── dashboard.py
│   ├── database.py
│   ├── energy.py
│   ├── llm.py
│   ├── main.py
│   ├── models.py
│   └── router.py
│
├── tests
│
├── gradio_app.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/EcoBridge.git

cd EcoBridge
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶ Run FastAPI

```bash
uvicorn app.main:app --reload
```

FastAPI

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 💬 Run Gradio

```bash
python gradio_app.py
```

---

# 📈 Run Dashboard

```bash
streamlit run app/dashboard.py
```

---

# 🛠 Technology Stack

### Backend

- FastAPI
- LiteLLM

### AI

- OpenAI GPT-4o
- OpenAI GPT-4o Mini

### Frontend

- Gradio
- Streamlit

### Database

- SQLite

### Visualization

- Plotly

### Language

- Python 3.11+

---

# 🎯 Target Users

- Students
- Universities
- SMEs
- AI Developers
- Researchers
- Enterprise IT Teams

---

# 🔮 Future Improvements

- Support Gemini
- Support Claude
- Support DeepSeek
- Machine Learning Prompt Classifier
- Live API Pricing
- Real Token Usage Tracking
- Carbon Emission Estimation
- User Preference Routing

---

# 👨‍💻 Team

**EcoBridge**

Bachelor of Information Technology (Hons)

Universiti Teknologi PETRONAS

