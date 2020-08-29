from flask import request, Response
import requests
from application import app
import random


@app.route('/get/slogan', methods=['GET', 'POST'])
def get_slogan():
    city= request.data.decode('utf-8')
    if city == 'London':
        slogans = ['We take what we get.','You dont win them all.','We play okay I guess.']
        return Response(slogans[random.randrange(0,3)],mimetype='text/plain')

    elif city == 'Manchester':
        slogans = ['Being okay is enough.','Its the taking part that counts, that may mean losing.','Staying up is enough.']
        return Response(slogans[random.randrange(0,3)],mimetype='text/plain')

    elif city == 'Leeds':
        slogans = ['We cant think of a slogan...','When the going gets tough, give up.','Some work for it, we wish for it.']
        return Response(slogans[random.randrange(0,3)],mimetype='text/plain')

    else:
        return 'This is not a city expected'        










