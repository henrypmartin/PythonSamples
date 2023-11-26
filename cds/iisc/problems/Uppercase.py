'''
Created on 25-Nov-2023

@author: Nomura
'''
from _io import StringIO

def uppercase(value:str) -> str:
    opstr = StringIO()
    
    for c in value:
        asciinum = ord(c)
        uc = chr(asciinum - 32) if 97<= asciinum <=122 else c
        opstr.write(uc)
        
    retustr = opstr.getvalue()
    opstr.close()
    
    return retustr

st='Henry-123'
print(f'Uppercase of {st} is {uppercase(st)}')