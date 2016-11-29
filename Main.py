from flask import Flask

class Account:
    def __init__(self,username, pw):
        self._username = username
        self._pw =pw

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"

@app.route('/english')
def english():
    return "<h2>Testing HTML English</h2>"

if __name__ == "__main__":
    app.run(debug=True)
