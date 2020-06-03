from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Hash import MD5

class AESCustom:
    def __init__(self, key):
        hashFunc = MD5.new()
        hashFunc.update(bytes(key,'utf-8'))
        self.key = hashFunc.digest()

    def pad(self, s):
        padding_size = AES.block_size - len(s) % AES.block_size
        return s + b"\0" * padding_size, padding_size

    def encrypt(self, message, key_size = 256):
        message, padding_size = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return iv + cipher.encrypt(message) + bytes([padding_size])

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:-1])
        padding_size = ciphertext[-1] * (-1)
        if padding_size == 0:
            return plaintext
        else:
            return plaintext[:padding_size]
        # return plaintext.rstrip(b"\0")