from flask import Flask, render_template, request, url_for
from flask_restful import Api, Resource 
import re
from math import gcd
import requests
import random


app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
    """
    Front page, have links to all the utilities of this app
    """
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    """
    handling the 404 error not found
    """

    return render_template('404.html', error=error)


@app.route('/number/')
@app.route('/number/<int:number>')
def number(number=1):
    """passing an integer as a parameter in the browser returns the integer plus 1

    If you don't pass any parameter 1 will be the example number
        
    example route http://127.0.0.1:5000/number/1 will return 2

    """
    fin_number = number + 1
    return render_template('number.html', number=str(number), fin_number=str(fin_number))


@app.route('/numbers/')
@app.route('/numbers/<int_list>')
def numbers(int_list='2,3'):
    """
    Passing a list of numbers separated by ',' you can this function returns the least common multiple of the numbers, can be 2 or more

    If you dont pass any number int_list default is 2,3

    example http://127.0.0.1:5000/numbers/2,3 returns 6
    """
    # Verifiying numbers in the list
    if not re.match(r'^\d+(?:,\d+)*,?$', int_list):
        return render_template('numbers_error.html')
    
    lcm = 1
    num_list = [int(num) for num in int_list.split(',')]
    for i in num_list:
        lcm = i*lcm//gcd(lcm,i)
    return render_template('numbers.html', int_list=list(num_list), lcm=str(lcm))


def chuck():
    """
    Function to do the request to the chucknorris jokes API.
    """
    r = requests.get('https://api.chucknorris.io/jokes/random')
    chuck = r.json()
    joke = chuck["value"]
    return render_template('chuck.html', joke=joke)


def dad():
    """
    function to do the request to the dad jokes
    """
    r = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    dad = r.json()
    joke = dad["joke"]
    return render_template('dad.html', joke=joke)


@app.route('/jokes/')
@app.route('/jokes/<string:toj>/')
def jokes(toj='random'):
    """
    Function that takes the parameter Chuck or Dad, to return a Chuck Norris joke or a Dad joke.
    If no paramaterer is passed returns a random Chuck or dad joke
    """
    if toj != 'random':
        if toj.lower() == 'chuck':
            return chuck()
        elif toj.lower() == 'dad':
            return dad()
        else:
            return render_template('joke_error.html', error=str(toj))
    if toj == 'random':
        ran = random.randint(1,2)
        if ran == 1:
            return chuck()
        if ran == 2:
            return dad()
