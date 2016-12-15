from flask import Flask, render_template

from classes.Development import Development
from classes.Peercoaching import Peercoaching


class Account:
    def __init__(self,username, pw):
        self._username = username
        self._pw =pw

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/english')
def english():
    return "<h2>Testing HTML English</h2>"

@app.route('/peercoaching')
def peercoaching():
    return Peercoaching.get(Peercoaching)

@app.route('/analyse')
def analyse():
    return "<h2>Testing HTML analyse</h2>"

@app.route('/development')
def development():
    return Development.get(Development)

@app.route('/project')
def project():
    return "<h2>Testing HTML project</h2>"

@app.route('/spar')
def spar():
    return "<h2>Testing HTML spar</h2>"

if __name__ == "__main__":
    app.run(debug=True)
