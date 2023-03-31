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
    assert data == {"hello": "world"}

def test_check_overlap(client):
    # Test case with overlapping ranges
    data = {
        'range1': {'start': "2023-04-01T09:00:00Z", 'end': "2023-04-01T10:00:00Z"},
        'range2': {'start': "2023-04-01T11:00:00Z", 'end': "2023-04-01T21:00:00Z"}
    }
    response = client.post('/check_overlap', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'overlap': False}

    # Test case with non-overlapping ranges
    data = {
        'range1': {'start': "2023-04-01T09:00:00Z", 'end': "2023-04-01T20:00:00Z"},
        'range2': {'start': "2023-04-01T11:00:00Z", 'end': "2023-04-01T21:00:00Z"}
    }
    response = client.post('/check_overlap', json=data)
    assert response.status_code == 200
    assert json.loads(response.data) == {'overlap': True}
