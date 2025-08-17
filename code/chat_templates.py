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

EMAIL_REWRITE_STYLE = "olde english"

MOVIE_REVIEW_INPUT = """Is this movie review sentiment positive or negative?

This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since the year 1900."""

EMAILS = [
    "Hi -- My Mixmaster4000 is producing a strange noise when I operate it. It also smells a bit smoky and plasticky, like burning electronics.  I need a replacement.",  # (B) Broken or defective item
    "Can I use my Mixmaster 4000 to mix paint, or is it only meant for mixing food?",  # (A) Pre-sale question OR (D) Other (please explain)
    "I HAVE BEEN WAITING 4 MONTHS FOR MY MONTHLY CHARGES TO END AFTER CANCELLING!!  WTF IS GOING ON???",  # (C) Billing question
    "How did I get here I am not good with computer.  Halp.",  # (D) Other (please explain)
]

EMAIL_CLASSIFICATIONS = """
    (A) Pre-sale question
    (B) Broken or defective item
    (C) Billing question
    (D) Other (please explain)
"""

EMAIL_CLASSIFICATION_FEW_SHOT_PROMPTING_EXAMPLES = """
    Email Content: Can I use my Mixmaster 4000 to mix paint, or is it only meant for mixing food?

    Category:
    Pre-sale question

    Classification:
    A


    Email Content: I HAVE BEEN WAITING 4 MONTHS FOR MY MONTHLY CHARGES TO END AFTER CANCELLING!!  WTF IS GOING ON???

    Category:
    Billing qusetion

    Classification:
    C
"""

with open("templates/individuals_jobs_description_prefix.txt", "r") as f:
    INDIVIDUALS_JOB_DESCRIPTION_PREFIX = f.read()

with open("templates/matterport_suffix.txt", "r") as f:
    MATTERPORT_SUFFIX = f.read()

with open("templates/matterport_10k_filing.txt", "r") as f:
    MATTERPORT_10K_FILING = f.read()

INDIVIDUALS_JOB_DESCRIPTION_DEFAULT_USER_INPUT = """Oak Valley, a charming small town, is home to a remarkable trio of individuals whose skills and dedication have left a lasting impact on the community.
At the town's bustling farmer's market, you'll find Laura Simmons, a passionate organic farmer known for her delicious and sustainably grown produce. Her dedication to promoting healthy eating has inspired the town to embrace a more eco-conscious lifestyle.
In Oak Valley's community center, Kevin Alvarez, a skilled dance instructor, has brought the joy of movement to people of all ages. His inclusive dance classes have fostered a sense of unity and self-expression among residents, enriching the local arts scene.
Lastly, Rachel O'Connor, a tireless volunteer, dedicates her time to various charitable initiatives. Her commitment to improving the lives of others has been instrumental in creating a strong sense of community within Oak Valley.
Through their unique talents and unwavering dedication, Laura, Kevin, and Rachel have woven themselves into the fabric of Oak Valley, helping to create a vibrant and thriving small town."""

TEMPLATE_DATA = {
    "animal_sound": {
        "template_prefix": "I will tell you the name of an animal. Please respond with the noise that this animal makes:",
        "template_suffix": "",
        "user_input_hint": "Chatbot will tell you the noise an animal makes\nEnter the name of an animal: ",
        "default_user_input": "",
        "assistant_prefill": "",
    },
    "polite_email": {
        "template_prefix": "For Claude.",
        "template_suffix": "<----- Make this email more polite but don't change anything else about it.",
        "user_input_hint": "Enter a rude email message that should be polished to make it sound more polite: ",
        "default_user_input": "",
        "assistant_prefill": "",
    },
    "identify_second_item": {
        "template_prefix": """Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.\n""",
        "template_suffix": "",
        "user_input_hint": "Don't enter anything - there are three default sentences defined in code: ",
        "default_user_input": SENTENCES,
        "assistant_prefill": "",
    },
    "haiku_topic": {
        "template_prefix": "Create a Haiku based on the following topic:",
        "template_suffix": "Start the response with a header: Your Haiku:",
        "user_input_hint": "Enter a topic and I will create a Haiku: ",
        "default_user_input": "",
        "assistant_prefill": "",
    },
    "haiku_topic_xml": {
        "template_prefix": "Create a Haiku based on the following topic:",
        "template_suffix": "Put it in XML tags.",
        "user_input_hint": "Enter a topic and I will create a Haiku: ",
        "default_user_input": "",
        "assistant_prefill": "",
    },
    "haiku_topic_xml_multiple": {
        "template_prefix": "Create a Haiku based on the following topic:",
        "template_suffix": "Put it in XML tags.",
        "user_input_hint": "Enter a topic and I will create a Haiku: ",
        "default_user_input": "",
        "assistant_prefill": "I will give the user two versions, and will use <haiku_a> and <haiku_b> respectively",
    },
    "haiku_topic_json": {
        "template_prefix": "Create a Haiku based on the following topic:",
        "template_suffix": "",
        "user_input_hint": "Enter a topic and I will create a Haiku: ",
        "default_user_input": "",
        # If you want to enforce JSON output (not deterministically, but close to it), you can prefill the assistant response.
        "assistant_prefill": 'Use JSON format with the keys as "first_line", "second_line", "third_line" etc.',
    },
    "olde_english_email": {
        "template_prefix": "Here is an email message:",
        "template_suffix": f"Make this email more {EMAIL_REWRITE_STYLE}.",
        "user_input_hint": "A sample message is already provided [Hi Zack, just pinging you for a quick update on that prompt you were supposed to write.]: ",
        "default_user_input": "Hi Zack, just pinging you for a quick update on that prompt you were supposed to write.",
        "assistant_prefill": f"<{EMAIL_REWRITE_STYLE.replace(" ", "_")}_email>",
    },
    "stephen_curry_goat": {
        "template_prefix": "",
        "template_suffix": "",
        "user_input_hint": "A sample message is already provided [Who is the best basketball player of all time? Please choose one specific player.]: ",
        "default_user_input": "Who is the best basketball player of all time? Please choose one specific player.",
        "assistant_prefill": "Stephen Curry is the best basketball player of all time because",
    },
    "movie_reviewer": {
        "template_prefix": "",
        "template_suffix": "",
        "user_input_hint": f"A sample message is already provided [{MOVIE_REVIEW_INPUT}]: ",
        "default_user_input": MOVIE_REVIEW_INPUT,
        "assistant_prefill": "",
    },
    "famous_movie_star": {
        "template_prefix": "",
        "template_suffix": "First brainstorm about some actors and their birth years in XML tags, then give your answer.",
        "user_input_hint": f"A sample message is already provided [Name a famous movie starring an actor who was born in the year 1956.]: ",
        "default_user_input": "Name a famous movie starring an actor who was born in the year 1956.",
        "assistant_prefill": "",
    },
    "misspelling": {
        "template_prefix": "Hia its me i have a q about dogs jkaerjv",
        "template_suffix": "jklmvca tx it help me muhch much atx fst fst answer short short tx",
        "user_input_hint": "Don't enter anything - default is provided as: ar cn brown?",
        "default_user_input": "ar cn brown?",
        "assistant_prefill": "",
    },
    "categorize_emails": {
        "template_prefix": f"Please classify this email into one of the following four categories {EMAIL_CLASSIFICATIONS}:",
        "template_suffix": "Return only the letter of the category and name of the category",
        "user_input_hint": "Don't enter anything - default is provided as",
        "default_user_input": "",
        "assistant_prefill": "",
    },
    "categorize_emails_letter_response": {
        "template_prefix": f"Please classify this email into one of the following four categories {EMAIL_CLASSIFICATIONS}:",
        "template_suffix": "Return only the letter wrapped in the following XML tag: <answer>",
        "user_input_hint": "Don't enter anything - default is provided as",
        "default_user_input": "",
        "assistant_prefill": "",
    },
    "categorize_emails_few_shot_prompting": {
        "template_prefix": EMAIL_CLASSIFICATION_FEW_SHOT_PROMPTING_EXAMPLES,
        "template_suffix": f"Please classify this email into one of the following four categories {EMAIL_CLASSIFICATIONS}. Follow the same output format as above, including whitespacing and line breaks. The category cannot be a single letter",
        "user_input_hint": "Don't enter anything - default is provided as",
        "default_user_input": "",
        "assistant_prefill": "",
    },
    "individuals_professions": {
        "template_prefix": INDIVIDUALS_JOB_DESCRIPTION_PREFIX,
        "template_suffix": "List all key individuals and their professions.",
        "user_input_hint": "Don't enter anything - default is provided as.",
        "default_user_input": INDIVIDUALS_JOB_DESCRIPTION_DEFAULT_USER_INPUT,
        "assistant_prefill": "",
    },
    "matterport_subscriber_base": {
        "template_prefix": "",
        "template_suffix": MATTERPORT_SUFFIX,
        "user_input_hint": "Don't enter anything - default is provided as.",
        "default_user_input": """What was Matterport's subscriber base on the precise date of May 31, 2020?
            Please read the below document. Then write a brief numerical answer inside tags.
            Then, in XML tags, pull the most relevant quote from the document and consider whether it answers the user's question or whether it lacks sufficient detail.
            Then write a brief numerical answer in XML tags.
        """,
        "assistant_prefill": "",
    },
    "matterport_subscriber_growth": {
        "template_prefix": "",
        "template_suffix": MATTERPORT_10K_FILING,
        "user_input_hint": "Don't enter anything - default is provided as.",
        "default_user_input": """From December 2018 to December 2022, by what amount did Matterport's subscribers grow?
            Show your train of thought by showing the subscriber numbers in all years.
            Calculate the multiple it grew by, e.g. 10-fold""",
        "assistant_prefill": "",
    },
}


def get_chat_template_data(template_name: str, default_user_input="") -> dict:
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
        default_user_input (str): Sets the default user input. If this is set,
            overwrites any templated default user input.

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

    # Some templates provide a default user input, which will be used unless
    # a custom default user input is provided to this function.
    if not default_user_input:
        default_user_input = TEMPLATE_DATA[template_name].get("default_user_input", "")

    return {
        "template_prefix": TEMPLATE_DATA[template_name]["template_prefix"],
        "template_suffix": TEMPLATE_DATA[template_name]["template_suffix"],
        "user_input_hint": TEMPLATE_DATA[template_name]["user_input_hint"],
        "default_user_input": default_user_input,
        "assistant_prefill": TEMPLATE_DATA[template_name]["assistant_prefill"],
    }
