function sendText() {
  const inputText = document.getElementById('inputText').value;
  if (inputText.trim() === '') return;  // Don't send empty text

  // Send the text to the server via Fetch API
  fetch('/encode', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: inputText })
  })
  .then(response => response.json())
  .then(data => {
      // Display received and encoded text
      document.getElementById('receivedText').innerText = data.received_text;
      document.getElementById('encodedText').innerText = data.encoded_text;
  })
  .catch(error => console.error('Error:', error));
}
