from pydantic import BaseModel


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str

    selected_model: str

    classification: str

    confidence: float

    reasoning: str

    estimated_tokens: int

    energy_score: int

    energy_saved_score: int

    estimated_cost_usd: float

    estimated_cost_saved_usd: float

    response_time_ms: float