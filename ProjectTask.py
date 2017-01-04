from datetime import datetime
from random import randint
class ProjectTask:
    def __init__(self):
        self.project1 = [["1-1",'task1',5],["1-2",'task2',10],["1-3",'task3',10],["1-4",'task4',10],["1-5",'task5',10],["1-6",'task6',10]];
        self.project2 = [["2-1",'task1',5],["2-2",'task2',10],["2-3",'task3',10],["2-4",'task4',10],["2-5",'task5',10],["2-6",'task6',10]];
        self.project3 = [["3-1",'task1',5],["3-2",'task2',10],["3-3",'task3',10],["3-4",'task4',10],["3-5",'task5',10],["3-6",'task6',10]];
        self.project4 = [["4-1",'task1',5],["4-2",'task2',10],["4-3",'task3',10],["4-4",'task4',10],["4-5",'task5',10],["4-6",'task6',10]];
        self.project56 = [["56-1",'task1',5],["56-2",'task2',10],["56-3",'task3',10],["56-4",'task4',10],["56-5",'task5',10],["56-6",'task6',10]];
        self.project78 = [["78-1",'task1',5],["78-2",'task2',10],["78-3",'task3',10],["78-4",'task4',10],["78-5",'task5',10],["78-6",'task6',10]];
        self.listofProjectNames =["project 1","project 2","project 3","project 4","project 56","project 78"];
        self.listOfProjectTask = (self.project1,self.project2,self.project3,self.project4,self.project56,self.project78);
        self.lastActionDate = None;
        self.cooldownSecOver = None;
        self.listItemsPerProject = [len(self.project1),len(self.project2),len(self.project3),len(self.project4),len(self.project56),len(self.project78)];

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
            if(len(self.listOfProjectTask[y]) != 0):
                x = y +1
            else:
                y = y +1

        return x
    def getProjectName(self,project_id):
        return self.listofProjectNames[project_id-1]

    def addRandomTimeToTask(self,project):
            for task in project:
                x = randint(0,9)
                task[2] = task[2] + x


    def updateListOftask(self,task_id):
        for projectTask in self.listOfProjectTask:
            for task in projectTask:
                if task[0] == task_id:
                    self.cooldownSecOver = task[2]
                    self.lastActionDate = datetime.now()
                    projectTask.remove(task);
                    self.addRandomTimeToTask(projectTask)

    

    def isCooldownOver(self,task_id):
        if (self.lastActionDate is None):
            self.updateListOftask(task_id)
          #  return "True"
        elif ((datetime.now()-self.lastActionDate).total_seconds() >= self.cooldownSecOver):
            self.updateListOftask(task_id)
        #    return "True"
     #   else:
    #        return "False"
   #    datetime.timedelta.total_seconds
    def getSecTimeLeftOnCounter(self):
        if self.lastActionDate is None or self.cooldownSecOver is None:
            
            return 0
        else:
            
            secLeft =  self.cooldownSecOver - ((datetime.now()-self.lastActionDate).total_seconds())
            if (secLeft >= 0 ):
                return secLeft
            else:
                return 0
#print(ProjectTask(1).getListOfTask()[1])