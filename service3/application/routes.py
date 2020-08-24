from flask import request, Response
import requests
from application import app
import random


#generates a team name
@app.route('/get/name',methods=['GET'])
def get_name():
    names = ['City','United','FC','Raiders','Bois','Eagles','Patriots','Cowboys','Ravens','Saints','Chiefs','Giants','Dodgers','Cardinals','Jaguars']
    name = names[random.randrange(15)]
    return Response(name,mimetype='text/plain')



