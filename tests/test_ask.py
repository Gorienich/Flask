import pytest
from unittest.mock import patch
from app.app import app, db, Question

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

@patch('app.openai_service.generate_response')  # Mock the OpenAI API call
def test_ask_question(mock_generate_response, client):
    # Define what the mock should return
    mock_generate_response.return_value = "Artificial Intelligence (AI) is a field of computer science."

    # Make a POST request to the '/ask' endpoint with a sample question
    response = client.post('/ask', json={'question': 'What is AI?'})

    # Parse the response data
    data = response.get_json()

    # Assertions
    assert response.status_code == 200
    assert 'question' in data
    assert 'answer' in data
    assert data['question'] == 'What is AI?'
    assert data['answer'] == "Artificial Intelligence (AI) is a field of computer science."
