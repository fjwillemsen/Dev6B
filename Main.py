from flask import Flask, render_template, request
from classes.Development import Development
from flask import Flask, render_template,request

from ProjectTask import *
from classes.Development import Development
from classes.Peercoaching import Peercoaching
from classes.english import English

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

@app.route('/analyse')
def analyse():
    return "<h2>Testing HTML analyse</h2>"

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
    return "<h2>Testing HTML spar</h2>"




if __name__ == "__main__":
    app.run(debug=True)
