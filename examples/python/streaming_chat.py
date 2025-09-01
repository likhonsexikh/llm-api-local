import os
from openai import OpenAI
from dotenv import load_dotenv

def stream_chat_response(client, message):
    """
    Sends a message to the chat model and streams the response.
    """
    print("\n--- Streaming Response ---")
    try:
        stream = client.chat.completions.create(
            model=os.getenv("LOCAL_MODEL_NAME", "ai/smollm2"),
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print("\n--- End of Stream ---")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please ensure the Docker Model Runner is running.")

def main():
    """
    Main function to set up client and run the streaming chat example.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Configure for local model using environment variables
    client = OpenAI(
        base_url=os.getenv("LOCAL_MODEL_BASE_URL", "http://localhost:8080/v1"),
        api_key=os.getenv("LOCAL_API_KEY", "dummy-key"),
    )

    user_message = "Tell me a short story about a robot who learns to paint."
    stream_chat_response(client, user_message)

if __name__ == "__main__":
    main()
