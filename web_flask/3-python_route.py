#!/usr/bin/python3

"""this module is a script that starts a Flask web application:
and display 'Hello HBNB!' 'HBNB!',   'c %s'  and text variable, display
“Python and a text variable iwhich
is set to is cool"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def greeting():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display():
    return 'HBNB!'


@app.route('/c/<path:text>', strict_slashes=False)
def Cp(text):
    sanitized_text = text.replace('_', ' ')
    return 'c %s' % sanitized_text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
