import unittest
from ProjectTask import *

class Test_Test_ProjectTask(unittest.TestCase):
    project_task = None

    def setUp(self):
        self.project_task = ProjectTask()
        print(" setting up")

    def tearDown(self):
        self.project_task = None
        print(" tear down")
    

    def test_getListOfTask(self):
        print("test 1")
        self.assertEqual(self.project_task.project2,self.project_task.getListOfTask(2))


    def test_b(self):
        
        print("test 2")

if __name__ == '__main__':
    unittest.main()
