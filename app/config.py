import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# EcoBridge Models
SIMPLE_MODEL = "gpt-4o-mini"
COMPLEX_MODEL = "gpt-4o"

MODEL_CONFIG = {
    SIMPLE_MODEL: {
        "display_name": "GPT-4o Mini",
        "weight": 1,
        "cost_per_1k": 0.00015
    },

    COMPLEX_MODEL: {
        "display_name": "GPT-4o",
        "weight": 8,
        "cost_per_1k": 0.005
    }
}