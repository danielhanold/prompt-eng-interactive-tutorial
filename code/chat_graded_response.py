from api_client import get_completion
import re

# Define a map of variants and human-readable prompts:
grade_variants_human_readable = {
    "count_to_three": "Make me count to three",
    "respond_like_a_3_year_old": "Respond like a 3-year old",
}


def single_chat(variant, system_prompt=""):
    user_prompt = ""
    while not user_prompt:
        user_prompt = input(
            f"\nEnter your query [variant: {grade_variants_human_readable[variant]}]: "
        )
        if not user_prompt:
            print("User prompt cannot be empty. Enter something!")

    return get_completion(user_prompt, system_prompt)


def grade_exercise(text, variant):
    match variant:
        case "count_to_three":
            pattern = re.compile(r"^(?=.*1)(?=.*2)(?=.*3).*$", re.DOTALL)
            return bool(pattern.match(text))
        case "respond_like_a_3_year_old":
            return bool(re.search(r"giggles", text) or re.search(r"soo", text))


def chat_with_grading(variant, system_prompt=""):
    response = single_chat(variant, system_prompt)
    print(response)
    print("\n--------------------------- GRADING ---------------------------")
    print(
        "This exercise has been correctly solved:",
        grade_exercise(response, variant),
    )
