#!/usr/bin/python3
"""This script starts a Flask web application on
route '/': displays 'Hello HBNB'
route '/hbnb': displays 'HBNB' """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """This returns the required string"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """This returns the string 'HBNB' """
    return "HBNB"


@app.route('/c/<text>')
def Cisfun(text):
    """This returns a text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>')
def pythoniscool(text="is cool"):
    """This return a string"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
