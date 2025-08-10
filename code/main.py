from api_client import validate_environment_variables
from chat_basic_loop import basic_chat_loop
from chat_graded_response import chat_with_grading

# Define system prompts.
SYSTEM_PROMPT_DEFAULT = "Keep your answer very short. Don't include a lot of background details that the user did not ask for."
SYSTEM_PROMPT_QUESTIONING = "Your answer should always be a series of critical thinking questions that further the conversation. (do not provide answers to your questions). Do not actually answer the user question."
SYSTEM_PROMPT_COMEDIAN = "You are a comedian. You are funny and you make people laugh. You are also a bit of a smart ass. Answer every question in the form of a joke."


def main():
    print("Basic testing with Anthropic API")
    validate_environment_variables()

    # Basic chat option.
    # basic_chat_loop()

    # Basic chat option with different system prompts.
    # basic_chat(SYSTEM_PROMPT)
    # basic_chat("Your respond should sound like a 3-year old.")

    # Chat with grading.
    chat_with_grading("count_to_three", SYSTEM_PROMPT_DEFAULT)


if __name__ == "__main__":
    main()
