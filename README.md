# flask_test
An API made in Flask.

This API has two main branches jokes and numbers:

### Jokes 
If you pass a path use the route '/jokes' you will get a random joke. Instead if you pass a path paragram with the word Chuck or the word Dad you will get a Chuck Norrris joke from the [Chuck Norris API](https://api.chucknorris.io) or a dad joke from [Dad jokes API](https://icanhazdadjoke.com/api).

If you dont pass any paramaters a random Chuck or Dad joke will be returned

### Numbers

- Using the path /numbers you must pass a list of integers as a path parameter this will return the least common multiple of the numbers.

- Using the path /number you must pass an integer and this will return the given number + 1.

If any paramater is passed the functions works with example code.

## Starting

You will need to clone this repository 

### Prerequirements
- You will need Python 3.X installed on your computer
- You will need some Python libraries such as requests and Flask.

## Installation

You can install all the requirements of this project using the following code:

- First create a virtual environment, in this example case we will call it:

```Bash
python3 -m venv flask_test
```

flask_test is the name of our virtual environment

- Once we have created your virtual environment you must activate it with:

If you are in Linux use:
```Bash
$ source flask_test/bin/activate
```
If you are in Windows use:
```Bash
flask_test\Scripts\activate
```

To deactivate the virtual environment just type:
```Bash
deactivate
```

Now that we have activate our virtual environment we can install all the libraries and dependencies we need using the following code:

```Bash
pip3 install -r requirements.txt
```

## Runing

Once you have installed the libraries needed in this project you can run the flask API using:

```Bash
$ flask run
```

copy and paste the url returned

You will be in the front page of the app, you can click on the list and see the functions, or you can write the url and paramaters by yourself

## Built with

- Python 3.8 or higher
- Flask
- requests

All the requirements are in the requirements.txt and how to install them are in the installing section.

## Thanks :blue_heart:

Thanks for checking out this app.
If you have any question or recommendation feel free to contact me.
I hope you liked it.