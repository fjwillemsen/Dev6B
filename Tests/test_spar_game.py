from unittest import TestCase

from spar_game import spar_game


class TestSpar_game(TestCase):
    def test_get_correctA(self):
        a = ['1932', 'Megaspar', 'Netherlands', '2004', '244', '404']
        oq1a = ['south africa']
        sg = spar_game()
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
        sg = spar_game()
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
        sg = spar_game()
        self.assertEqual(sg.difficulty('energy'), 0.5, 'correct')
        self.assertEqual(sg.difficulty('bread'), 1, 'correct')
        self.assertEqual(sg.difficulty('pizza'), 2, 'correct')

    def test_set_item(self):
        sg = spar_game()
        self.assertEqual(sg.set_item('test'), 'test', 'correct')


    def test_getscore(self):
        sg = spar_game()
        sg.incscore(50)
        self.assertEqual(sg.getscore(), 50, 'correct')


    # def test_get(self):
    #     self.fail()
    #
    # def test_check(self):
    #     self.fail()

