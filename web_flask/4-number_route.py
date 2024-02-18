#!/usr/bin/python3
"""
starts a Flask web application
"""

import os
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_display(text=None):
    """ returns a page that shows user url input """
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ returns a page that shows user url input """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number', strict_slashes=False)
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ returns a page that shows an int """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
