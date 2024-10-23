document.getElementById('prompt-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const prompt = document.getElementById('prompt').value;
  
  const responseContainer = document.getElementById('response-container');
  responseContainer.innerHTML = 'Generating...';

  try {
      const response = await fetch('/api/generate', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ prompt }),
      });
      
      const data = await response.json();
      if (data.response) {
          responseContainer.innerHTML = `<p>${data.response}</p>`;
      } else {
          responseContainer.innerHTML = `<p>Error: ${data.error}</p>`;
      }
  } catch (error) {
      responseContainer.innerHTML = `<p>Error: ${error.message}</p>`;
  }
});
