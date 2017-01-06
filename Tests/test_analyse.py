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
    def setUp(self):
        self.testobject = Analyse("Bert")
        self.diagrams = dict(
            {1: GetDevelopDia(),
             2: GetLogicalDia(),
             3: GetPhysicalDia(),
             4: GetProcesdia(),
             5: GetUseCaseDia()})
        self.requirement = dict(
            {1: Requirement("Must", Priority(True, False, False, False), Status(False), 1),
             2: Requirement("Should", Priority(False, True, False, False), Status(False), 2),
             3: Requirement("Could", Priority(False, False, True, False), Status(False), 3),
             4: Requirement("Would", Priority(False, False, False, True), Status(False), 4)})

    def test_CheckDia(self):
        if not self.testobject.CheckDia(1, 2, 3, 4, 5, self.diagrams):
            self.fail()
        else:
            pass

    def test_CheckReq(self):
        if not self.testobject.CheckReq(1, 2, 3, 4, self.requirement):
            self.fail()
        else:
            pass
    # def test_addpoints(self):
    #     initial= self.testobject.database.getamount()
    #     endvalue = initial + 5
    #     self.testobject.database.runquery(self.testobject.username)
    #     if not int(self.testobject.database.getamount())==endvalue:
    #         self.fail()


