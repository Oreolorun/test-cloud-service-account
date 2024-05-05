from flask import Flask, jsonify, request

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


if __name__ == "__main__":
    app.run(debug=True)
