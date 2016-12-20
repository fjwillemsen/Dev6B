from unittest import TestCase
from english import English

class TestEnglish(TestCase):
    
    def test_simplePresent(self):
        eng = English()
        self.assertEqual(eng.simplePresent('likes'),'Correct')
        self.assertEqual(eng.simplePresent('incorrect'),'Wrong')
        self.assertEqual(eng.simplePresent(''),'Wrong')

    def test_simplePast(self):
        eng = English()
        self.assertEqual(eng.simplePast('ate'),'Correct')
        self.assertEqual(eng.simplePresent('incorrect'),'Wrong')
        self.assertEqual(eng.simplePresent(''),'Wrong')

    def test_goingToFuture(self):
        eng = English()
        self.assertEqual(eng.goingToFuture('is going to phone'),'Correct')
        self.assertEqual(eng.simplePresent('incorrect'),'Wrong')
        self.assertEqual(eng.simplePresent(''),'Wrong')

    def test_presentPerfect(self):
        eng = English()
        self.assertEqual(eng.presentPerfect('have been'),'Correct')
        self.assertEqual(eng.simplePresent('incorrect'),'Wrong')
        self.assertEqual(eng.simplePresent(''),'Wrong')

    def test_pastPerfect(self):
        eng = English()
        self.assertEqual(eng.pastPerfect('had eaten'),'Correct')
        self.assertEqual(eng.simplePresent('incorrect'),'Wrong')
        self.assertEqual(eng.simplePresent(''),'Wrong')

    def test_opt1Check(self):
        eng = English()
        self.assertEqual(eng.opt1Check("aspect"),"Correct")
        self.assertEqual(eng.opt1Check("asspect"),"Wrong")
        self.assertEqual(eng.opt1Check("empty"),"Wrong")

    def test_opt2Check(self,):
        eng = English()
        self.assertEqual(eng.opt2Check("possible"),"Correct")
        self.assertEqual(eng.opt2Check("posible"),"Wrong")
        self.assertEqual(eng.opt2Check("empty"),"Wrong")

    def test_opt3Check(self,):
        eng = English()
        self.assertEqual(eng.opt3Check("population"),"Correct")
        self.assertEqual(eng.opt3Check("poppulation"),"Wrong")
        self.assertEqual(eng.opt3Check("empty"),"Wrong")

    def test_opt4Check(self,):
        eng = English()
        self.assertEqual(eng.opt4Check("suppose"),"Correct")
        self.assertEqual(eng.opt4Check("supose"),"Wrong")
        self.assertEqual(eng.opt4Check("empty"),"Wrong")

    def test_opt5Check(self,):
        eng = English()
        self.assertEqual(eng.opt5Check("tomorrow"),"Correct")
        self.assertEqual(eng.opt5Check("tomorow"),"Wrong")
        self.assertEqual(eng.opt5Check("empty"),"Wrong")

    def test_govCheck(self, ):
        eng = English()
        self.assertEqual(eng.govCheck("government"),"Correct")
        #anything that is not ^ is wrong
        self.assertEqual(eng.govCheck("attended"),"Wrong")
        self.assertEqual(eng.govCheck(""),"Wrong")

    def test_sprCheck(self, ):
        eng = English()
        self.assertEqual(eng.sprCheck("spread"),"Correct")
        #anything that is not ^ is wrong
        self.assertEqual(eng.sprCheck("attended"),"Wrong")
        self.assertEqual(eng.sprCheck(""),"Wrong")

    def test_attCheck(self, ):
        eng = English()
        self.assertEqual(eng.attCheck("attended"),"Correct")
        #anything that is not ^ is wrong
        self.assertEqual(eng.attCheck("spread"),"Wrong")
        self.assertEqual(eng.attCheck(""),"Wrong")

    def test_jobCheck(self, ):
        eng = English()
        self.assertEqual(eng.jobCheck("jobs"),"Correct")
        #anything that is not ^ is wrong
        self.assertEqual(eng.jobCheck("attended"),"Wrong")
        self.assertEqual(eng.jobCheck(""),"Wrong")

    def test_busCheck(self, ):
        eng = English()
        self.assertEqual(eng.busCheck("business"),"Correct")
        #anything that is not ^ is wrong
        self.assertEqual(eng.busCheck("attended"),"Wrong")
        self.assertEqual(eng.busCheck(""),"Wrong")

    def test_checkAmountCorrect(self):
        eng = English()
        #grenswaarde analyse
        correct = ["Correct","Correct","Correct","Correct","Correct","Correct","Correct","Correct",
                   "Wrong","Wrong","Wrong","Wrong""Wrong","Wrong","Wrong"]#net goed/op grens
        alsoCorrect = ["Correct","Correct","Correct","Correct","Correct","Correct","Correct","Correct","Correct",
                    "Correct","Correct","Correct","Wrong","Wrong","Wrong"]#boven grens
        incorrect = ["Correct","Correct","Correct","Correct","Correct","Correct","Correct","Wrong",
                     "Wrong","Wrong","Wrong","Wrong""Wrong","Wrong","Wrong"]#onder de grens
        self.assertEqual(eng.checkAmountCorrect(correct),True)
        self.assertEqual(eng.checkAmountCorrect(alsoCorrect),True)
        self.assertEqual(eng.checkAmountCorrect(incorrect),False)