class ProjectTask:
    def __init__(self):
        self.project1 = [("1-1",'task1',5),("1-2",'task2',10),("1-3",'task3',10),("1-4",'task4',10),("1-5",'task5',10),("1-6",'task6',10)];
        self.project2 = [("1-1",'task1',5),("1-2",'task2',10),("1-3",'task3',10),("1-4",'task4',10),("1-5",'task5',10),("1-6",'task6',10)];
        self.project3 = [("1-1",'task1',5),("1-2",'task2',10),("1-3",'task3',10),("1-4",'task4',10),("1-5",'task5',10),("1-6",'task6',10)];
        self.project4 = [("1-1",'task1',5),("1-2",'task2',10),("1-3",'task3',10),("1-4",'task4',10),("1-5",'task5',10),("1-6",'task6',10)];
        self.project56 = [("1-1",'task1',5),("1-2",'task2',10),("1-3",'task3',10),("1-4",'task4',10),("1-5",'task5',10),("1-6",'task6',10)];
        self.project78 = [("1-1",'task1',5),("1-2",'task2',10),("1-3",'task3',10),("1-4",'task4',10),("1-5",'task5',10),("1-6",'task6',10)];
        self.listOfProjectTask = (self.project1,self.project2,self.project3,self.project4,self.project56,self.project78);

    def getListOfTask(self,project_id):
        self.project_id =project_id-1
        return self.listOfProjectTask[self.project_id]



    def updateListOftask(self,task_id):
        for projectTask in self.listOfProjectTask:
            for task in projectTask:
                if task[0] == task_id:
                    projectTask.remove(task);
  
       

#print(ProjectTask(1).getListOfTask()[1])