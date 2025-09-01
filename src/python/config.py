import os
from dataclasses import dataclass
from openai import OpenAI

@dataclass
class LocalModelConfig:
    """
    A dataclass to hold the configuration for the local model client.
    Loads values from environment variables with sensible defaults.
    """
    base_url: str = os.getenv("LOCAL_MODEL_BASE_URL", "http://localhost:8080/v1")
    model_name: str = os.getenv("LOCAL_MODEL_NAME", "ai/smollm2")
    api_key: str = os.getenv("LOCAL_API_KEY", "dummy-key")
    max_tokens: int = int(os.getenv("DEFAULT_MAX_TOKENS", "150"))
    temperature: float = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))

    def get_client(self) -> OpenAI:
        """Returns an OpenAI client configured with these settings."""
        return OpenAI(base_url=self.base_url, api_key=self.api_key)

    def validate(self):
        """
        A placeholder for validating configuration.
        In a real app, this could test the connection to the base_url.
        """
        if not self.base_url.startswith("http"):
            raise ValueError("base_url must be a valid URL.")
        print("Configuration validation check passed (placeholder).")
        return True
