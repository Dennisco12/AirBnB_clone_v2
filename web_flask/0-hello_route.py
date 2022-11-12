#!/usr/bin/python3
"""This script starts a Flask web application on route '/' """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """This returns the required string"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
