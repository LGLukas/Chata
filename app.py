from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Liste mit AI-Projektideen
ideen = [
    "🔊 Stimme-Kloner mit KI und Mikrofon",
    "🤖 Chatbot mit Star-Wars-Wissen (kein API, nur lokale Daten)",
    "🎨 Text-to-Image Generator mit Stable Diffusion lokal",
    "🧠 Eigenes kleines neuronales Netz zum Handschrift erkennen",
    "💬 Discord-Bot mit RPG-System & KI-Events",
    "📚 Lern-KI, die deinen Stoff abfragt und dir Quizfragen stellt",
    "📸 Bild-KI, die Bilder erkennt und passende Fakten liefert",
    "🧾 KI, die Rechnungen scannt und automatisch sortiert",
    "📈 Persönliche KI-Analyse deiner Lernstatistiken",
    "🎮 Spiel-KI: NPCs mit eigener Entscheidungslogik"
]

@app.route("/", methods=["GET", "POST"])
def index():
    idee = None
    if request.method == "POST":
        idee = random.choice(ideen)
    return render_template("index.html", idee=idee)

if __name__ == "__main__":
    app.run(debug=True)
