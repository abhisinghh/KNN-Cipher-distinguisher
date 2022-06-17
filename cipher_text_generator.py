
import os
from os import urandom
import encryption_algos
from binascii import hexlify as hexa, unhexlify as unhexa
import pandas as pd


input_file = open('key.txt','r')
key_1 = 0
with input_file as f:
    key_1 = next(f)
    key_1 = key_1.strip()
print(key_1)
key_1 = unhexa(key_1)
print(key_1)



counter = 0

def encrypt_plain_text(input, counter) :
    key = key_1
    if counter <= 33 :
        aes = encryption_algos.aes_encryption_cbc()
        ct = aes.encryptor(input, key)
        counter += 1

    elif counter > 33 and counter <= 66 :
        des3_ecb = encryption_algos.des3_encryption_ecb()
        ct = des3_ecb.encryptor(input, key)
        counter += 1

    else :
        blowfish = encryption_algos.blowfish_encryption_cbc()
        ct = blowfish.encryptor(input, key)
        counter += 1
    return ct, counter


input_file = open('plain_texts.txt','r')
input_plain_texts = []
cipher_texts = []

for readline in input_file :
    pt = readline.strip()
    input_plain_texts.append(pt)

input_file.close()


for input in input_plain_texts :
    ct, counter = encrypt_plain_text(input, counter)
    cipher_texts.append(ct)
#print(len(cipher_texts))
df = pd.DataFrame(cipher_texts)
print(df.shape)
df.to_csv('cipher_texts.csv')
