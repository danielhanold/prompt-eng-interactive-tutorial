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
        "user_input_hint": "Chatbot will tell you the noise an animal makes\nEnter the name of an animal: ",
    },
    "polite_email": {
        "template_prefix": "For Claude.",
        "template_suffix": "<----- Make this email more polite but don't change anything else about it.",
        "user_input_hint": "Enter a rude email message that should be polished to make it sound more polite: ",
    },
    "identify_second_item": {
        "template_prefix": """Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.\n""",
        "template_suffix": "",
        "user_input_hint": "Don't enter anything - there are three default sentences defined in code: ",
    },
    "haiku_topic": {
        "template_prefix": "Create a Haiku based on the following topic:",
        "template_suffix": "Start the response with a header: Your Haiku:",
        "user_input_hint": "Enter a topic and I will create a Haiku: ",
    },
    "haiku_topic_xml": {
        "template_prefix": "Create a Haiku based on the following topic:",
        "template_suffix": "Put it in XML tags.",
        "user_input_hint": "Enter a topic and I will create a Haiku: ",
    },
    "misspelling": {
        "template_prefix": "Hia its me i have a q about dogs jkaerjv",
        "template_suffix": "jklmvca tx it help me muhch much atx fst fst answer short short tx",
        "user_input_hint": "Don't enter anything - default is provided as: ar cn brown?",
    },
}


def get_chat_template_data(template_name: str) -> dict:
    """Retrieve template configuration data for a given template name.

    This function validates the template name and returns the complete
    configuration including template prefix/suffix, user input query,
    and any default user input for the specified template. The function
    automatically handles template-specific default inputs based on the
    template type.

    Args:
        template_name (str): Name of the template to retrieve. Must be a key
            in TEMPLATE_DATA. Available templates include:
            - "animal_sound": Ask for animal sounds
            - "polite_email": Convert rude emails to polite ones
            - "identify_second_item": Identify second item in predefined list

    Returns:
        dict: Template configuration containing:
            - template_prefix (str): Text to prepend to user input
            - template_suffix (str): Text to append to user input
            - user_input_hint (str): Prompt text to display to user
            - default_user_input (str): Default input for certain templates

    Raises:
        ValueError: If template_name is not found in TEMPLATE_DATA.

    Example:
        >>> config = get_chat_template_data("animal_sound")
        >>> print(config["user_input_hint"])
        Chatbot will tell you the noise an animal makes
        Enter the name of an animal:
    """
    # Validate template_name.
    if template_name not in TEMPLATE_DATA.keys():
        raise ValueError("Template name is not valid.")

    # Determine if a default should be provided for the user input in this template.
    default_user_input = ""
    match template_name:
        case "identify_second_item":
            default_user_input = SENTENCES
        case "misspelling":
            default_user_input = "ar cn brown?"
        case _:
            default_user_input = ""

    return {
        "template_prefix": TEMPLATE_DATA[template_name]["template_prefix"],
        "template_suffix": TEMPLATE_DATA[template_name]["template_suffix"],
        "user_input_hint": TEMPLATE_DATA[template_name]["user_input_hint"],
        "default_user_input": default_user_input,
    }
