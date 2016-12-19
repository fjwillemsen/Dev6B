from flask import Flask, render_template,g
from string import Template
import sqlite3
import os
import sys
import random
from flask_sqlalchemy import SQLAlchemy


class spar_game:
    count = 0
    score = 0

    time = 0

    item = ''

    info="Enter information that helps with answering the questions"
    correctA=['1932','Megaspar','Netherlands','2004','244','404']
    q=['In what year was Spar founded','Which of the following is not part of Spar',
       'In which of the following countries was Spar founded','When where the first Spar stores opened in Indonesia',
       'How many Spar stores are located in The Netherlands','What is the average store size(m2) in The Netherlands']
    q1a=['1946','1932','1968']
    q2a=['Spar Drive-Thru','Megaspar','Hotspar']
    q3a=['Germany','Netherlands','France']
    q4a=['1987','2004','2015']
    q5a=['244','251','249']
    q6a=['404','505','606']

    correctOA=['South Africa']
    oq = ['In which of the following countries does the Spar have the highest sales(in millions) -'
          ' France, Italy or South Africa']
    oq1a=['South Africa']

    quests = []

    # ids = random.sample(range(0,4),4)
    # qID = []
    #     q1 = question(1, 'In what year was Spar founded', '1946', '1932', '1968', '1932')
    #     q2 = question(2, 'Which of the following is not part of Spar', 'Spar Drive-Thru', 'Megaspar', 'Hotspar',
    #                   'Megaspar')
    #     q3 = question(3, 'In which of the following countries was Spar founded', 'Germany', 'Netherlands', 'France',
    #                   'Netherlands')
    #     q4 = question(4, 'When where the first Spar stores opened in Indonesia', '1987', '2004', '2015', '2004')
    #     q5 = question(5, 'What is the average store size(m2) in The Netherlands', '404', '505', '606', '404')
    #     q6 = question(6, 'How many Spar stores are located in The Netherlands', '244', '251', '249', '244')
    #     q7 = question(7, 'In which of the following countries does the Spar have the highest sales(in millions)',
    #                   'France', 'Italy', 'South Africa', 'South Africa')

    def __init__(self, duration):
        self.sDuration = duration

    def gen_question(self):
        self.qID = random.sample(range(0,6),4)
        # self.qID = random.sample(range(0,4), 4)
        # ID = random.randint(0,4)
        # self.qID.append(ID)
        # while len(self.qID) <= 4:
        #     ID = random.randint(0,4)
        #     for i in range(len(self.qID)):
        #         if ID != self.qID[i]:
        #             q = True
        #         else:
        #             q = False
        #     if q:
        #         self.qID.append(ID)
        # print(str(self.qID))
        # for i in range(len(self.qID)):
        #     self.quests.append(self.q[i])
        # self.quests.append(self.oq)
        # print(str(self.quests))

    def get_quest(self,i):
        return self.quests[i]



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
            return self.correctOA[0]


    def get_answer(self,i,u):
        if(i == 0):
            return self.q1a[u]
        elif (i == 1):
            return self.q2a[u]
        elif (i == 2):
            return self.q3a[u]
        elif (i == 3):
            return self.q4a[u]
        elif (i == 4):
            return self.q5a[u]
        elif (i == 5):
            return self.q6a[u]

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

    def get(self,it,s):
        # self.gen_question(self)
        template = Template(render_template("spar_game.html"))
        return template.substitute(item=it,q1=self.q[self.qID[0]],q2=self.q[self.qID[1]],q3=self.q[self.qID[2]],q4=self.q[self.qID[3]],
                                   q5=self.oq[0],
                                   q1a1=self.get_answer(self,self.qID[0],0),q1a2=self.get_answer(self,self.qID[0],1),q1a3=self.get_answer(self,self.qID[0],2),
                                   q2a1=self.get_answer(self,self.qID[1],0),q2a2=self.get_answer(self,self.qID[1],1),q2a3=self.get_answer(self,self.qID[1],2),
                                   q3a1=self.get_answer(self,self.qID[2],0),q3a2=self.get_answer(self,self.qID[2],1),q3a3=self.get_answer(self,self.qID[2],2),
                                   q4a1=self.get_answer(self,self.qID[3],0),q4a2=self.get_answer(self,self.qID[3],1),q4a3=self.get_answer(self,self.qID[3],2),
                                   score=s,t=self.time)

    def check(self,s,ua):
        template = Template(render_template("spar_res.html"))
        for index in range(len(ua)):
            print("Correct answer:" + str(self.get_correctA(index) + ". Input: " + ua[index]))
            if self.get_correctA(index) == ua[index]:
                self.incscore(50)
        self.score = 0
        return template.substitute(score=s)
