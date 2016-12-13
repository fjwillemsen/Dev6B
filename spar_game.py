from flask import Flask, render_template
from string import Template
import random

class spar_game:
    count=0
    def __init__(self, duration):
        self.sDuration = duration

    def generate_question(self):
        #get question from database
        question = "test"
        return question

    def generate_answers(self):
        #get answers from database
        if(self.count<2):
            self.count+=1
            answer = "test1"
        else:
            answer = "test2"
        return answer

    def get(self,sitem,quest,ans1,ans2,ans3):
        template = Template(render_template("spar_game.html"))
        return template.substitute(item=sitem,question=quest,answer1=ans1,answer2=ans2,answer3=ans3,discount=25)

    def check(self, user_answer, answer):
        if user_answer == answer:
            return "correct"
        elif user_answer != answer:
            return "incorrect"
