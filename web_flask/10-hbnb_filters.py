#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filter', strict_slases=False)
def hbnbfilter():
    """ displays html filter """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
