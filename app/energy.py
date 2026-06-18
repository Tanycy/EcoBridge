"""
Sources / assumptions:
- Token estimate: 1 token ≈ 4 characters (standard approximation)
- Energy per 1K tokens: Gemini Flash ~0.0003 kWh, GPT-4o ~0.003 kWh
  (GPT-4o is ~10x heavier — consistent with the energy_scores ratio
   already established in the project: gemini-flash=1, gpt-4o=10)
- Carbon intensity: 0.5 kg CO2/kWh (average global data centre, IEA 2023)
- Cost per 1K tokens: Gemini Flash $0.000075, GPT-4o $0.005
"""
 
# Backward-compatible scores (kept for any existing references)
energy_scores = {
    "gemini/gemini-2.0-flash": 1,
    "gpt-4o": 10,
    # Legacy short names
    "gemini-flash": 1,
}
 
# Energy consumed per 1,000 tokens (kWh)
ENERGY_PER_1K_TOKENS_KWH = {
    "gemini/gemini-2.0-flash": 0.0003,
    "gpt-4o": 0.003,
    "gemini-flash": 0.0003,   # legacy alias
}
 
# Cost per 1,000 tokens (USD)
COST_PER_1K_TOKENS_USD = {
    "gemini/gemini-2.0-flash": 0.000075,
    "gpt-4o": 0.005,
    "gemini-flash": 0.000075,
}
 
# Carbon intensity: grams of CO2 per kWh
CARBON_G_PER_KWH = 500
 
def _estimate_tokens(prompt: str) -> int:
    #Rough token count: 1 token ≈ 4 characters
    return max(1, len(prompt) // 4)
 
def calculate_energy(model: str, prompt: str = "") -> dict:
    """
    Calculate energy, carbon, and cost for a single request.
    Also returns savings versus always routing to gpt-4o.
 
    Parameters
    ----------
    model  : LiteLLM model string (e.g. 'gemini/gemini-2.0-flash')
    prompt : The original prompt text (used to estimate token count)
 
    Returns
    -------
    dict with keys:
        model              - model string used
        estimated_tokens   - rough token count
        energy_kwh         - estimated energy consumed (kWh)
        carbon_g           - estimated CO2 emitted (grams)
        cost_usd           - estimated API cost (USD)
        energy_saved_kwh   - kWh saved vs always using gpt-4o
        carbon_saved_g     - grams CO2 saved vs always using gpt-4o
        cost_saved_usd     - USD saved vs always using gpt-4o
        energy_score       - relative score (1=light, 10=heavy)
    """
    tokens = _estimate_tokens(prompt)
    tokens_k = tokens / 1000
 
    energy_rate = ENERGY_PER_1K_TOKENS_KWH.get(model, 0.003)
    cost_rate = COST_PER_1K_TOKENS_USD.get(model, 0.005)
    score = energy_scores.get(model, 10)
 
    energy_kwh = energy_rate * tokens_k
    carbon_g = energy_kwh * CARBON_G_PER_KWH
    cost_usd = cost_rate * tokens_k
 
    # Savings = what gpt-4o would have cost minus what we actually used
    heavy_energy = ENERGY_PER_1K_TOKENS_KWH["gpt-4o"] * tokens_k
    heavy_carbon = heavy_energy * CARBON_G_PER_KWH
    heavy_cost = COST_PER_1K_TOKENS_USD["gpt-4o"] * tokens_k
 
    return {
        "model": model,
        "estimated_tokens": tokens,
        "energy_kwh": round(energy_kwh, 8),
        "carbon_g": round(carbon_g, 6),
        "cost_usd": round(cost_usd, 8),
        "energy_saved_kwh": round(heavy_energy - energy_kwh, 8),
        "carbon_saved_g": round(heavy_carbon - carbon_g, 6),
        "cost_saved_usd": round(heavy_cost - cost_usd, 8),
        "energy_score": score,
    }
