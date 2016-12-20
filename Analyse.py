 # Priority of a requirement. (Must, should, could or would)
from flask import render_template,request
import random
from datetime import datetime, timedelta


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

#Returns a random string for a requirement
#TODO: Make it so that there can't be duplicate requirements (Ex: a must and a could both have "ADD MAIL-SUPPORT" as text)
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

#This class keeps track of which priorities have been taken and returns one that hasn t been taken previously with getpriority
class Randomater:
    must = Priority(True, False, False, False)
    musttaken = False
    should = Priority(False, True, False, False)
    shouldtaken = False
    could = Priority(False, False, True, False)
    couldtaken = False
    would = Priority(False, False, False, True)
    wouldtaken = False
    def getpriority(self):
        lucioooballl = random.randint(0,3)
        if( lucioooballl == 0):
            if(not self.musttaken):
                self.musttaken = True
                return self.must
            else:
                return self.getpriority()
        if (lucioooballl == 1):
            if (not self.shouldtaken):
                self.shouldtaken= True
                return self.should
            else:
                return self.getpriority()
        if (lucioooballl == 2):
            if (not self.wouldtaken):
                self.wouldtaken = True
                return self.would
            else:
                return self.getpriority()
        if (lucioooballl == 3):
            if (not self.couldtaken):
                self.couldtaken = True
                return self.could
            else:
                return self.getpriority()

 #Actual Analyse Class
class Analyse:
    def __init__(self, username):
        self.requirements = self.GenerateRequirements()
        self.username = username

        self.cooldowntill = datetime.now() - timedelta(days=10)
    def GetCurrentView(self,request):
        usern = self.username
        if self.cooldowntill > datetime.now():
            return render_template("analysecompleted.html", user=usern, date=self.cooldowntill)
        elif request.method == 'POST':
            first = request.form['First']
            second = request.form['Second']
            third = request.form['Third']
            four = request.form['Fourth']
            if self.Check(first,second,third,four,self.requirements):
                print("test")
                self.cooldowntill = datetime.now() + timedelta(minutes=1)
                return render_template("analysecompleted.html", user=usern, date=self.cooldowntill)
            else:
                print("test2")
                return render_template("analyse.html", user=usern, requirements=self.requirements, completed = True)
        #IF NOT A POST REQUEST; RELOAD THE PAGE AND GENERATE NEW REQUIREMENTS
        else:
            self.requirements = self.GenerateRequirements()
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
    def GenerateRequirements(self):

        hallojumbo = Randomater()
        requirements = dict(
            {1: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 1),
             2: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 2),
             3: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 3),
             4: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 4)})
        return requirements


