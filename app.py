import os
from flask import Flask, send_from_directory

app = Flask(__name__)

SITE_DIR = os.path.join(os.path.dirname(__file__), "site")

@app.route("/")
def index():
    return send_from_directory(SITE_DIR, "index.html")

@app.route("/<path:path>")
def static_docs(path):
    full_path = os.path.join(SITE_DIR, path)

    if os.path.isdir(full_path):
        return send_from_directory(full_path, "index.html")

    return send_from_directory(SITE_DIR, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)