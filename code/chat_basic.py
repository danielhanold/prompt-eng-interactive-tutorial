from api_client import get_completion

DEFAULT_QUERY = "What is Celine Dion's single most popular song?"


def _basic_chat(
    system_prompt: str,
    max_tokens: int,
    default_query: str,
    input_prompt="Enter your query: ",
):
    """Private helper function to handle a single chat interaction.

    Prompts the user for input, uses the default query if no input is provided,
    displays the interaction details, and returns the AI response.

    Args:
        system_prompt (str): The system prompt to use for the AI model.
        max_tokens (int): Maximum number of tokens in the AI response.
        default_query (str): Default query to use if user provides no input.
        input_prompt (str, optional): Custom prompt text to display to user.
            Defaults to "Enter your query: ".

    Returns:
        str: The AI model's response text.

    Side Effects:
        - Prints session details (max tokens, system prompt) to stdout
        - Prompts user for input via stdin
        - Prints user input and AI response to stdout
    """
    print("\n----------------------------------------------------------------\n")
    print(
        f"=== User turn === \nMax tokens: {max_tokens}\nSystem prompt: {system_prompt or "None"}"
    )
    user_input = ""
    while not user_input:
        user_input = input(input_prompt)
        if not user_input:
            user_input = default_query
        if not user_input:
            print("You have to enter something here.")
    print(f"User input: {user_input}")

    print("\n=== Assistant turn ===")
    response = get_completion(user_input, system_prompt, max_tokens)
    print(response)
    return response


def basic_chat(
    system_prompt="", max_tokens=2000, default_query=DEFAULT_QUERY, input_prompt=""
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
        default_query (str, optional): Default query to use if user provides
            no input. Defaults to DEFAULT_QUERY.
        input_prompt (str, optional): Custom prompt text to display to user.
            If empty, auto-generates prompt with default_query. Defaults to "".

    Returns:
        str: The AI model's response text.

    Example:
        >>> response = basic_chat("You are a helpful assistant", 1000)
        >>> basic_chat()  # Uses all defaults
    """
    # Set a default message for the default prompt.
    if not input_prompt:
        input_prompt = f"Enter your query [{default_query}]: "
    response = _basic_chat(system_prompt, max_tokens, default_query, input_prompt)
    return response


def basic_chat_loop(
    system_prompt="", max_tokens=2000, default_query=DEFAULT_QUERY, input_prompt=""
):
    """Start an interactive chat loop with the AI model.

    Continuously prompts the user for queries and displays AI responses until
    the program is terminated. The first prompt uses "your" and subsequent
    prompts use "another" for better user experience. Ignores the input_prompt
    parameter and auto-generates appropriate prompts.

    Args:
        system_prompt (str, optional): System prompt for the AI model.
            If empty string, uses the default system prompt. Defaults to "".
        max_tokens (int, optional): Maximum number of tokens in each response.
            Defaults to 2000.
        default_query (str, optional): Default query to use if user provides
            no input. Defaults to DEFAULT_QUERY.
        input_prompt (str, optional): Ignored in this function. Auto-generates
            appropriate prompts. Defaults to "".

    Returns:
        None: This function runs indefinitely and doesn't return.

    Note:
        This function runs indefinitely until interrupted (Ctrl+C).

    Example:
        >>> basic_chat_loop("You are a comedian", 500)
        >>> basic_chat_loop()  # Uses all defaults
    """
    is_first_run = True
    while True:
        glue_word = "your" if is_first_run else "another"
        input_prompt = f"Enter {glue_word} query [{default_query}]: "
        _basic_chat(system_prompt, max_tokens, default_query, input_prompt)
        is_first_run = False
