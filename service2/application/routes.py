from flask import request,Response
import requests
from application import app
import random


#generates a team name
@app.route('/get/city',methods=['GET'])
def get_city():
    cities = ['London','Manchester','Leeds']
    city = cities[random.randrange(0,3)]
    return Response(city,mimetype='text/plain')