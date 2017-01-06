from ProjectTask import ProjectTask
from english import English
from Analyse import Analyse
from Spar import Spar
from flask import Flask, render_template, request
import pymysql
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
global connection
global cursor
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
    global connection
    global cursor
    return render_template("Projects.html",taskList=task.getListOfTask(task.getProjectNumber()),time=task.getSecTimeLeftOnCounter(),pName=task.getProjectName(task.getProjectNumber()))

@app.route('/project_task', methods=['POST'])
def projectTask():
    global connection
    global cursor
    taskID =request.form['taskID']

    task.isCooldownOver(taskID,connection,cursor)
    #progress=task.getScoreFromDb(connection,cursor),
    return render_template("Projects.html",taskList=task.getListOfTask(task.getProjectNumber()),time=task.getSecTimeLeftOnCounter(),pName=task.getProjectName(task.getProjectNumber()))

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

def changeScore(value, modifier):
    if value is not None:
        cursor.execute("UPDATE user SET score = '" + value + "'")
    elif modifier is not None:
        cursor.execute("UPDATE user SET score = score " + modifier)
task.isCooldownOver(1,connection,cursor)
if __name__ == "__main__":
    global connection
    global cursor

    #Uncomment before pushing to run on server / Comment when testing locally
    app.run(host='145.24.222.234', port=8080)
    connection = pymysql.connect(host='localhost', port=8081, user='root', passwd='2cKF97', db='CollegeCraft')

    #Uncomment when testing locally / Comment before pushing to run on server
    #app.run(debug=True)
    #connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='2cKF97', db='CollegeCraft')


    cursor = connection.cursor()
    

