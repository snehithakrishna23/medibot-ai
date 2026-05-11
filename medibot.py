import streamlit as st
import whisper
import tempfile
from dotenv import load_dotenv

from deep_translator import GoogleTranslator
from streamlit_mic_recorder import mic_recorder

from pdf_utils import (
    get_vectorstore,
    create_vectorstore_from_uploaded_pdfs
)

from rag_pipeline import create_qa_chain

load_dotenv()
model = whisper.load_model("base")

st.set_page_config(
    page_title="MediBot",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"  # <--- Add this line
)

# Load external CSS
with open("styles.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )



def main():

    # ── Sidebar ──
    with st.sidebar:
        st.markdown("""
        <div style="display:flex;align-items:center;gap:12px;padding-bottom:20px;border-bottom:1px solid rgba(96,165,250,0.08);margin-bottom:16px">
            <div style="width:42px;height:42px;background:linear-gradient(135deg,#1d4ed8,#4f46e5);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px">🩺</div>
            <span style="font-size:20px;font-weight:600;background:linear-gradient(90deg,#60a5fa,#818cf8);-webkit-background-clip:text;-webkit-text-fill-color:transparent">MediBot</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="font-size:10px;letter-spacing:0.12em;color:#334155;text-transform:uppercase;font-weight:500;margin-bottom:10px">Features</p>
        <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:20px">
            <div style="display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;font-size:13px;color:#64748b">
                <div style="width:5px;height:5px;border-radius:50%;background:linear-gradient(135deg,#22d3ee,#818cf8);flex-shrink:0"></div>Medical Q&A
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;font-size:13px;color:#64748b">
                <div style="width:5px;height:5px;border-radius:50%;background:linear-gradient(135deg,#22d3ee,#818cf8);flex-shrink:0"></div>Voice Assistant
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;font-size:13px;color:#64748b">
                <div style="width:5px;height:5px;border-radius:50%;background:linear-gradient(135deg,#22d3ee,#818cf8);flex-shrink:0"></div>Multiple PDF Upload
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;font-size:13px;color:#64748b">
                <div style="width:5px;height:5px;border-radius:50%;background:linear-gradient(135deg,#22d3ee,#818cf8);flex-shrink:0"></div>Source Viewer
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;font-size:13px;color:#64748b">
                <div style="width:5px;height:5px;border-radius:50%;background:linear-gradient(135deg,#22d3ee,#818cf8);flex-shrink:0"></div>RAG + FAISS Retrieval
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.info(
            "For educational purposes only. Consult a medical professional for real advice."
        )

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        uploaded_files = st.file_uploader(
            "📄 Upload Medical PDF",
            type="pdf",
            accept_multiple_files=True
        )

    # ── Main Header ──
    st.markdown("""
    <div style='margin-bottom:4px'>
        <p style='font-size:11px;letter-spacing:0.14em;color:#334155;text-transform:uppercase;font-weight:500;margin:0 0 6px'>AI Healthcare Assistant</p>
        <h1 style='font-size:34px;font-weight:700;background:linear-gradient(135deg,#e2e8f0 0%,#93c5fd 50%,#818cf8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:0 0 4px;line-height:1.2'>MediBot AI</h1>
        <p style='font-size:14px;color:#475569;margin:0 0 16px'>Your multilingual AI-powered medical companion</p>
    </div>
    """, unsafe_allow_html=True)

     # ── Voice Input ──
    audio = mic_recorder(
        start_prompt="🎙️start", # Just the mic icon!
        stop_prompt="⏹️stop",  # Just the stop icon!
        key="recorder",
        just_once=True,
        use_container_width=False
    )

    # ── Chat memory ──
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # ── Display previous messages ──
    for message in st.session_state.messages:
        st.chat_message(
            message['role'],
            avatar="🧑" if message['role'] == 'user' else "🩺"
        ).markdown(message['content'])

    

    voice_prompt = None

    if audio:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio['bytes'])
            audio_path = f.name
            
        transcript = model.transcribe(audio_path, task="transcribe")
        voice_prompt = transcript["text"]
        st.success(f"🎤 Voice detected: {voice_prompt}")
       
    # ── Text Input ──
    prompt = st.chat_input("Ask your medical question...")

    final_prompt = prompt if prompt else voice_prompt

    if final_prompt:

        st.chat_message("user", avatar="🧑").markdown(final_prompt)
        st.session_state.messages.append({'role': 'user', 'content': final_prompt})

        translated_prompt = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(final_prompt)

        try:
            if uploaded_files:
                vectorstore = create_vectorstore_from_uploaded_pdfs(uploaded_files)
            else:
                vectorstore = get_vectorstore()

            qa_chain = create_qa_chain(vectorstore)

            with st.spinner("Analyzing medical documents..."):
                response = qa_chain.invoke({'query': translated_prompt})

            result = response["result"]
            source_documents = response["source_documents"]

            st.chat_message("assistant", avatar="🩺").markdown(result)

            with st.expander("📄 View Source Documents"):
                for i, doc in enumerate(source_documents):
                    st.markdown(f"#### 📄 Source {i+1}")
                    st.write(doc.page_content)

            st.session_state.messages.append({"role": "assistant", "content": result})

        except Exception as e:
            st.error(f"Error: {str(e)}")
             
   


    st.caption("🩺 MediBot AI | Built with Streamlit, Groq, Whisper & FAISS")


if __name__ == "__main__":
    main()