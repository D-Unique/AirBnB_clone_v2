#!/usr/bin/python3

"""the `4-number_route` module
starts a flask web application listening on `0.0.0.0:5000`
"""
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """returns `Hello HBNB!` message"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """returns `HBNB` message"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """returns `c` + `text`"""
    text = text.replace("_", " ")
    return "C %s" % escape(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>")
def number(n):
    """returns `n` + `is a number` only if `n` is an integer"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>")
def rander_number(n):
    """render the '5-number.html' page only if 'n' is an integer """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
