import requests

# ElevenLabs API anahtarını buraya yaz (zaten senin aktif API key’in bu)
API_KEY = "sk_b7d751949a4ab42dc2efac51e9b1b39f84a6ef226d702a6c"

# Karakterlere göre ses ID'leri – Lehçe konuşan sesler
VOICE_IDS = {
    "meli": "EXAVITQu4vr4xnSDxMaL",   # Yasmin Alves (örnek ID, gerekirse değiştiririz)
    "melo": "MF3mGyEYCl7XYWbV9V6O",    # Haven Sands (örnek ID)
    "narrator": "TxGEqnHWrfWFTfGW9XjX" # ElevenLabs varsayılan anlatıcı
}

def generate_mp3(character, text, filename):
    voice_id = VOICE_IDS.get(character.lower())
    if not voice_id:
        return f"[HATA] Tanınmayan karakter: {character}"

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.8
        }
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            with open(f"static/{filename}", "wb") as f:
                f.write(response.content)
            return f"[OK] {filename} başarıyla oluşturuldu."
        else:
            return f"[HATA] Ses üretilemedi: {response.status_code} – {response.text}"
    except Exception as e:
        return f"[HATA] İstek hatası: {str(e)}"
