#!/bin/bash

# This script provides a cURL example for interacting with the local LLM API.

curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy-key" \
  -d '{
    "model": "ai/smollm2",
    "messages": [
      {"role": "user", "content": "Hello! How are you?"}
    ]
  }'
