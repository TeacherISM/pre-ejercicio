import pytest
from flask_testing import TestCase
from app import app, lambda_handler

class MyTest(TestCase):
    def create_app(self):
        return app

    def test_hello_world(self):
        response = self.client.get('/')
        self.assert200(response)  # assert the response status code is 200
        self.assertEqual(response.data.decode(), 'Hola Andreina')

def test_lambda_handler():
    event = {
        "httpMethod": "GET",
        "path": "/",
        "queryStringParameters": None, 
        'body': None,
        'resource': '/',
        'requestContext': {
            'resourcePath': '/',
            'httpMethod': 'GET',
            'path': '/',
        },
        'headers': {
            'X-Forwarded-Proto': 'https',
        }
    }
    context = {}  # context can be an empty dictionary in most cases

    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    assert response['body'] == "Hola Andreina"