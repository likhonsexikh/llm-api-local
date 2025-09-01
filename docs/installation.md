# Installation Guide

This guide provides detailed steps to set up and run the LLM API Local project.

## 📋 Prerequisites

Before you begin, ensure you have the following installed and configured:

- **Docker Desktop**: Make sure Docker Desktop is installed and running on your machine. You can download it from the [official Docker website](https://www.docker.com/products/docker-desktop/).
- **Docker Model Runner**: The Docker Model Runner feature must be enabled in Docker Desktop. Please see the [official documentation](https://docs.docker.com/desktop/model-runner/) for instructions on how to enable it.
- **Python**: Python 3.8 or newer is required for the Python examples. You can download it from [python.org](https://www.python.org/).
- **Node.js**: Node.js 16 or newer is required for the JavaScript/TypeScript examples. You can download it from [nodejs.org](https://nodejs.org/).
- **Git**: You will need Git to clone the repository.

## 🚀 Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/likhonsexikh/llm-api-local.git
cd llm-api-local
```

### 2. Install Dependencies

Next, install the necessary dependencies for the language you wish to use.

**For Python examples:**

```bash
# Install main dependencies
pip install -r requirements.txt

# Install development dependencies (for running tests)
pip install -r requirements-dev.txt
```

**For JavaScript/TypeScript examples:**

```bash
# Install Node.js dependencies
npm install
```

### 3. Pull and Run the Local AI Model

This project uses Docker Model Runner to serve the local AI model.

**Pull the model:**
First, pull the small language model from Docker Hub. This only needs to be done once.

```bash
docker model pull ai/smollm2
```

**Run the model:**
Next, start the local API server. This command will run the model in a container and expose the OpenAI-compatible API on `http://localhost:8080`.

```bash
docker model run ai/smollm2
```

You can verify that the server is running by opening a new terminal and checking the list of running models:

```bash
docker model ls
```

### 4. Run the Examples

With the model running, you can now execute the example scripts.

**Python example:**

```bash
python examples/python/basic_chat.py
```

**JavaScript example:**

```bash
node examples/javascript/basic-chat.js
```

You are now fully set up to use and develop the LLM API Local project!
