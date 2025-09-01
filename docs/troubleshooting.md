# Troubleshooting Guide

This guide covers common issues you might encounter while using the LLM API Local project and how to resolve them.

## Common Issues

### Connection Refused Error

If you see an error like `Connection refused` or `APIConnectionError`, it usually means the local model server is not running or is not accessible.

**Solutions:**

1.  **Check if the Docker Model Runner is running:**
    Open a terminal and run `docker model ls`. You should see the `ai/smollm2` model listed.

2.  **Restart the model server:**
    If the model is not running, start it with:
    ```bash
    docker model run ai/smollm2
    ```
    If it is running, sometimes restarting it can fix connection issues.

### Model Not Found

If you receive an error indicating the model was not found, follow these steps:

1.  **Verify the model is pulled:**
    Make sure you have the model on your machine.
    ```bash
    docker model pull ai/smollm2
    ```

2.  **Check the running models via the API:**
    You can query the server's model endpoint to see which models it's serving.
    ```bash
    curl http://localhost:8080/v1/models
    ```
    Ensure the model name in your code (`ai/smollm2`) matches the one served by the API.

### Port Already in Use

If you see an error like `Port 8080 is already allocated`, it means another application on your machine is using that port.

**Solutions:**

1.  **Find the process using the port:**
    You can use a command like `lsof` (on macOS/Linux) or `netstat` (on Windows) to find out what's using the port.
    ```bash
    # On macOS or Linux
    lsof -i :8080
    ```

2.  **Run the model on a different port:**
    You can map the model server to a different host port. For example, to use port 8081:
    ```bash
    docker model run -p 8081:8080 ai/smollm2
    ```
    If you do this, you **must** update the `base_url` in your client configuration to `http://localhost:8081/v1`. You can do this by setting the `LOCAL_MODEL_BASE_URL` environment variable.

## Further Help

If you encounter issues not covered here, please feel free to:
- Open an issue on our [GitHub Issues page](https://github.com/likhonsexikh/llm-api-local/issues).
- Start a discussion on our [GitHub Discussions page](https://github.com/likhonsexikh/llm-api-local/discussions).
