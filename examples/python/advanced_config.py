import os
from openai import OpenAI
from dotenv import load_dotenv
from src.python.config import LocalModelConfig

def main():
    """
    Demonstrates using a configuration class to set up the client.
    """
    load_dotenv()

    # Initialize configuration from environment variables
    config = LocalModelConfig()

    # Get a pre-configured client
    client = config.get_client()

    print("--- Running Chat with Advanced Configuration ---")
    print(f"Model: {config.model_name}, Temperature: {config.temperature}, Max Tokens: {config.max_tokens}")

    try:
        response = client.chat.completions.create(
            model=config.model_name,
            messages=[{"role": "user", "content": "What are the benefits of using a config class?"}],
            temperature=config.temperature,
            max_tokens=config.max_tokens,
        )
        print("\nResponse:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
