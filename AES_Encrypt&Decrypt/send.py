
"""
-> Question 2 (8 points)
    For this question, you’ll encrypt and decrypt a message_in_bytes. I recommend using a library for the actual encryption. In class we used the cryptography package.

    A)    Encryption (3 points for code, 1 point for encrypted result)
        Create a UTF-8 encoded string with your name and banner number: “Jane Doe - B00123456”. Encrypt it with AES-128 encryption in ECB mode with a private key of your choice.

    B)    Decryption (3 points for code, 1 point for decrypted result)
        Decrypt the secret message_in_bytes to recover your name and banner number.
"""

from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import os
import random
import base64
import sys

BLOCK_SIZE = 16  # Bytes


key = b'ghp_v4PGwsGceoHq'

'''
def CreateKey():
    #Generates a random 16 digit key 

    key = urandom(16)
    print(key)
    #return key

'''
file_size = 0
        
# 1) determine ize of file and check if not empty 
def GetMessage(infile):
    file_size = os.path.getsize(infile)
    n = file_size

   

    if n ==0:
        print("Error: Plain txt file empty program Terminated")
        sys.exit()
    else:
        # Count the number of hashable objects and set zip object to store all letters with their frequency 
        with open(infile) as ip_file:
            message_in_bytes = ip_file.read()
        message_in_bytes = bytes(message_in_bytes, 'utf-8')

        return message_in_bytes



def EncryptMessage(padded_message):
    aes_obj = AES.new(key, AES.MODE_ECB)
    encrypted_text = aes_obj.encrypt(padded_message)
    return base64.b64encode(encrypted_text)


#   File Handling functions
def CreateFile(message_in_bytes):
 
    with open("cipher_message.dat", "wb") as cipher_file:
        cipher_file.write(message_in_bytes)

def SaveEncrypt(encrypted_text, encrypted_dir): 
    try:
        with open(encrypted_dir + "\AES-128.dat", "wb") as fout:
            fout.write(encrypted_text)
    except FileNotFoundError:
        print("Error: No Safe Directory found to store encrypted message_in_bytes program terminated")

def GetFilePath(search_name):
      # 1) check all folders and sub folders for secure message_in_bytes file
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

def GetDirPath(search_name):
      # 1) check all folders and sub folders for secure message_in_bytes file
    # should be only used incase file not found   
    root = os.path.abspath(os.getcwd())
    folder_name = search_name
    folder_path = str(root) + str(folder_name)

    isExist = os.path.exists(folder_path)
   
    if isExist == True:
        return folder_path
        
    else:
        for root, sub_directories, files in os.walk(root):
                for name in sub_directories:
                            folder_path = os.path.join(root, name)
        return folder_path


def main():
    print("Hi there ")    
    
    file_name = GetFilePath("SecureMessage.txt")
    dir_name = GetDirPath("EncryptedMessage")
    message_in_bytes = GetMessage(file_name) # Returns message in bytes 
    padded_message = pad(message_in_bytes, BLOCK_SIZE)
    encrypted_message = EncryptMessage(padded_message)
    SaveEncrypt(encrypted_message, dir_name)
    

if __name__ == "__main__":
    main()

