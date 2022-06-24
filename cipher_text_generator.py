
import os
from os import urandom
import encryption_algos
from binascii import hexlify as hexa, unhexlify as unhexa
import pandas as pd
import natsort

#just for our understanding to see output in block format#
def blocks(data):
    BLOCKLEN = 524288
    data = data.decode('ANSI')
    split = [(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]

    return split[0]


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
key_IDEA_64 = urandom(16)
key_sm4_128 = urandom(16)

counter = 0

def encrypt_plain_text_cbc(input, counter) :
    
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

def encrypt_plain_text_ecb(input, counter) :
    
        aes_256_ecb = encryption_algos.aes_encryption_ecb()
        ct_aes_256_ecb = aes_256_ecb.encryptor(input, key_aes_256)
        
        aes_128_ecb = encryption_algos.aes_encryption_ecb()
        ct_aes_128_ecb = aes_128_ecb.encryptor(input, key_aes_128)
        
        des3_56_ecb = encryption_algos.des3_encryption_ecb()
        ct_des3_56_ecb = des3_56_ecb.encryptor(input, key_3des_56)
        
        des1_56_ecb = encryption_algos.des1_encryption_ecb()
        ct_des1_56_ecb = des1_56_ecb.encryptor(input, key_1des_56)
        
        camellia_128_ecb = encryption_algos.camellia_encryption_ecb()
        ct_camellia_128_ecb = camellia_128_ecb.encryptor(input, key_camellia_128)
        
        blowfish_64_ecb = encryption_algos.blowfish_encryption_ecb()
        ct_blowfish_64_ecb = blowfish_64_ecb.encryptor(input, key_blowfish_64)
        
        IDEA_64_ecb = encryption_algos.IDEA_encryption_ecb()
        ct_IDEA_64_ecb = IDEA_64_ecb.encryptor(input, key_IDEA_64)
        
        
        SM4_128_ecb = encryption_algos.SM4_encryption_ecb()
        ct_SM4_128_ecb = SM4_128_ecb.encryptor(input, key_sm4_128)
        
        return ct_aes_256_ecb , ct_aes_128_ecb, ct_des3_56_ecb, ct_des1_56_ecb, ct_camellia_128_ecb, ct_blowfish_64_ecb, ct_IDEA_64_ecb, ct_SM4_128_ecb

input_dir = "D:\\Abhimanyu Singh\\2 knn experiement\\plaintext_data\\"
input_files_list = []

for file in os.listdir(input_dir) :
    input_files_list.append(input_dir + file)


input_files_list = natsort.natsorted(input_files_list,reverse=False)
#input_file = 'D:\\Abhimanyu Singh\\2 knn experiement\\plaintext_data\\plain_text_file1.txt'

input_str = ''

output_dir_ecb_1 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\aes_256'
output_dir_ecb_2 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\aes_128'
output_dir_ecb_3 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\des_3_56'
output_dir_ecb_4 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\des_1_56'
output_dir_ecb_5 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\camellia_128'
output_dir_ecb_6 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\blowfish_64'
output_dir_ecb_7 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\idea_64'
output_dir_ecb_8 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\ecb\\sm4_128'

output_dir_cbc_1 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\aes_256'
output_dir_cbc_2 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\aes_128'
output_dir_cbc_3 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\des_3_56'
output_dir_cbc_4 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\des_1_56'
output_dir_cbc_5 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\camellia_128'
output_dir_cbc_6 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\blowfish_64'
output_dir_cbc_7 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\idea_64'
output_dir_cbc_8 = 'D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\cbc\\sm4_128'


counter = 0 

#----------------------------------------------------------------------------------------
for file in input_files_list :
    input_str = ''
    with open(file, encoding='ANSI') as fp:
        file_data = fp.read()
        input_str += (file_data)
        
    #print( len(input_str))
    
    ct_aes_256_cbc , ct_aes_128_cbc, ct_des3_56_cbc, ct_des1_56_cbc, ct_camellia_128_cbc, ct_blowfish_64_cbc, ct_IDEA_64_cbc, ct_SM4_128_cbc   =   encrypt_plain_text_cbc(input_str.encode("ANSI"), counter)
    #print(len(unhexa(ct_aes_256_cbc)))
    
    # --------------------------------------------------------------------------
    output_file = open(output_dir_cbc_1 + "\\""cipher_text_file_aes_256_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_aes_256_cbc)
    output_file.close()


    output_file = open(output_dir_cbc_2 + "\\""cipher_text_file_aes_128_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_aes_128_cbc)
    output_file.close()

    
    output_file = open(output_dir_cbc_3 + "\\""cipher_text_file_des_3_56_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_des3_56_cbc)
    output_file.close()

    output_file = open(output_dir_cbc_4 + "\\""cipher_text_file_des_1_56_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_des1_56_cbc)
    output_file.close()

    output_file = open(output_dir_cbc_5 + "\\""cipher_text_file_camellia_128_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_camellia_128_cbc)
    output_file.close()

    output_file = open(output_dir_cbc_6 + "\\""cipher_text_file_blowfish_64_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_blowfish_64_cbc)
    output_file.close()

    output_file = open(output_dir_cbc_7 + "\\""cipher_text_file_idea_64_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_IDEA_64_cbc)
    output_file.close()

    output_file = open(output_dir_cbc_8 + "\\""cipher_text_file_sm4_128_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_SM4_128_cbc)
    output_file.close()

    #---------------------------------------------------------------------
    ct_aes_256_ecb , ct_aes_128_ecb, ct_des3_56_ecb, ct_des1_56_ecb, ct_camellia_128_ecb, ct_blowfish_64_ecb, ct_IDEA_64_ecb, ct_SM4_128_ecb   =   encrypt_plain_text_ecb(input_str.encode("ANSI"), counter)    
    #print(len(unhexa(ct_aes_256_ecb)))


    output_file = open(output_dir_ecb_1 + "\\""cipher_text_file_aes_256_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_aes_256_ecb)
    output_file.close()


    output_file = open(output_dir_ecb_2 + "\\""cipher_text_file_aes_128_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_aes_128_ecb)
    output_file.close()

    
    output_file = open(output_dir_ecb_3 + "\\""cipher_text_file_des_3_56_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_des3_56_ecb)
    output_file.close()

    output_file = open(output_dir_ecb_4 + "\\""cipher_text_file_des_1_56_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_des1_56_ecb)
    output_file.close()

    output_file = open(output_dir_ecb_5 + "\\""cipher_text_file_camellia_128_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_camellia_128_ecb)
    output_file.close()

    output_file = open(output_dir_ecb_6 + "\\""cipher_text_file_blowfish_64_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_blowfish_64_ecb)
    output_file.close()

    output_file = open(output_dir_ecb_7 + "\\""cipher_text_file_idea_64_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_IDEA_64_ecb)
    output_file.close()

    output_file = open(output_dir_ecb_8 + "\\""cipher_text_file_sm4_128_" + str(counter) + ".txt" + '', "wb")
    output_file.write(ct_SM4_128_ecb)
    output_file.close()
    
    counter += 1
    
    # ---------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#  ---------------save the keys

key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_aes_256.txt','wb')
key_file.write(hexa(key_aes_256))
key_file.close()
key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_aes_128.txt','wb')
key_file.write(hexa(key_aes_128))
key_file.close()
key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_3des_56.txt','wb')
key_file.write(hexa(key_3des_56))
key_file.close()
key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_1des_56.txt','wb')
key_file.write(hexa(key_1des_56))
key_file.close()
key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_camellia_128.txt','wb')
key_file.write(hexa(key_camellia_128))
key_file.close()
key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_blowfish_64.txt','wb')
key_file.write(hexa(key_blowfish_64))
key_file.close()
key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_IDEA_64.txt','wb')
key_file.write(hexa(key_IDEA_64))
key_file.close()
key_file = open('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\keys\\key_sm4_128.txt','wb')
key_file.write(hexa(key_sm4_128))
key_file.close()

