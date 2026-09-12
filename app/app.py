from flask import Flask, jsonify
import socket
import os
import platform
import datetime

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
DEPLOY_ENV = os.environ.get("DEPLOY_ENV", "development")

@app.route("/")
def home():
    return f"""
    <h2>🚀 Application has been deployed!</h2>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Environment:</b> {DEPLOY_ENV}</p>
    <p><b>Version:</b> {APP_VERSION}</p>
    <p><b>Server Time:</b> {datetime.datetime.utcnow().isoformat()} UTC</p>
    """

@app.route("/health")
def health():
    return "OK", 200

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "environment": DEPLOY_ENV,
        "version": APP_VERSION
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)