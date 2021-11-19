import pymysql
import time

class Database:
    def __init__(self):
        self.db=pymysql.connect(host='localhost', user='mrchoidb', passwd='password1234', db='OS')
        self.cur = self.db.cursor()
        print('good')
        
    def selectAllJson(self):
        sql = "select * from login;"
        self.cur.execute(sql)
        result= self.cur.fetchall()
        return result
    
    
    def insertLogin(self,userID,userPW):
        sql ="insert into login(userID,userPW) values(%s,%s);"
        self.cur.execute(sql,(userID,userPW))
        self.db.commit();
        return "good"

