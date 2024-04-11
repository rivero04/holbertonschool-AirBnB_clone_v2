#!/usr/bin/python3
""" Flask """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_states(id=None):
    """
    List states by ID.
    """
    state_info = []
    all_states = storage.all(State)
    if id is None:
        for key in all_states:
            state_info.append(all_states[key])
    else:
        id = 'State.' + id
        state_info = all_states.get(id)
    return render_template('9-states.html', states=state_info, id=id)
    return render_template('9-states.html', state=id)


@app.teardown_appcontext
def close_session(exception=None):
    """Close storage session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
