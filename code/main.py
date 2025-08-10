from api_client import validate_environment_variables
from chat_basic_loop import basic_chat_loop
from chat_graded_response import chat_with_grading
from constants import SYSTEM_PROMPT_DEFAULT


def main():
    print("Basic testing with Anthropic API")
    validate_environment_variables()

    # Basic chat option.
    # basic_chat_loop()

    # Basic chat option with different system prompts.
    # basic_chat(SYSTEM_PROMPT)
    # basic_chat("Your respond should sound like a 3-year old.")

    # Chat with grading.
    chat_with_grading("count_to_three")


if __name__ == "__main__":
    main()
