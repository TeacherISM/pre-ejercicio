from ..src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class TestHandler(TestCase):
    def test_handler(self):
        result = app.handler(None, None)
        self.assertEqual(result, "Andrés says: Hello World!")