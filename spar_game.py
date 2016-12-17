from flask import Flask, render_template
from string import Template
import random

class spar_game:
    count = 0
    score = 0

    time = 0

    item = ''

    info="Enter information that helps with answering the questions"
    correctA=['','','','','']
    q=['','','','','']
    q1a=['','','']
    q2a=['']
    q3a=['','','']
    q4a=['','','']
    q5a=['','','']

    def __init__(self, duration):
        self.sDuration = duration

    def gen_question(self):
        #get question from database
        for index in range(len(self.q)):
            self.q[index] = "test"+str(index)
            print(self.q[index])

    def get_quest(self,i):
        return self.q[i]

    def gen_answers(self):
        # get answers from database
        for index in range(len(self.q1a)):
            self.correctA[0] = "test"+str(index+1)
            self.q1a[index] = "test"+str(index+1)
            print(self.q1a[index])
        for index in range(len(self.q2a)):
            self.correctA[1] = "test" + str(index + 1)
            self.q2a[index] = "test"+str(index+1)
            print(self.q2a[index])
        for index in range(len(self.q3a)):
            self.correctA[2] = "test" + str(index + 1)
            self.q3a[index] = "test"+str(index+1)
            print(self.q3a[index])
        for index in range(len(self.q4a)):
            self.correctA[3] = "test" + str(index + 1)
            self.q4a[index] = "test"+str(index+1)
            print(self.q4a[index])
        for index in range(len(self.q5a)):
            self.correctA[4] = "test" + str(index + 1)
            self.q5a[index] = "test"+str(index+1)
            print(self.q5a[index])

    def get_correctA(self,u):
        if (u == 0):
            return self.correctA[u]
        elif (u == 1):
            return self.correctA[u]
        elif (u == 2):
            return self.correctA[u]
        elif (u == 3):
            return self.correctA[u]
        elif (u == 4):
            return self.correctA[u]


    def get_answer(self,i,u):
        if(i==0):
            return self.q1a[u]
        elif (i == 1):
            return self.q2a[u]
        elif (i == 2):
            return self.q3a[u]
        elif (i == 3):
            return self.q4a[u]
        elif (i == 4):
            return self.q5a[u]

    def difficulty(self,item):
        if item == 'energy':
            self.time = 3
        elif item == 'bread':
            self.time = 2
        elif item == 'pizza':
            self.time = 1

    def incscore(self,i):
        self.score += i

    def getscore(self):
        return self.score

    def get(self,it,q1,q2,q3,q4,q5,q1a1,q1a2,q1a3,q2a1,q3a1,q3a2,q3a3,q4a1,q4a2,q4a3,q5a1,q5a2,q5a3,s):
        template = Template(render_template("spar_game.html",radio=True,open=False,info=False))
        return template.substitute(item=it,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q1a1=q1a1,q1a2=q1a2,q1a3=q1a3,q2a1=q2a1,q3a1=q3a1,
                                   q3a2=q3a2,q3a3=q3a3,q4a1=q4a1,q4a2=q4a2,q4a3=q4a3,q5a1=q5a1,q5a2=q5a2,q5a3=q5a3,score=s,t=self.time)

    def check(self, s):
        template = Template(render_template("spar_res.html"))
        self.score = 0
        return template.substitute(score=s)
