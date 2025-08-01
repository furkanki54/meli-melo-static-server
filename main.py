from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Meli & Melo ses sunucusu aktif!"

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
