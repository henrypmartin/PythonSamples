'''
Created on 23-Nov-2023

@author: Henry Martin
'''

def decToBinaryConverter(num : int) -> str:
    oplist=[128, 64, 32, 16, 8, 4, 2, 1]
    
    for idx, binaryvalue in enumerate(oplist):
        if num < binaryvalue:
            oplist[idx] = 0
        else:
            oplist[idx] = 1
            num -= binaryvalue
    
    return " ".join(map(str, oplist))
    

#print(decToBinaryConverter(1))

toContinue='yes'

while toContinue=='yes':    
    userInp = int(input("Enter number between 0 to 255:"))
    
    if 0 <= userInp <= 255:
        print(f"Decimal to binary for {userInp} is {decToBinaryConverter(userInp)}")
        toContinue = input("Do you wish to continue? (enter yes/no):")
        toContinue = toContinue.lower()
    else:
        print("Enter valid number between 0 and 255")        
    