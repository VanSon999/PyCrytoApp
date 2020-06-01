from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Hash import MD5

class AESCustom:
    def __init__(self, key):
        hashFunc = MD5.new()
        hashFunc.update(bytes(key,'utf-8'))
        self.key = hashFunc.digest()

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key_size = 256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")