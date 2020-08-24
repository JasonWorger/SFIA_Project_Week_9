from flask import request, Response
import requests
from application import app
import random


@app.route('/get/slogan', methods=['GET', 'POST'])
def get_slogan():
    city= request.data.decode(utf-8)
    if city == 'London':
        slogans = ['The harder you work, the harder it is to lose.','Win from Within.','Play hard, smart and together.']
        return Response(slogans[random.randrange(3)],mimetype='text/plain')

    elif city == 'Manchester':
        slogans = ['A winner is a dreamer who never gives up.','Coming together is the beginning. Staying together is progress. Working together is success.','Champions play as one.']
        return Response(slogans[random.randrange(3)],mimetype='text/plain')

    elif city == 'Leeds':
        slogans = ['It’s not how you start, but how you finish.','Never let good enough BE enough.','Some wish for it, we work for it.']
        return Response(slogans[random.randrange(3)],mimetype='text/plain')

    else:
        return Response 'This is not a city expected'        










