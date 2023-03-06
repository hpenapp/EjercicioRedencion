#"""
#CONEXIÓN A LA BASE DE DATOS POR SQLALCHEMY
import sqlalchemy as db

def dbconn():
    try:
        conn = db.create_engine("mysql+pymysql://root:DataLake.2023@192.168.100.140:3306/DcDataLakeDB")
        print("db connected")
        return conn
    except Exception as e:
        print('Hay un error: ', e)
#"""


"""
#CONEXIÓN A LA BASE DE DATOS POR PYMYSQL
import pymysql.cursors
def dbconn(): 
    try:
        conn = pymysql.connect(host= "192.168.100.140",
                               port=3306,
                               user= "root",
                               passwd= "DataLake.2023",
                               database="DcDataLakeDB")
        print(conn)
        return conn
    except Exception as e:
        print('Hay un error: ', e)
"""