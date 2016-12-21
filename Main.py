from flask import Flask, render_template,request
from ProjectTask import ProjectTask
from Development import Development
from Peercoaching import Peercoaching
from english import English
from Analyse import Analyse
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
task = ProjectTask()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/english',methods = ['POST', 'GET'])
def english():
    return English().getView(request)


@app.route('/peercoaching')
def peercoaching():
    return Peercoaching.get(Peercoaching)


analypage = Analyse("USERNAME")
@app.route('/analyse',methods=['GET', 'POST'])
def analyse():
    return Analyse.GetCurrentView(analypage, request)

@app.route('/development')
def development():
    return Development.get(Development)

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
    app.run(debug=True)
