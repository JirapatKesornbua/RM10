
from telnetlib import STATUS
import mysql.connector


def conDB():
    mydb = mysql.connector.connect(
            host="localhost",
            user="longtest",
            password="12345",
            database="longtest",
        )
    return  mydb

class Con:
    def getNamehard_ware():
        
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def gethard_ware_ID(ID):
        
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE id = {} ".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def inserthard_ware(name,hard_ware):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hard_ware (name, hw_name, status, value) VALUES ('{}','{}','OFF',0.0)".format(name,hard_ware)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def updatahard_ware(id,status):
         mydb = conDB()
         mycursor = mydb.cursor(dictionary=True)
         sql = "UPDATE hard_ware SET status='{}' WHERE id={}".format(status,id)
         mycursor.execute(sql)
         mydb.commit()
         mycursor.close()
         mydb.close()
         return True

    def deletehard_ware():
         mydb = conDB()
         mycursor = mydb.cursor(dictionary=True)
         sql = "DELETE FROM hard_ware WHERE id = '20'"
         mycursor.execute(sql)
         mydb.commit()
         mycursor.close()
         mydb.close()
         return True



data = Con.deletehard_ware()

print(data)

