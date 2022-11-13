#!/usr/bin/python3
"""This starts a web flask application
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """This displays a html page in template"""
    path = '9-states.html'
    all_states = storage.all(State)
    all_states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template(path, all_states=all_states, id=id)


@app.teardown_appcontext
def teardown():
    """This removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    url.run(host='0.0.0.0', port=5000)
