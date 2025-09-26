from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/hello")
def hello():
    return "Hello from Flask!"

if __name__ == "__main__":
    # For local testing only
    app.run(host="0.0.0.0", port=5000)

