 # Priority of a requirement. (Must, should, could or would)
from flask import render_template,request
import random


class Priority:
    def __init__(self,must,should,could,would):
        self.must = must
        self.should = should
        self.could = could
        self.would = would
        if would:
            self.text = "would"
        if could:
            self.text = "could"
        if should:
            self.text = "should"
        if must:
            self.text = "must"

    def IsMust(self):
        return self.must
    def IsShould(self):
        return self.should
    def IsCould(self):
        return self.could
    def IsWould(self):
        return self.would
 # Status of a requirement, wether one has been completed or not
class Status:
    def __init__(self,done):
        self.done = done
    def IsDone(self):
        return self.done
    def setDone(self):
        self.done = True
 # A requirement, has a basic text, an instance of the Priority class and an instance of the Status class
class Requirement:
    def __init__(self, text, priority ,status,position):
        self.status = status
        self.priority = priority
        self.text = text
        self.position = position


def randomreq():
    textrand = [10]
    for i in range(10):
        textrand.append(0)
    textrand[0] = "Make UI"
    textrand[1] = "Add Charts"
    textrand[2] = "Make UML Diagrams"
    textrand[3] = "Add Coffee-Options"
    textrand[4] = "Add Email-Support"
    textrand[5] = "Import Australiankitties"
    textrand[6] = "Add Itemlist"
    textrand[7] = "Implement Adminfeatures"
    textrand[8] = "Add Main Menu"
    textrand[9] = "Add Contact Page"
    textrand[10] = "Implement Design Patterns"
    return textrand[random.randint(0,10)]

 #Actual Analyse Class
class Analyse:
    def __init__(self, username):
        must = Priority(True,False,False,False)
        should = Priority(False, True, False, False)
        could = Priority(False, False, True, False)
        would = Priority(False, False, False, True)
        self.requirements = dict({1: Requirement(randomreq(), could, Status(False),1),2:Requirement(randomreq(), would, Status(False),2),3:Requirement(randomreq(), must,Status(False),3),4:Requirement(randomreq(), should, Status(False),4)})

        # self.requirementone = Requirement("Make UI", must,Status(False))
        # self.requirementtwo = Requirement("Add Charts", should, Status(False))
        # self.requirementthree = Requirement("Add Email Notifications", could, Status(False))
        # self.requirementfour = Requirement("Add Coffee Button", would, Status(False))
        self.username = username

    
    def GetCurrentView(self,request):
        usern = self.username
        if request.method == 'POST':

            requir = self.requirements

            first = request.form['First']
            second = request.form['Second']
            third = request.form['Third']
            four = request.form['Fourth']
            if(self.Check(first,second,third,four,requir)):
                print("test")
                return render_template("analysecompleted.html", user=usern)

            else:
                print("test2")
                return render_template("analyse.html", user=usern, requirements=self.requirements, completed = True)

        else:
            return render_template("analyse.html", user=usern, requirements=self.requirements, completed=False)

    def Check(self,first, second, third, fourth,requirements):
        one = False
        two = False
        three = False
        four = False
        for i,Requirement in iter(requirements.items()):
            if Requirement.priority.must and str(Requirement.position) == first:
                one = True
            if Requirement.priority.should and str(Requirement.position) == second:
                two = True
            if Requirement.priority.could and str(Requirement.position) == third:
                three = True
            if Requirement.priority.would and str(Requirement.position) == fourth:
                four = True
        if(one and two and three and four):
            returnval = True
        else:
            returnval = False
        return returnval



