document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('send-btn').addEventListener('click', function() {
        sendMessageRASA();
    });

    document.getElementById('user-input-rasa').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessageRASA();
        }
    });

    function sendMessageRASA() {
        var userInput = document.getElementById('user-input-rasa').value;
        if (userInput.trim() !== '') {
            displayUserMessage(userInput);
            fetch('/model', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({input:userInput}),
            })
            .then(response => response.json())
            .then(data => {
                displayBotMessage(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });

            document.getElementById('user-input-rasa').value = '';
        }
    }

    function displayBotMessage(message) {
        var chatBox = document.getElementById('chat-box');
        var botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'chat-message bot-message';
        botMessageDiv.innerHTML = '<p>' + message + '</p>';
        chatBox.appendChild(botMessageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function displayUserMessage(message) {
        var chatBox = document.getElementById('chat-box');
        var userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'chat-message user-message';
        userMessageDiv.innerHTML = '<p>' + message + '</p>';
        chatBox.appendChild(userMessageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

});

