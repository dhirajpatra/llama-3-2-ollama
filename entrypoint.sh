#!/bin/bash

# Start the Ollama server in the background
ollama serve &

# Get the PID of the Ollama server process
OLLAMA_PID=$!

# Wait for the Ollama server to become available
echo "Waiting for the Ollama server to start..."
until curl -s http://localhost:11434 > /dev/null; do
  sleep 2
done
echo "Ollama server is running."

# Check if the model already exists
MODEL_PATH="/root/.ollama/models/llama3.2:1b"
if [ ! -d "$MODEL_PATH" ]; then
  echo "Model not found. Pulling model..."
  ollama pull llama3.2:1b
else
  echo "Model already exists. Skipping pull."
fi

# Wait for the Ollama server process to finish
wait $OLLAMA_PID
