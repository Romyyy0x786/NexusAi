# 🤖 NEXUS-AI: Autonomous Multi-Agent Decision System

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Groq LPU](https://img.shields.io/badge/Inference-Groq_LPU-orange.svg)](https://groq.com/)
[![Framework](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://python.langchain.com/)

NEXUS-AI is a high-performance **Multi-Agent Orchestration System** designed to solve complex, multi-step problems through decentralized reasoning.

Unlike standard LLM chat systems, NEXUS-AI simulates a **professional team environment** where specialized AI agents collaborate, audit, and autonomously refine solutions.

---

## 🚀 Key Features

- **Collaborative Multi-Agent Flow**  
  Planner, Reasoning, and Critic agents work together autonomously.

- **Autonomous Self-Correction**  
  A Critic agent audits outputs and triggers replanning if flaws are detected.

- **Explainable AI (XAI)**  
  Transparent decision tracing through an Explainability Layer.

- **Ultra-Low Latency**  
  Optimized for **Groq LPU hardware** enabling near-instant inference.

---

## 🛠️ Technology Stack

- **Core Model:** Llama 3.3 70B  
- **Agent Framework:** LangChain  
- **Frontend:** Streamlit + Custom CSS  
- **API Provider:** Groq Cloud (LPU Acceleration)  
- **Language:** Python 3.10+

---

## 📊 System Workflow

```mermaid
graph TD
    A[User Problem] --> B[Planner Agent]
    B -->|Strategic Plan| C[Reasoning Agent]
    C -->|Proposed Solution| D[Critic Agent]

    D -->|Flaws Found| E[Self-Correction Loop]
    E -->|Refinement Feedback| C

    D -->|Approved| F[Final Validated Output]
    F --> G[Explainability Layer]
    G -->|Decision Trace| A

    style E fill:#f96,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px

---

## Setup & Installation
