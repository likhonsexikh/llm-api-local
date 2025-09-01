import pytest
from unittest.mock import patch, MagicMock
from src.python.config import LocalModelConfig
from examples.python import basic_chat

def test_local_model_config_initialization():
    """
    Tests that the LocalModelConfig dataclass initializes correctly with default values.
    """
    config = LocalModelConfig()
    assert config.base_url == "http://localhost:8080/v1"
    assert config.model_name == "ai/smollm2"
    assert config.api_key == "dummy-key"

@patch('examples.python.basic_chat.OpenAI')
def test_basic_chat_main_logic(mock_openai_class, capsys):
    """
    Tests the main logic of the basic_chat example by mocking the OpenAI client.
    This ensures the client is called with the correct parameters and that the
    response is printed, without making a real API call.
    """
    # Arrange: Configure the mock for the OpenAI client
    mock_client_instance = MagicMock()
    mock_completion = MagicMock()
    mock_completion.choices = [MagicMock()]
    mock_completion.choices[0].message.content = "This is a mocked response."
    mock_client_instance.chat.completions.create.return_value = mock_completion
    mock_openai_class.return_value = mock_client_instance

    # Act: Run the main function from the example script
    basic_chat.main()

    # Assert: Verify the behavior
    # 1. Check that the OpenAI client was instantiated with the expected URL and key
    mock_openai_class.assert_called_once()
    call_args = mock_openai_class.call_args
    assert call_args.kwargs['base_url'] == 'http://localhost:8080/v1'
    assert call_args.kwargs['api_key'] == 'dummy-key'

    # 2. Check that the 'create' method was called on the client instance
    mock_client_instance.chat.completions.create.assert_called_once()
    create_call_args = mock_client_instance.chat.completions.create.call_args
    assert create_call_args.kwargs['model'] == 'ai/smollm2'

    # 3. Check that the mocked response was printed to stdout
    captured = capsys.readouterr()
    assert "Response from model:" in captured.out
    assert "This is a mocked response." in captured.out
