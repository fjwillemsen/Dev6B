from unittest import TestCase

from spar_game import spar_game

from Main import *

class TestSpar_game(TestCase):
    q = [0,1,2,3]

    def test_get_correctA(self):
        a = ['1932', 'Megaspar', 'Netherlands', '2004', '244', '404']
        oq1a = ['south africa']
        sg = spar_game(self.q)
        self.assertEqual(sg.get_correctA(0), a[0], 'correct')
        self.assertEqual(sg.get_correctA(1), a[1], 'correct')
        self.assertEqual(sg.get_correctA(2), a[2], 'correct')
        self.assertEqual(sg.get_correctA(3), a[3], 'correct')
        self.assertEqual(sg.get_correctA(4), oq1a[0], 'correct')


    def test_get_answer(self):
        q1a = ['1946', '1932', '1968']
        q2a = ['Spar Drive-Thru', 'Megaspar', 'Hotspar']
        q3a = ['Germany', 'Netherlands', 'France']
        q4a = ['1987', '2004', '2015']
        q5a = ['244', '251', '249']
        q6a = ['404', '505', '606']
        sg = spar_game(self.q)
        self.assertEqual(sg.get_answer(0, 0), q1a[0], 'correct')
        self.assertEqual(sg.get_answer(0, 1), q1a[1], 'correct')
        self.assertEqual(sg.get_answer(0, 2), q1a[2], 'correct')
        self.assertEqual(sg.get_answer(1, 0), q2a[0], 'correct')
        self.assertEqual(sg.get_answer(1, 1), q2a[1], 'correct')
        self.assertEqual(sg.get_answer(1, 2), q2a[2], 'correct')
        self.assertEqual(sg.get_answer(2, 0), q3a[0], 'correct')
        self.assertEqual(sg.get_answer(2, 1), q3a[1], 'correct')
        self.assertEqual(sg.get_answer(2, 2), q3a[2], 'correct')
        self.assertEqual(sg.get_answer(3, 0), q4a[0], 'correct')
        self.assertEqual(sg.get_answer(3, 1), q4a[1], 'correct')
        self.assertEqual(sg.get_answer(3, 2), q4a[2], 'correct')
        self.assertEqual(sg.get_answer(4, 0), q5a[0], 'correct')
        self.assertEqual(sg.get_answer(4, 1), q5a[1], 'correct')
        self.assertEqual(sg.get_answer(4, 2), q5a[2], 'correct')
        self.assertEqual(sg.get_answer(5, 0), q6a[0], 'correct')
        self.assertEqual(sg.get_answer(5, 1), q6a[1], 'correct')
        self.assertEqual(sg.get_answer(5, 2), q6a[2], 'correct')

    def test_difficulty(self):
        sg = spar_game(self.q)
        self.assertEqual(sg.difficulty('energy'), 0.5, 'correct')
        self.assertEqual(sg.difficulty('bread'), 1, 'correct')
        self.assertEqual(sg.difficulty('pizza'), 2, 'correct')

    def test_score(self):
        sg = spar_game(self.q)
        sg.incscore(50)         #score = 50
        self.assertEqual(sg.getscore(), 50, 'correct')
        self.assertNotEqual(sg.getscore(), 49, 'correct')
        self.assertNotEqual(sg.getscore(), 51, 'correct')

    def test_flow(self):
        sg1 = spar_game(self.q)
        sg2 = spar_game(self.q)
        sg3 = spar_game(self.q)
        i = 0
        j = 0
        while j < 3:
            j = j + 1
            if j == 1:
                item = 'pizza'
                sg1.beforeGet(item)  # score = 0
                self.assertEqual(sg1.get_item(), item, 'correct')  # score = 0
                self.assertEqual(sg1.difficulty(item), 2, 'correct')  # score = 0
                self.assertEqual(sg1.getscore(), 0, 'correct')  # score = 0
                bA = ['mindig spar!', 'mindig spar']
                while i < 7:
                    i = i + 1
                    if i == 1:
                        time = 20
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', 'South Africa']
                        self.assertEqual(sg1.afterQ(ua,time,False), time, 'correct')  #score = 400
                        sg1.calcScoreQ2(bA[0])                                          #score = 800
                        self.assertEqual(sg1.getscore(),800, 'correct')
                        sg1.calcScoreQ2(bA[1])                                          #score = 400
                        self.assertEqual(sg1.getscore(), 400, 'correct')
                    elif i == 2:
                        time = 20
                        ua = ['1932', 'Megaspar', 'a', 'a', 'a']
                        self.assertEqual(sg1.afterQ(ua, time, False), 200, 'correct')  # score = 200
                    elif i == 3:
                        time = 20
                        ua = ['1932', 'Megaspar', 'Netherlands', 'a', 'a']
                        self.assertEqual(sg1.afterQ(ua, time, False), time, 'correct')  # score = 300
                    elif i == 4:
                        time = 16
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', '']
                        self.assertEqual(sg1.afterQ(ua, time, False), time, 'correct')  # score = 400
                        sg1.calcScoreQ2(bA[0])  # score = 800
                        self.assertEqual(sg1.getscore(), 800, 'correct')
                        sg1.calcScoreQ2(bA[1])  # score = 400
                        self.assertEqual(sg1.getscore(), 400, 'correct')
                    elif i == 5:
                        time = 15
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', '']
                        self.assertEqual(sg1.afterQ(ua, time, False), time, 'correct')  # score = 400
                        sg1.calcScoreQ2(bA[0])  # score = 800
                        self.assertEqual(sg1.getscore(), 800, 'correct')
                        sg1.calcScoreQ2(bA[1])  # score = 400
                        self.assertEqual(sg1.getscore(), 400, 'correct')
                    elif i == 6:
                        time = 14
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', '']
                        self.assertEqual(sg1.afterQ(ua, time, False), 400, 'correct')  # score = 400
            elif j == 2:
                item = 'bread'
                sg2.beforeGet(item)  # score = 0
                self.assertEqual(sg2.get_item(), item, 'correct')  # score = 0
                self.assertEqual(sg2.difficulty(item), 1, 'correct')  # score = 0
                self.assertEqual(sg2.getscore(), 0, 'correct')  # score = 0
                while i < 7:
                    i = i + 1
                    if i == 1:
                        time = 20
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', '']
                        self.assertEqual(sg2.afterQ(ua,time, False), time, 'correct')  #score = 250
                        sg2.calcScoreQ2(bA[0])  # score = 800
                        self.assertEqual(sg2.getscore(), 800, 'correct')
                        sg2.calcScoreQ2(bA[1])  # score = 400
                        self.assertEqual(sg2.getscore(), 400, 'correct')
                    elif i == 2:
                        time = 20
                        ua = ['1932', 'Megaspar', '', '', '']
                        self.assertEqual(sg2.afterQ(ua, time, False), 200, 'correct')  # score = 100
                    elif i == 3:
                        time = 20
                        ua = ['1932', 'Megaspar', 'Netherlands', '', '']
                        self.assertEqual(sg2.afterQ(ua, time, False), 300, 'correct')  # score = 150
                    elif i == 4:
                        time = 16
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', '']
                        self.assertEqual(sg2.afterQ(ua,time, False), time, 'correct')  #score = 250
                        sg2.calcScoreQ2(bA[0])  # score = 800
                        self.assertEqual(sg2.getscore(), 800, 'correct')
                        sg2.calcScoreQ2(bA[1])  # score = 400
                        self.assertEqual(sg2.getscore(), 400, 'correct')
                    elif i == 5:
                        time = 15
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', '']
                        self.assertEqual(sg2.afterQ(ua, time, False), time, 'correct')  # score = 250
                    elif i == 6:
                        time = 14
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', '']
                        self.assertEqual(sg2.afterQ(ua, time, False), 500, 'correct')  # score = 250
            elif j == 2:
                item = 'energy'
                sg3.beforeGet(item)  # score = 0
                self.assertEqual(sg3.get_item(), item, 'correct')  # score = 0
                self.assertEqual(sg3.difficulty(item), 0.5, 'correct')  # score = 0
                self.assertEqual(sg3.getscore(), 0, 'correct')  # score = 0
                while i < 7:
                    i = i + 1
                    if i == 1:
                        time = 20
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', 'South Africa']
                        self.assertEqual(sg3.afterQ(ua,time, False), 125, 'correct')  #score = 125
                    elif i == 2:
                        time = 20
                        ua = ['1932', 'Megaspar', '', '', '']
                        self.assertEqual(sg3.afterQ(ua, time, False), 50, 'correct')  # score = 50
                    elif i == 3:
                        time = 20
                        ua = ['1932', 'Megaspar', 'Netherlands', '', '']
                        self.assertEqual(sg3.afterQ(ua, time, False), 75, 'correct')  # score = 75
                    elif i == 4:
                        time = 16
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', 'South Africa']
                        self.assertEqual(sg3.afterQ(ua,time, False), 125, 'correct')  #score = 125
                    elif i == 5:
                        time = 15
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', 'South Africa']
                        self.assertEqual(sg3.afterQ(ua, time, False), 125, 'correct')  # score = 125
                    elif i == 6:
                        time = 14
                        ua = ['1932', 'Megaspar', 'Netherlands', '2004', 'South Africa']
                        self.assertEqual(sg3.afterQ(ua, time, False), 125, 'correct')  # score = 125


