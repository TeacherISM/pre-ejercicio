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

    def test_welcome(self):
        response = self.app.get('/welcome')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>Title</title>\n</head>\n<body>\nHello Luis Javier!\n</body>\n</html>')
