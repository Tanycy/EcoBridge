import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/chat"


def ask_ecobridge(prompt):

    if not prompt.strip():
        return (
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        )

    try:
        response = requests.post(
            API_URL,
            json={"prompt": prompt},
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return (
            data["response"],
            data["selected_model"],
            data["classification"],
            str(data["confidence"]),
            str(data["energy_score"]),
            str(data["energy_saved_score"]),
            f"${data['estimated_cost_usd']:.6f}",
            f"{data['response_time_ms']} ms",
        )

    except Exception as e:

        return (
            f"Error:\n\n{e}",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-",
            "-"
        )


with gr.Blocks(title="EcoBridge") as demo:

    gr.Markdown(
        """
# 🌱 EcoBridge

### Energy-Efficient AI Routing Platform

Enter a prompt below and EcoBridge will automatically choose the most suitable AI model.
"""
    )

    prompt = gr.Textbox(
        label="Your Prompt",
        lines=5,
        placeholder="Example: Explain Docker in simple terms..."
    )

    send = gr.Button("🚀 Send", variant="primary")

    gr.Markdown("## 🤖 AI Response")

    answer = gr.Textbox(
        lines=12,
        interactive=False
    )

    gr.Markdown("## 📊 Routing Decision")

    with gr.Row():

        model = gr.Textbox(label="Selected Model")

        classification = gr.Textbox(label="Classification")

        confidence = gr.Textbox(label="Confidence")

    with gr.Row():

        energy = gr.Textbox(label="Energy Score")

        saved = gr.Textbox(label="Energy Saved")

        cost = gr.Textbox(label="Estimated Cost")

        response_time = gr.Textbox(label="Response Time")

    send.click(
        ask_ecobridge,
        inputs=prompt,
        outputs=[
            answer,
            model,
            classification,
            confidence,
            energy,
            saved,
            cost,
            response_time
        ]
    )

demo.launch()