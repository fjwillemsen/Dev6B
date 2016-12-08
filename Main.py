from flask import Flask, render_template, request
from Development import Development

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

@app.route('/werk')
def werk():
    return "<h2>Testing HTML werk</h2>"

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

@app.route('/project')
def project():
    return "<h2>Testing HTML project</h2>"

@app.route('/spar')
def spar():
    return "<h2>Testing HTML spar</h2>"

if __name__ == "__main__":
    app.run(debug=True)
