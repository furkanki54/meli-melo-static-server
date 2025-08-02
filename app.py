from flask import Flask, request, jsonify
from generate_mp3 import generate_mp3
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Meli & Melo MP3 Üretici API Aktif!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    character = data.get("character")
    text = data.get("text")
    filename = data.get("filename")

    if not all([character, text, filename]):
        return jsonify({"error": "character, text ve filename alanları zorunludur."}), 400

    result = generate_mp3(character, text, filename)
    return jsonify({"message": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
