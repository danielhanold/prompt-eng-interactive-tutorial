from api_client import get_completion

DEFAULT_QUERY = "What is Celine Dion's single most popular song?"


def _basic_chat(
    system_prompt: str,
    max_tokens: int,
    default_query: str,
    glue_word="your",
):
    """Private helper function to handle a single chat interaction.

    Prompts the user for input, uses the default query if no input is provided,
    and displays the AI response with token count information.

    Args:
        system_prompt (str): The system prompt to use for the AI model.
        max_tokens (int): Maximum number of tokens in the AI response.
        default_query (str): Default query to use if user provides no input.
        glue_word (str, optional): Word to use in the input prompt
            ("your" for first interaction, "another" for subsequent).
            Defaults to "your".
    """
    print("\n----------------------------------------------------------------")
    user_prompt = (
        input(f"\nEnter {glue_word} query [{default_query}]: ") or default_query
    )
    if not user_prompt:
        user_prompt = default_query

    print(
        f"\nClaude's response\nMax tokens: {max_tokens}\nSystem prompt: {system_prompt or "None"}"
    )
    print(f"===> {get_completion(user_prompt, system_prompt, max_tokens)}")


def basic_chat(
    system_prompt="",
    max_tokens=2000,
    default_query=DEFAULT_QUERY,
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

    Example:
        >>> basic_chat("You are a helpful assistant", 1000)
        >>> basic_chat()  # Uses default system prompt
    """
    _basic_chat(system_prompt, max_tokens, default_query)


def basic_chat_loop(
    system_prompt="",
    max_tokens=2000,
    default_query=DEFAULT_QUERY,
):
    """Start an interactive chat loop with the AI model.

    Continuously prompts the user for queries and displays AI responses until
    the program is terminated. The first prompt uses "your" and subsequent
    prompts use "another" for better user experience.

    Args:
        system_prompt (str, optional): System prompt for the AI model.
            If empty string, uses the default system prompt. Defaults to "".
        max_tokens (int, optional): Maximum number of tokens in each response.
            Defaults to 2000.
        default_query (str, optional): Default query to use if user provides
            no input. Defaults to DEFAULT_QUERY.

    Note:
        This function runs indefinitely until interrupted (Ctrl+C).

    Example:
        >>> basic_chat_loop("You are a comedian", 500)
        >>> basic_chat_loop()  # Uses all defaults
    """
    is_first_run = True
    while True:
        glue_word = "your" if is_first_run else "another"
        _basic_chat(system_prompt, max_tokens, default_query, glue_word)
        is_first_run = False
