from api_client import validate_environment_variables
from chat_basic_loop import basic_chat_loop
from chat_graded_response import chat_with_grading
from constants import SYSTEM_PROMPT_DEFAULT


def main():
    print("Basic testing with Anthropic API")
    validate_environment_variables()

    # Chatper 1: Basic Prompt Structure
    # Basic chat option.
    # basic_chat_loop()

    # Basic chat option with different system prompts.
    # basic_chat_loop("Your respond should sound like a 3-year old.")

    # Chat with grading.
    # chat_with_grading("count_to_three")
    # chat_with_grading("respond_like_a_3_year_old", "Respond like a 3 year old")

    # Chapter 2: Being Clear and Direct
    # basic_chat_loop("", 4000)
    chat_with_grading("more_than_800_words")


if __name__ == "__main__":
    main()
