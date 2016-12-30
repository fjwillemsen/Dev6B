from unittest import TestCase
from Analyse import *

class TestGetDevelopDia(TestCase):
    def test_GetDevelopDia(self):
        self.Development = GetDevelopDia()
        if(self.Development.view.name == "Development" and self.Development.name != None):
            pass
    def test_GetLogicalDia(self):
        self.Logical = GetLogicalDia()
        if (self.Logical.view.name == "Logical" and self.Logical.name != None):
            pass

    def test_GetPhysicalDia(self):
        self.Physical = GetPhysicalDia()
        if (self.Physical.view.name == "Logical" and self.Physical.name != None):
            pass

    def test_GetProcessDia(self):
        self.Process = GetProcesdia()
        if (self.Process.view.name == "Logical" and self.Process.name != None):
            pass

    def test_GetUseCaseDia(self):
        self.UseCase = GetUseCaseDia()
        if (self.UseCase.view.name == "Logical" and self.UseCase.name != None):
            pass