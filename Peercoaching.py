from flask import render_template
import database
from Person import Person

class Peercoaching:
    global db
    #db = database.database(None, 'localhost', 3306)

    def _init__ (self):
        self.Exp = Person.pWerkExp
        self.Energy = Person.pEnergy
        self.mentalState = Person.pMentalState

    def get(self):
        return render_template('peercoaching.html')