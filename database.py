import pymysql

class database:

    global connection, cursor, username, port, ip, user, password, db
    connection = None
    cursor = None
    username = None
    port = 3306
    ip = '127.0.0.1'
    user = 'root'
    password = '2cKF97'
    db = 'CollegeCraft'

    def __init__(self, pusername, pip, pport):
        global username, ip, port, cursor, connection
        if pusername is not None:
            username = pusername
        ip = pip
        port = pport
        connection = pymysql.connect(host=ip, port=port, user=user, passwd=password, db=db, autocommit=True)
        cursor = connection.cursor()

    def prepare(self, query):
        if username is not None:
            query = query + " WHERE username='" + username + "';"
        else:
            query = query + " WHERE username IS NOT NULL;"
        return query


    #   Setters

    def setScore(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE user SET score = '" + value + "'"))

    def setDev(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE user SET development=" + value))

    def setEng(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE user SET english = '" + value + "'"))

    def setSpar(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE user SET spar = '" + value + "'"))

    def setAnalyse(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE user SET analyse = '" + value + "'"))

    def setProject(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE user SET project = '" + value + "'"))

    def setPeercoaching(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE user SET peercoaching = '" + value + "'"))

    def setEx1(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE english_ex SET ex1 = '" + value + "'"))

    def setEx2(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE english_ex SET ex2 = '" + value + "'"))

    def setEx3(self, value):
        value = str(value)
        if value is not None:
            cursor.execute(self.prepare("UPDATE english_ex SET ex3 = '" + value + "'"))

    #   Getters

    def getScore(self):
        cursor.execute(self.prepare("SELECT score FROM user"))
        return cursor.fetchone()[0]

    def getDev(self):
        cursor.execute(self.prepare("SELECT development FROM user"))
        return cursor.fetchone()[0]

    def getEng(self):
        cursor.execute(self.prepare("SELECT english FROM user"))
        return cursor.fetchone()[0]

    def getSpar(self):
        cursor.execute(self.prepare("SELECT spar FROM user"))
        return cursor.fetchone()[0]

    def getAnalyse(self):
        cursor.execute(self.prepare("SELECT analyse FROM user"))
        return cursor.fetchone()[0]

    def getProject(self):
        cursor.execute(self.prepare("SELECT project FROM user"))
        return cursor.fetchone()[0]

    def getPeercoaching(self):
        cursor.execute(self.prepare("SELECT peercoaching FROM user"))
        return cursor.fetchone()[0]

    def getEx1(self):
        cursor.execute(self.prepare("SELECT ex1 FROM english_ex"))
        return cursor.fetchone()[0]

    def getEx2(self):
        cursor.execute(self.prepare("SELECT ex2 FROM english_ex"))
        return cursor.fetchone()[0]

    def getEx3(self):
        cursor.execute(self.prepare("SELECT ex3 FROM english_ex"))
        return cursor.fetchone()[0]