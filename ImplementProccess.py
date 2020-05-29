import hashlib
import os
import random
import string
from Cryptodome.PublicKey import RSA
def hashSha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

def checkPathFileOrFolder(path, folder = False):
    if(folder):
        return os.path.isdir(path)
    else:
        return os.path.isfile(path)

def saveFile(path, text):
    f = open(path,'w')
    f.write(text)
    f.close()

def generateSymmetricKey(length):
    allCharacter = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(allCharacter) for i in range(int(length)))

def generateAsymmetricKey(size, folder):
    key = RSA.generate(int(size))
    