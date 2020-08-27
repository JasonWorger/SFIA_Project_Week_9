from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):
    
    def test_team_slogan(self): 
        with patch('requests.get') as i:
                i.return_value.text = 'London'
                with patch('random.randrange') as r:
                    r.return_value = 1
                    response = self.client.post(
                    url_for('get_slogan'),
                    data = 'London')
                    self.assertIn(b'Win from Within.', response.data)
    
    def test_team_slogan2(self): 
        with patch('requests.get') as i:
                i.return_value.text = 'Manchester'
                with patch('random.randrange') as r:
                    r.return_value = 2
                    response = self.client.post(
                    url_for('get_slogan'),
                    data = 'Manchester')
                    self.assertIn(b'Champions play as one.', response.data)
    

    def test_team_slogan3(self): 
        with patch('requests.get') as i:
                i.return_value.text = 'Leeds'
                with patch('random.randrange') as r:
                    r.return_value = 1
                    response = self.client.post(
                    url_for('get_slogan'),
                    data = 'Leeds')
                    self.assertIn(b'Never let good enough BE enough.', response.data)
    
    def test_team_slogan4(self): 
        with patch('requests.get') as i:
                i.return_value.text = 'Leicester'
                with patch('random.randrange') as r:
                    r.return_value = 1
                    response = self.client.post(
                    url_for('get_slogan'),
                    data = 'Leicester')
                    self.assertIn(b'This is not a city expected', response.data)
                    
                



