from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Task 4.2: Docker Deployment</h1><p>My Flask app is running successfully.</p>"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)