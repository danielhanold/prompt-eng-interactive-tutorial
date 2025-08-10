from api_client import get_completion


def basic_chat_loop(system_prompt=""):
    is_first_run = True
    while True:
        glue_word = "your" if is_first_run else "another"
        default_query = "What is Celine Dion's single most popular song?"
        user_prompt = (
            input(f"\nEnter {glue_word} query [{default_query}]: ") or default_query
        )
        if not user_prompt:
            user_prompt = default_query

        print("Claude's response:")
        print(get_completion(user_prompt, system_prompt))
        is_first_run = False
