from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simple dataset for quotes/poems
poems = {
    "rain": [
        "The rain falls gently, a song of peace, washing worries into release.",
        "Drops like silver threads stitch the sky, weaving calm as clouds pass by."
    ],
    "happy": [
        "Happiness blooms where kindness is sown.",
        "A smile is sunshine you wear on your soul."
    ],
    "love": [
        "Love is the gentle fire that warms the coldest night.",
        "Two hearts, one rhythm — love’s eternal song."
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    keyword = request.form.get("keyword", "").lower()
    if keyword in poems:
        result = random.choice(poems[keyword])
    else:
        result = "Sorry, I don’t have poems for that word yet. Try 'rain', 'happy', or 'love'."
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
