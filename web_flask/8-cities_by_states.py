#!/usr/bin/python3
"""
starts flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ displays html of cities in states in order """
    state = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the storage on teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
