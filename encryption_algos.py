
import os
from Crypto.Cipher import DES
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa, unhexlify as unhexa
from os import urandom




#just for our understanding to see output in block format#
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]) for i in range(0, len(data), BLOCKLEN)]

    return ' '.join(split)

#create a random key


class aes_encryption_cbc :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(16)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
        aes_encrypt = cipher.encryptor()
        cipher_text = aes_encrypt.update(padded_data) + aes_encrypt.finalize()
        hexa_data = hexa(cipher_text)
        return hexa_data



class blowfish_encryption_cbc :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(8)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend = default_backend())
        blowfish_encrypt = cipher.encryptor()
        cipher_text = blowfish_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data


class des3_encryption_cbc :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(8)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend = default_backend())
        des3_encrypt = cipher.encryptor()
        cipher_text = des3_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data

class des1_encryption_cbc :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(8)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        des_1_encrypt = DES.new(key, DES.MODE_CBC, iv=iv)
        cipher_text = des_1_encrypt.encrypt(plain_text)
        hexa_data = hexa(cipher_text)
        return hexa_data

class camelia_encryption_cbc :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(16)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv), backend = default_backend())
        camelia_encrypt = cipher.encryptor()
        cipher_text = camelia_encrypt.update(padded_data) + aes_encrypt.finalize()
        hexa_data = hexa(cipher_text)
        return hexa_data

class SM4_encryption_cbc :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(16)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.SM4(key), modes.CBC(iv), backend = default_backend())
        SM4_encrypt = cipher.encryptor()
        cipher_text = SM4_encrypt.update(padded_data) + aes_encrypt.finalize()
        hexa_data = hexa(cipher_text)
        return hexa_data

class IDEA_encryption_cbc :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        iv = urandom(8)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv), backend = default_backend())
        IDEA_encrypt = cipher.encryptor()
        cipher_text = IDEA_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data



class aes_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        #iv = urandom(16)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = default_backend())
        aes_encrypt = cipher.encryptor()
        cipher_text = aes_encrypt.update(padded_data) + aes_encrypt.finalize()
        hexa_data = hexa(cipher_text)
        return hexa_data


class blowfish_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key
        #iv = urandom(8)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.Blowfish(key), modes.ECB(), backend = default_backend())
        des3_encrypt = cipher.encryptor()
        cipher_text = des3_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data


class des3_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend = default_backend())
        des3_encrypt = cipher.encryptor()
        cipher_text = des3_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data

class des1_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        des_1_encrypt = DES.new(key, DES.MODE_ECB)
        cipher_text = des_1_encrypt.encrypt(plain_text)
        hexa_data = hexa(cipher_text)
        return hexa_data


class camelia_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key


        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.Camellia(key), modes.ECB(), backend = default_backend())
        camelia_encrypt = cipher.encryptor()
        cipher_text = camelia_encrypt.update(padded_data) + aes_encrypt.finalize()
        hexa_data = hexa(cipher_text)
        return hexa_data

class SM4_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.SM4(key), modes.ECB(), backend = default_backend())
        SM4_encrypt = cipher.encryptor()
        cipher_text = SM4_encrypt.update(padded_data) + aes_encrypt.finalize()
        hexa_data = hexa(cipher_text)
        return hexa_data

class IDEA_encryption_ecb :
    BLOCKLEN = 16 #16 bytes

    def encryptor(self,plain_text, key) :
        self.plain_text = plain_text
        self.key = key

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text) + padder.finalize()

        cipher = Cipher(algorithms.IDEA(key), modes.ECB(), backend = default_backend())
        IDEA_encrypt = cipher.encryptor()
        cipher_text = IDEA_encrypt.update(padded_data) + des3_encrypt.finalize()

        hexa_data = hexa(cipher_text)
        return hexa_data
