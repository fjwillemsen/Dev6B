from unittest import TestCase

from Analyse import *


class TestPriority(TestCase):
    def setUp(self):
        self.must = Priority(True,False,False,False)
        self.should = Priority(False, True, False, False)
        self.could = Priority(False, False, True, False)
        self.would = Priority(False, False, False, True)


    #If priority is at least must, returns true
    def test_IsMust(self):
        correctness = True
        if not self.must.IsMust():
            correctness = False
        if self.should.IsMust():
            correctness = False
        if self.could.IsMust():
            correctness = False
        if self.would.IsMust():
            correctness = False
        if not correctness:
            self.fail()


    #If priority is at least should and not must, return true
    def test_IsShould(self):
        correctness = True
        if self.must.IsShould():
            correctness = False
        if not self.should.IsShould():
            correctness = False
        if self.could.IsShould():
            correctness = False
        if self.would.IsShould():
            correctness = False
        if not correctness:
            self.fail()

    # If priority is at least could and not must,should, return true
    def test_IsCould(self):
        correctness = True
        if self.must.IsCould():
            correctness = False
        if self.should.IsCould():
            correctness = False
        if not self.could.IsCould():
            correctness = False
        if self.would.IsCould():
            correctness = False
        if not correctness:
            self.fail()

    # If priority is atleast would and not could,should or must, return true
    def test_IsWould(self):
        correctness = True
        if self.must.IsWould():
            correctness = False
        if self.should.IsWould():
            correctness = False
        if  self.could.IsWould():
            correctness = False
        if not self.would.IsWould():
            correctness = False
        if not correctness:
            self.fail()
