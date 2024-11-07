import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from PIL import Image
import io
import base64
from typing import Union

# MODEL = "llama3.2:1b"
MODEL = "llama3.2-vision"

# Set up a session for optimized HTTP requests
session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount("http://", HTTPAdapter(max_retries=retries))

# API call to the Llama model via Ollama
def query_llama(prompt: str, image: Union[bytes, None] = None) -> str:
    """
    Queries the Llama model via Ollama API.

    Args:
    - prompt (str): User input text.
    - image (bytes, optional): Image file bytes. Defaults to None.

    Returns:
    - str: Response from the Llama model.
    """
    url = "http://ollama:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "temperature": 0.5,  # Lower temperature for more consistent responses
        "max_length": 1500,  # Reduce max_length to decrease response time if possible
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    if image:
        # Encode image to base64
        encoded_image = base64.b64encode(image).decode("utf-8")
        data["messages"][0]["content"] += f"\n\nImage: data:image/jpeg;base64,{encoded_image}"

    try:
        response = session.post(url, headers=headers, json=data, timeout=300)
        response.raise_for_status()  # Ensure a successful response
        return response.json().get("message", {}).get("content", "No response")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return "There was an error processing your request."

# Streamlit app UI
st.title("Llama 3.2 Vision 11B LLM Model Chat")

# Input fields
user_input = st.text_input("Ask something:")
image_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

# Send button with input validation
if st.button("Send") and (user_input or image_file):
    with st.spinner("Generating response..."):
        # Convert uploaded image to bytes
        image_bytes = image_file.read() if image_file else None

        answer = query_llama(user_input, image_bytes)
        st.write(answer)

        # Display uploaded image
        if image_file:
            st.image(image_file)