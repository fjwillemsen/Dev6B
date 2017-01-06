import random as r
from flask import Flask, render_template, request
from string import Template
import database

class Development:

    xgensize = 0
    ygensize = 0
    xgendestination = 0
    ygendestination = 0
    xgennumberofsteps = 0
    ygennumberofsteps = 0

    global db
    db = database.database(None, 'localhost', 3306)

    def get(self):
        temp = Template(render_template("development.html"))
        code = self.generateCode(12)
        answer = self.getDecryptedCode(code)
        self.generateLocation()
        print(answer)
        print(self.xgendestination, ", ", self.ygendestination)
        return temp.substitute(devscore = db.getDev(), numbercode=code, answercode=answer,
                               xsize = self.xgensize, ysize = self.ygensize, xnumberofsteps = self.xgennumberofsteps, ynumberofsteps = self.ygennumberofsteps, xdestination = self.xgendestination, ydestination = self.ygendestination)

    # Assignment 1
    def generateCode(self, max):
        code = ""
        for i in range(0,max):
            code += str(r.randint(0,9))
        return Development.encodeString(self, code)

    def encodeString(self, string):
        result = ""
        count = 0
        for i in string:
            if count !=0 and count %4 == 0:
                result += '-'
            result += i
            count += 1
        return result

    def getDecryptedCode(self, code):
        result = ""
        for i in code:
            if i != '-':
                if int(i) < 5:
                    result += str(int(i) + 4)
                else:
                    result += str(int(i) - 3)
        return Development.encodeString(self, result)

    # Assignment 2
    def generateLocation(self):
        self.xgensize = r.randint(1,10)
        self.ygensize = r.randint(1,10)
        self.xgennumberofsteps = r.randint(10,40)
        self.ygennumberofsteps = r.randint(10,40)
        self.xgendestination = (self.xgensize * self.xgennumberofsteps)
        self.ygendestination = (self.ygensize * self.ygennumberofsteps)

    #Answer
    def answers(self, form):
        correct = []
        if form is not None:
            if form.get('answer1') == form.get('useranswer1'):
                correct.append(1)
            if form.get('answer2x') == form.get('useranswer2x') and form.get('answer2y') == form.get('useranswer2y'):
                correct.append(2)
            if  form.get('answer3.1') == form.get('useranswer3.1') and \
                form.get('answer3.2') == form.get('useranswer3.2') and \
                form.get('answer3.3') == form.get('useranswer3.3') and \
                form.get('answer3.4') == form.get('useranswer3.4') and \
                form.get('answer3.5') == form.get('useranswer3.5') and \
                form.get('answer3.6') == form.get('useranswer3.6') and \
                form.get('answer3.7') == form.get('useranswer3.7'):
                correct.append(3)
        return self.checkCorrect(correct)

    def checkCorrect(self, correct):
        temp = Template(render_template("development-answers.html"))
        newscore = len(correct) * 33 + 1
        if newscore > int(db.getDev()):
            db.setDev(newscore)

        if len(correct) < 1:
            return temp.substitute(text = "You didn't pass a single test. You failed us.")
        if len(correct) < 3:
            return temp.substitute(text = "Looks like you didn't pass all tests. These are the ones you did pass: " + ", ".join(map(str, correct)))
        if len(correct) > 2:
            return temp.substitute(text = "Congratulations, you passed every test!")