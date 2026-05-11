import os

from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts import CUSTOM_PROMPT_TEMPLATE


def set_custom_prompt():

    prompt = PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    return prompt


def create_qa_chain(vectorstore):

    qa_chain = RetrievalQA.from_chain_type(

        llm=ChatGroq(
            model_name="llama-3.1-8b-instant",
            temperature=0,
            groq_api_key=os.environ["GROQ_API_KEY"]
        ),

        chain_type="stuff",

        retriever=vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 2}
        ),

        return_source_documents=True,

        chain_type_kwargs={
            'prompt': set_custom_prompt()
        }
    )

    return qa_chain