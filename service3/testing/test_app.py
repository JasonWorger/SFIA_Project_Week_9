from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class Service3Test(TestBase):
    
    def test_random_name(self):
        with patch('application.routes.get/name') as g:
            g.return_value.data = 1

            response = self.client.get(url_for('generate'))
            self.assertIn(b'City', response.data)
