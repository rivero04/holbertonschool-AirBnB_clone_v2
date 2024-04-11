#!/usr/bin/python3
""" Flask """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Base route that displays "Hello HBNB!"."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that displays "HBNB"."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route that displays "C " followed by the value of the text variable,
    replacing underscores with spaces."""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route that displays "Python "
    followed by the value of the text variable,
    replacing underscores with spaces."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/python/', strict_slashes=False)
def python_cool():
    """Route that displays "Python is cool"."""
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Route that displays "n is a number" if n is an integer."""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
