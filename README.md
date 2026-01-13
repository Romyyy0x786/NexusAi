# 🤖 NEXUS-AI: Autonomous Multi-Agent Decision System

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Groq LPU](https://img.shields.io/badge/Inference-Groq_LPU-orange.svg)](https://groq.com/)
[![Framework](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://python.langchain.com/)

NEXUS-AI is a high-performance **Multi-Agent Orchestration System** designed to solve complex, multi-step problems through decentralized reasoning. Unlike standard LLM chats, NEXUS-AI simulates a professional team environment where specialized agents collaborate, audit, and refine outputs autonomously.

## 🚀 Key Features
- **Collaborative Multi-Agent Flow:** Includes specialized agents for Planning, Reasoning, and Quality Control.
- **Autonomous Self-Correction:** A Critic agent audits the solution and triggers a re-planning loop if flaws are detected.
- **Explainable AI (XAI):** A "Deep Explain" feature that traces the neural decision path for the user.
- **Ultra-Low Latency:** Optimized for Groq's LPU (Language Processing Unit) for near-instant agent communication.

 

## 🛠️ Technology Stack
- **Core Engine:** Llama 3.3 70B (State-of-the-art Reasoning Model)
- **Agent Framework:** LangChain (Prompt Engineering & Chaining)
- **UI/UX:** Streamlit with Custom CSS (Futuristic Dark Theme)
- **API Provider:** Groq Cloud (LPU Hardware Acceleration)

## 📦 Setup & Installation
1. **Clone Repo:** `git clone https://github.com/YOUR_USERNAME/NEXUS-AI.git`
2. **Install:** `pip install -r requirements.txt`
3. **API Key:** Create a `.env` file and add `GROQ_API_KEY=your_key_here`
4. **Run:** `python -m streamlit run interface.py`


   graph TD
    A[User Problem] --> B[Planner Agent]
    B -- Strategic Plan --> C[Reasoning Agent]
    C -- Proposed Solution --> D[Critic Agent]
    
    D -- "If Flaws Found (Red Path)" --> E[Self-Correction Loop]
    E -- Feedback/Refinement --> C
    
    D -- "If Approved (Green Path)" --> F[Final Validated Output]
    F --> G[Explainability Layer]
    G -- Decision Trace --> A


