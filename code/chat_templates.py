from api_client import get_completion


TEMPLATE_DATA = {
    "animal_sound": {
        "template_prefix": "I will tell you the name of an animal. Please respond with the noise that this animal makes:",
        "template_suffix": "",
        "input": "Chatbot will tell you the noise an animal makes\nEnter the name of an animal",
        "input_blank": "You have to actually enter the name of an animal. Please re-do!",
    },
    "polite_email": {
        "template_prefix": "For Claude.",
        "template_suffix": "<----- Make this email more polite but don't change anything else about it.",
        "input": "Enter a rude email message that should be polished to make it sound more polite",
        "input_blank": "You have to actually enter the a message - it cannot be blank!",
    },
}


def basic_chat_template(
    template_name: str, system_prompt="", max_tokens=2000, default_query=""
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
    # Validate template_name.
    if template_name not in TEMPLATE_DATA.keys():
        raise ValueError("Template name is not valid.")

    # Get user input.
    print("\n----------------------------------------------------------------")
    default_query_display = "None" if default_query == "" else default_query
    user_input = ""
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

    print(f"===> {get_completion(user_prompt, system_prompt, max_tokens)}")
