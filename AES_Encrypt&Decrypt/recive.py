
"""
-> Question 2 (8 points)
    For this question, you'll encrypt and decrypt a message. I recommend using a library for the actual encryption. In class we used the cryptography package.

    A)    Encryption (3 points for code, 1 point for encrypted result)
        Create a UTF-8 encoded string with your name and banner number: “Jane Doe - B00123456”. Encrypt it with AES-128 encryption in ECB mode with a private key of your choice.

    B)    Decryption (3 points for code, 1 point for decrypted result)
        Decrypt the secret message to recover your name and banner number.
"""
from fileinput import filename
import struct
from tarfile import BLOCKSIZE
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import binascii
import os
import base64

from os import  listdir
from os.path import isfile, join
import shutil
import sys
key = b'ghp_v4PGwsGceoHq'

BLOCK_SIZE = 16  # Bytes


def GetFilepath(search_name):
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
            #fsz = struct.unpack('<Q', fin.read(struct.calcsize('<Q')))[0]
            return fin.read()

# Decrypt the message

    #padded_message = AESECBPKCS5Padding(key, "b64")
    #encode('utf8')

def Decrypt(message):
    aes_obj = AES.new(key, AES.MODE_ECB)
    message = base64.b64decode(message)
    decrypted_text = unpad(aes_obj.decrypt(message), BLOCK_SIZE)
    print('The decrypted text', str(decrypted_text))
    return decrypted_text


def main():
    #current_dir = os.path.abspath(os.getcwd())
    #encrypted_message_dir = current_dir + "\EncryptedMessage"
    #print("sd:   " + encrypted_message_dir)
    #onlyfiles = [f for f in listdir(encrypted_message_dir) if isfile(join(encrypted_message_dir, f))]

    filename = GetFilepath("\Qustion_2\EncryptedMessage\AES-128.dat")
   # filename = "Qustion_2\EncryptedMessage\AES-128.txt"
    message = GetMessage(filename)
    #unpadded_message = unpad(message)
    print("Decrypting message..... ")
   # unpadded_message = un_pad(message)
    print(message)
    Decrypt(message)
  
if __name__ == "__main__":
    main()
