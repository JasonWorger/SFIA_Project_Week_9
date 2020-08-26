from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_london_city(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_city'))
            self.assertIn(b'London', response.data)

    def test_manchester_city(self):
        with patch('random.randrange') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_city'))
            self.assertIn(b'Manchester', response.data)

    def test_leeds_city(self):
        with patch('random.randrange') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_city'))
            self.assertIn(b'Leeds', response.data)
    
