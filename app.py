# app.py
import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain import hub
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# MODEL = "llama3.2:1b"
MODEL = "llama3.2:1b"

# Set up a session for optimized HTTP requests
session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount("http://", HTTPAdapter(max_retries=retries))

# Loading the vectorstore
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OllamaEmbeddings(model=MODEL))

# Loading the Llama3 model
llm = Ollama(model=MODEL)

# Using the vectorstore as the retriever
retriever = vectorstore.as_retriever()

# Formatting the docs
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Loading the QA chain from langchain hub
rag_prompt = hub.pull("rlm/rag-prompt")

# Creating the QA chain
qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

# API call to the Llama model via Ollama
def query_llama(prompt):
    try:
        answer = qa_chain.invoke(prompt)
        return answer
    except Exception as e:
        st.error(f"Error: {e}")
        return "There was an error processing your request."

# Streamlit app UI
st.title("Llama 3.2 1B Smallest LLM Model Chat")

# Streamlined input and response display
user_input = st.text_input("Ask something:")
if st.button("Send") and user_input:
    with st.spinner("Generating response..."):
        answer = query_llama(user_input)
        st.write(answer)
