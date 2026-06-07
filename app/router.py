from app.classifier import classify_prompt

def select_model(prompt):

    task = classify_prompt(prompt)

    if task == "simple":

        return "gemini-flash"

    return "gpt-4o"