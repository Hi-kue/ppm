import mysql.connector
from colors import colors


# Connecting to MYSQL Database Using Python Connector
database = mysql.connector.connect(
    host="localhost",
    user="Hikue",
    password="T2DEo2ZHEoyFwtpK15qJ@",
    database="Information"
)
# Cursor
cur = database.cursor()


class DATABASE():
    def __init__(self) -> None:
        pass

    def DBOV(num, email, password, type, name):
        try:
            data_information = {
                'num': int(num),
                'email': str(email),
                'password': str(password),
                'type': str(type),
                'name': str(name)
            }
        except Exception as e:
            return f'Error Occured: {e}'

        return data_information

    def DBIV(*args):
        try:
            add_information = (
                "INSERT INTO Information "
                "(num, email, password, type, name) "
                "VALUES (%(num)s, %(email)s, %(password)s, %(type)s, %(name)s)"
            )

            cur.execute(add_information, args)
        except Exception as e:
            return f'{colors.CBOLD}{colors.CREDBG2}{colors.CBLACK}Error Occured: {e}{colors.ENDC}'

        return f'{colors.CBOLD}{colors.CGREENBG2}{colors.CBLACK}DATABASE INSERTION SUCCESSFUL.{colors.ENDC}'
