from src import app
import sys
sys.path.append('/src')

def test_handler():
    event = {}
    context = {}
    response = app.handler(event, context)

    assert response['statusCode'] == 200
    assert response['body'] == 'Hello, world!!'