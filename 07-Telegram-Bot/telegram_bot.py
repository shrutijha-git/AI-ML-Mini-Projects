
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


# STEP 1: Load bot token from .env
project_dir = Path(__file__).resolve().parent
load_dotenv(project_dir / ".env")

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# STEP 2: Define responses
TOPICS = {
    "python": (
        "Python is a popular programming language used "
        "in automation, web development, data science, and AI."
    ),
    "machine learning": (
        "Machine learning is a branch of AI that learns "
        "patterns from data."
    ),
    "ml": (
        "Machine learning uses data to train models "
        "that make predictions."
    ),
    "artificial intelligence": (
        "Artificial intelligence enables computers "
        "to perform tasks that require intelligence."
    ),
    "ai": (
        "AI is used in chatbots, recommendations, "
        "computer vision, and many other applications."
    ),
    "nlp": (
        "Natural Language Processing helps computers "
        "understand and process human language."
    ),
    "numpy": (
        "NumPy is a Python library for efficient "
        "numerical computing and arrays."
    ),
    "pandas": (
        "Pandas is a Python library used for "
        "data analysis and manipulation."
    ),
}


# STEP 3: Handle /start
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Hello! Welcome to my AI/ML Learning Bot!\n\n"
        "Ask me about Python, AI, ML, NLP, NumPy, or Pandas.\n"
        "Type /help to see available commands."
    )


# STEP 4: Handle /help
async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show available commands\n"
        "/about - Learn about this bot\n\n"
        "You can also send questions about "
        "Python, AI, ML, NLP, NumPy, and Pandas."
    )


# STEP 5: Handle /about
async def about(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "I am a Python Telegram bot created "
        "as part of an AI/ML mini-project portfolio.\n\n"
        "I use predefined responses to answer "
        "basic programming and AI questions."
    )


# STEP 6: Handle normal text messages
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = update.message.text.lower().strip()

    if text in {"hi", "hello", "hey", "good morning"}:
        response = "Hello! How can I help you today?"

    elif text in {"bye", "goodbye", "see you"}:
        response = "Goodbye! Have a great day!"

    elif "thank" in text:
        response = "You're welcome!"

    else:
        response = None

        # Check longer topic names first.
        for topic in sorted(TOPICS, key=len, reverse=True):
            import re

            if re.search(
                rf"\b{re.escape(topic)}\b",
                text,
            ):
                response = TOPICS[topic]
                break

        if response is None:
            response = (
                "I'm still learning!\n"
                "Ask me about Python, AI, ML, NLP, "
                "NumPy, or Pandas."
            )

    await update.message.reply_text(response)


# STEP 7: Handle unknown commands
async def unknown_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Unknown command. Type /help to see the commands."
    )


# STEP 8: Start the bot
def main():
    if not TOKEN or TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        raise ValueError(
            "Bot token missing! Add your token "
            "to the .env file."
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message,
        )
    )

    app.add_handler(
        MessageHandler(filters.COMMAND, unknown_command)
    )

    print("Telegram bot is running...")
    print("Open Telegram and send /start.")
    print("Press Ctrl+C to stop the bot.")

    app.run_polling()


if __name__ == "__main__":
    main()
