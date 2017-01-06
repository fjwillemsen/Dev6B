from unittest import TestCase, mock
from Development import Development
from werkzeug.datastructures import ImmutableMultiDict
from flask import render_template
from string import Template

__author__ = 'floris-jan'


class TestDevelopment(TestCase):

  def test_generateCode(self):
    dev = Development()
    self.failUnlessEqual(type(dev), type(Development()))
    self.failUnlessEqual(len(dev.generateCode(12)), 12+2)

  def test_encodeString(self):
    dev = Development()
    self.failUnlessEqual(type(dev), type(Development()))
    self.failUnlessEqual(len(dev.generateCode(12)), len(dev.generateCode(12)))
    self.failUnless(dev.generateCode(12).find('-') == 4)

  def test_getDecryptedCode(self):
    dev = Development()
    self.failUnlessEqual(type(dev), type(Development()))
    code = dev.generateCode(12)
    result = ""
    for i in code:
        if i != '-':
            if int(i) < 5:
                result += str(int(i) + 4)
            else:
                result += str(int(i) - 3)
    result = dev.encodeString(result)
    self.failUnlessEqual(dev.getDecryptedCode(code), result)

  def test_get(self):
    dev = Development()
    self.failUnlessEqual(type(dev), type(Development()))
    self.failUnlessEqual(dev.xgensize, 0)
    self.failUnlessEqual(dev.ygensize, 0)
    self.failUnlessEqual(dev.xgendestination, 0)
    self.failUnlessEqual(dev.ygendestination, 0)
    self.failUnlessEqual(dev.xgennumberofsteps, 0)
    self.failUnlessEqual(dev.ygennumberofsteps, 0)
    dev.generateLocation()
    self.failUnlessEqual(type(dev.xgensize), type(0))
    self.failUnlessEqual(type(dev.ygensize), type(0))
    self.failUnlessEqual(type(dev.xgendestination), type(0))
    self.failUnlessEqual(type(dev.ygendestination), type(0))
    self.failUnlessEqual(type(dev.xgennumberofsteps), type(0))
    self.failUnlessEqual(type(dev.ygennumberofsteps), type(0))

  def test_generateLocation(self):
      dev = Development()
      self.failUnlessEqual(type(dev), type(Development()))
      dev.generateLocation()
      self.failUnlessEqual(dev.xgendestination, dev.xgensize * dev.xgennumberofsteps)
      self.failUnlessEqual(dev.ygendestination, dev.ygensize * dev.ygennumberofsteps)

  def test_answers(self):
      dev = Development()
      self.failUnlessEqual(type(dev), type(Development()))

      #form mock object
      form = ImmutableMultiDict([('answer3.3', 'array'), ('useranswer3.2', ''), ('answer3.5', 'double'),
                                 ('answer2y', '152'), ('answer3.6', 'string'), ('answer3.7', 'array'),
                                 ('useranswer3.3', ''), ('useranswer3.4', ''), ('answer1', '6642-7685-6744'),
                                 ('useranswer3.6', ''), ('useranswer2x', ''), ('useranswer3.5', ''),
                                 ('useranswer3.1', ''), ('answer3.2', 'double'), ('answer3.1', 'string'),
                                 ('useranswer1', ''), ('useranswer2y', ''), ('answer2x', '111'), ('useranswer3.7', ''),
                                 ('answer3.4', 'int')])

      self.failIf(form.get('answer1') is None)
      self.failIf(form.get('answer2x') is None)
      self.failIf(form.get('answer2y') is None)
      self.failIf(form.get('answer3.1') is None)
      self.failIf(form.get('answer3.2') is None)
      self.failIf(form.get('answer3.3') is None)
      self.failIf(form.get('answer3.4') is None)
      self.failUnlessEqual(type(form.get('answer1')), type(form.get('useranswer1')))
      self.failUnlessEqual(type(form.get('answer2x')), type(form.get('useranswer2x')))
      self.failUnlessEqual(type(form.get('answer2y')), type(form.get('useranswer2y')))
      self.failUnlessEqual(type(form.get('answer3.1')), type(form.get('useranswer3.1')))
      self.failUnlessEqual(type(form.get('answer3.2')), type(form.get('useranswer3.2')))
      self.failUnlessEqual(type(form.get('answer3.3')), type(form.get('useranswer3.3')))
      self.failUnlessEqual(type(form.get('answer3.4')), type(form.get('useranswer3.4')))
      self.failUnlessEqual(type(form.get('answer3.5')), type(form.get('useranswer3.5')))
      self.failUnlessEqual(type(form.get('answer3.6')), type(form.get('useranswer3.6')))
      self.failUnlessEqual(type(form.get('answer3.7')), type(form.get('useranswer3.7')))

  def test_checkCorrect(self):
      dev = Development()
      self.failUnlessEqual(type(dev), type(Development()))
      correct = [1]
      self.failUnlessEqual(len(correct), 1)
      correct = [1,2]
      self.failUnlessEqual(len(correct), 2)
      correct = [1,2,3]
      self.failUnlessEqual(len(correct), 3)
