import os

from litellm import completion

from app.config import OPENAI_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY or ""


def generate_response(model: str, prompt: str):

    response = completion(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content