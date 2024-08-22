from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def greeting():
    return 'Hello HBNB!'
