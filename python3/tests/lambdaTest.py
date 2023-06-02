import sys
from src import app
# from unittest import TestCase # Importing the TestCase class
sys.path.append('../src')

# # Using unittest
# class Test(TestCase):
#     # Check lambda for response 'Salva Milanés'
#     def test_lambda_handler(self):
#         result = app.lambda_handler(None, None)
#         self.assertEqual(result, 'Salva Milanés')

# Using pytest
def test_lambda_handler():
    result = app.lambda_func(None, None)
    assert result == 'Salvador Milanés'


