from flask import request,Response
import requests
from application import app
import random


#generates a random football team name
@app.route('/get_team',methods=['GET'])
def get_team():
    teams = ['The Glorious Bottle Rockets','The Grim Koalas','Heavenly Llamas','The Coyotes','The Hot Cardinals','Raiders','The Goats','The Vipers','Ruthless Ducks','The Parrots']
    team = teams[random.randrange(10)]
    return Response(team,mimetype='text/plain')