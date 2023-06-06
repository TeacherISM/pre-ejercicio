import pytest
from src import app

def test_handler():
    response = app.handler(None, None)
    assert response == "Hello, world! A01352283"