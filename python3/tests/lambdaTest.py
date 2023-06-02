import sys
from src import app
# from unittest import TestCase # Importing the TestCase class
sys.path.append('../src')

# Using pytest
def test_lambda_handler():
    result = app.lambda_func(None, None)
    assert result == 'Salvador Milanés'