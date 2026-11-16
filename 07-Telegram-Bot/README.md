# Project 7 — Telegram Bot Using Python

## Project Overview

This project implements a Telegram chatbot using Python and the Telegram Bot API. It responds to user messages, handles commands, and provides basic explanations of Python and AI/ML concepts.

The bot uses the `python-telegram-bot` library to communicate with Telegram. It runs using long polling, which allows the program to receive messages without setting up a public web server.

This is a rule-based chatbot rather than a machine learning model. It demonstrates API integration, asynchronous programming, environment variables, and event-driven message handling.

## Technologies Used

- Python
- Telegram Bot API
- python-telegram-bot
- python-dotenv
- Environment variables

## Project Structure

```text
07-Telegram-Bot/
├── telegram_bot.py
├── requirements.txt
├── README.md
├── .env.example
└── .env
```

The `.env` file is local and must not be uploaded to GitHub.

## Features

- Responds to `/start`, `/help`, and `/about`
- Handles greetings and goodbyes
- Answers basic questions about Python, AI, ML, NLP, NumPy, and Pandas
- Provides fallback responses for unsupported topics
- Uses environment variables to protect the bot token

## How It Works

1. BotFather creates the Telegram bot and provides an API token.
2. The token is stored locally in `.env`.
3. Python loads the token using `python-dotenv`.
4. The application connects to Telegram using `python-telegram-bot`.
5. Command handlers process Telegram commands.
6. A message handler processes ordinary text.
7. The bot sends a predefined response based on message content.

## Setup Instructions

### 1. Create a Telegram Bot

Open [BotFather](https://t.me/BotFather) in Telegram.

Send `/newbot` and follow the instructions.

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```dotenv
TELEGRAM_BOT_TOKEN=your_actual_token_here
```

Never publish the actual token.

### 4. Run the Bot

```bash
python telegram_bot.py
```

### 5. Test the Bot

Open the bot in Telegram and send:

- `/start`
- `/help`
- `/about`
- `Hello`
- `What is Python?`
- `Explain machine learning`

Press `Ctrl+C` in the terminal to stop the bot.

## Limitations

- The bot supports only predefined topics.
- It does not use a trained NLP model.
- It cannot answer arbitrary questions.
- The bot must remain running to receive messages.
- This version uses local polling rather than cloud hosting.

## Future Improvements

- Integrate the NLP chatbot from Project 5.
- Add more commands and supported topics.
- Store user preferences in a database.
- Add inline buttons.
- Deploy the bot to a cloud hosting platform.

## Learning Outcomes

Through this project, I learned:

- How to create a Telegram bot using BotFather.
- How the Telegram Bot API works.
- How to handle commands and messages in Python.
- How asynchronous functions work.
- How to store API credentials securely.
- How to run and test a Telegram bot locally.

## Project Status

Completed locally after successful Telegram testing — Project 7 of 9 in the AI/ML Mini Projects portfolio.
