1. install flask bush in terminal after downloading repository if you don't have it:
   pip install Flask openai

2. insert your openAI key in .env
   OPENAI_API_KEY=your_openai_api_key_here

3. Ensure you have the pytest and pytest-mock modules installed:
   pip install pytest pytest-mock

4. To run your tests, use:
   pytest

5. check the requirements.text

6. start the app
   python app.py

   Visit http://127.0.0.1:5000/ (as it usually free on port :: 5000)


* Flask Backend: Manages requests and responses, connects with the OpenAI API.
* OpenAI Integration: The openai_service.py handles the communication with the OpenAI API.
* Frontend: Simple HTML form with a button that sends a request to the Flask backend and displays the OpenAI response.
