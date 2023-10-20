#!/usr/bin/python3
"""List States"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """Render template with states
    """
    path = '7-states_list.html'
    states = storage.all(State)
    # sort State object alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def teardown_db(self):
    """Close db storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
