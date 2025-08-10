from api_client import get_completion


def basic_chat_loop(system_prompt="", max_tokens=2000):
    is_first_run = True
    while True:
        glue_word = "your" if is_first_run else "another"
        default_query = "What is Celine Dion's single most popular song?"
        user_prompt = (
            input(f"\nEnter {glue_word} query [{default_query}]: ") or default_query
        )
        if not user_prompt:
            user_prompt = default_query

        print(f"Claude's response (max tokens: {max_tokens}):")
        print(get_completion(user_prompt, system_prompt, max_tokens))
        is_first_run = False
