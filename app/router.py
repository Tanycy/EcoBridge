from app.classifier import classify_prompt, classify
 
# Model registry — change model strings here if providers change
MODEL_SIMPLE = "gemini/gemini-2.0-flash"
MODEL_COMPLEX = "gpt-4o"
 
# Human-readable display names for dashboard
MODEL_DISPLAY = {
    MODEL_SIMPLE: "Gemini Flash",
    MODEL_COMPLEX: "GPT-4o",
}
 
 
def select_model(prompt: str) -> str:
    task = classify_prompt(prompt)
    if task == "simple":
        return MODEL_SIMPLE
    return MODEL_COMPLEX
 
def route(prompt: str) -> dict:
    result = classify(prompt)
    model = MODEL_SIMPLE if result.classification == "simple" else MODEL_COMPLEX
 
    return {
        "prompt": result.prompt,
        "prompt_length": result.prompt_length,
        "classification": result.classification,
        "confidence": result.confidence,
        "reasoning": result.reasoning,
        "model": model,
        "model_display": MODEL_DISPLAY[model],
    }
