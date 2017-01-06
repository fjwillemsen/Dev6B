import random
import string
from flask import Flask, render_template, request
from string import Template

class Peer_anl:

    def answerIs(self, q):
        if q == "[!] UML diagrams are used to show the flow of a program. (true/false)":
            return "false"
        elif q == "[!] Software analysis is useless when building software in C. (true/false)":
            return "false"
        elif q == "[?] Are there any jobs for creating UML diagrams? (Yes/No)":
            return "yes"
        elif q == "[?] When creating a flowdiagram, the life of a process doesn/'t matter. (Yes/No)":
            return "no"
        elif q == "[?] Are Analysis teachers cool? (Yes/No)":
            return "no"

    def generateQuestion(self):
        questions = "[!] UML diagrams are used to show the flow of a program. (true/false)", "[!] Software analysis is useless when building software in C. (true/false)", "[?] Are there any jobs for creating UML diagrams? (Yes/No)", "[?] When creating a flowdiagram, the life of a process doesn/'t matter. (Yes/No)", "[?] Are Analysis teachers cool? (Yes/No)"
        r_quest = questions[random.randint(0, 4)]
        return r_quest

    def get(self):
        temp = Template(render_template("peer_anl.html"))

        rand_quest = self.generateQuestion()
        answer_to_quest = self.answerIs(rand_quest)

        print('Question: ' + rand_quest)
        print('Answer: ' + answer_to_quest)

        return temp.substitute(quest=rand_quest, answerquest=answer_to_quest)


