#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filter(id=None):
    """ Display a page for hbnb_filters. """
    data = storage.all(State)
    states = []
    for key in data:
        states.append(data[key])

    data = storage.all(Amenity)
    amenities = []
    for key in data:
        amenities.append(data[key])

    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)