
import os
from os import urandom
import encryption_algos
from binascii import hexlify as hexa, unhexlify as unhexa
import pandas as pd

#just for our understanding to see output in block format#
def blocks(data):
    BLOCKLEN = 512
    split = [hexa(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]

    return ' '.join(split)


#input_file = open('key.txt','r')
#key_1 = 0
#with input_file as f:
#    key_1 = next(f)
#    key_1 = key_1.strip()
#print(key_1)
#key_1 = unhexa(key_1)
#print(key_1)

key_aes_256 = urandom(32)
key_aes_128 = urandom(16)
key_3des_56 = urandom(8)
key_1des_56 = urandom(8)
key_camellia_128 = urandom(16)
key_blowfish_64 = urandom(8)
key_IDEA_64 = urandom(8)
key_sm4_128 = urandom(16)

counter = 0

def encrypt_plain_text(input, counter) :
    
        aes_256_cbc = encryption_algos.aes_encryption_cbc()
        ct_aes_256_cbc = aes_256_cbc.encryptor(input, key_aes_256)
        
        aes_128_cbc = encryption_algos.aes_encryption_cbc()
        ct_aes_128_cbc = aes_128_cbc.encryptor(input, key_aes_128)
        
        des3_56_cbc = encryption_algos.des3_encryption_cbc()
        ct_des3_56_cbc = des3_56_cbc.encryptor(input, key_3des_56)
        
        des1_56_cbc = encryption_algos.des1_encryption_cbc()
        ct_des1_56_cbc = des1_56_cbc.encryptor(input, key_1des_56)
        
        camellia_128_cbc = encryption_algos.camellia_encryption_cbc()
        ct_camellia_128_cbc = camellia_128_cbc.encryptor(input, key_camellia_128)
        
        blowfish_64_cbc = encryption_algos.blowfish_encryption_cbc()
        ct_blowfish_64_cbc = blowfish_64_cbc.encryptor(input, key_blowfish_64)
        
        IDEA_64_cbc = encryption_algos.IDEA_encryption_cbc()
        ct_IDEA_64_cbc = IDEA_64_cbc.encryptor(input, key_IDEA_64)
        
        
        SM4_128_cbc = encryption_algos.SM4_encryption_cbc()
        ct_SM4_128_cbc = SM4_128_cbc.encryptor(input, key_sm4_128)
        
        return ct_aes_256_cbc , ct_aes_128_cbc, ct_des3_56_cbc, ct_des1_56_cbc, ct_camellia_128_cbc, ct_blowfish_64_cbc, ct_IDEA_64_cbc, ct_SM4_128_cbc

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
