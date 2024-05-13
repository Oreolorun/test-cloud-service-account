from flask import Flask, jsonify, request
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

app = Flask(__name__)


@app.get("/")
def home_page():
    return jsonify(
        {
            "text": "Welcome"
        }
    )


@app.get("/user")
def user():
    name = request.args.get("name", "stranger")
    return jsonify(
        {
            "text": f"Hello {name}"
        }
    )


@app.get("/profession/<job>")
def job(job):
    return jsonify(
        {
            "text": job
        }
    )


@app.post("/llm")
def llm():
    text = request.json.get("prompt", "Say hello and inform user there is no prompt")

    generation_config = {
        "max_output_tokens": 573,
        "temperature": 1,
        "top_p": 1,
    }

    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    vertexai.init(project="personal-projects-421515", location="europe-west1")
    model = GenerativeModel(
        "gemini-1.0-pro-002",
    )
    responses = model.generate_content(
        [text],
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    return jsonify(responses.candidates[0].content.parts[0].text)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
