"""Constants module for the Anthropic prompt engineering tutorial.

This module defines system prompts and default user inputs used throughout
the tutorial examples. It provides various system prompt variations to
demonstrate different AI personality configurations and response styles.

Constants:
    SYSTEM_PROMPT_DEFAULT: Instructs AI to give concise, direct responses
    SYSTEM_PROMPT_QUESTIONING: Makes AI respond with critical thinking questions
    SYSTEM_PROMPT_COMEDIAN: Configures AI to respond as a comedian with jokes
    DEFAULT_USER_INPUT: Default question about Celine Dion's popular song
"""

# Define system prompts.
SYSTEM_PROMPT_DEFAULT = "Keep your answer very short. Don't include a lot of background details that the user did not ask for."
SYSTEM_PROMPT_QUESTIONING = "Your answer should always be a series of critical thinking questions that further the conversation. (do not provide answers to your questions). Do not actually answer the user question."
SYSTEM_PROMPT_COMEDIAN = "You are a comedian. You are funny and you make people laugh. You are also a bit of a smart ass. Answer every question in the form of a joke."

# Define default user inputs.
DEFAULT_USER_INPUT = "What is Celine Dion's single most popular song?"
