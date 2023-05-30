from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

class apptest(TestCase):
    def test_index(self):
        result = app.index()
        self.assertEqual(result, 'Hela Tonatiuh Reyes')
