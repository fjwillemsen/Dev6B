from flask import Flask, render_template, request
from Development import Development
import webbrowser,time
from ProjectTask import *
from datetime import datetime
class Account:
    def __init__(self,username, pw):
        self._username = username
        self._pw =pw

app = Flask(__name__)
task = ProjectTask()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/english')
def english():
    return "<h2>Testing HTML English</h2>"

@app.route('/werk')
def werk():
    return "<h2>Testing HTML werk</h2>"

@app.route('/analyse')
def analyse():
    return "<h2>Testing HTML analyse</h2>"

@app.route('/development')
def development():
    return Development.get(Development)

@app.route('/project/')
def project():
    return render_template("Projects.html",taskList=task.getListOfTask(1))

@app.route('/spar')
def spar():
    return "<h2>Testing HTML spar</h2>"



@app.route('/project/<int:project_id>')
def project1(project_id):
    return render_template("Projects.html",taskList=task.getListOfTask(project_id)) 

@app.route('/project_task', methods=['POST'])
def projectTask():
    taskID =request.form['taskID']

   # task.updateListOftask(taskID)
    task.isCooldownOver(taskID)
    return render_template("Projects.html",taskList=task.getListOfTask(1))

if __name__ == "__main__":
    webbrowser.open('http://localhost:5000',new=2, autoraise=True)
    app.run(debug=True)
