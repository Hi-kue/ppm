import mysql.connector

class CONNECTIONDB():
    
    def CDBET(): 
        database = mysql.connector.connect(
            host="",
            user="",
            passwd=""
        )
        
        cursor = database.cursor()
        cursor.execute