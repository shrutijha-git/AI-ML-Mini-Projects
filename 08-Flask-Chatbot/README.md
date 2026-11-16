# Project 8 — Flask Chatbot with Web Interface

## Project Overview

This project is a browser-based chatbot built using Python, Flask, HTML, CSS, and JavaScript. It allows users to enter messages through a web interface and receive automated responses.

The Flask backend processes messages using predefined rules and keyword matching, while JavaScript communicates with the backend using the Fetch API. HTML provides the page structure, and CSS creates a responsive chat interface.

This is a rule-based chatbot, not a trained machine learning model. Its main purpose is to demonstrate how a Python backend can communicate with a web frontend.

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Fetch API
- JSON

## Project Structure

```text
08-Flask-Chatbot/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Features

- Responsive web-based chat interface
- Flask backend
- JavaScript message handling
- JSON API for chatbot responses
- Greetings and goodbyes
- Responses to basic AI/ML and Python questions
- Fallback messages for unsupported topics
- Basic input validation

## How It Works

1. The user enters a message into the website.
2. JavaScript sends the message to Flask using a POST request.
3. Flask receives the JSON message at `/chat`.
4. The chatbot checks predefined rules and keywords.
5. Flask returns a JSON response.
6. JavaScript displays the response in the chat interface.

## Flask Routes

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Displays the chatbot webpage |
| `/chat` | POST | Receives messages and returns responses |

## Installation

From the project folder, run:

```bash
python -m pip install -r requirements.txt
```

## Running the Project

```bash
python app.py
```

Open:

`http://127.0.0.1:5000`

## Example Conversations

**User:** Hello

**Bot:** Hello! How can I help you today?

**User:** What is Flask?

**Bot:** Flask is a lightweight Python web framework used to build websites and APIs.

**User:** What is your name?

**Bot:** I'm your AI Learning Chatbot, built using Flask!

## Limitations

- The chatbot uses predefined responses rather than a trained NLP model.
- It supports only a limited set of topics.
- It does not remember conversation history.
- The development server runs locally and is not configured for production deployment.
- Responses depend on keyword matching and may not capture the user's full intent.

## Future Improvements

- Integrate the trained NLP classifier from Project 5.
- Add a conversation history feature.
- Support more topics.
- Connect to a database.
- Deploy the application to a hosting platform.
- Add more advanced NLP capabilities.

## Learning Outcomes

Through this project, I learned:

- How Flask routes work.
- How to connect a Python backend to HTML, CSS, and JavaScript.
- How to send POST requests using the Fetch API.
- How to work with JSON responses.
- How to build a responsive chatbot interface.
- How to validate user input and handle errors.

## Project Status

Completed after successful local testing — Project 8 of 9 in the AI/ML Mini Projects portfolio.