import pymysql
import time

class UserDatabase:
    def __init__(self):
        self.db=pymysql.connect(
            host='localhost',
            user='DH',
            passwd='dpdms1215',
            db='snoring')
        
        self.cur=self.db.cursor()
        print('good')
        
    def selectALLJson(self):
        sql = "select * from User;"
        self.cur.execute(sql)
        result= self.cur.fetchall()
        return result
    
    def insertJson(self,id,passwd,username):
        sql = "insert into User() values(%s);"
        val = ('{{"id":"{}", "passwd":"{}","username":"{}"}}').format(id,passwd,username)
        self.cur.execute(sql,val)
        self.db.commit()

