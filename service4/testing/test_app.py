from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    # def test_team_slogan(self):
    #     with self.client:
    #         self.client.get(
    #             url_for('get_slogan'),
    #             data = city)    
    #         with patch('requests.get') as i:
    #             i.return_value.text = 'London'
    #             response = self.client.post(url_for('get_slogan'))
    #             self.assertIn(b'London', response.data)    
    #         with patch('random.randrange') as r:
    #             r.return_value = 1
    #             response = self.client.post(url_for('get_slogan'))
    #             self.assertIn(b'Win from Within.', response.data)

    def test_team_slogan(self):
        with self.client:  
            with patch('requests.get') as i:
                i.return_value.text = 'London'
                response = self.client.get(url_for('get_slogan'))
                self.assertIn(b'London', response.data)    
            with patch('random.randrange') as r:
                r.return_value = 1
                response = self.client.get(
                url_for('get_slogan'),
                data = city)
                self.assertIn(b'Win from Within.', response.data)
                self.assertIn(b'London', response.data) 
                



