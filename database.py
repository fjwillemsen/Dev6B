import pymysql

class database:
    def __init__(self,host,port, user,passwd):
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db='collegecraft')
    def runnquery(self,query):
        cur = self.conn.cursor()
        cur.execute(query)
        cur.close()
        return cur
    def close(self):
        self.conn.close()

databaser = database('localhost',3306,'root','d8dfc737')


for row in databaser.runnquery("SELECT xp FROM user WHERE iduser = 1").fetchall() :
    print(row[0], row[0])
