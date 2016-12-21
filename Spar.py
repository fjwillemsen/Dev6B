from flask import Flask, render_template

class Spar:
    def __init__(self, duration):
        self.sDuration = duration

    def get(self):
        return render_template("spar.html")


