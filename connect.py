import mysql.connector


# Connecting to MYSQL Database Using Python Connector
database = mysql.connector.connect(
    host="localhost",
    user="Hikue",
    passwd="T2DEo2ZHEoyFwtpK15qJ@"
)

# Cursor
cur = database.cursor()

class DATABASE():
    def __init__(self) -> None:
        pass

    def make_database():
        cur.execute()

    def add_to_database(num, email, password, type, name):
        cur.execute('')
        database.commit()
        
    def ret_database_values():
        pass
