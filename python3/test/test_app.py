from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

class AppTest(TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Hello, Luis Javier!", result.data)
