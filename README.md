# 🧠 Multi-Agent AI Business Intelligence System (RAG-Powered)

An advanced **AI-powered Business Intelligence & Decision Support System** built using **Multi-Agent Architecture**, **RAG (Retrieval-Augmented Generation)**, and modern LLM frameworks.

This project transforms raw data into **actionable insights, dashboards, and strategic recommendations** using collaborative AI agents.

---

## 🚀 Overview

Instead of relying on a single AI model, this system simulates a real-world analytics team composed of specialized AI agents that work together to:

- Retrieve relevant knowledge from documents
- Analyze structured and unstructured data
- Summarize complex reports
- Generate business recommendations
- Coordinate the entire workflow

---

## 🧠 System Architecture

The system is built around a **Multi-Agent Framework**:

- 🔎 **Retriever Agent** → Fetches relevant information from documents & vector database  
- 📊 **Analyst Agent** → Detects trends, patterns, and insights from data  
- 📝 **Summarizer Agent** → Converts long reports into concise summaries  
- 💡 **Recommender Agent** → Produces strategic, data-driven business decisions  
- 🎛️ **Supervisor Agent** → Orchestrates and manages all agent interactions  

---

## ⚡ Key Features

- 🔗 RAG pipeline with vector database integration  
- 🧠 Short-term + long-term semantic memory system  
- 📊 Automatic dashboard generation from CSV/Excel uploads  
- 📈 Interactive visualizations using Plotly  
- 💬 Chat-based AI interface (Streamlit UI)  
- 🌍 Full support for Arabic & English  
- 📁 Upload support for PDF, CSV, and Excel files  
- ⚡ High-speed inference using Groq + LLaMA 3.3 70B  

---

## 🛠️ Tech Stack

- LangGraph (Multi-Agent Orchestration)
- LangChain
- Chroma Vector Database
- Streamlit
- Groq API (LLaMA 3.3 70B)
- Plotly
- Python

---

## 📁 Project Structure (Example)
project/
│
├── app/
│ ├── agents/
│ ├── memory/
│ ├── tools/
│ ├── ui/
│ └── main.py
│
├── data/
├── vectorstore/
├── requirements.txt
