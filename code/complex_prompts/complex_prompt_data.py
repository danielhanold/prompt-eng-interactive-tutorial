from . import persona_career_coach


PROMPT_ELEMENTS = [
    "HISTORY",
    "QUESTION",
    "TASK_CONTEXT",
    "TONE_CONTEXT",
    "TASK_DESCRIPTION",
    "EXAMPLES",
    "IMMEDIATE_TASK",
    "PRECOGNITION",
    "OUTPUT_FORMATTING",
    "PREFILL",
]

PERSONAS = ["career_coach"]


def _get_prompt_data(persona: str) -> str:
    if persona not in PERSONAS:
        raise ValueError("This persona is not available.")

    return "MyPrompt"


def compose_complex_prompt(persona: str) -> str:
    prompt = _get_prompt_data(persona)

    # if TASK_CONTEXT:
    #     PROMPT += f"""{TASK_CONTEXT}"""

    # if TONE_CONTEXT:
    #     PROMPT += f"""\n\n{TONE_CONTEXT}"""

    # if TASK_DESCRIPTION:
    #     PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

    # if EXAMPLES:
    #     PROMPT += f"""\n\n{EXAMPLES}"""

    # if INPUT_DATA:
    #     PROMPT += f"""\n\n{INPUT_DATA}"""

    # if IMMEDIATE_TASK:
    #     PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

    # if PRECOGNITION:
    #     PROMPT += f"""\n\n{PRECOGNITION}"""

    # if OUTPUT_FORMATTING:
    #     PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

    return prompt
