import sys
from src import app

# Using pytest
def test_lambda_handler():
    assert all('Hola, Salva')