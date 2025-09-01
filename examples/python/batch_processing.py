import os
from openai import OpenAI
from dotenv import load_dotenv

def process_multiple_requests(client, requests):
    """
    Processes a list of chat completion requests in a batch.
    """
    responses = []
    print(f"--- Starting Batch Processing for {len(requests)} requests ---")
    for i, request in enumerate(requests):
        print(f"Processing request {i+1}/{len(requests)} (ID: {request['id']})...")
        try:
            response = client.chat.completions.create(
                model=os.getenv("LOCAL_MODEL_NAME", "ai/smollm2"),
                messages=request["messages"],
                max_tokens=request.get("max_tokens", 150)
            )
            responses.append({
                "id": request["id"],
                "response": response.choices[0].message.content
            })
        except Exception as e:
            print(f"Error processing request {request['id']}: {e}")
            responses.append({
                "id": request["id"],
                "response": f"Error: {e}"
            })
    print("--- Batch Processing Complete ---")
    return responses

def main():
    """
    Main function to set up client and run the batch processing example.
    """
    load_dotenv()
    client = OpenAI(
        base_url=os.getenv("LOCAL_MODEL_BASE_URL", "http://localhost:8080/v1"),
        api_key=os.getenv("LOCAL_API_KEY", "dummy-key"),
    )

    # A list of requests to be processed
    batch_requests = [
        {
            "id": "req_001",
            "messages": [{"role": "user", "content": "What is the capital of France?"}],
        },
        {
            "id": "req_002",
            "messages": [{"role": "user", "content": "Summarize the plot of 'Moby Dick' in one sentence."}],
            "max_tokens": 50,
        },
        {
            "id": "req_003",
            "messages": [{"role": "user", "content": "Translate 'hello world' to Spanish."}],
        },
    ]

    results = process_multiple_requests(client, batch_requests)

    print("\n--- Batch Results ---")
    for result in results:
        print(f"Request ID: {result['id']}\nResponse: {result['response']}\n")

if __name__ == "__main__":
    main()
