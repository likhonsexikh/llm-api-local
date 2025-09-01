import os
from openai import OpenAI
from dotenv import load_dotenv

def main():
    """
    Main function to run the basic chat example.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Configure for local model using environment variables
    client = OpenAI(
        base_url=os.getenv("LOCAL_MODEL_BASE_URL", "http://localhost:8080/v1"),
        api_key=os.getenv("LOCAL_API_KEY", "dummy-key"),
    )

    print("Sending request to local model...")
    # Use exactly like the OpenAI API
    try:
        response = client.chat.completions.create(
            model=os.getenv("LOCAL_MODEL_NAME", "ai/smollm2"),
            messages=[
                {"role": "user", "content": "Hello! How are you?"}
            ]
        )

        print("Response from model:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure the Docker Model Runner is running and the model is available.")

if __name__ == "__main__":
    main()
