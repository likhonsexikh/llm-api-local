# LLM API Local

> Run OpenAI-compatible AI models locally using Docker Model Runner with familiar OpenAI client libraries

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/Docker-Required-blue.svg)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-16+-green.svg)](https://nodejs.org/)

## 🚀 What is LLM API Local?

LLM API Local enables you to run AI language models locally on your machine while maintaining full compatibility with OpenAI's API. Switch from cloud-based AI services to local inference with just **3 lines of code changes**.

### Key Features

- 🏠 **Local Inference**: Keep your data private and run models offline
- 💰 **Cost-Free**: No API usage fees or token limits
- 🔄 **OpenAI Compatible**: Use existing OpenAI client libraries without changes
- 🐳 **Docker Powered**: Leverages Docker Model Runner for easy setup
- ⚡ **Fast Setup**: Get running in under 5 minutes
- 🛡️ **Privacy First**: Your conversations never leave your machine

## 📋 Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Docker Model Runner enabled
- Python 3.8+ (for Python examples)
- Node.js 16+ (for JavaScript/TypeScript examples)

## ⚡ Quick Start

### 1. Start the Local Model

```bash
# Pull the small language model
docker model pull ai/smollm2

# Start the local API server
docker model run ai/smollm2
```

This starts an OpenAI-compatible API server at `http://localhost:8080`

### 2. Use with Python

```python
from openai import OpenAI

# Configure for local model (3 line changes!)
client = OpenAI(
    base_url="http://localhost:8080/v1",  # 1. Local endpoint
    api_key="dummy-key"                   # 2. Dummy key (required)
)

# Use exactly like OpenAI API
response = client.chat.completions.create(
    model="ai/smollm2",                   # 3. Local model name
    messages=[
        {"role": "user", "content": "Hello! How are you?"}
    ]
)

print(response.choices[0].message.content)
```

### 3. Use with JavaScript/TypeScript

```javascript
import OpenAI from 'openai';

// Configure for local model
const openai = new OpenAI({
    baseURL: 'http://localhost:8080/v1',
    apiKey: 'dummy-key'
});

// Use exactly like OpenAI API
const response = await openai.chat.completions.create({
    model: 'ai/smollm2',
    messages: [
        { role: 'user', content: 'Hello! How are you?' }
    ]
});

console.log(response.choices[0].message.content);
```

### 4. Use with cURL/REST API

```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy-key" \
  -d '{
    "model": "ai/smollm2",
    "messages": [
      {"role": "user", "content": "Hello! How are you?"}
    ]
  }'
```

## 📂 Project Structure

```
llm-api-local/
├── README.md                 # This file
├── AGENTS.md                 # AI agent instructions
├── examples/
│   ├── python/
│   │   ├── basic_chat.py           # Simple chat example
│   │   ├── streaming_chat.py       # Streaming responses
│   │   ├── batch_processing.py     # Process multiple requests
│   │   └── advanced_config.py      # Advanced configuration
│   ├── javascript/
│   │   ├── basic-chat.js           # Basic JavaScript example
│   │   ├── basic-chat.ts           # TypeScript version
│   │   ├── streaming-chat.js       # Streaming example
│   │   └── express-server.js       # Express.js integration
│   └── rest-api/
│       ├── curl-examples.sh        # cURL command examples
│       └── postman-collection.json # Postman collection
├── src/
│   ├── python/
│   │   ├── __init__.py
│   │   ├── client.py               # Python client wrapper
│   │   ├── config.py               # Configuration management
│   │   └── utils.py                # Utility functions
│   └── javascript/
│       ├── client.js               # JavaScript client wrapper
│       ├── client.ts               # TypeScript definitions
│       └── config.js               # Configuration utilities
├── tests/
│   ├── test_python_client.py       # Python tests
│   ├── test_js_client.test.js      # JavaScript tests
│   └── integration_tests.py       # Integration tests
├── docs/
│   ├── installation.md             # Detailed installation guide
│   ├── configuration.md            # Configuration options
│   ├── troubleshooting.md          # Common issues and solutions
│   └── api-reference.md            # Complete API reference
├── requirements.txt                # Python dependencies
├── package.json                    # Node.js dependencies
└── docker-compose.yml             # Alternative Docker setup
```

## 🔧 Installation

### Option 1: Use Examples Directly

1. Clone this repository:
```bash
git clone https://github.com/likhonsexikh/llm-api-local.git
cd llm-api-local
```

2. Install dependencies:
```bash
# For Python examples
pip install -r requirements.txt

# For JavaScript examples
npm install
```

3. Start the local model:
```bash
docker model pull ai/smollm2
docker model run ai/smollm2
```

4. Run examples:
```bash
# Python example
python examples/python/basic_chat.py

# JavaScript example
node examples/javascript/basic-chat.js
```

### Option 2: Use as Library

**Python:**
```bash
pip install openai python-dotenv
```

**JavaScript:**
```bash
npm install openai dotenv
```

## 🎯 Use Cases

### Perfect For:
- 🔒 **Privacy-sensitive applications** - Healthcare, legal, financial
- 💻 **Development and testing** - No API costs during development
- 🌐 **Offline applications** - Work without internet connection
- 🏫 **Educational projects** - Learn AI without cloud dependencies
- 🛠️ **Rapid prototyping** - Quick iterations without API limits

### Example Applications:
- Personal AI assistant
- Code review and generation
- Document analysis and summarization
- Creative writing helper
- Data analysis and insights
- Customer service chatbot (local deployment)

## ⚙️ Configuration

### Environment Variables

Create a `.env` file:
```env
# Local model configuration
LOCAL_MODEL_BASE_URL=http://localhost:8080/v1
LOCAL_MODEL_NAME=ai/smollm2
LOCAL_API_KEY=dummy-key

# Optional: Model parameters
DEFAULT_MAX_TOKENS=150
DEFAULT_TEMPERATURE=0.7
DEFAULT_TOP_P=1.0
```

### Advanced Configuration

```python
# config.py
import os
from dataclasses import dataclass

@dataclass
class LocalModelConfig:
    base_url: str = os.getenv("LOCAL_MODEL_BASE_URL", "http://localhost:8080/v1")
    model_name: str = os.getenv("LOCAL_MODEL_NAME", "ai/smollm2")
    api_key: str = os.getenv("LOCAL_API_KEY", "dummy-key")
    max_tokens: int = int(os.getenv("DEFAULT_MAX_TOKENS", "150"))
    temperature: float = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
    
    def validate(self):
        """Validate configuration and test connection."""
        # Implementation here
        pass
```

## 🚀 Advanced Examples

### Streaming Responses

```python
def stream_chat_response(message):
    stream = client.chat.completions.create(
        model="ai/smollm2",
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
```

### Batch Processing

```python
def process_multiple_requests(requests):
    responses = []
    for request in requests:
        response = client.chat.completions.create(
            model="ai/smollm2",
            messages=request["messages"],
            max_tokens=request.get("max_tokens", 150)
        )
        responses.append({
            "id": request["id"],
            "response": response.choices[0].message.content
        })
    return responses
```

### Error Handling

```python
import logging
from openai import OpenAIError

def safe_chat_completion(messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="ai/smollm2",
                messages=messages
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            logging.error(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                return "Sorry, I'm having trouble connecting to the local model."
            time.sleep(1)
```

## 🔍 Available Models

Current supported models via Docker Model Runner:
- `ai/smollm2` - Small, efficient language model (recommended for getting started)
- More models coming soon...

Check available models:
```bash
docker model ls
```

## 🧪 Testing

Run the test suite:
```bash
# Python tests
python -m pytest tests/ -v

# JavaScript tests
npm test

# Integration tests (requires running model)
python tests/integration_tests.py
```

## 🛠️ Troubleshooting

### Common Issues

**Connection Refused Error:**
```bash
# Check if Docker Model Runner is running
docker model ls

# Restart the model
docker model run ai/smollm2
```

**Model Not Found:**
```bash
# Verify model is pulled
docker model pull ai/smollm2

# Check running models
curl http://localhost:8080/v1/models
```

**Port Already in Use:**
```bash
# Check what's using port 8080
lsof -i :8080

# Use different port
docker model run -p 8081:8080 ai/smollm2
# Then update base_url to http://localhost:8081/v1
```

For more troubleshooting, see [docs/troubleshooting.md](docs/troubleshooting.md)

## 📊 Performance

### Typical Performance (MacBook Pro M1):
- **Response Time**: 100-500ms for short responses
- **Throughput**: 10-50 tokens/second (model dependent)
- **Memory Usage**: 2-8GB RAM (model dependent)
- **CPU Usage**: Varies based on model size and complexity

### Optimization Tips:
- Use smaller models for faster responses
- Limit `max_tokens` for quicker completions
- Batch similar requests when possible
- Monitor Docker container resource usage

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/llm-api-local.git
cd llm-api-local

# Install development dependencies
pip install -r requirements-dev.txt
npm install --include=dev

# Run tests
make test

# Run linting
make lint
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Docker Model Runner](https://docs.docker.com/desktop/model-runner/) for making local AI models accessible
- [OpenAI](https://openai.com/) for the API standard that enables compatibility
- [llama.cpp](https://github.com/ggerganov/llama.cpp) for the underlying inference engine
- The open-source AI community for developing amazing local models

## 🔗 Related Projects

- [Ollama](https://github.com/ollama/ollama) - Another local AI model runner
- [LocalAI](https://github.com/go-skynet/LocalAI) - OpenAI alternative for local models
- [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) - Web interface for local models

## 📬 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/likhonsexikh/llm-api-local/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/likhonsexikh/llm-api-local/discussions)

---

**Made with ❤️ for developers who value privacy and local AI**

⭐ If this project helps you, please give it a star!
