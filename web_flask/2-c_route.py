#!/usr/bin/python3
"""This module creates a basic flask app and causes it to listen to 0.0.0.0"""


from flask import Flask
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
