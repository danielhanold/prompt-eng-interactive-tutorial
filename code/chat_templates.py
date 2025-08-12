# <user_input> - Wraps raw text provided by the end user, often unaltered, so the LLM can distinguish it from control instructions.
# <query> - Encapsulates a specific question or search request for the LLM to address.
# <instructions> - Marks developer-provided guidance on how the LLM should respond or behave.
# <context> - Provides relevant background or situational details for the LLM to use when answering.
# <examples> - Contains sample inputs and outputs to illustrate the desired response style or format.
# <metadata> - Holds auxiliary data (e.g., user ID, timestamps) that is not part of the natural language prompt but may influence processing.

from api_client import get_completion

SENTENCES = """- I like how cows sound
- This sentence is about spiders
- This sentence may appear to be about dogs but it's actually about pigs"""

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
    "identify_second_item": {
        "template_prefix": """Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.\n""",
        "template_suffix": "",
        "input": "Don't enter anything - there are three default sentences defined in code.",
        "input_blank": "You have to actually enter the a message - it cannot be blank!",
    },
}


def basic_chat_template(
    template_name: str, system_prompt="", max_tokens=2000, default_query=""
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
        default_query (str, optional): Default query to use if user provides
            no input (only for templates that prompt for user input). Defaults to "".

    Returns:
        None: This function handles all output directly via print statements.

    Raises:
        ValueError: If template_name is not found in TEMPLATE_DATA.

    Side Effects:
        - Prints template instructions and prompts to stdout
        - May prompt user for input via stdin (depending on template)
        - Prints formatted user prompt, system prompt, and AI response to stdout

    Example:
        >>> basic_chat_template("animal_sound")
        >>> basic_chat_template("polite_email", "Be very polite", 1000, "I'm busy!")
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

    print(f"===> {get_completion(user_prompt, system_prompt, max_tokens)}")
