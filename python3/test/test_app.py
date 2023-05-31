# test_hello_world.py
import pytest
from src import app

def test_lambda_handler():
    response = app.lambda_handler(None, None)
    assert response == {"Hola, Mateo"}
    
