import requests
import streamlit as st


MODEL = "llama3.2:1b"

# API call to the Llama model via Ollama
def query_llama(prompt):
    url = "http://ollama:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "temperature": 0.7,
        "max_length": 2048,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("message", {}).get("content", "No response")

# Streamlit app UI
st.title("Llama 3.2 Chat")

user_input = st.text_input("Ask something:")
if st.button("Send"):
    if user_input:
        answer = query_llama(user_input)
        st.write(answer)
    else:
        st.write("Please enter a question.")
