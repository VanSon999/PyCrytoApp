import hashlib
import os
import random
import string
import time
from Cryptodome.Hash import SHA256
from datetime import datetime
from algorithm import algorithmAES
from algorithm import algorithmTripleDES
from algorithm import algorithmRSA

def hashSha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

def generateHashFromOrigin(origin):
    hash_ = SHA256.new()
    hash_.update(origin)
    return hash_.digest()

def checkHashAfterDecrypted(decrypted):
    hashValue = decrypted[-SHA256.digest_size:]
    hash_ = SHA256.new()
    hash_.update(decrypted[:-SHA256.digest_size])
    if (hash_.digest() == hashValue):
        return True, decrypted[:-SHA256.digest_size]
    else:
        return False, decrypted[:-SHA256.digest_size]

def checkPathFileOrFolder(path, folder = False):
    if(folder):
        return os.path.isdir(path)
    else:
        return os.path.isfile(path)

def checkFileKeyType(path, en = True, rsa = False):
    types = ''
    if(en):
        types = ".pubk"
    else:
        types = ".prvk"

    if(rsa):
        return path.lower().endswith(types)
    else:
        return path.lower().endswith('.txt')

def checkKey(str, en = True, rsa = False):
    if(os.path.isfile(str)):
        return checkFileKeyType(str,en,rsa)
    else:
        return rsa == False

def checkPathEncryptOrDecrypt(pathSource, pathOut):
    return (checkPathFileOrFolder(pathSource) or checkPathFileOrFolder(pathSource, True)) and checkPathFileOrFolder(pathOut, True)

def saveFile(path, text):
    # print(path)
    f = open(path,'w')
    f.write(text)
    f.close()

def getpathFolder(str):
    if(os.path.isfile(str)):
        return os.path.dirname(str)
    else:
        return str

def generateSymmetricKey(length):
    allCharacter = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(allCharacter) for i in range(int(length)))

def generateAsymmetricKey(size, folder):
    createdTime = str(datetime.now()).replace(':', '-')
    algorithmRSA.generateAsymKey(size,folder,createdTime)

def parseKeySymmetric(key):
    if(os.path.isfile(key)):
        fileKey = open(key, 'r')
        return fileKey.read()
    else:
        return key

def getAllFileInFolder(path): # not in subfolder
    dirs = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            # print(item)
            dirs.append(os.path.join(path, item))
    return dirs
# --------------------------------------------AES-------------------------------------------------------
def encryptAES(inPath, inKey, outPath, proccessBar, remove):
    if(os.path.isfile(inPath)):
        encryptFileAES(inPath,inKey,outPath,proccessBar,remove)
    else:
        encryptFolderAES(inPath,inKey,outPath,proccessBar,remove)

def encryptFileAES(originPath,key_,outFolder, proccessBar, remove = False):
    originFile = open(originPath,"rb")
    plaintext = originFile.read()
    proccessBar.setProperty("value", 20)
    plaintextAndHash = plaintext + generateHashFromOrigin(plaintext)
    proccessBar.setProperty("value", 40)
    key = parseKeySymmetric(key_)
    aes = algorithmAES.AESCustom(key)
    encrypted = aes.encrypt(plaintextAndHash)
    proccessBar.setProperty("value", 80)
    outputFile = open(outFolder + "/" + os.path.basename(originPath) + '.cipher',"wb")
    outputFile.write(encrypted)
    proccessBar.setProperty("value", 85)
    originFile.close()
    if(remove): os.remove(originPath)
    proccessBar.setProperty("value", 90)
    outputFile.close()

def encryptFolderAES(originPath, key_, outFolder, proccessBar, remove = False):
    listFile = getAllFileInFolder(originPath)
    amountFile = len(listFile)
    key = parseKeySymmetric(key_)
    aes = algorithmAES.AESCustom(key)
    for i, pathFile in enumerate(listFile):
        originFile = open(pathFile,"rb")
        plaintext = originFile.read()
        plaintextAndHash = plaintext + generateHashFromOrigin(plaintext)
        encrypted = aes.encrypt(plaintextAndHash)
        outputFile = open(outFolder + "/" + os.path.basename(pathFile) + '.cipher',"wb")
        outputFile.write(encrypted)
        originFile.close()
        if(remove): os.remove(pathFile)
        outputFile.close()
        proccessBar.setProperty("value", int((i/amountFile)*90))

def decryptAES(inPath, inKey, outPath, proccessBar, remove):
    if(os.path.isfile(inPath)):
        return decryptFileAES(inPath,inKey,outPath,proccessBar,remove)
    else:
        return decryptFolderAES(inPath,inKey,outPath,proccessBar,remove)

def decryptFileAES(cipherPath, key_, outFolder, proccessBar, remove = False):
    cipherFile = open(cipherPath,"rb")
    ciphertext = cipherFile.read()
    key = parseKeySymmetric(key_)
    aes = algorithmAES.AESCustom(key)
    proccessBar.setProperty("value", 20)
    plaintextAndHash = aes.decrypt(ciphertext)
    proccessBar.setProperty("value", 50)
    checked, plaintext = checkHashAfterDecrypted(plaintextAndHash)
    proccessBar.setProperty("value", 60)
    outputFile = open(outFolder + "/Decrypt_" + os.path.basename(cipherPath)[:-7],"wb")
    outputFile.write(plaintext)
    proccessBar.setProperty("value", 80)
    cipherFile.close()
    if(remove): os.remove(cipherPath)
    outputFile.close()
    proccessBar.setProperty("value", 90)
    return checked

def decryptFolderAES(cipherPath, key_, outFolder, proccessBar, remove = False):
    listFile = getAllFileInFolder(cipherPath)
    amountFile = len(listFile)
    key = parseKeySymmetric(key_)
    aes = algorithmAES.AESCustom(key)
    returnValue = True
    for i, pathFile in enumerate(listFile):
        cipherFile = open(pathFile,"rb")
        ciphertext = cipherFile.read()
        plaintextAndHash = aes.decrypt(ciphertext)
        checked, plaintext = checkHashAfterDecrypted(plaintextAndHash)
        outputFile = open(outFolder + "/Decrypt_" + os.path.basename(pathFile)[:-7],"wb")
        outputFile.write(plaintext)
        cipherFile.close()
        if(remove): os.remove(pathFile)
        outputFile.close()
        returnValue = returnValue and checked
        proccessBar.setProperty("value", int((i/amountFile)*90))
    return returnValue
# --------------------------------------------3DES-------------------------------------------------------
def encrypt3DES(inPath, inKey, outPath, proccessBar, remove):
    if(os.path.isfile(inPath)):
        encryptFile3DES(inPath,inKey,outPath,proccessBar,remove)
    else:
        encryptFolder3DES(inPath,inKey,outPath,proccessBar,remove)

def encryptFile3DES(originPath,key_,outFolder, proccessBar, remove = False):
    originFile = open(originPath,"rb")
    plaintext = originFile.read()
    proccessBar.setProperty("value", 20)
    plaintextAndHash = plaintext + generateHashFromOrigin(plaintext)
    proccessBar.setProperty("value", 40)
    key = parseKeySymmetric(key_)
    tripleDes = algorithmTripleDES.TripleDESCustom(key)
    encrypted = tripleDes.encrypt(plaintextAndHash)
    proccessBar.setProperty("value", 80)
    outputFile = open(outFolder + "/" + os.path.basename(originPath) + '.cipher',"wb")
    outputFile.write(encrypted)
    proccessBar.setProperty("value", 85)
    originFile.close()
    if(remove): os.remove(originPath)
    proccessBar.setProperty("value", 90)
    outputFile.close()

def encryptFolder3DES(originPath,key_,outFolder, proccessBar, remove = False):
    listFile = getAllFileInFolder(originPath)
    amountFile = len(listFile)
    key = parseKeySymmetric(key_)
    tripleDes = algorithmTripleDES.TripleDESCustom(key)
    for i, pathFile in enumerate(listFile):
        originFile = open(pathFile,"rb")
        plaintext = originFile.read()
        plaintextAndHash = plaintext + generateHashFromOrigin(plaintext)
        encrypted = tripleDes.encrypt(plaintextAndHash)
        outputFile = open(outFolder + "/" + os.path.basename(pathFile) + '.cipher',"wb")
        outputFile.write(encrypted)
        originFile.close()
        if(remove): os.remove(pathFile)
        outputFile.close()
        proccessBar.setProperty("value", int((i/amountFile)*90))

def decrypt3DES(inPath, inKey, outPath, proccessBar, remove):
    if(os.path.isfile(inPath)):
        return decryptFile3DES(inPath,inKey,outPath,proccessBar,remove)
    else:
        return decryptFolder3DES(inPath,inKey,outPath,proccessBar,remove)

def decryptFile3DES(cipherPath, key_, outFolder, proccessBar, remove = False):
    cipherFile = open(cipherPath,"rb")
    ciphertext = cipherFile.read()
    key = parseKeySymmetric(key_)
    tripleDes = algorithmTripleDES.TripleDESCustom(key)
    proccessBar.setProperty("value", 20)
    plaintextAndHash = tripleDes.decrypt(ciphertext)
    proccessBar.setProperty("value", 50)
    checked, plaintext = checkHashAfterDecrypted(plaintextAndHash)
    proccessBar.setProperty("value", 60)
    outputFile = open(outFolder + "/Decrypt_" + os.path.basename(cipherPath)[:-7],"wb")
    outputFile.write(plaintext)
    proccessBar.setProperty("value", 80)
    cipherFile.close()
    if(remove): os.remove(cipherPath)
    outputFile.close()
    proccessBar.setProperty("value", 90)
    return checked

def decryptFolder3DES(cipherPath, key_, outFolder, proccessBar, remove = False):
    listFile = getAllFileInFolder(cipherPath)
    amountFile = len(listFile)
    key = parseKeySymmetric(key_)
    tripleDES = algorithmTripleDES.TripleDESCustom(key)
    returnValue = True
    for i, pathFile in enumerate(listFile):
        cipherFile = open(pathFile,"rb")
        ciphertext = cipherFile.read()
        plaintextAndHash = tripleDES.decrypt(ciphertext)
        checked, plaintext = checkHashAfterDecrypted(plaintextAndHash)
        outputFile = open(outFolder + "/Decrypt_" + os.path.basename(pathFile)[:-7],"wb")
        outputFile.write(plaintext)
        cipherFile.close()
        if(remove): os.remove(pathFile)
        outputFile.close()
        returnValue = returnValue and checked
        proccessBar.setProperty("value", int((i/amountFile)*90))
    return returnValue
# --------------------------------------------RSA-------------------------------------------------------
def encryptRSA(inPath, inKey, outPath, proccessBar, remove):
    if(os.path.isfile(inPath)):
        encryptFileRSA(inPath,inKey,outPath,proccessBar,remove)
    else:
        encryptFolderRSA(inPath,inKey,outPath,proccessBar,remove)

def encryptFileRSA(originPath,key_,outFolder, proccessBar, remove = False):
    originFile = open(originPath,"rb")
    plaintext = originFile.read()
    proccessBar.setProperty("value", 20)
    plaintextAndHash = plaintext + generateHashFromOrigin(plaintext)
    proccessBar.setProperty("value", 40)
    rsa = algorithmRSA.RSACustom(key_) #key_ is path
    encrypted = rsa.encrypt(plaintextAndHash)
    proccessBar.setProperty("value", 80)
    outputFile = open(outFolder + "/" + os.path.basename(originPath) + '.cipher',"wb")
    outputFile.write(encrypted)
    proccessBar.setProperty("value", 85)
    originFile.close()
    if(remove): os.remove(originPath)
    proccessBar.setProperty("value", 90)
    outputFile.close()

def encryptFolderRSA(originPath,key_,outFolder, proccessBar, remove = False):
    listFile = getAllFileInFolder(originPath)
    amountFile = len(listFile)
    rsa = algorithmRSA.RSACustom(key_)
    for i, pathFile in enumerate(listFile):
        originFile = open(pathFile,"rb")
        plaintext = originFile.read()
        plaintextAndHash = plaintext + generateHashFromOrigin(plaintext)
        encrypted = rsa.encrypt(plaintextAndHash)
        outputFile = open(outFolder + "/" + os.path.basename(pathFile) + '.cipher',"wb")
        outputFile.write(encrypted)
        originFile.close()
        if(remove): os.remove(pathFile)
        outputFile.close()
        proccessBar.setProperty("value", int((i/amountFile)*90))

def decryptRSA(inPath, inKey, outPath, proccessBar, remove):
    if(os.path.isfile(inPath)):
        return decryptFileRSA(inPath,inKey,outPath,proccessBar,remove)
    else:
        return decryptFolderRSA(inPath,inKey,outPath,proccessBar,remove)

def decryptFileRSA(cipherPath, key_, outFolder, proccessBar, remove = False):
    cipherFile = open(cipherPath,"rb")
    ciphertext = cipherFile.read()
    rsa = algorithmRSA.RSACustom(key_)
    proccessBar.setProperty("value", 20)
    plaintextAndHash = rsa.decrypt(ciphertext)
    proccessBar.setProperty("value", 50)
    checked, plaintext = checkHashAfterDecrypted(plaintextAndHash)
    proccessBar.setProperty("value", 60)
    outputFile = open(outFolder + "/Decrypt_" + os.path.basename(cipherPath)[:-7],"wb")
    outputFile.write(plaintext)
    proccessBar.setProperty("value", 80)
    cipherFile.close()
    if(remove): os.remove(cipherPath)
    outputFile.close()
    proccessBar.setProperty("value", 90)
    return checked

def decryptFolderRSA(cipherPath, key_, outFolder, proccessBar, remove = False):
    listFile = getAllFileInFolder(cipherPath)
    amountFile = len(listFile)
    rsa = algorithmRSA.RSACustom(key_)
    returnValue = True
    for i, pathFile in enumerate(listFile):
        cipherFile = open(pathFile,"rb")
        ciphertext = cipherFile.read()
        plaintextAndHash = rsa.decrypt(ciphertext)
        checked, plaintext = checkHashAfterDecrypted(plaintextAndHash)
        outputFile = open(outFolder + "/Decrypt_" + os.path.basename(pathFile)[:-7],"wb")
        outputFile.write(plaintext)
        cipherFile.close()
        if(remove): os.remove(pathFile)
        outputFile.close()
        returnValue = returnValue and checked
        proccessBar.setProperty("value", int((i/amountFile)*90))
    return returnValue