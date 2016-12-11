from unittest import TestCase
from classes.Analyse import Status

class TestStatus(TestCase):
    def setUp(self):
        self.donest = Status(True)
        self.notdone = Status(False)
        self.variabdone = Status(False)

    #Returns falls if not done, returns true if done
    def test_IsDone(self):
        if not self.donest.IsDone():
            self.fail()
        if self.notdone.IsDone():
            self.fail()

    #Sets done to true
    def test_setDone(self):
        if not self.variabdone.IsDone():
            self.variabdone.setDone()
            if not self.variabdone.IsDone():
                self.fail()

