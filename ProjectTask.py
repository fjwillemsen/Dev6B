from datetime import datetime
from random import randint
import pymysql
class ProjectTask:
    def __init__(self):
        self.project1 = [["1-1",'task1',5],["1-2",'task2',10],["1-3",'task3',10],["1-4",'task4',10],["1-5",'task5',10],["1-6",'task6',10]];
        self.project2 = [["2-1",'task1',5],["2-2",'task2',10],["2-3",'task3',10],["2-4",'task4',10],["2-5",'task5',10],["2-6",'task6',10]];
        self.project3 = [["3-1",'task1',5],["3-2",'task2',10],["3-3",'task3',10],["3-4",'task4',10],["3-5",'task5',10],["3-6",'task6',10],["3-7",'task7',20],["3-8",'task8',20]];
        self.project4 = [["4-1",'task1',5],["4-2",'task2',10],["4-3",'task3',10],["4-4",'task4',10],["4-5",'task5',10],["4-6",'task6',10],["4-7",'task7',20],["4-8",'task8',20]];
        self.project56 = [["56-1",'task1',5],["56-2",'task2',10],["56-3",'task3',10],["56-4",'task4',10],["56-5",'task5',10],["56-6",'task6',10],["56-7",'task7',10],["56-8",'task8',10],["56-9",'task9',10],["56-10",'task10',10]];
        self.project78 = [["78-1",'task1',5],["78-2",'task2',10],["78-3",'task3',10],["78-4",'task4',10],["78-5",'task5',10],["78-6",'task6',10],["78-7",'task7',10],["78-8",'task8',10],["78-9",'task9',10],["78-10",'task10',10]];
        self.projectEND = [["end",'veel wacht plezier',0]];
        self.listofProjectNames =["project 1","project 2","project 3","project 4","project 56","project 78","het einde"];
        self.listOfProjectTask = [self.project1,self.project2,self.project3,self.project4,self.project56,self.project78,self.projectEND];
        self.lastActionDate = None;
        self.cooldownSecOver = None;
        self.listItemsPerProject = [len(self.project1),len(self.project2),len(self.project3),len(self.project4),len(self.project56),len(self.project78),len(self.projectEND)];

    def getListOfTask(self,project_id):
        self.project_id =project_id-1
        return self.listOfProjectTask[self.project_id]

    def getItemDoneForProject(self,project_id):
        nr= str(0+ self.listItemsPerProject[project_id-1] - len(self.listOfProjectTask[project_id-1]) )+"/" +str(self.listItemsPerProject[project_id-1])
        return nr

    def getProjectNumber(self):
        x = 0
        y = 0
        while(x==0):
            if(y<len(self.listOfProjectTask)):
                if(len(self.listOfProjectTask[y]) != 0):
                    x = y +1
                else:
                    y = y +1
            else:
                x = y
        return x

    def getProjectName(self,project_id):
        return self.listofProjectNames[project_id-1]

    def addRandomTimeToTask(self,project):
            for task in project:
                x = randint(2,9)
                task[2] = task[2] + x
            
    def setScore2Db(self,connection,cursor):
        sql = "UPDATE user set project = project +1;"
        try:
            cursor.execute(sql)
        except:
            connection.rollback()

    def getScoreFromDb(self,connection,cursor):
        sql = "SELECT project from user;"
        res = None
        try:
            cursor.execute(sql)
            res = cursor.fetchone()
        except:
            print("dit gaat niet werken")

        return res

    def resetScoreOnDb(self,connection,cursor):
        sql = "UPDATE user set project = 0;"
        try:
            cursor.execute(sql)
        except:
            connection.rollback()

    def updateListOftask(self,task_id,connection,cursor):
        for projectTask in self.listOfProjectTask:
            for task in projectTask:
                if task[0] == task_id:
                    self.cooldownSecOver = task[2]
                    self.lastActionDate = datetime.now()
                    projectTask.remove(task);
                    self.addRandomTimeToTask(projectTask)
                  #  self.setScore2Db(connection,cursor)

    def updateListOftask_UNITTEST(self,task_id):
        for projectTask in self.listOfProjectTask:
            for task in projectTask:
                if task[0] == task_id:
                    self.cooldownSecOver = task[2]
                    self.lastActionDate = datetime.now()
                    projectTask.remove(task);
                    self.addRandomTimeToTask(projectTask)

    def isCooldownOver(self,task_id,connection,cursor):
        if (self.lastActionDate is None):
            self.updateListOftask(task_id,connection,cursor)
        elif ((datetime.now()-self.lastActionDate).total_seconds() >= self.cooldownSecOver):
            self.updateListOftask(task_id,connection,cursor)

    def isCooldownOver_UNITTEST(self,task_id):
        if (self.lastActionDate is None):
            self.updateListOftask_UNITTEST(task_id)
        elif ((datetime.now()-self.lastActionDate).total_seconds() >= self.cooldownSecOver):
            self.updateListOftask_UNITTEST(task_id)



    def getSecTimeLeftOnCounter(self):
        if self.lastActionDate is None or self.cooldownSecOver is None:
            return 0
        else:
            secLeft =  self.cooldownSecOver - ((datetime.now()-self.lastActionDate).total_seconds())
            if (secLeft >= 0 ):
                return secLeft
            else:
                return 0