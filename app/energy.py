from app.config import SIMPLE_MODEL, COMPLEX_MODEL

# EcoBridge Relative Computational Weights
MODEL_WEIGHTS = {
    SIMPLE_MODEL: 1,
    COMPLEX_MODEL: 8
}

# Estimated API cost per 1000 tokens (USD)
MODEL_COST = {
    SIMPLE_MODEL: 0.000075,
    COMPLEX_MODEL: 0.005
}


def estimate_tokens(prompt: str):
    return max(1, len(prompt) // 4)


def calculate_energy(model: str, prompt: str):

    tokens = estimate_tokens(prompt)
    print("Model:", model)
    print("MODEL_WEIGHTS:", MODEL_WEIGHTS)

    energy_score = MODEL_WEIGHTS[model]

    baseline_score = MODEL_WEIGHTS[COMPLEX_MODEL]

    energy_saved_score = baseline_score - energy_score

    estimated_cost = MODEL_COST[model] * (tokens / 1000)

    baseline_cost = MODEL_COST[COMPLEX_MODEL] * (tokens / 1000)

    estimated_cost_saved = baseline_cost - estimated_cost

    return {
        "estimated_tokens": tokens,
        "energy_score": energy_score,
        "energy_saved_score": energy_saved_score,
        "estimated_cost_usd": round(estimated_cost, 6),
        "estimated_cost_saved_usd": round(estimated_cost_saved, 6)
    }