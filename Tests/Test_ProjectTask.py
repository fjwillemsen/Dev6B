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


    def test_UpdateTaskList(self):
        self.project_task.updateListOftask("4-3")
        self.assertEqual(5,len(self.project_task.project4))
        self.assertEqual(10,self.project_task.cooldownSecOver)
        self.assertFalse(self.project_task.lastActionDate is None)


    def test_isCdOver_1stIFTrue(self):
        self.project_task.isCooldownOver("2-3")
        self.assertEqual(5,len(self.project_task.project2))

    def test_isCdOver_2ndIFTrue(self):
        self.project_task.lastActionDate = datetime.now()
        self.project_task.cooldownSecOver = 0
        self.project_task.isCooldownOver("2-3")
        self.assertEqual(5,len(self.project_task.project2))

    def test_isCdOver_2ndIFFalse(self):
        self.project_task.lastActionDate = datetime.now()
        self.project_task.cooldownSecOver = 20
        self.project_task.isCooldownOver("2-3")
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
