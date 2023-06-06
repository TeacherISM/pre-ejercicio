import unittest
from src import handler


class TestHandler(unittest.TestCase):
    def test_handler(self):
        # Arrange
        event = {}
        context = {}

        # Act
        result = handler(event, context)

        # Assert
        self.assertEqual(result, "Andrés says: Hello World!")
