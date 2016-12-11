from flask import Flask, render_template, request

from classes.Development import Development
from classes.Peercoaching import Peercoaching
from Spar import Spar
from spar_game import spar_game

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
    return Spar.get(Spar)

@app.route('/spar-game', methods=['POST'])
def sparg():
    item = request.form['item']
    print(item)
    return spar_game.get(spar_game, item,spar_game.generate_answers(spar_game),spar_game.generate_answers(spar_game),spar_game.generate_answers(spar_game),spar_game.generate_answers(spar_game))

@app.route('/spar-check', methods=['POST'])
def sparcheck():
    useranswer = request.form['answer']
    answer = spar_game.generate_answers(spar_game)
    print(answer)
    return spar_game.check(spar_game, useranswer, answer)


if __name__ == "__main__":
    app.run(debug=True)

