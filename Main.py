from Spar import Spar
from flask import Flask, render_template, request

from classes.Development import Development
from classes.Peercoaching import Peercoaching
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
    spar_game.gen_question(spar_game)
    item = request.form['item']
    spar_game.set_item(spar_game,item)
    spar_game.difficulty(spar_game,item)
    print(item)
    return spar_game.get(spar_game, item)

@app.route('/spar-check', methods=['POST'])
def sparcheck():
    useranswer = [request.form['q1a'],request.form['q2a'],request.form['q3a'],request.form['q4a'],str(request.form['q5a']).lower().strip()]
    print(useranswer[4])
    # for index in range(len(useranswer)):
    #     print("Correct answer:" + str(spar_game.get_correctA(spar_game, index) + ". Input: " + useranswer[index]))
    #     if spar_game.get_correctA(spar_game,index) == useranswer[index]:
    #         spar_game.incscore(spar_game,50)
    return spar_game.check(spar_game,useranswer)

if __name__ == "__main__":
    app.run(debug=True,port=12341)

