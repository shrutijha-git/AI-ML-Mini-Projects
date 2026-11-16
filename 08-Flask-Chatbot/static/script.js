
const chatForm = document.getElementById("chat-form");
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

// Add a message to the chat interface.
function addMessage(text, sender) {
    const message = document.createElement("div");

    message.classList.add("message");

    if (sender === "user") {
        message.classList.add("user-message");
    } else {
        message.classList.add("bot-message");
    }

    // textContent prevents HTML injection.
    message.textContent = text;

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send a message to the Flask backend.
chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = userInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");

    userInput.value = "";
    userInput.disabled = true;
    sendButton.disabled = true;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.error || "Something went wrong."
            );
        }

        addMessage(data.response, "bot");

    } catch (error) {
        addMessage(
            "Sorry, I couldn't connect to the server. " +
            error.message,
            "bot"
        );

    } finally {
        userInput.disabled = false;
        sendButton.disabled = false;
        userInput.focus();
    }
});
