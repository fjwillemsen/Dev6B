from unittest import TestCase
from Peer_anl import Peer_anl

class TestPeerANL(TestCase):

    def test_generateQuest(self):
        self.failUnlessEqual(("[!] UML diagrams are used to show the flow of a program. (true/false)" or "[!] Software analysis is useless when building software in C. (true/false)" or "[?] Are there any jobs for creating UML diagrams? (Yes/No)" or "[?] When creating a flowdiagram, the life of a process doesn/'t matter. (Yes/No)" or "[?] Are Analysis teachers cool? (Yes/No)"), Peer_anl.generateQuestion())

    def test_ifAnswer0(self):
        self.failUnlessEqual(Peer_anl.answerIs(Peer_anl, "[!] UML diagrams are used to show the flow of a program. (true/false)"), "false")

    def test_ifAnswer1(self):
        self.failUnlessEqual(Peer_anl.answerIs(Peer_anl, "[!] Software analysis is useless when building software in C. (true/false)"), "false")

    def test_ifAnswer2(self):
        self.failUnlessEqual(Peer_anl.answerIs(Peer_anl, "[?] Are there any jobs for creating UML diagrams? (Yes/No)"), "yes")

    def test_ifAnswer3(self):
        self.failUnlessEqual(Peer_anl.answerIs(Peer_anl, "[?] When creating a flowdiagram, the life of a process doesn/'t matter. (Yes/No)"), "no")

    def test_ifAnswer4(self):
        self.failUnlessEqual(Peer_anl.answerIs(Peer_anl, "[?] Are Analysis teachers cool? (Yes/No)"), "no")