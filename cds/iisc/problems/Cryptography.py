'''
Created on 26-Nov-2023

@author: Henry Martin
'''

import random, time

def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for i in plaintext:
        ciphertext += i
        for j in range (0,key):
            ciphertext += random.choice(alphabet)
    return ciphertext

def decrypt(ciphertext:str, key:int) -> str:
    return ciphertext[:len(ciphertext):key+1]

plaintext = input("Enter a message to encrypt (plaintext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (key>=1 and key<=10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))

print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)

print(f'Encrypted message is {ciphertext}')

ciphertext = input("Enter a ciphertext to decrypt:")
key = int(input("Input a key as a number between 1 and 10"))

print("Decrypting ciphertext...")

plaintext = decrypt(ciphertext, key)

print(f'Decrypted message is {plaintext}')