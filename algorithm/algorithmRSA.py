import zlib
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def generateAsymKey(size, folder, createdTime):
    key = RSA.generate(int(size.split(' ')[0]))
    publicFile = open(folder + "/PulicKey_" + createdTime + '(' + size.split(' ')[0] + ").pubk", "wb") #+ "(" + number  + ")
    privateFile = open(folder + "/PrivateKey_" + createdTime + '(' + size.split(' ')[0] + ").prvk", "wb")
    publicFile.write(key.publickey().exportKey())
    privateFile.write(key.exportKey())
    publicFile.close()
    privateFile.close()

class RSACustom:
    def __init__(self, key_):
        self.key = open(key_,"rb").read() #private or public follow function
    
    # def encrypt(self, plaintext):
    #     publickey = RSA.import_key(self.key)
    #     encryptor = PKCS1_v1_5.new(publickey)
    #     encrypted = encryptor.encrypt(plaintext)
    #     return encrypted

    # def decrypt(self, ciphertext):
    #     privatekey = RSA.importKey(self.key)
    #     sentinel = Random.new().read(20)
    #     decryptor = PKCS1_v1_5.new(privatekey)
    #     decrypted = decryptor.decrypt(ciphertext,sentinel)
    #     return decrypted
    def encrypt(self, plaintext):
        rsa_key = RSA.importKey(self.key)
        rsa_key = PKCS1_OAEP.new(rsa_key)
        blob = zlib.compress(plaintext)
        #
        chunk_size = 470
        offset = 0
        end_loop = False
        encrypted =  b''
        #
        while not end_loop:
            #The chunk
            chunk = blob[offset:offset + chunk_size]
            #If the data chunk is less then the chunk size, then we need to add
            #padding with " ". This indicates the we reached the end of the file
            #so we end loop here
            if len(chunk) % chunk_size != 0:
                end_loop = True
                chunk += b' ' * (chunk_size - len(chunk))

            #Append the encrypted chunk to the overall encrypted file
            encrypted += rsa_key.encrypt(chunk)

            #Increase the offset by chunk size
            offset += chunk_size

        #Base 64 encode the encrypted file
        return base64.b64encode(encrypted)

    def decrypt(self, ciphertext):
        rsakey = RSA.importKey(self.key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted_blob = base64.b64decode(ciphertext)
        #
        chunk_size = 512
        offset = 0
        decrypted = b''
        #
        while offset < len(encrypted_blob):
            chunk = encrypted_blob[offset: offset + chunk_size]

            #Append the decrypted chunk to the overall decrypted file
            decrypted += rsakey.decrypt(chunk)

            #Increase the offset by chunk size
            offset += chunk_size
        
        return zlib.decompress(decrypted)

