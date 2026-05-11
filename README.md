# 🏥 MediBot AI
### *Multilingual Medical Assistant using RAG & LLMs*

> **An intelligent, voice-enabled, multilingual medical chatbot** that uses **Retrieval-Augmented Generation (RAG)** to deliver **accurate, source-cited answers** from medical documents — in both **Telugu** and **English**.



## 📖 Project Overview

**MediBot AI** is a **production-ready AI application** designed to make medical knowledge **accessible to everyone** — regardless of language or technical ability. Built for **healthcare professionals, students, and patients**, MediBot AI allows users to:

- Upload **medical PDFs**
- Ask questions in **natural language** (or by **voice**)
- Receive **grounded, accurate answers** with **source citations**

Unlike generic AI chatbots, **MediBot AI uses Retrieval-Augmented Generation (RAG)** to ground every response in the **actual content of your medical documents** — **eliminating hallucinations** and ensuring trustworthiness.

> 🎯 **Mission:** Bridge the **language and technology gap** in healthcare by providing an intelligent, multilingual, voice-enabled medical assistant.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **RAG-Powered Chatbot** | Answers **grounded in your medical documents**, not generic AI knowledge |
| 📄 **PDF Upload & Q&A** | Upload **any medical PDF** and query it instantly |
| 🎙️ **Voice Input (Whisper)** | Speak your question — **OpenAI Whisper** transcribes it in real-time |
| 🌐 **Multilingual Support** | Full **Telugu + English** interface and responses |
| 🗄️ **FAISS Vector Database** | **Lightning-fast semantic search** over document embeddings |
| 📎 **Source Document Viewer** | See **exactly which passages** answered your question |
| 🎨 **Futuristic UI** | Custom CSS with a sleek, **modern medical-grade design** |
| ☁️ **Cloud Deployed** | Live on **Streamlit Cloud** — zero setup required |

---


**Flow:**
1. User uploads a **medical PDF** → parsed, chunked, and embedded
2. **Embeddings stored in FAISS** for semantic search
3. User submits query (**text or voice via Whisper**)
4. **FAISS retrieves top-K** relevant document chunks
5. **Groq LLM** generates a grounded answer using retrieved context
6. **Answer + source document excerpts** displayed to user

---

## 🚀 Installation

### Prerequisites

- **Python 3.10+**
- **`ffmpeg`** installed (for Whisper voice input)
- A **[Groq API Key](https://console.groq.com)**

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medibot-ai.git
cd medibot-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a **`.env`** file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Application

```bash
streamlit run medibot.py
```

Open your browser at **`http://localhost:8501`** 🎉

---

## 📋 Usage

**Option 1 — Chat with Preloaded Medical Knowledge**
1. Open the app
2. Type your **medical question in English or Telugu**
3. Get a **grounded answer with source citations**

**Option 2 — Upload Your Own Medical PDF**
1. Click **"Upload Medical Document"** in the sidebar
2. Upload any **`.pdf`** (medical reports, research papers, drug guides)
3. Ask questions **specific to your document**

**Option 3 — Voice Query**
1. Click the **🎙️ microphone button**
2. **Speak your question** in English or Telugu
3. **Whisper transcribes → RAG answers**

---

## 📁 Project Structure

```
medibot-ai/
│
├── medibot.py              # Main Streamlit application
├── requirements.txt        # Python dependencies
├── styles.css              # Custom futuristic UI styles
├── architecture.png        # System architecture diagram
├── medical-chatbot-ppt.pdf # Project presentation
│
├── screenshots/
│   ├── homepage.png        # UI screenshots
│   ├── chatbot.png
│   └── voice-input.png
│
├── data/
│   └── medical.pdf         # Default medical knowledge base
│
└── vectorstore/            # FAISS index (auto-generated)
```

---


## 🌟 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://medibot-ai-2311.streamlit.app)

> **🚀 Demo live:** [https://medibot-ai-2311.streamlit.app](https://medibot-ai-2311.streamlit.app)

---
