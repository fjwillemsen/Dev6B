from flask import Flask, render_template
from Person import Person


class Peercoaching:
    def _init__ (self):
        self.Exp = Person.pWerkExp
        self.Energy = Person.pEnergy
        self.mentalState = Person.pMentalState

    def get(self):
        return render_template('peercoaching.html')