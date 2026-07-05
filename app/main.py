import time

from fastapi import FastAPI

from app.models import ChatRequest
from app.router import route
from app.llm import generate_response
from app.energy import calculate_energy
from app.database import create_database, insert_request

app = FastAPI(
    title="EcoBridge API",
    description="Energy-Aware AI Routing Platform",
    version="1.0"
)

# Create database when FastAPI starts
create_database()


@app.get("/")
def home():
    return {
        "project": "EcoBridge",
        "version": "1.0",
        "status": "Running"
    }


@app.get("/route")
def test_route(prompt: str):
    """
    Test only the routing engine.
    """
    return route(prompt)


@app.post("/chat")
def chat(request: ChatRequest):

    start_time = time.perf_counter()

    # Step 1: Classify & Route
    routing_result = route(request.prompt)

    # Step 2: Call AI Model
    ai_response = generate_response(
        model=routing_result["model"],
        prompt=request.prompt
    )

    # Step 3: Calculate Energy & Cost
    energy_result = calculate_energy(
        routing_result["model"],
        request.prompt
    )

    # Step 4: Response Time
    response_time = round(
        (time.perf_counter() - start_time) * 1000,
        2
    )

    # Step 5: Save into Database
    insert_request({

        "prompt": request.prompt,
        "response": ai_response,

        "classification": routing_result["classification"],
        "confidence": routing_result["confidence"],
        "reasoning": routing_result["reasoning"],

        "selected_model": routing_result["model_display"],

        "estimated_tokens": energy_result["estimated_tokens"],

        "energy_score": energy_result["energy_score"],
        "energy_saved_score": energy_result["energy_saved_score"],

        "estimated_cost_usd": energy_result["estimated_cost_usd"],
        "estimated_cost_saved_usd": energy_result["estimated_cost_saved_usd"],

        "response_time_ms": response_time
    })

    # Step 6: Return Response
    return {

        "response": ai_response,

        "classification": routing_result["classification"],

        "confidence": routing_result["confidence"],

        "reasoning": routing_result["reasoning"],

        "selected_model": routing_result["model_display"],

        "estimated_tokens": energy_result["estimated_tokens"],

        "energy_score": energy_result["energy_score"],

        "energy_saved_score": energy_result["energy_saved_score"],

        "estimated_cost_usd": energy_result["estimated_cost_usd"],

        "estimated_cost_saved_usd": energy_result["estimated_cost_saved_usd"],

        "response_time_ms": response_time
    }