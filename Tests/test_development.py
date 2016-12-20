from unittest import TestCase
from classes.Development import Development
from string import Template

__author__ = 'floris-jan'


class TestDevelopment(TestCase):
  def test_generateCode(self):
    self.failUnlessEqual(len(Development.generateCode(12)), 12+2)

  def test_encodeString(self):
    self.failUnlessEqual(len(Development.generateCode(12)), len(Development.generateCode(12)))
    self.failUnless(Development.generateCode(12).find('-') == 4)

  def test_getDecryptedCode(self):
    code = Development.generateCode(12)
    result = ""
    for i in code:
        if i != '-':
            if int(i) < 5:
                result += str(int(i) + 4)
            else:
                result += str(int(i) - 3)
    result = Development.encodeString(result)
    self.failUnlessEqual(Development.getDecryptedCode(code), result)

  def test_get(self):
    dev = Development
    # self.failUnless(isinstance(Development.get()) == isinstance(Template()))
