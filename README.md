🏥 MediBot AI
Multilingual Medical Assistant using RAG & LLMs

An intelligent, voice-enabled, multilingual medical chatbot that uses Retrieval-Augmented Generation (RAG) to deliver accurate, source-cited answers from medical documents — in both Telugu and English.

📖 Project Overview
MediBot AI is a production-ready AI application designed to make medical knowledge accessible to everyone — regardless of language or technical ability. Built for healthcare professionals, students, and patients, MediBot AI allows users to upload medical PDFs, ask questions in natural language (or by voice), and receive grounded, accurate answers with source citations.
Unlike generic AI chatbots, MediBot AI uses Retrieval-Augmented Generation (RAG) to ground every response in the actual content of your medical documents — eliminating hallucinations and ensuring trustworthiness.

🎯 Mission: Bridge the language and technology gap in healthcare by providing an intelligent, multilingual, voice-enabled medical assistant.


✨ Features
FeatureDescription🤖 RAG-Powered ChatbotAnswers grounded in your medical documents, not generic AI knowledge
📄 PDF Upload & Q&AUpload any medical PDF and query it instantly
🎙️ Voice Input (Whisper)Speak your question — OpenAI Whisper transcribes it in real-time
🌐 Multilingual SupportFull Telugu + English interface and responses
🗄️ FAISS Vector DatabaseLightning-fast semantic search over document embeddings
📎 Source Document ViewerSee exactly which passages answered your question
🎨 Futuristic UICustom CSS with a sleek, modern medical-grade design
☁️ Cloud DeployedLive on Streamlit Cloud — zero setup required

🛠️ Tech Stack
┌─────────────────────────────────────────────────────────────────┐
│  FRONTEND          │  AI / LLM          │  RAG PIPELINE         │
│  ─────────────     │  ──────────        │  ────────────         │
│  Streamlit         │  Groq LLaMA 3      │  LangChain            │
│  Custom CSS        │  HuggingFace       │  FAISS Vector DB      │
│  Futuristic Theme  │  Embeddings        │  PyPDF Loader         │
│                    │                    │  RecursiveTextSplitter│
├─────────────────────────────────────────────────────────────────┤
│  VOICE & NLP       │  DEPLOYMENT        │  LANGUAGE             │
│  ───────────       │  ──────────        │  ────────             │
│  OpenAI Whisper    │  Streamlit Cloud   │  Python 3.10+         │
│  Multilingual NLP  │  GitHub            │  Telugu + English     │
└─────────────────────────────────────────────────────────────────┘

🏗️ Architecture
                        ┌─────────────────────────────────────┐
                        │         PDF INGESTION PIPELINE       │
                        │  PDF → Text Chunks → Embeddings      │
                        │  (HuggingFace) → FAISS Vector Store  │
                        └──────────────┬──────────────────────┘
                                       │
                                       ▼
┌─────────────┐    ┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────────────┐
│  User Input │    │ Whisper ASR │    │    FAISS     │    │  Groq LLM   │    │  Response +     │
│ (Text/Voice)│───▶│ Transcribe  │───▶│  Retrieval  │───▶│  Generation │───▶│  Source Docs    │
│             │    │ (if Voice)  │    │  Top-K Docs  │    │  (LLaMA 3)  │    │  Cited Answer   │
└─────────────┘    └─────────────┘    └──────────────┘    └──────────────┘    └─────────────────┘

        ▲                                                                              │
        │                              LangChain RetrievalQA Chain                    │
        └──────────────────────────────────────────────────────────────────────────────┘
Flow:

User uploads a medical PDF → parsed, chunked, and embedded
Embeddings stored in FAISS for semantic search
User submits query (text or voice via Whisper)
FAISS retrieves top-K relevant document chunks
Groq LLM generates a grounded answer using retrieved context
Answer + source document excerpts displayed to user


🚀 Installation
Prerequisites

Python 3.10+
ffmpeg installed (for Whisper voice input)
A Groq API Key

1. Clone the Repository
bashgit clone https://github.com/yourusername/medibot-ai.git
cd medibot-ai
2. Create a Virtual Environment
bashpython -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bashpip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the project root:
envGROQ_API_KEY=your_groq_api_key_here
5. Run the Application
bashstreamlit run medibot.py
Open your browser at http://localhost:8501 🎉

📋 Usage
Option 1 — Chat with Preloaded Medical Knowledge

Open the app
Type your medical question in English or Telugu
Get a grounded answer with source citations

Option 2 — Upload Your Own Medical PDF

Click "Upload Medical Document" in the sidebar
Upload any .pdf (medical reports, research papers, drug guides)
Ask questions specific to your document

Option 3 — Voice Query

Click the 🎙️ microphone button
Speak your question in English or Telugu
Whisper transcribes → RAG answers


📁 Project Structure
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

🔧 Configuration
ParameterDefaultDescriptionCHUNK_SIZE500Text chunk size for splittingCHUNK_OVERLAP50Overlap between chunksTOP_K_DOCS4Number of retrieved docs per queryLLM_MODELllama3-8b-8192Groq model to useEMBEDDING_MODELsentence-transformers/all-MiniLM-L6-v2HuggingFace embedding model

🌟 Live Demo
Try it live: https://medibot-ai-2311.streamlit.app


🔮 Future Enhancements

 🌍 More Languages — Hindi, Tamil, Kannada, Malayalam with auto-detection
 🧬 Symptom Checker — AI-driven triage with differential diagnosis
 📊 Health Analytics Dashboard — Personalized health trend visualization
 🔐 HIPAA Compliance Module — Enterprise-grade data security
 📱 Mobile App — Native iOS & Android with offline support
 🤝 Doctor Connect — Seamless telemedicine integration
 🗣️ Text-to-Speech — Read answers aloud in Telugu/English
 🏥 Hospital API Integration — Connect with EHR systems

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.
