import unittest, Development

class Test_testDevelopment(unittest.TestCase):

    def test1(self):
        self.failUnless(Development.generateCode(self, 12))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
