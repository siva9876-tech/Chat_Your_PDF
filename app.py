import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))




def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    vector_store = Chroma.from_texts(
        texts=text_chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_store
    

def get_conversational_chain(vector_store):
    prompt_template = """
    Answer the question accurately using only the provided context.

    If the answer is not available in the context, respond exactly:
    Answer is not available in the context.

    Context:
    {context}

    Question:
    {input}

    Answer:
    """

    model = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template(prompt_template)

    document_chain = create_stuff_documents_chain(
        llm=model,
        prompt=prompt
    )

    retrieval_chain = create_retrieval_chain(
        vector_store.as_retriever(search_kwargs={"k": 3}),
        document_chain
    )

    return retrieval_chain


def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    chain = get_conversational_chain(vector_store)

    response = chain.invoke({
        "input": user_question
    })

    answer = response.get(
        "answer",
        "Answer is not available in the context."
    )

    st.write("Reply:", answer)




def main():
    st.set_page_config(page_title="Chat PDF")
    st.header("Chat with PDF using Gemini 💁")

    user_question = st.text_input(
        "Ask a Question from the PDF Files"
    )

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")

        pdf_docs = st.file_uploader(
            "Upload your PDF files and click Submit & Process",
            accept_multiple_files=True,
            type=["pdf"]
        )

        if st.button("Submit & Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF file.")
                return

            with st.spinner("Processing PDFs..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)

                if text_chunks:
                    get_vector_store(text_chunks)
                    st.success("PDFs processed successfully!")
                else:
                    st.warning("No text could be extracted from the PDFs.")
if __name__ == "__main__":
    main() 