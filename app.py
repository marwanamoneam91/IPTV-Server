from flask import Flask, send_from_directory
import os

app = Flask(__name__)
VIDEO_FOLDER = "videos"

@app.route("/videos/<path:filename>")
def serve_video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

@app.route("/")
def home():
    return "Server is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
