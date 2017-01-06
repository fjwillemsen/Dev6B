import unittest
from ProjectTask import *

class Test_Test_ProjectTask(unittest.TestCase):
    project_task = None

    def setUp(self):
        self.project_task = ProjectTask()

    def tearDown(self):
        self.project_task = None
    

    def test_getListOfTask(self):
        self.assertEqual(self.project_task.project2,self.project_task.getListOfTask(2))

    def test_getProjectName(self):
        self.assertEqual(self.project_task.listofProjectNames[1],self.project_task.getProjectName(2))

    def test_getItemDoneForProject(self):
        self.project_task.listOfProjectTask[4] = []
        self.assertEqual("0/8",self.project_task.getItemDoneForProject(4))

    def test_getProjectNumber_None(self):
        self.assertEqual(1,self.project_task.getProjectNumber())

    def test_getProjectNumber_Some(self):
        self.project_task.listOfProjectTask[0] =[]
        self.project_task.listOfProjectTask[1] =[]
        self.project_task.listOfProjectTask[2] =[]
        self.assertEqual(4,self.project_task.getProjectNumber())

    def test_getProjectNumber_All(self):
        self.project_task.listOfProjectTask[0] =[]
        self.project_task.listOfProjectTask[1] =[]
        self.project_task.listOfProjectTask[2] =[]
        self.project_task.listOfProjectTask[3] =[]
        self.project_task.listOfProjectTask[4] =[]
        self.project_task.listOfProjectTask[5] =[]
        self.project_task.listOfProjectTask[6] =[]
        self.assertEqual(7,self.project_task.getProjectNumber())

    def test_UpdateTaskList(self):
        self.project_task.updateListOftask_UNITTEST("4-3")
        self.assertEqual(7,len(self.project_task.project4))
        self.assertEqual(10,self.project_task.cooldownSecOver)
        self.assertFalse(self.project_task.lastActionDate is None)


    def test_isCdOver_1stIFTrue(self):
        self.project_task.isCooldownOver_UNITTEST("2-3")
        self.assertEqual(5,len(self.project_task.project2))

    def test_isCdOver_2ndIFTrue(self):
        self.project_task.lastActionDate = datetime.now()
        self.project_task.cooldownSecOver = 0
        self.project_task.isCooldownOver_UNITTEST("2-3")
        self.assertEqual(5,len(self.project_task.project2))

    def test_isCdOver_2ndIFFalse(self):
        self.project_task.lastActionDate = datetime.now()
        self.project_task.cooldownSecOver = 20
        self.project_task.isCooldownOver_UNITTEST("2-3")
        self.assertEqual(6,len(self.project_task.project2))

    def test_amountSecLeft_1stIFTrue(self):
        self.assertAlmostEqual(0,self.project_task.getSecTimeLeftOnCounter())

    def test_amountSecLeft_2ndIFTrue(self):
        self.project_task.cooldownSecOver = 1000
        self.project_task.lastActionDate = datetime.now()
        self.assertGreater(self.project_task.getSecTimeLeftOnCounter(),1)

    def test_amountSecLeft_2ndIFFalse(self):
        self.project_task.cooldownSecOver = -1000
        self.project_task.lastActionDate = datetime.now()
        self.assertGreater(1,self.project_task.getSecTimeLeftOnCounter())



if __name__ == '__main__':
    unittest.main()
