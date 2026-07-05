from app.classifier import classify_prompt, classify
from app.config import SIMPLE_MODEL, COMPLEX_MODEL

# Human-readable names
MODEL_DISPLAY = {
    SIMPLE_MODEL: "GPT-4o Mini",
    COMPLEX_MODEL: "GPT-4o",
}


def select_model(prompt: str) -> str:
    task = classify_prompt(prompt)

    if task == "simple":
        return SIMPLE_MODEL

    return COMPLEX_MODEL


def route(prompt: str) -> dict:

    result = classify(prompt)

    model = (
        SIMPLE_MODEL
        if result.classification == "simple"
        else COMPLEX_MODEL
    )

    return {
        "prompt": result.prompt,
        "prompt_length": result.prompt_length,
        "classification": result.classification,
        "confidence": result.confidence,
        "reasoning": result.reasoning,
        "model": model,
        "model_display": MODEL_DISPLAY[model],
    }