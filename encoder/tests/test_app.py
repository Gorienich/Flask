import pytest
from encoder.app import app  # Use the full path to app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_encode_text(client):
    # Send POST request to /encode with text to be encoded
    response = client.post('/encode', json={'text': 'Hello'})
    
    # Assert the response code is 200
    assert response.status_code == 200
    
    # Get JSON data from response
    data = response.get_json()
    
    # Assert that the response contains 'received_text' and 'encoded_text'
    assert 'received_text' in data
    assert 'encoded_text' in data
    
    # Assert that the received text matches what was sent
    assert data['received_text'] == 'Hello'
    
    # Assert the encoded text is correctly encoded (Caesar cipher shift by 3)
    assert data['encoded_text'] == 'Khoor'
