import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

MODEL = "llama3.2:1b"

# Set up a session for optimized HTTP requests
session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount("http://", HTTPAdapter(max_retries=retries))

# API call to the Llama model via Ollama
def query_llama(prompt):
    url = "http://ollama:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "temperature": 0.5,  # Lower temperature for more consistent responses
        "max_length": 1500,  # Reduce max_length to decrease response time if possible
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    try:
        response = session.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()  # Ensure a successful response
        return response.json().get("message", {}).get("content", "No response")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return "There was an error processing your request."

# Streamlit app UI
st.title("Llama 3.2 1B Smalles LLM Model Chat")

# Streamlined input and response display
user_input = st.text_input("Ask something:")
if st.button("Send") and user_input:
    with st.spinner("Generating response..."):
        answer = query_llama(user_input)
        st.write(answer)
