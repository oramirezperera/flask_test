from flask import Flask, render_template, request, url_for
from flask_restful import Api, Resource
import re
from math import gcd
import requests
import random


app = Flask(__name__)
api = Api(app, catch_all_404s=True)


class Hello(Resource):
    """
    First message, all the paramaters you can use and how to use them
    """
    def get(self):
        return {"message": "Please, type one of these paramaters in the url, number, numbers, jokes, jokes/chuck or jokes/dad"}


class Number(Resource):
    """passing an integer as a parameter in the browser returns the integer plus 1

    If you don't pass any parameter 1 will be the example number
        
    example route http://127.0.0.1:5000/number/1 will return 2

    """
    def get(self, number=1):
        fin_number = number + 1
        return {"number": number, "result": fin_number}



class Numbers(Resource):
    """
    Passing a list of numbers separated by ',' you can this function returns the least common multiple of the numbers, can be 2 or more

    If you dont pass any number int_list default is 2,3

    example http://127.0.0.1:5000/numbers/2,3 returns 6
    """
    def get(self, int_list="2,3"):
    # Verifiying numbers in the list
        if not re.match(r'^\d+(?:,\d+)*,?$', int_list):
            return {"message": "Please write a list of integers separated by ','"}
    
        lcm = 1
        num_list = [int(num) for num in int_list.split(',')]
        for i in num_list:
            lcm = i*lcm//gcd(lcm,i)
        return {"integer list": num_list, "least common multiple": lcm}


def chuck():
    """
    Function to do the request to the chucknorris jokes API.
    """
   
    r = requests.get('https://api.chucknorris.io/jokes/random')
    chuck = r.json()
    chuck_id = chuck["id"]
    joke = chuck["value"]
    return {"id": chuck_id, "data":joke}


def dad():
    """
    function to do the request to the dad jokes
    """
    r = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    dad = r.json()
    dad_id = dad["id"]
    joke = dad["joke"]
    return {"id": dad_id, "data":joke}


class Jokes(Resource):
    """
    Function that takes the parameter Chuck or Dad, to return a Chuck Norris joke or a Dad joke.
    If no paramaterer is passed returns a random Chuck or dad joke
    """
    def get(self, toj='random'):
        if toj != 'random':
            if toj.lower() == 'chuck':
                return chuck()
            elif toj.lower() == 'dad':
                return dad()
            else:
                return {"message": f"the paramater {toj} is not valid, try chuck or dad"}
        if toj == 'random':
            ran = random.randint(1,2)
            if ran == 1:
                return chuck()
            if ran == 2:
                return dad()

api.add_resource(Hello, "/")
api.add_resource(Number, "/number/", "/number/<int:number>")
api.add_resource(Numbers, "/numbers/", "/numbers/<int_list>")
api.add_resource(Jokes, "/jokes/", "/jokes/<string:toj>")