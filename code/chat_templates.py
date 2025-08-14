"""Chat templates module for structured prompt engineering examples.

This module provides predefined prompt templates and helper functions for
demonstrating structured prompting techniques. It includes XML tag conventions
for separating different types of content in prompts and template data for
various prompt engineering exercises.

XML Tag Conventions:
    <user_input>: Wraps raw text provided by the end user, often unaltered,
                  so the LLM can distinguish it from control instructions
    <query>: Encapsulates a specific question or search request for the LLM to address
    <instructions>: Marks developer-provided guidance on how the LLM should respond
    <context>: Provides relevant background or situational details for the LLM
    <examples>: Contains sample inputs and outputs to illustrate desired response style
    <metadata>: Holds auxiliary data (e.g., user ID, timestamps) that may influence processing

Functions:
    get_chat_template_data: Retrieve template configuration for a given template name
    basic_chat_template_old: Legacy templated chat function (deprecated)

Constants:
    TEMPLATE_DATA: Dictionary mapping template names to their configurations
    SENTENCES: Sample sentences used in the "identify_second_item" template
"""

from api_client import get_completion

SENTENCES = """- I like how cows sound
- This sentence is about spiders
- This sentence may appear to be about dogs but it's actually about pigs"""

TEMPLATE_DATA = {
    "animal_sound": {
        "template_prefix": "I will tell you the name of an animal. Please respond with the noise that this animal makes:",
        "template_suffix": "",
        "user_input_query": "Chatbot will tell you the noise an animal makes\nEnter the name of an animal",
    },
    "polite_email": {
        "template_prefix": "For Claude.",
        "template_suffix": "<----- Make this email more polite but don't change anything else about it.",
        "user_input_query": "Enter a rude email message that should be polished to make it sound more polite",
    },
    "identify_second_item": {
        "template_prefix": """Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.\n""",
        "template_suffix": "",
        "user_input_query": "Don't enter anything - there are three default sentences defined in code.",
    },
}


def get_chat_template_data(template_name: str) -> dict:
    """Retrieve template configuration data for a given template name.

    This function validates the template name and returns the complete
    configuration including template prefix/suffix, user input query,
    and any default user input for the specified template.

    Args:
        template_name (str): Name of the template to retrieve. Must be a key
            in TEMPLATE_DATA.

    Returns:
        dict: Template configuration containing:
            - template_prefix (str): Text to prepend to user input
            - template_suffix (str): Text to append to user input
            - user_input_query (str): Prompt text to display to user
            - default_user_input (str): Default input for certain templates

    Raises:
        ValueError: If template_name is not found in TEMPLATE_DATA.

    Example:
        >>> config = get_chat_template_data("animal_sound")
        >>> print(config["user_input_query"])
        Chatbot will tell you the noise an animal makes
        Enter the name of an animal
    """
    # Validate template_name.
    if template_name not in TEMPLATE_DATA.keys():
        raise ValueError("Template name is not valid.")

    # Determine if a default should be provided for the user input in this template.
    default_user_input = ""
    match template_name:
        case "identify_second_item":
            default_user_input = SENTENCES
        case _:
            default_user_input = ""

    return {
        "template_prefix": TEMPLATE_DATA[template_name]["template_prefix"],
        "template_suffix": TEMPLATE_DATA[template_name]["template_suffix"],
        "user_input_query": TEMPLATE_DATA[template_name]["user_input_query"],
        "default_user_input": default_user_input,
    }


def basic_chat_template_old(
    template_name: str, system_prompt="", max_tokens=2000, default_query=""
):
    """Execute a templated chat interaction using predefined prompt templates.

    DEPRECATED: This function is kept for backward compatibility.
    Use basic_chat_template from chat_basic module instead.

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
        default_query (str, optional): Default query to use if user provides
            no input (only for templates that prompt for user input). Defaults to "".

    Returns:
        str: The AI model's response text.

    Raises:
        ValueError: If template_name is not found in TEMPLATE_DATA.

    Side Effects:
        - Prints template instructions and prompts to stdout
        - May prompt user for input via stdin (depending on template)
        - Prints formatted user prompt, system prompt, and AI response to stdout

    Example:
        >>> basic_chat_template_old("animal_sound")
        >>> basic_chat_template_old("polite_email", "Be very polite", 1000, "I'm busy!")
    """
    # Validate template_name.
    if template_name not in TEMPLATE_DATA.keys():
        raise ValueError("Template name is not valid.")

    # Get user input or use pre-defined input.
    print("\n----------------------------------------------------------------")
    match template_name:
        case "identify_second_item":
            user_input = SENTENCES
        case _:
            user_input = ""

    default_query_display = "None" if default_query == "" else default_query
    while not user_input:
        user_input = input(
            f"{TEMPLATE_DATA[template_name]["input"]} [Default: {default_query_display}]: "
        )

        # If a non-empty default query was provided, use it.
        if not user_input:
            user_input = default_query

        # If we're still left with no input, ask the user to provide one.
        if not user_input:
            print(TEMPLATE_DATA[template_name]["input_blank"])

    # Generate prompt based on template and user_input.
    user_prompt = " ".join(
        [
            TEMPLATE_DATA[template_name]["template_prefix"],
            f"<user_input>{user_input}</user_input>",
            TEMPLATE_DATA[template_name]["template_suffix"],
        ]
    )

    # Print response.
    print(f"\nClaude's response\nMax tokens: {max_tokens}")
    print(f"User prompt: {user_prompt}")
    print(f"System prompt: {system_prompt or "None"}")

    response = get_completion(user_prompt, system_prompt, max_tokens)
    print(f"===> {response}")
    return response
