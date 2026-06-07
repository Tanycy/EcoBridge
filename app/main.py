from fastapi import FastAPI
from app.router import select_model

app = FastAPI()

@app.get("/")
def home():

    return {
        "project": "EcoBridge"
    }

@app.get("/route")
def route(prompt: str):

    model = select_model(prompt)

    return {
        "prompt": prompt,
        "selected_model": model
    }