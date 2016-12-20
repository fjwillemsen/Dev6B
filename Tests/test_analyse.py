# from unittest import TestCase
# from flask import request
# from classes.Analyse import *
#
# class TestAnalyse(TestCase):
#     def setUp(self):
#         self.CorrectAnalyse = Analyse("Username")
#         must = Priority(True, False, False, False)
#         should = Priority(False, True, False, False)
#         could = Priority(False, False, True, False)
#         would = Priority(False, False, False, True)
#         self.CorrectAnalyse.requirements = dict({1: Requirement(randomreq(), could, Status(False),1),2:Requirement(randomreq(), would, Status(False),2),3:Requirement(randomreq(), must,Status(False),3),4:Requirement(randomreq(), should, Status(False),4)})
#
#         self.getter = request
#         self.getter.method = 'GET'
#         self.poster = request
#         self.poster.method = 'POST'
#         self.poster.form['First'] = 3
#         self.poster.form['Second'] = 4
#         self.poster.form['Third'] = 1
#         self.poster.form['Fourth'] = 2
#     # If request is post and has the correct answers ->returns analysecompleted render,
#     # If request is post and has the wrong answers -> returns analyse render with completed true
#     # If request is not post, return analyse render
#     def test_GetCurrentView(self):
#         renders = self.CorrectAnalyse.GetCurrentView(self.getter)
#         if not renders.template()=="analyse.html":
#             self.fail()
#
#
#
#     def test_Check(self):
#         self.fail()
from unittest import TestCase
from Analyse import *

class TestAnalyse(TestCase):
    testobject = Analyse("Bert")

    def test_GenerateRequirements(self):
        self.fail()

