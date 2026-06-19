from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hitachi Energy Test Lab is running!"


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "UP"
        }
    )


@app.route("/version")
def version():
    return jsonify(
        {
            "version": "1.0"
        }
    )


@app.route("/users")
def users():
    return jsonify(
        [
            {
                "id": 1,
                "name": "Alice"
            },
            {
                "id": 2,
                "name": "Bob"
            }
        ]
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )