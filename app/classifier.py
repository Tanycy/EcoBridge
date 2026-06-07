def classify_prompt(prompt: str):

    complex_keywords = [
        "analyze",
        "compare",
        "algorithm",
        "calculate",
        "explain"
    ]

    for word in complex_keywords:

        if word in prompt.lower():

            return "complex"

    return "simple"