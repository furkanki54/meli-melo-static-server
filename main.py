from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return 'Meli & Melo Static Server Aktif!'

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
