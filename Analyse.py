from flask import render_template,request
import random
from datetime import datetime, timedelta
#import database
# from Main import changeScore
class View:
    def __init__(self,name):
        self.name = name

class Diagram:
    def __init__(self, view, name):
        self.view = view
        self.name = name

def GetDevelopDia():
    textrand = [2]
    for i in range(2):
        textrand.append(0)
    textrand[0] = "Component"
    textrand[1] = "Package"
    return Diagram(View("Development"),textrand[random.randint(0, 1)])

def GetLogicalDia():
    textrand = [2]
    for i in range(2):
        textrand.append(0)
    textrand[0] = "State"
    textrand[1] = "Class"
    return Diagram(View("Logical"),textrand[random.randint(0, 1)])

def GetPhysicalDia():
    return Diagram(View("Physical"),"Deployment")

def GetProcesdia():
    textrand = [2]
    for i in range(2):
        textrand.append(0)
    textrand[0] = "Sequence"
    textrand[1] = "Flow"
    return Diagram(View("Process"),textrand[random.randint(0, 1)])

def GetUseCaseDia():
    return Diagram(View("Use Case"),"Use Case")

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

#This class keeps track of which priorities have been taken and returns one that hasn t been taken previously with getpriority. Same for diagrams
class Randomater:
    must = Priority(True, False, False, False)
    musttaken = False
    should = Priority(False, True, False, False)
    shouldtaken = False
    could = Priority(False, False, True, False)
    couldtaken = False
    would = Priority(False, False, False, True)
    wouldtaken = False
    devtaken = False
    logtaken = False
    phytaken = False
    protaken = False
    usetaken = False
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
    def getdiagram(self):
        lucioooballl = random.randint(0, 4)
        if (lucioooballl == 0):
            if (not self.devtaken):
                self.devtaken = True
                return GetDevelopDia()
            else:
                return self.getdiagram()
        if (lucioooballl == 1):
            if (not self.logtaken):
                self.logtaken = True
                return GetLogicalDia()
            else:
                return self.getdiagram()
        if (lucioooballl == 2):
            if (not self.phytaken):
                self.phytaken = True
                return GetPhysicalDia()
            else:
                return self.getdiagram()
        if (lucioooballl == 3):
            if (not self.protaken):
                self.protaken = True
                return GetProcesdia()
            else:
                return self.getdiagram()
        if (lucioooballl == 4):
            if (not self.usetaken):
                self.usetaken = True
                return GetUseCaseDia()
            else:
                return self.getdiagram()

#Actual Analyse Class
class Analyse:
    def __init__(self, username):
        self.requirements = self.GenerateRequirements()
        self.username = username
        self.cooldowntillreq = datetime.now() - timedelta(days=10)
        self.cooldowntilldia = datetime.now() - timedelta(days=10)
        #self.database = database.database(None, '145.24.222.234', 3306)
        self.currentscore= 0;
    def GetCurrentView(self,request):
        usern = self.username
        if request.method == 'POST':
            if request.form['type']=="req":
                first = request.form['First']
                second = request.form['Second']
                third = request.form['Third']
                four = request.form['Fourth']
                if self.CheckReq(first, second, third, four, self.requirements):
                    self.currentscore +=5
                    self.cooldowntillreq = datetime.now() + timedelta(minutes=1)
            if request.form['type'] == "dia":
                dev = request.form['Dev']
                log = request.form['Log']
                phy = request.form['Phy']
                pro = request.form['Pro']
                use = request.form['Use']
                if self.CheckDia(dev,log,phy,pro,use,self.diagrams):
                    self.currentscore +=5
                    self.cooldowntilldia = datetime.now() + timedelta(minutes=1)
        #IF NOT A POST REQUEST; RELOAD THE PAGE AND GENERATE NEW REQUIREMENTS
        else:
            self.requirements = self.GenerateRequirements()
            self.diagrams = self.GenerateDiagrams()

        self.requirementstatus = self.CheckTimerReq()
        self.diagramstatus = self.CheckTimerDia()
        return render_template("analyse.html", user=usern, requirements=self.requirements, datedia = self.cooldowntilldia ,datereq=self.cooldowntillreq, diagrams=self.diagrams, attempt=False, requirementscompleted=self.requirementstatus,diagramscompleted=self.diagramstatus,score=self.currentscore)

    def CheckTimerReq(self):
        returnvalue = False
        if self.cooldowntillreq > datetime.now():
            returnvalue = True
        return returnvalue
    def CheckTimerDia(self):
        returnvalue = False
        if self.cooldowntilldia > datetime.now():
            returnvalue = True
        return returnvalue

    def CheckReq(self, first, second, third, fourth, requirements):
        one = False
        two = False
        three = False
        four = False
        for i,Requirement in iter(requirements.items()):
            if Requirement.priority.must and str(Requirement.position) == str(first):
                one = True
            if Requirement.priority.should and str(Requirement.position) == str(second):
                two = True
            if Requirement.priority.could and str(Requirement.position) == str(third):
                three = True
            if Requirement.priority.would and str(Requirement.position) == str(fourth):
                four = True
        if(one and two and three and four):
            returnval = True
        else:
            returnval = False
        return returnval

    def CheckDia(self, first, second, third, fourth,fifth, diagrams):
        one = False
        two = False
        three = False
        four = False
        five = False
        returnbool = False
        if(int(first)>=1 and int(first) <=5):
            if diagrams[int(first)].view.name == "Development":
                one = True
        if (int(second) >= 1 and int(second) <= 5):
            if diagrams[int(second)].view.name == "Logical":
                two = True
        if (int(third) >= 1 and int(third) <= 5):
            if diagrams[int(third)].view.name == "Physical":
                three = True
        if (int(fourth) >= 1 and int(fourth) <= 5):
            if diagrams[int(fourth)].view.name == "Process":
                four = True
        if (int(fifth) >= 1 and int(fifth) <= 5):
            if diagrams[int(fifth)].view.name == "Use Case":
                five = True
        if one and two and three and four and five:
            returnbool = True
        return returnbool

    def GenerateRequirements(self):
        hallojumbo = Randomater()
        requirements = dict(
            {1: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 1),
             2: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 2),
             3: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 3),
             4: Requirement(randomreq(), hallojumbo.getpriority(), Status(False), 4)})
        return requirements
    def GenerateDiagrams(self):
        hallojumbo = Randomater()
        Diagrams = dict(
            {1:hallojumbo.getdiagram(),
             2:hallojumbo.getdiagram(),
             3:hallojumbo.getdiagram(),
             4:hallojumbo.getdiagram(),
             5:hallojumbo.getdiagram()})
        return Diagrams
