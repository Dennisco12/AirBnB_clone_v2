#!/usr/bin/python3
"""Thnis starts a web flask application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/cities_by_states')
def cities_by_state():
    """This displays a HTML page"""
    file_path = '8-cities_by_states.html'
    all_states = storage.all(State)
    all_states = sorted(all_states.values(), key=lambda state: state.name)
    all_cities = storage.all(City)
    all_cities = sorted(all_cities.values(), key=lambda city: city.name)
    return render_template(file_path, all_states=all_states,
            all_cities=all_cities)

@app.teardown_appcontext
def teardown():
    """This removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
