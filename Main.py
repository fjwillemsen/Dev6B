from ProjectTask import ProjectTask
from english import English
from Analyse import Analyse
from Spar import Spar
from flask import Flask, render_template, request
import pymysql
from Development import Development
from Peercoaching import Peercoaching
from Peer_dev import Peer_dev
from Peer_anl import Peer_anl
from spar_game import spar_game
from string import Template
import database

import random

class Account:
    def __init__(self,username, pw):
        self._username = username
        self._pw =pw

app = Flask(__name__,static_url_path='/../static')
task = ProjectTask()
q = random.sample(range(0,6),4)
sparG = spar_game(q)

# db = database.database(None, 'localhost', 3306)

@app.route('/')
def index():
    temp = Template(render_template("index.html"))
    # return temp.substitute(score = db.getScore())
    return render_template("index.html")

@app.route('/english',methods = ['POST', 'GET'])
def english():
    return English().getView1(request)

@app.route('/english2',methods = ['POST', 'GET'])
def english2():
    return English().getView2(request)

@app.route('/english3',methods = ['POST', 'GET'])
def english3():
    return English().getView3(request)

@app.route('/peercoaching')
def peercoaching():
    return Peercoaching.get(Peercoaching())

@app.route('/peer_dev')
def peer_dev():
    return Peer_dev.get(Peer_dev())

@app.route('/peer_anl')
def peer_anl():
    return Peer_anl.get(Peer_anl())

@app.route('/peeranl_answer', methods=['POST'])
def peeranl_answer():
    print('Answer: ' + str(request.form.get('answer')))
    print('Useranswer: ' + str(request.form.get('useranswer')))
    if str(request.form.get('answer')) == str(request.form.get('useranswer')):
        db.setPeercoaching(db.getPeercoaching()+2)
        return "<p> WINNING! </p>"
    else:
        db.setPeercoaching(db.getPeercoaching()-1)
        return "<p> LOSUR! </p>"



analypage = Analyse("USERNAME")
@app.route('/analyse',methods=['GET', 'POST'])
def analyse():
    return analypage.GetCurrentView(request)

@app.route('/development')
def development():
    return Development().get()

@app.route('/development-answer', methods=['POST'])
def developmentanswer():
    return Development().answers(request.form)

@app.route('/project/')
def project():
    #return render_template("Projects.html",taskList=task.getListOfTask(1),time=task.getSecTimeLeftOnCounter())
    return project1(1)

@app.route('/project/<int:project_id>')
def project1(project_id):
    return render_template("Projects.html",taskList=task.getListOfTask(task.getProjectNumber()),time=task.getSecTimeLeftOnCounter(),progress=task.getItemDoneForProject(task.getProjectNumber()),pName=task.getProjectName(task.getProjectNumber()))

@app.route('/project_task', methods=['POST'])
def projectTask():
    taskID =request.form['taskID']

    task.isCooldownOver(taskID)

    return render_template("Projects.html",taskList=task.getListOfTask(task.getProjectNumber()),time=task.getSecTimeLeftOnCounter(),progress=task.getItemDoneForProject(task.getProjectNumber()),pName=task.getProjectName(task.getProjectNumber()))

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
    print("ua: " + useranswer[0])
    print("ua: " + useranswer[1])
    print("ua: " + useranswer[2])
    print("ua: " + useranswer[3])
    print("ua: " + useranswer[4])
    return sparG.afterQ(useranswer,int(timer),True)

@app.route('/spar/Q2-check', methods=['POST'])
def sparq2check():
    ua = request.form['qq'].lower().strip()
    return sparG.checkQ2(ua)

if __name__ == "__main__":


    #Uncomment before pushing to run on server / Comment when testing locally
    #app.run(host='145.24.222.234', port=8080)

    #Uncomment when testing locally / Comment before pushing to run on server
    app.run(debug=True)
