from api_client import validate_environment_variables
from chat_basic import basic_chat, basic_chat_loop
from chat_grading import chat_with_grading
from chat_templates import basic_chat_template
from constants import SYSTEM_PROMPT_DEFAULT


def main():
    """Main entry point for the Anthropic prompt engineering tutorial.

    Demonstrates various prompt engineering techniques through interactive
    chat examples. Contains code for multiple tutorial chapters covering
    basic prompts, role prompting, data separation, and more. Most examples
    are commented out by default.

    Current active example: Chat with grading using "respond_like_a_3_year_old"
    variant to demonstrate childlike response patterns.

    Tutorial Chapters Covered:
    - Chapter 1: Basic Prompt Structure
    - Chapter 2: Being Clear and Direct
    - Chapter 3: Role Prompting
    - Chapter 4: Separating Data & Instructions

    Side Effects:
        - Validates environment variables (API key, model name)
        - Prints tutorial progress messages
        - May prompt user for input and display AI responses

    Raises:
        ValueError: If required environment variables are not set.
    """
    print("Basic testing with Anthropic API")
    validate_environment_variables()

    ###
    # Chatper 1: Basic Prompt Structure
    ###
    # Basic chat option.
    # basic_chat_loop()

    # Basic chat option with different system prompts.
    # basic_chat_loop("Your respond should sound like a 3-year old.")

    # Chat with grading.
    # chat_with_grading("count_to_three")
    chat_with_grading(
        "respond_like_a_3_year_old", basic_chat, "Respond like a giggly 3 year old"
    )

    ###
    # Chapter 2: Being Clear and Direct
    ###
    # basic_chat_loop("", 4000)
    # chat_with_grading("more_than_800_words")

    ###
    # Chatper 3: Role prompting
    ###
    # basic_chat("You are a cat.", 2000, "What do you think about skateboarding")
    # basic_chat(
    #     "you are a cat talking to a crowd of skateboarders.",
    #     2000,
    #     "What do you think about skateboarding",
    # )

    # # In earlier versions of Claude, the model would not be able to answer this question.
    # basic_chat(
    #     "",
    #     2000,
    #     "Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?",
    # )

    # # With a system prompt, the model can answer the question.
    # basic_chat(
    #     "You are a logic bot designed to answer complex logic problems.",
    #     2000,
    #     "Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?",
    # )

    ###
    # Chatper 4: Separating Data & Instructions
    ###
    # basic_chat_template("animal_sound")
    # basic_chat_template(
    #     "polite_email",
    #     "",
    #     2000,
    #     "Show up at 6am tomorrow because I'm the CEO and I say so.",
    # )
    # basic_chat_template("identify_second_item")


if __name__ == "__main__":
    main()
