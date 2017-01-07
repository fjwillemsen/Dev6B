from flask import Flask, render_template, request
from database import database
class English:
    def simplePresent(self, answer):
        if answer == 'likes':
            return "Correct"
        return "Wrong"

    def simplePast(self,answer):
        if answer == 'ate':
            return "Correct"
        return "Wrong"

    def goingToFuture(self, answer):
        if answer == 'is going to phone':
            return "Correct"

        return "Wrong"

    def presentPerfect(self, answer):
        if answer == 'have been':
            return "Correct"

        return "Wrong"

    def pastPerfect(self, answer):
        if answer == 'had eaten':
            return "Correct"

        return "Wrong"

    def opt1Check(self,answer):
        if answer == "aspect":
            return "Correct"
        return "Wrong"

    def opt2Check(self,answer):
        if answer == "possible":
            return "Correct"
        return "Wrong"

    def opt3Check(self,answer):
        if answer == "population":
            return "Correct"
        return "Wrong"

    def opt4Check(self,answer):
        if answer == "suppose":
            return "Correct"
        return "Wrong"

    def opt5Check(self,answer):
        if answer == "tomorrow":
            return "Correct"
        return "Wrong"


    def govCheck(self, answer):
        if answer == "government":
            return "Correct"
        return "Wrong"

    def sprCheck(self, answer):
        if answer == "spread":
            return "Correct"
        return "Wrong"

    def attCheck(self, answer):
        if answer == "attended":
            return "Correct"
        return "Wrong"

    def jobCheck(self, answer):
        if answer == "jobs":
            return "Correct"
        return "Wrong"

    def busCheck(self, answer):
        if answer == "business":
            return "Correct"
        return "Wrong"

    def checkAmountCorrect(self, list):
        cnt = 0
        for x in list:
            if x == "Correct":
                cnt = cnt + 1

        if cnt >= 3:
            return True
        return False

    def checkAllCorrect(self, list):
        cnt = 0
        for x in list:
            if x == "Correct":
                cnt = cnt + 1

        if cnt == 5:
            return True
        return False

    def getView1(self, request):
        if request.method == 'POST':
            simplePresentA = request.form['Simple present']
            simplePastA = request.form['Simple past']
            futureA = request.form['Going-to future']
            presentPerfectA = request.form['Present perfect']
            pastPerfectA = request.form['Past perfect']

            a1 = self.simplePresent(simplePresentA)
            a2 = self.simplePast(simplePastA)
            a3 = self.goingToFuture(futureA)
            a4 = self.presentPerfect(presentPerfectA)
            a5 = self.pastPerfect(pastPerfectA)
            # db = database('root', 'localhost',3306)
            list = [a1, a2, a3, a4, a5]
            if self.checkAmountCorrect(list):
                # if self.checkAllCorrect(list):
                #     db.setEx1(1)
                #     print("(set ex1 to 1)")
                return render_template('checkEnglishResult.html', answers = list,ref = "/english2")
            else:
                return render_template('english_exercise1.html', failed = 1, time = 5000)
        return render_template('english_exercise1.html', failed = 0)

    def getView2(self, request):
        if request.method == 'POST':
            opt1 = request.form["options1"]
            opt2 = request.form["options2"]
            opt3 = request.form["options3"]
            opt4 = request.form["options4"]
            opt5 = request.form["options5"]
            o1 = self.opt1Check(opt1)
            o2 = self.opt2Check(opt2)
            o3 = self.opt3Check(opt3)
            o4 = self.opt4Check(opt4)
            o5 = self.opt5Check(opt5)
            # db = database('root', 'localhost',3306)
            list = [o1,o2,o3,o4,o5]
            if self.checkAmountCorrect(list):
                # if self.checkAllCorrect(list):
                #     db.setEx2(1)
                #     print('set ex2 to 1')
                return render_template('checkEnglishResult.html', answers = list,ref = "/english3")
            else:
                return render_template('english_exercise2.html', failed = 1, time = 5000)
        return render_template('english_exercise2.html', failed = 0)

    def getView3(self, request):
        if request.method == 'POST':
            f1 = request.form["government"]
            f2 = request.form["spread"]
            f3 = request.form["attended"]
            f4 = request.form["jobs"]
            f5 = request.form["business"]
            a11 = self.govCheck(f1)
            a12 = self.sprCheck(f2)
            a13 = self.attCheck(f3)
            a14 = self.jobCheck(f4)
            a15 = self.busCheck(f5)
            # db = database('root', 'localhost',3306)
            list = [a11,a12,a13,a14,a15]
            if self.checkAmountCorrect(list):
                # if self.checkAllCorrect(list):
                #     db.setEx3(1)
                #     if db.getEx1() == 1 and db.getEx2() == 1 and db.getEx3() == 1:
                #         db.setEng(1)
                #     print("set x3 to 1 and user english=1 "
                #           "if each x1,x2,x3 == 1. global = all score from vakken together")
                return render_template('checkEnglishResult.html', answers = list,ref = "empty")
            else:
                return render_template('english_exercise3.html', failed = 1, time = 5000)
        return render_template('english_exercise3.html', failed = 0)