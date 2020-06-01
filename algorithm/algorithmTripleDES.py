from Cryptodome.Cipher import DES3
from Cryptodome.Hash import MD5
from Cryptodome import Random

class TripleDESCustom:
    def __init__(self, key):
        hashFunc = MD5.new()
        hashFunc.update(bytes(key,'utf-8'))
        self.key = hashFunc.digest()
    
    def pad(self, s):
        padding_size = (DES3.block_size - len(s) % DES3.block_size)
        return s + b'\0' * padding_size,padding_size
    
    def encrypt(self, plaintext):
        iv = Random.new().read(DES3.block_size)
        cipher = DES3.new(self.key,DES3.MODE_CFB,iv)
        padPlainText, padding = self.pad(plaintext)
        return iv + cipher.encrypt(padPlainText) + bytes([padding])

    def decrypt(self, ciphertext):
        iv = ciphertext[:DES3.block_size]
        cipher = DES3.new(self.key,DES3.MODE_CFB,iv)
        plaintext = cipher.decrypt(ciphertext[DES3.block_size:-1])
        padding_size = ciphertext[-1]*(-1)
        if(padding_size == 0):
            return plaintext
        else:
            return plaintext[:padding_size]