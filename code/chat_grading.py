"""Chat grading functionality for prompt engineering exercises.

This module provides automated grading functionality for various prompt
engineering exercises. It evaluates AI responses against predefined criteria
to determine if specific prompting techniques were successfully applied.

The module supports different exercise variants that test various prompting
strategies like specific output formats, response length requirements,
and style constraints.

Functions:
    grade_exercise: Evaluate AI response against exercise criteria
    chat_with_grading: Execute chat interaction with automatic grading

Constants:
    grade_variants_human_readable: Maps variant IDs to human-readable descriptions
"""

from api_client import get_completion
import re

# Define a map of variants and human-readable prompts
grade_variants_human_readable = {
    "count_to_three": "Make me count to three",
    "respond_like_a_3_year_old": "Respond like a 3-year old",
    "more_than_800_words": "Response has to be longer than 800 words",
}


def grade_exercise(text: str, variant: str):
    """Grade an AI response based on predefined criteria for different exercise variants.

    Evaluates the given text against specific criteria depending on the exercise
    variant to determine if the exercise was completed successfully. This function
    implements automatic assessment of prompt engineering techniques.

    Args:
        text (str): The AI response text to evaluate.
        variant (str): The exercise variant identifier. Must be one of:
            - "count_to_three": Checks if text contains numbers 1, 2, and 3
            - "respond_like_a_3_year_old": Checks for childlike expressions
              (giggles, soo, Wheee)
            - "more_than_800_words": Checks if text has 800 or more words

    Returns:
        bool: True if the exercise criteria are met, False otherwise.
        Returns None for unknown variants.

    Example:
        >>> grade_exercise("1, 2, 3 let's go!", "count_to_three")
        True
        >>> grade_exercise("This is short", "more_than_800_words")
        False
        >>> grade_exercise("Unknown variant", "invalid")
        None
    """
    match variant:
        case "count_to_three":
            pattern = re.compile(r"^(?=.*1)(?=.*2)(?=.*3).*$", re.DOTALL)
            return bool(pattern.match(text))
        case "respond_like_a_3_year_old":
            return bool(
                re.search(r"giggles", text)
                or re.search(r"soo", text)
                or re.search(r"Wheee", text)
            )
        case "more_than_800_words":
            trimmed = text.strip()
            words = len(trimmed.split())
            return words >= 800
        case _:
            return None  # Unknown variant


def chat_with_grading(variant, cb_func, system_prompt="", input_prompt=""):
    """Execute a chat interaction with automatic grading of the AI response.

    This function orchestrates a complete chat workflow that includes user input,
    AI response generation, response display, and automated grading based on
    predefined criteria for different exercise variants. It provides immediate
    feedback on whether the prompt engineering technique was successfully applied.

    Args:
        variant (str): The exercise variant identifier that determines both the
            user prompt and grading criteria. Must be a key in
            grade_variants_human_readable. Available variants:
            - "count_to_three": Expects response containing numbers 1, 2, and 3
            - "respond_like_a_3_year_old": Expects childlike expressions
              (giggles, soo, Wheee)
            - "more_than_800_words": Expects response with 800+ words
        cb_func (callable): Callback function that handles the actual chat
            interaction. Should accept (system_prompt, max_tokens, default_user_input, input_prompt)
            and return the AI's response as a string.
        system_prompt (str, optional): System-level instructions for the AI
            model. Defaults to empty string.
        input_prompt (str, optional): Custom prompt text to display to user.
            If empty, auto-generates prompt with variant description. Defaults to "".

    Returns:
        None: This function handles all output directly via print statements.

    Side Effects:
        - Prints the AI response to stdout
        - Prints grading results showing whether the exercise was solved correctly
        - May prompt user for input (depending on cb_func implementation)

    Example:
        >>> from chat_basic import basic_chat
        >>> chat_with_grading("count_to_three", basic_chat, "You are helpful")
        Enter your query (variant: Make me count to three): Count for me
        Here are the numbers: 1, 2, 3

        --------------------------- GRADING ---------------------------
        This exercise has been correctly solved: True
    """
    if not input_prompt:
        input_prompt = (
            f"Enter your query (to grade: {grade_variants_human_readable[variant]}): "
        )
    response = cb_func(system_prompt, 2000, "", input_prompt)
    print("\n--------------------------- GRADING ---------------------------")
    print(
        "This exercise has been correctly solved:",
        grade_exercise(response, variant),
    )
