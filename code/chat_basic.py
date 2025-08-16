"""Basic chat functionality for Anthropic prompt engineering tutorial.

This module provides core chat interaction functions that demonstrate various
prompt engineering techniques. It includes single-shot chat, continuous chat
loops, and templated chat interactions for structured prompt examples.

The module serves as the primary interface for user interactions with the AI
model, handling user input, prompt formatting, and response display.

Functions:
    basic_chat: Execute a single chat interaction with optional configuration
    basic_chat_loop: Start continuous chat session with the AI model
    basic_chat_template: Execute templated chat using predefined prompt structures
    _basic_chat: Private helper for handling individual chat interactions

Constants:
    DEFAULT_USER_INPUT: Default question used when user provides no input
"""

from api_client import get_completion
from chat_templates import get_chat_template_data

# from chat_templates import

DEFAULT_USER_INPUT = "What is Celine Dion's single most popular song?"


def _basic_chat(
    system_prompt: str,
    max_tokens: int,
    default_user_input="",
    user_input_hint="Enter your query: ",
    user_prompt_prefix="",
    user_prompt_suffix="",
    assistant_prefill="",
):
    """Private helper function to handle a single chat interaction.

    Prompts the user for input, uses the default query if no input is provided,
    displays the interaction details, and returns the AI response. This function
    constructs a formatted prompt with optional prefix and suffix elements.

    Args:
        system_prompt (str): The system prompt to use for the AI model.
        max_tokens (int): Maximum number of tokens in the AI response.
        default_user_input (str, optional): Default user input to use if user
            provides no input. Defaults to "".
        user_input_hint (str, optional): Custom prompt text to display to user.
            Defaults to "Enter your query: ".
        user_prompt_prefix (str, optional): Text to prepend to the user prompt.
            Defaults to "".
        user_prompt_suffix (str, optional): Text to append to the user prompt.
            Defaults to "".
        assistant_prefill (str, optional): assistant_prefill string for assistant response.

    Returns:
        str: The AI model's response text.

    Side Effects:
        - Prints session details (max tokens, system prompt, prefix/suffix) to stdout
        - Prompts user for input via stdin repeatedly until valid input received
        - Prints user input and formatted user prompt to stdout
        - Prints AI response to stdout

    Note:
        This is a private function used internally by other chat functions.
        The user prompt is formatted as: prefix + <user_input>input</user_input> + suffix
    """
    print("\n----------------------------------------------------------------\n")
    debug_data = [
        "=== User turn ===",
        f"Max tokens:         {max_tokens}",
        f"System prompt:      {system_prompt or "None"}",
        f"Default User Input: {default_user_input}",
        f"Prompt prefix:      {user_prompt_prefix}",
        f"Prompt suffix:      {user_prompt_suffix}",
        f"Assistant prefill:  {assistant_prefill}",
    ]
    print("\n".join(debug_data), end="\n\n")

    # Allow downstream functions to provide default user input, which will skip gathering user input.
    user_input = ""

    # Gather user input, if necessary.
    while not user_input:
        user_input = input(f"==> {user_input_hint}")
        if not user_input:
            user_input = default_user_input
        if not user_input:
            print("You have to enter something here.")

    # Generate prompt based on prefix, user_input, and suffix.
    user_prompt_data = []
    if user_prompt_prefix:
        user_prompt_data.append(user_prompt_prefix)
    user_prompt_data.append(f"<user_input>{user_input}</user_input>")
    if user_prompt_suffix:
        user_prompt_data.append(user_prompt_suffix)

    user_prompt = " ".join(user_prompt_data)
    print(f"\nUser input:    {user_input}")

    return get_completion(user_prompt, system_prompt, max_tokens, assistant_prefill)


def basic_chat(
    system_prompt="",
    max_tokens=2000,
    default_user_input=DEFAULT_USER_INPUT,
    user_input_hint="",
):
    """Execute a single chat interaction with the AI model.

    Prompts the user for a query and displays the AI's response. If no input
    is provided, uses the default query. This is a wrapper around _basic_chat
    for single-shot interactions.

    Args:
        system_prompt (str, optional): System prompt for the AI model.
            If empty string, uses the default system prompt. Defaults to "".
        max_tokens (int, optional): Maximum number of tokens in the response.
            Defaults to 2000.
        default_user_input (str, optional): Default user input to use if user provides
            no input. Defaults to DEFAULT_USER_INPUT.
        user_input_hint (str, optional): Custom prompt text to display to user.
            If empty, auto-generates prompt with default_user_input. Defaults to "".

    Returns:
        str: The AI model's response text.

    Side Effects:
        - Prompts user for input via stdin
        - Prints session details, user input, and AI response to stdout

    Example:
        >>> response = basic_chat("You are a helpful assistant", 1000)
        >>> basic_chat()  # Uses all defaults
    """
    # Set a default message for the default prompt.
    if not user_input_hint:
        user_input_hint = (
            f"Default user input: {default_user_input or "None"}\nEnter your query: "
        )

    # Get response from LLM.
    return _basic_chat(system_prompt, max_tokens, default_user_input, user_input_hint)


def basic_chat_template(
    template_name: str, system_prompt="", max_tokens=2000, default_user_input=""
):
    """Execute a templated chat interaction using predefined prompt templates.

    Uses structured prompt templates from TEMPLATE_DATA to format user input
    with XML tags and generate AI responses. Some templates have predefined
    input (like "identify_second_item"), while others prompt the user for input.

    Args:
        template_name (str): Name of the template to use. Must be a key in
            TEMPLATE_DATA. Available templates:
            - "animal_sound": Prompts for animal name, asks for the sound it makes
            - "polite_email": Prompts for rude email, asks to make it polite
            - "identify_second_item": Uses predefined sentences, asks for second item
        system_prompt (str, optional): System prompt for the AI model.
            Defaults to "".
        max_tokens (int, optional): Maximum number of tokens in the AI response.
            Defaults to 2000.
        default_user_input (str, optional): Default query to use if user provides
            no input. Overwrites any default set for this template.

    Returns:
        str: The AI model's response text.

    Raises:
        ValueError: If template_name is not found in TEMPLATE_DATA (raised by
            get_chat_template_data).

    Side Effects:
        - Prints template instructions and prompts to stdout
        - May prompt user for input via stdin (depending on template)
        - Prints formatted user prompt, system prompt, and AI response to stdout

    Example:
        >>> response = basic_chat_template("animal_sound")
        >>> response = basic_chat_template("polite_email", "Be very polite", 1000, "I'm busy!")
    """

    # Get template data.
    template_data = get_chat_template_data(template_name, default_user_input)

    # Get response from LLM.
    return _basic_chat(
        system_prompt,
        max_tokens,
        template_data["default_user_input"],
        template_data["user_input_hint"],
        template_data["template_prefix"],
        template_data["template_suffix"],
        template_data["assistant_prefill"],
    )


def basic_chat_loop(
    system_prompt="",
    max_tokens=2000,
    default_user_input=DEFAULT_USER_INPUT,
    user_input_hint="",
):
    """Start an interactive chat loop with the AI model.

    Continuously prompts the user for queries and displays AI responses until
    the program is terminated. The first prompt uses "your" and subsequent
    prompts use "another" for better user experience. Ignores the user_input_hint
    parameter and auto-generates appropriate prompts.

    Args:
        system_prompt (str, optional): System prompt for the AI model.
            If empty string, uses the default system prompt. Defaults to "".
        max_tokens (int, optional): Maximum number of tokens in each response.
            Defaults to 2000.
        default_user_input (str, optional): Default user input to use if user provides
            no input. Defaults to DEFAULT_USER_INPUT.
        user_input_hint (str, optional): Ignored in this function. Auto-generates
            appropriate prompts. Defaults to "".

    Returns:
        None: This function runs indefinitely and doesn't return.

    Side Effects:
        - Repeatedly prompts user for input via stdin
        - Prints session details, user input, and AI responses to stdout
        - Runs until program termination (Ctrl+C or similar)

    Note:
        This function runs indefinitely until interrupted (Ctrl+C).
        Each iteration displays the current session configuration and AI response.

    Example:
        >>> basic_chat_loop("You are a comedian", 500)
        >>> basic_chat_loop()  # Uses all defaults
    """
    is_first_run = True
    while True:
        glue_word = "your" if is_first_run else "another"
        user_input_hint = f"Enter {glue_word} query [{default_user_input}]: "
        _basic_chat(system_prompt, max_tokens, default_user_input, user_input_hint)
        is_first_run = False
