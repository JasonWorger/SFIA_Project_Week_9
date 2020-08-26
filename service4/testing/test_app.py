import unittest
from flask import url_for
from os import getenv
from unittest.mock import patch
from app import app, db
from app.models import Team
from flask_testing import TestCase
from testing.test_setup import TestBase

class Service1Test(TestBase):
    
    def test_generate_teams(self):
        response = self.client.get(url_for("generate"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Team Name", response.data)

    def test_view_teams(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"All Teams", response.data)

