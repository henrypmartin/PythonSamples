'''
Created on 25-Nov-2023

@author: Nomura
'''

def getSumOfDigits(num:int) -> int:
    digitsum=0
    
    while(num>0):
        digitsum += (num % 10)
        num = num // 10
    
    return digitsum

num=50454
print(f'Sum of all the digits of {num} is {getSumOfDigits(num)}')