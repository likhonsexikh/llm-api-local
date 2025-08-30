# AGENTS.md

## Project Overview

This project demonstrates how to run OpenAI-compatible AI models locally using Docker Model Runner, providing a cost-effective and privacy-focused alternative to cloud-based AI services. The project includes examples for Python, JavaScript/TypeScript, and REST API implementations.

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Client Code   │───▶│ Docker Model     │───▶│   AI Model      │
│ (Python/JS/API) │    │ Runner Server    │    │ (ai/smollm2)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                    OpenAI Compatible API
                    http://localhost:8080/v1
```

## Key Components

### 1. Local AI Model Server
- **Tool**: Docker Model Runner
- **Model**: `ai/smollm2` (small language model for local inference)
- **API**: OpenAI-compatible endpoints
- **Port**: Default `8080` (configurable)

### 2. Client Libraries
- **Python**: `openai` package
- **JavaScript/TypeScript**: `openai` npm package
- **REST API**: Direct HTTP calls

## Development Environment Setup

### Prerequisites
- Docker Desktop with Docker Model Runner feature enabled
- Python 3.8+ (for Python examples)
- Node.js 16+ (for JavaScript/TypeScript examples)

### Initial Setup
```bash
# Pull the AI model
docker model pull ai/smollm2

# Start the local model server
docker model run ai/smollm2
# This starts a server at http://localhost:8080 with OpenAI-compatible API
```

### Environment Variables
Create a `.env` file with:
```env
# Local model configuration
LOCAL_MODEL_BASE_URL=http://localhost:8080/v1
LOCAL_MODEL_NAME=ai/smollm2
LOCAL_API_KEY=dummy-key  # Required by OpenAI library but not validated locally
```

## Code Structure

```
project/
├── AGENTS.md              # This file - agent instructions
├── README.md             # User-facing documentation
├── .env                  # Environment configuration
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
├── src/
│   ├── python/
│   │   ├── chat_client.py      # Python OpenAI client example
│   │   ├── streaming_chat.py   # Streaming responses example
│   │   └── batch_processing.py # Batch processing example
│   ├── javascript/
│   │   ├── chat-client.js      # JavaScript client example
│   │   ├── chat-client.ts      # TypeScript client example
│   │   └── streaming-chat.js   # Streaming example
│   └── examples/
│       ├── rest-api-curl.sh    # cURL examples
│       └── postman-collection.json
├── tests/
│   ├── test_python_client.py
│   └── test_js_client.test.js
└── docs/
    ├── api-reference.md
    └── troubleshooting.md
```

## Core Implementation Pattern

### The Three-Line Change Pattern
When adapting existing OpenAI code for local models, you only need to change:

1. **Base URL**: Point to local server
2. **API Key**: Use dummy value (required but not validated)
3. **Model Name**: Use local model name

### Python Implementation Template
```python
from openai import OpenAI
import os

# Configuration
client = OpenAI(
    base_url=os.getenv("LOCAL_MODEL_BASE_URL", "http://localhost:8080/v1"),
    api_key=os.getenv("LOCAL_API_KEY", "dummy-key")
)

def chat_completion(messages, **kwargs):
    """Standard chat completion with local model."""
    return client.chat.completions.create(
        model=os.getenv("LOCAL_MODEL_NAME", "ai/smollm2"),
        messages=messages,
        **kwargs
    )
```

### JavaScript Implementation Template
```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
    baseURL: process.env.LOCAL_MODEL_BASE_URL || 'http://localhost:8080/v1',
    apiKey: process.env.LOCAL_API_KEY || 'dummy-key'
});

export async function chatCompletion(messages, options = {}) {
    return await openai.chat.completions.create({
        model: process.env.LOCAL_MODEL_NAME || 'ai/smollm2',
        messages,
        ...options
    });
}
```

## Testing Strategy

### Unit Tests
- Test client initialization with various configurations
- Mock server responses for consistent testing
- Validate API request/response formats

### Integration Tests
- Test against running Docker Model Runner instance
- Verify OpenAI API compatibility
- Test streaming responses and error handling

### Performance Tests
- Measure local inference latency
- Compare performance with cloud APIs
- Test concurrent request handling

## Common Patterns & Best Practices

### 1. Error Handling
```python
try:
    response = client.chat.completions.create(...)
    return response.choices[0].message.content
except Exception as e:
    logger.error(f"Local model error: {e}")
    # Implement fallback strategy
    return handle_model_error(e)
```

### 2. Configuration Management
```python
class ModelConfig:
    def __init__(self):
        self.base_url = os.getenv("LOCAL_MODEL_BASE_URL", "http://localhost:8080/v1")
        self.model_name = os.getenv("LOCAL_MODEL_NAME", "ai/smollm2")
        self.api_key = os.getenv("LOCAL_API_KEY", "dummy-key")
    
    def validate_connection(self):
        # Check if local model server is running
        pass
```

### 3. Streaming Responses
```python
def stream_chat(messages):
    stream = client.chat.completions.create(
        model="ai/smollm2",
        messages=messages,
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
```

## Debugging & Troubleshooting

### Common Issues
1. **Connection Refused**: Docker Model Runner not started
2. **Model Not Found**: Wrong model name in requests
3. **API Key Error**: OpenAI library requires API key parameter

### Debug Commands
```bash
# Check if model server is running
curl http://localhost:8080/v1/models

# Test basic completion
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "ai/smollm2", "messages": [{"role": "user", "content": "test"}]}'

# Check Docker Model Runner status
docker model ls
```

### Logging Configuration
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("local_model_client")
```

## Security Considerations

### Local Development
- Models run locally - no data sent to external services
- API keys are dummy values for local use
- Network traffic stays on localhost

### Production Considerations
- If exposing model server beyond localhost, implement proper authentication
- Consider rate limiting for multi-user scenarios
- Monitor resource usage and implement proper scaling

## Performance Optimization

### Model Configuration
- Adjust `max_tokens` based on use case
- Tune `temperature` for desired creativity/consistency balance
- Use appropriate `top_p` and `top_k` parameters

### Resource Management
- Monitor Docker container resource usage
- Implement request queuing for high concurrency
- Consider model warm-up strategies

## AI Agent Guidelines

### When Working on This Project

1. **Always test against the local model server** - Don't assume external API behavior
2. **Maintain OpenAI API compatibility** - Any changes should work with standard OpenAI client libraries  
3. **Focus on local-first design** - Prioritize functionality that works without internet
4. **Document resource requirements** - Note memory/CPU usage for different models
5. **Implement graceful degradation** - Handle cases where local model is unavailable

### Code Quality Standards

- Follow existing patterns in the three-line configuration approach
- Include comprehensive error handling
- Add logging for debugging local model interactions
- Write tests that work with mock servers when local model isn't available
- Document any model-specific behaviors or limitations

### Testing Requirements

- Test with Docker Model Runner running
- Verify OpenAI library compatibility  
- Include examples for both streaming and non-streaming use cases
- Test error conditions (server down, invalid model name, etc.)

## Resources

- [Docker Model Runner Documentation](https://docs.docker.com/desktop/model-runner/)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [OpenAI JavaScript Library](https://github.com/openai/openai-node)
- [OpenAPI 3.0 Specification](https://spec.openapis.org/oas/v3.0.3)

---

*This AGENTS.md file should be updated as the project evolves. AI agents should refer to this file for context about project architecture, development patterns, and best practices.*
