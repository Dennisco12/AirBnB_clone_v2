#!/usr/bin/python3
"""This starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list')
def states_list():
    """This displays a HTML page inside the BODY tag"""
    path = '7-states_list.html'
    all_states = storage.all(State)
    all_states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template(path, all_states=all_states)

@app.teardown_appcontext
def teardown():
    """This removes the current SQLAlchemy session"""
    storage.close()

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
