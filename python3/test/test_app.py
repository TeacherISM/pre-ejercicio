import unittest
from flask import Flask, render_template
import sys
sys.path.append('../src')

class FlaskRenderingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True

    def test_home_page_rendering(self):
        with self.app.test_request_context('/'):
            response = self.app.dispatch_request()
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello, Luis Javier!', response.data)


if __name__ == '__main__':
    unittest.main()
