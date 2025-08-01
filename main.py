from flask import Flask, send_from_directory
import os

# Flask uygulaması tanımlanıyor
app = Flask(__name__, static_folder='static')

# Anasayfa
@app.route('/')
def home():
    return '✅ Meli & Melo ses sunucusu aktif!'

# MP3 dosyaları için URL
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Uygulama başlatılıyor
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
