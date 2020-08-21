from flask import request,Response
import requests
from application import app
import random


#generates a random 2 worded football team name
@app.route('/get_team_1',methods=['GET'])
def get_team():
    teams = ['The Devils','The Koalas','Heavenly Llamas','The Coyotes','The Cardinals','The Raiders','The Goats','The Vipers','Ruthless Ducks','The Parrots']
    team = teams[random.randrange(10)]
    return Response(team,mimetype='text/plain')


#generates a random 3 worded football team name
@app.route('/get_team_2',methods=['GET'])
def get_team():
    teams = ['The Bottle Rockets','The Old Mavericks','The Careless Roaches','The Old Bois','The Slow Chargers','The Stark Squids','The Ancient Dogs','The Awesome Porcupines','The Determined Beasts','The Lucky Stingers']
    team = teams[random.randrange(10)]
    return Response(team,mimetype='text/plain')