
import re

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# STEP 1: Predefined chatbot knowledge
RESPONSES = {
    "machine learning": (
        "Machine learning is a branch of artificial intelligence "
        "where computers learn patterns from data."
    ),
    "artificial intelligence": (
        "Artificial intelligence enables computers to perform "
        "tasks that normally require human intelligence."
    ),
    "natural language processing": (
        "Natural Language Processing helps computers understand "
        "and work with human language."
    ),
    "python": (
        "Python is a popular programming language used in "
        "AI, data science, automation, and web development."
    ),
    "flask": (
        "Flask is a lightweight Python web framework "
        "used to build websites and APIs."
    ),
    "numpy": (
        "NumPy is a Python library for numerical computing "
        "and working with arrays."
    ),
    "pandas": (
        "Pandas is a Python library used for data analysis "
        "and working with structured datasets."
    ),
    "nlp": (
        "NLP stands for Natural Language Processing. "
        "It helps computers process human language."
    ),
    "ml": (
        "ML stands for Machine Learning, which allows "
        "computers to learn patterns from data."
    ),
    "ai": (
        "AI stands for Artificial Intelligence. "
        "It is used in chatbots, recommendations, "
        "image recognition, and other applications."
    ),
}


# STEP 2: Chatbot response logic
def get_bot_response(message):
    text = message.lower().strip()

    if not text:
        return "Please enter a message."

    if text in {"hi", "hello", "hey", "good morning"}:
        return "Hello! How can I help you today?"

    if text in {"bye", "goodbye", "see you"}:
        return "Goodbye! Have a wonderful day!"

    if "thank" in text:
        return "You're welcome! Happy to help."

    if "your name" in text:
        return "I'm your AI Learning Chatbot, built using Flask!"

    if "what can you do" in text or text == "help":
        return (
            "I can answer basic questions about Python, AI, ML, "
            "NLP, NumPy, Pandas, and Flask."
        )

    # Check longer phrases first and match whole words.
    for topic in sorted(RESPONSES, key=len, reverse=True):
        if re.search(rf"\b{re.escape(topic)}\b", text):
            return RESPONSES[topic]

    return (
        "I'm still learning! Try asking me about "
        "Python, AI, ML, NLP, NumPy, Pandas, or Flask."
    )


# STEP 3: Home page
@app.route("/")
def home():
    return render_template("index.html")


# STEP 4: Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Please send a JSON object."
        }), 400

    message = data.get("message")

    if not isinstance(message, str):
        return jsonify({
            "error": "The message must be text."
        }), 400

    if len(message) > 2000:
        return jsonify({
            "error": "Message is too long."
        }), 400

    response = get_bot_response(message)

    return jsonify({
        "response": response
    })


# STEP 5: Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
