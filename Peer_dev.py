import random
import string
from flask import Flask, render_template, request
from string import Template

class Peer_dev:
    def generateCode(self, max):
        code = ""
        for i in range(0,max):
            code += random.choice(string.ascii_letters).lower()

        return Peer_dev.encodeString(self, code)

    def encodeString(self, string):
        result = ""
        count = 0
        for i in string:
            if count !=0 and count %2 == 0:
                result += '-'
            result += i
            count += 1
        return result

    def getDecryptedCode(self, code):
        result = ""
        for i in code:
            if i != '-':
                if ord(i) < 108:
                    result += chr(ord(i) - 3)
                else:
                    result += chr(ord(i) + 5)
        return Peer_dev.encodeString(self, result)

    def get(self):
        temp = Template(render_template("peer_dev.html"))
        code = self.generateCode(6)
        print('Code: ' + code)
        answer = self.getDecryptedCode(code)
        print('Answer: ' + answer)
        return temp.substitute(numbercode=code, answercode=answer)
