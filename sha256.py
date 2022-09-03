import dataclasses
from email import header
from genericpath import isfile
import hashlib
from typing import Tuple
import os
from tabulate import tabulate
from dataclasses import dataclass, astuple, asdict

file_path = "./..."


@dataclass(frozen=True, order=True)
class SHA256():
    password: str
    hashed_password: str

    def sha256_hash(**kwargs) -> str or Tuple[str, str] or tabulate:
        if os.path.isdir('SAFE'):
            if os.path.isfile('Encrypt-List'):
                return
        else:
            os.makedirs('SAFE')

        hashed_pass = [hashlib.sha256(value.encode()).hexdigest()
                       for value in kwargs.values()]

        password = [value for value in kwargs.values()]
        
        content = dict(zip(password, hashed_pass))
        
        table = tabulate(
            content.items(),
            headers= ['Password', 'Hashed'],
            tablefmt='fancy_grid',
            showindex=True
        )
        
        with open(file_path, 'a+', encoding='utf-8') as file:
            file.write(table)
            file.write('\n')
            
        return table