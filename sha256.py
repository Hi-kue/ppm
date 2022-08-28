from turtle import color
import hashlib
import os
from colors import colors


folder_path = os.makedir('PASSWORDS')
file_path = open('PASSWORDS/PASSWORDS[SHA256].txt', 'a+')

# NOTE: sha256.py used to convert normal passwords into hashes.


class SHA256():
    def __init__(self, type):
        self.type = type

    def CPSHA256(password=[], type=1) -> None:
        empty = []
        hashed_passwords = []

        if len(password) != empty & type == 1:
            # Return an array of hashed values with their counterparts in a file.
            for i in enumerate(password):
                hashed_passwords = hashlib.sha256(
                    i.encode('utf-8')
                ).hexdigest()

                if file_path.mode == 'a+':
                    # File format ->  password : hashed password
                    file_path.write(f'{password[i]} : {hashed_passwords}')

                    # return hashed passwords for data manipulation
                    return hashed_passwords

            return print(f'{colors.CBOLD}{colors.CGREENBG2}{colors.CBLACK}Hashing successful.{colors.ENDC}')

        else:
            return print(f'{colors.CBOLD}{colors.CREDBG2}{colors.CBLACK}Password has no content.{colors.ENDC}')
