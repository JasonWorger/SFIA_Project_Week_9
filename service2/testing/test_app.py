from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

class TestResponse(TestBase):

    def test_random_city(self):
        with patch('application.routes.get/city') as g:
            g.return_value.data = 1

            response = self.client.get(url_for('generate'))
            self.assertIn(b'London', response.data)