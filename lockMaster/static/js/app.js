function uploadFile() {
  const fileInput = document.getElementById('uploadFile');
  const file = fileInput.files[0];
  
  if (!file) {
    document.getElementById('uploadStatus').innerText = "No file selected!";
    return;
  }

  const formData = new FormData();
  formData.append('file', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.message) {
      document.getElementById('uploadStatus').innerText = data.message;
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
function unlockFile() {
  fetch('/unlock', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ locked_file: 'me.png.zip' })  // Ensure the file name is correct
  })
  .then(response => response.json())
  .then(data => {
      if (data.error) {
          console.error('Unlock error:', data.error);
          // Display error message to user
      } else {
          console.log('Unlock successful:', data);
          // Handle successful unlock (e.g., display extracted content)
      }
  })
  .catch(error => console.error('Error:', error));
}

