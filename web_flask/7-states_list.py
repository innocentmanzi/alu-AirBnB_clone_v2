#!/usr/bin/python3
<<<<<<< HEAD

"""Script that starts a Flask web application"""
=======
"""List States"""
>>>>>>> da3e1968b81d6c222deee24dfe9b583b9c784aca

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/states_list', strict_slashes=False)
def states():
    """returns list of states"""
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """closes the current SQLAlchemy session"""
=======
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
>>>>>>> da3e1968b81d6c222deee24dfe9b583b9c784aca
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
