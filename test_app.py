import pytest
from flask import json
from app import application  # Replace 'app' with the name of your application file

@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {"hello": "pakistan"}

def test_check_overlap(client):
    # Test case with overlapping ranges
    data = {
        'range1': {'start': 1, 'end': 5},
        'range2': {'start': 3, 'end': 7}
    }
    response = client.post('/check_overlap', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'overlap': True}

    # Test case with non-overlapping ranges
    data = {
        'range1': {'start': 1, 'end': 5},
        'range2': {'start': 6, 'end': 10}
    }
    response = client.post('/check_overlap', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'overlap': False}
