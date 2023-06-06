from src import app
from unittest import TestCase

class TestHandler(TestCase):
    def test_handler(self):
        result = app.handler(None, None)
        self.assertEqual(result, "Andrés says: Hello World!")
