
from flask import Flask, jsonify
from datetime import datetime, timezone
import os
import time

app = Flask(__name__)
started_at = time.time()
request_count = 0

@app.before_request
def count_request():
    global request_count
    request_count += 1

@app.route("/")
def home():
    return """
    <html>
        <head><title>ML DevOps Lab</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 80px;">
            <h1>ML DevOps CI/CD Pipeline</h1>
            <p>Welcome to my Flask web application.</p>
            <p>Deployment and testing environment is running.</p>
            <a href="/health">Check Application Health</a><br><br>
            <a href="/metrics">View Monitoring Metrics</a>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "ML DevOps Lab",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

@app.route("/metrics")
def metrics():
    return jsonify({
        "requests_received": request_count,
        "uptime_seconds": round(time.time() - started_at, 2),
        "status": "UP"
    }), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
