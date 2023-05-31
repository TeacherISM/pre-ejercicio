import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_today(client):
    response = client.get('/today')
    assert response.status_code == 200
    assert response.json['date'] == '2023-05-30'  # Replace with the current date

def test_get_tomorrow(client):
    response = client.get('/tomorrow')
    assert response.status_code == 200
    assert response.json['date'] == '2023-05-31'  # Replace with tomorrow's date

def test_invalid_endpoint(client):
    response = client.get('/invalid')
    assert response.status_code == 404

if __name__ == '__main__':
    pytest.main()