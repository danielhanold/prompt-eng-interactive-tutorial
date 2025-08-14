"""Shared API client module for Anthropic Claude integration.

This module provides the core API functionality for communicating with
Anthropic's Claude AI model. It handles environment variable validation,
API client initialization, and completion requests with proper error handling.

The module exposes both a private helper function for direct API calls and
a public interface that automatically handles default system prompts.

Functions:
    validate_environment_variables: Validates required environment variables
    get_completion: Public interface for getting AI completions
    _get_completion: Private helper for direct API calls

Environment Variables Required:
    ANTHROPIC_API_KEY: API key for Anthropic's service
    ANTHROPIC_MODEL_NAME: Name of the Claude model to use
"""

from constants import SYSTEM_PROMPT_DEFAULT
from os import environ
import anthropic

# Define required environment variables.
API_KEY = environ.get("ANTHROPIC_API_KEY", "")
MODEL_NAME = environ.get("ANTHROPIC_MODEL_NAME", "")

client = anthropic.Anthropic(api_key=API_KEY)


def validate_environment_variables():
    """Validate that required environment variables are set.

    Checks for the presence of ANTHROPIC_API_KEY and ANTHROPIC_MODEL_NAME
    environment variables required for API communication.

    Raises:
        ValueError: If ANTHROPIC_API_KEY is not set.
        ValueError: If ANTHROPIC_MODEL_NAME is not set.

    Example:
        >>> validate_environment_variables()  # Raises if vars missing
    """
    if not environ.get("ANTHROPIC_API_KEY"):
        raise ValueError("API_KEY is not set")
    if not environ.get("ANTHROPIC_MODEL_NAME"):
        raise ValueError("OPENAI_MODEL is not set")


def _get_completion(prompt: str, system_prompt: str, max_tokens: int):
    """Private function to make direct API calls to Anthropic's Claude.

    Makes a single API request with fixed temperature of 0.0 for deterministic
    responses. This function is used internally by get_completion().

    Args:
        prompt (str): The user message to send to the model.
        system_prompt (str): System-level instructions for the model.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: The model's response text.

    Raises:
        anthropic.APIError: If the API request fails.
        anthropic.RateLimitError: If rate limits are exceeded.

    Note:
        This is a private function. Use get_completion() instead for the public API.
    """
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=max_tokens,
        temperature=0.0,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}],
    )
    # Extract text from the first content block
    content_block = message.content[0]
    # Type-safe access to text attribute
    return getattr(content_block, "text", str(content_block))


def get_completion(prompt: str, system_prompt="", max_tokens=2000):
    """Get completion from Anthropic API with optional system prompt.

    Public interface for generating AI completions. Automatically uses the
    default system prompt if none is provided, ensuring consistent behavior
    across the application.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): System prompt to use. If empty string,
            uses the default system prompt. Defaults to "".
        max_tokens (int, optional): Maximum tokens in the response. Defaults to 2000.

    Returns:
        str: The model's response text.

    Example:
        >>> response = get_completion("What is the capital of France?")
        >>> response = get_completion("Tell me a joke", "You are a comedian", 500)
    """
    if not system_prompt:  # More Pythonic - handles "", None, etc.
        return _get_completion(
            prompt, system_prompt=SYSTEM_PROMPT_DEFAULT, max_tokens=max_tokens
        )
    return _get_completion(prompt, system_prompt, max_tokens)
