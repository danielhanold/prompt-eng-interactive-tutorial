from api_client import get_completion


TEMPLATE_DATA = {
    "animal_sound": {
        "template": "I will tell you the name of an animal. Please respond with the noise that animal makes.",
        "input": f"Chatbot will tell you the noise an animal makes\nEnter the name of an animal: ",
        "input_blank": "You have to actually enter the name of an animal. Please re-do!",
    }
}


def basic_chat_template(
    template_name: str,
    system_prompt="",
    max_tokens=2000,
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

    print("\n----------------------------------------------------------------")
    user_prompt = ""
    while not user_prompt:
        user_prompt = input(TEMPLATE_DATA[template_name]["input"])
        if not user_prompt:
            print(TEMPLATE_DATA[template_name]["input_blank"])

    # Generate template.
    user_prompt = f"{TEMPLATE_DATA[template_name]["template"]}. Animal: {user_prompt}"

    # Print response.
    print(
        f"\nClaude's response\nMax tokens: {max_tokens}\nSystem prompt: {system_prompt or "None"}"
    )
    print(f"===> {get_completion(user_prompt, system_prompt, max_tokens)}")
