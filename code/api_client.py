"""
Shared API client module.
This contains the core API functionality that other modules can use.
"""

from constants import SYSTEM_PROMPT_DEFAULT
from os import environ
import anthropic

# Define required environment variables.
API_KEY = environ.get("ANTHROPIC_API_KEY", "")
MODEL_NAME = environ.get("ANTHROPIC_MODEL_NAME", "")

client = anthropic.Anthropic(api_key=API_KEY)


def validate_environment_variables():
    if not environ.get("ANTHROPIC_API_KEY"):
        raise ValueError("API_KEY is not set")
    if not environ.get("ANTHROPIC_MODEL_NAME"):
        raise ValueError("OPENAI_MODEL is not set")


def _get_completion(prompt: str, system_prompt: str, max_tokens: int):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=max_tokens,
        temperature=0.0,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def get_completion(prompt: str, system_prompt="", max_tokens=2000):
    """Get completion from Anthropic API with optional system prompt.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): System prompt to use. If empty string,
            uses the default system prompt. Defaults to "".
        max_tokens (int, optional): Maximum tokens in the response. Defaults to 2000.

    Returns:
        str: The model's response text.
    """
    if not system_prompt:  # More Pythonic - handles "", None, etc.
        return _get_completion(
            prompt, system_prompt=SYSTEM_PROMPT_DEFAULT, max_tokens=max_tokens
        )
    return _get_completion(prompt, system_prompt, max_tokens)
