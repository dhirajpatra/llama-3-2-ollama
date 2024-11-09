# app.py
import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from langchain.memory import ConversationBufferMemory

# Model configuration
MODEL = "llama3.2:1b"
OLLAMA_URL = "http://ollama:11434/api/chat"

# Setting up a session for HTTP requests with retries
session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount("http://", HTTPAdapter(max_retries=retries))

# Initialize LangChain's Conversation Memory
memory = ConversationBufferMemory(memory_key="history")

# API call to Ollama with context from LangChain's memory
def query_llama(prompt):
    # Retrieve conversation history as a list of messages from memory
    history = memory.load_memory_variables({}).get("history", [])
    
    # Format history into messages for Ollama's API
    messages = [{"role": "user", "content": msg} for msg in history] + [{"role": "user", "content": prompt}]
    data = {
        "model": MODEL,
        "temperature": 0.5,
        "max_length": 1500,
        "messages": messages,
        "stream": False
    }
    
    try:
        headers = {"Content-Type": "application/json"}
        response = session.post(OLLAMA_URL, headers=headers, json=data)
        response.raise_for_status()
        
        # Extract and store the assistant's response in memory
        answer = response.json().get("message", {}).get("content", "No response")
        memory.save_context({"input": prompt}, {"output": answer})  # Update memory with user input and response
        return answer
    except requests.RequestException as e:
        st.error(f"Request error: {e}")
        return "There was an error processing your request."

# Streamlit app UI
st.title("Llama 3.2 1B Chatbot with Conversation Memory")

# User input and display of the chatbot response
user_input = st.text_input("Ask something:")
if st.button("Send"):
    if user_input:
        with st.spinner("Generating response..."):
            answer = query_llama(user_input)
            st.write(answer)
    else:
        st.write("Please enter a question.")
