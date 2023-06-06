import unittest
from src import app


class TestHandler(unittest.TestCase):
    def test_handler(self):
        # Act
        result = app.handler(None, None)

        # Assert
        self.assertEqual(result, "Andrés says: Hello World!")
