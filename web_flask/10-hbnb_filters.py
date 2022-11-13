#!/usr/bin/python3
"""This starts a web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filter():
    """This displays an html page like 6-index.html"""
    path = '10-hbnb_filters.html'
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    return render_template(path, all_states=all_states,
                           all_amenities=all_amenities)


@app.teardown_appcontext
def teardown():
    """This removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.url_run(host='0.0.0.0', port=5000)
