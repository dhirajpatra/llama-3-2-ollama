# app.py
import requests
import streamlit as st

MODEL = "llama3.2:1b"

# API call to the Llama model via Ollama
def query_llama(prompt):
    url = "http://ollama:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "temperature": 0.5,
        "max_length": 1500,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("message", {}).get("content", "No response from model.")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit app UI
st.title("Llama 3.2 Chat")

user_input = st.text_input("Ask something:")
if st.button("Send"):
    if user_input:
        answer = query_llama(user_input)
        st.write(answer)
    else:
        st.write("Please enter a question.")
