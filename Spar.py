from flask import Flask, render_template

class Spar:

    def get(self):
        return render_template("spar.html")


