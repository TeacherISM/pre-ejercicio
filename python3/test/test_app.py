from ..src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_handler(self):
        result = app.handler(None , None)
        self.assertEqual(result, "Hello, world! A01352283")
