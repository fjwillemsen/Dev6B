from unittest import TestCase
from Analyse import *

class TestGetDevelopDia(TestCase):
    def test_GetDevelopDia(self):
        self.Development = GetDevelopDia()
        if(self.Development.view.name == "Development" and self.Development.name != None):
            pass
        else:
            self.fail()
    def test_GetLogicalDia(self):
        self.Logical = GetLogicalDia()
        if (self.Logical.view.name == "Logical" and self.Logical.name != None):
            pass
        else:
            self.fail()
    def test_GetPhysicalDia(self):
        self.Physical = GetPhysicalDia()
        if (self.Physical.view.name == "Physical" and self.Physical.name != None):
            pass
        else:
            self.fail()
    def test_GetProcessDia(self):
        self.Process = GetProcesdia()
        if (self.Process.view.name == "Process" and self.Process.name != None):
            pass
        else:
            self.fail()
    def test_GetUseCaseDia(self):
        self.UseCase = GetUseCaseDia()
        if (self.UseCase.view.name == "Use Case" and self.UseCase.name != None):
            pass
        else:
            self.fail()
