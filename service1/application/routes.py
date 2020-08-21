from flask import render_template, url_for, Response
from application import app, db
from application.models import Team
import requests
import random

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')



@app.route('/generate', methods=['GET','POST'])
def generate_team():
    city = requests.get('http://service2:5001/get/city')
    name = requests.get('http://service3:5002/get/name')
    slogan = requests.post('http://service4:5003/get/slogan', data=city)

    team_data = Team(city=city.text, name=name.text, slogan=slogan.text)
    db.session.add(team_data)
    db.session.commit()

    return render_template('generate.html', title= 'Team Name', data1=city.text, data2=name.text, data3=slogan.text)
