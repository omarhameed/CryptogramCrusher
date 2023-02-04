"""
-> Question 2 (8 points)
    For this question, you'll encrypt and decrypt a message. I recommend using a library for the actual encryption. In class we used the cryptography package.

    A)    Encryption (3 points for code, 1 point for encrypted result)
        Create a UTF-8 encoded string with your name and banner number: “Jane Doe - B00123456”. Encrypt it with AES-128 encryption in ECB mode with a private key of your choice.

    B)    Decryption (3 points for code, 1 point for decrypted result)
        Decrypt the secret message to recover your name and banner number.
"""

from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import os
import base64
import sys
key = b'ghp_v4PGwsGceoHq'

BLOCK_SIZE = 16  # Bytes


def GetFilePath(search_name):
      # 1) check all folders and sub folders for secure message file
    # should be only used incase file not found   
    root = os.path.abspath(os.getcwd())
    filename = search_name
    file_path = str(root) + str(filename)

    isExist = os.path.exists(file_path)
   
    if isExist == True:
        return file_path
        
    else:
        for root, sub_directories, files in os.walk(root):
                for name in files:
                        if name == search_name : 
                            file_path = os.path.join(root, name)
        return file_path



def GetMessage(file_name):
    file_size = os.path.getsize(file_name)
    n = file_size

    if n ==0:
        print("Error: Plain txt file empty program Terminated")
        sys.exit()
    else:
        with open(file_name, mode= "r") as fin:
            return fin.read()

def Decrypt(message):
    aes_obj = AES.new(key, AES.MODE_ECB)
    message = base64.b64decode(message)
    decrypted_text = unpad(aes_obj.decrypt(message), BLOCK_SIZE)
    return decrypted_text.decode()
def SaveDecrypt(decrypted_text):
   
    with open("DecryptedMessage.txt", "w") as fout:
            fout.write(decrypted_text)
    

def main():


    filename = GetFilePath("\Qustion_2\EncryptedMessage\AES-128.dat")
    message = GetMessage(filename)
    print("Decrypting message..... ")
    message = bytes(message, 'utf-8')
    decrypted_text = Decrypt(message)
    SaveDecrypt(decrypted_text)
  
if __name__ == "__main__":
    main()
