from unittest import TestCase
from Peer_dev import Peer_dev

class TestPeerDEV(TestCase):

  def test_generateCode(self):
    self.failUnlessEqual(len(Peer_dev.generateCode(Peer_dev, 6)), 6+2)

  def test_encodeString(self):
    self.failUnlessEqual(len(Peer_dev().generateCode(6)), len(Peer_dev().generateCode(6)))
    self.failUnless(Peer_dev().generateCode(6).find('-') == 2)

  def test_getDecryptedCode(self):
    code = Peer_dev().generateCode(6)
    result = ""
    for i in code:
        if i != '-':
            if ord(i) < 108:
                result += chr(ord(i) - 3)
            else:
                result += chr(ord(i) + 5)
    result = Peer_dev().encodeString(result)
    self.failUnlessEqual(Peer_dev().getDecryptedCode(code), result)
