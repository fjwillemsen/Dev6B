from ProjectTask import ProjectTask
from english import English
from Analyse import Analyse
from Spar import Spar
from flask import Flask, render_template, request

from Development import Development
from Peercoaching import Peercoaching
from spar_game import spar_game

import random

class Account:
    def __init__(self,username, pw):
        self._username = username
        self._pw =pw

app = Flask(__name__,static_url_path='/../static')
task = ProjectTask()
q = random.sample(range(0,6),4)
sparG = spar_game(q)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/english',methods = ['POST', 'GET'])
def english():
    return English().getView(request)


@app.route('/peercoaching')
def peercoaching():
    return Peercoaching.get(Peercoaching())


analypage = Analyse("USERNAME")
@app.route('/analyse',methods=['GET', 'POST'])
def analyse():
    return Analyse.GetCurrentView(analypage, request)

@app.route('/development')
def development():
    return Development.get(Development())

@app.route('/development-answer', methods=['POST'])
def developmentanswer():
    print('Answer: ' + str(request.form.get('answer')))
    print('Useranswer: ' + str(request.form.get('useranswer')))
    if str(request.form.get('answer')) == str(request.form.get('useranswer')):
        return "<p>Congratz!</p>"
    else:
        return "<p>Failure</p>"

@app.route('/project/')
def project():
    return render_template("Projects.html",taskList=task.getListOfTask(1),time=task.getSecTimeLeftOnCounter())

@app.route('/project/<int:project_id>')
def project1(project_id):
    return render_template("Projects.html",taskList=task.getListOfTask(project_id),time=task.getSecTimeLeftOnCounter())

@app.route('/project_task', methods=['POST'])
def projectTask():
    taskID =request.form['taskID']

    task.isCooldownOver(taskID)
    return render_template("Projects.html",taskList=task.getListOfTask(1),time=task.getSecTimeLeftOnCounter())

@app.route('/spar')
def spar():
    return Spar.get(Spar())

@app.route('/spar/Q2')
def sparQ2():
    return sparG.getQ2()

@app.route('/spar-game', methods=['POST'])
def sparg():
    item = request.form['item']
    print(item)
    return sparG.get(item)

@app.route('/spar-res')
def sparres():
    return sparG.getRes()

@app.route('/spar-check', methods=['POST'])
def sparcheck():
    useranswer = [request.form['q1a'],request.form['q2a'],request.form['q3a'],request.form['q4a'],str(request.form['q5a']).lower().strip()]
    timer = request.form['timer']
    return sparG.afterQ(useranswer,int(timer),True)

@app.route('/spar/Q2-check', methods=['POST'])
def sparq2check():
    ua = request.form['qq'].lower().strip()
    return sparG.checkQ2(ua)

if __name__ == "__main__":
    app.run(host='145.24.222.234', port=8080)
    # app.run(debug=True)
