import os

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

#setupllm(using local pipeline)
HUGGINGFACE_REPO_ID="google/flan-t5-base"

def load_llm(huggingface_repo_id):
    hf_pipeline = pipeline(
        "text2text-generation",
        model=huggingface_repo_id,
        max_new_tokens=512,
        temperature=0.5
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    return llm

#connect llm with faiss and create chain

CUSTOM_PROMPT_TEMPLATE = """
You are a medical assistant.

Answer ONLY from the provided medical context.

If the answer is not available in the context, say:
"I could not find the answer in the medical documents."

Do not make up information.

Context:
{context}

Question:
{question}

Provide a concise answer.
"""
def set_custom_prompt(custom_prompt_template):
    prompt=PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

# Load Database
DB_FAISS_PATH="vectorstore/db_faiss"
embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db=FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)

# Create QA chain
qa_chain=RetrievalQA.from_chain_type(
    llm=load_llm(HUGGINGFACE_REPO_ID),
    chain_type="stuff",
    retriever=db.as_retriever(
        search_type="similarity",
        search_kwargs={"k":2}
    ),
    return_source_documents=True,
    chain_type_kwargs={'prompt':set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
)

# Now invoke with a single query
user_query=input("Write Query Here: ")
response=qa_chain.invoke({'query': user_query})
print("RESULT: ", response["result"])
print("SOURCE DOCUMENTS: ", response["source_documents"])