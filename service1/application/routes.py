from flask import render_template, url_for, Response
from application import app, db
from application.models import Team
import requests
import random

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    teamData = Team.query.all()
    return render_template('home.html', title = 'Home', teams=teamData)



@app.route('/generateView', methods=['GET'])
def generate_view():
    return render_template('generate.html', title= 'Team Name')

@app.route('/generate', methods=['GET'])
def generate_team():
    city = requests.get('http://service2:5001/get/city')
    name = requests.get('http://service3:5002/get/name')
    slogan = requests.post('http://service4:5003/get/slogan', data=city)

    db_data = Team(city=city.text, name=name.text, slogan=slogan.text)
    db.session.add(db_data)
    db.session.commit()
    teams_record=db_data.query.all()

    return render_template('generate.html', title= 'Team Name')

