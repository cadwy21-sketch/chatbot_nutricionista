function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();
    if (!message) return;

    const chatLog = document.getElementById('chat-log');
    chatLog.innerHTML += `<p><strong>Tú:</strong> ${message}</p>`;
    userInput.value = '';

    fetch('/chat', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: message})
    })
    .then(res => res.json())
    .then(data => {
    chatLog.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    chatLog.scrollTop = chatLog.scrollHeight;
    });
}
