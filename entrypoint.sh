#!/bin/bash

# Start the Ollama server in the background
ollama serve &
OLLAMA_PID=$!

# Check if the model exists and download it if necessary
MODEL_PATH="/root/.ollama/models/llama3.2:1b"
if [ ! -d "$MODEL_PATH" ]; then
  echo "Model not found. Pulling model..."
  ollama pull llama3.2:1b
else
  echo "Model already exists. Skipping pull."
fi

# Wait for the Ollama server to become available
echo "Waiting for the Ollama server to start..."
until curl -s http://localhost:11434 > /dev/null; do
  echo "Ollama server is still starting..."
  sleep 2
done
echo "Ollama server is running."

# Keep the container running by waiting on the Ollama server process
wait $OLLAMA_PID
