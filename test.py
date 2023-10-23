from app import app
import json

client = app.test_client()
data = {'username': 'test_user3', 'password': 'password123'}

def test_signup_success():
    response = client.post('/auth/signup', json=data)
    assert response.status_code == 200
    assert b'success' in response.data

def test_already_exist()
    reponse = client.post('/auth/signup', json=data)
    assert response.status_code == 409
    assert b'Already Registered' in response.data
