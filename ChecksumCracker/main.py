import os
import sys
from hashlib import sha256


def GetMessage(infile):
    file_size = os.path.getsize(infile)
    n = file_size

   

    if n ==0:
        print("Error: Plain txt file empty program Terminated")
        sys.exit()
    else:
        # Count the number of hashable objects and set zip object to store all letters with their frequency 
        with open(infile) as ip_file:
            message = ip_file.read()
        message_in_bytes = bytes(message, 'utf-8')

        return message_in_bytes

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

def ShaHash(message):
    print("SHA256 value is (In Hexadecimal Digits): \n"+ sha256(message).hexdigest()+ "\n")


def Checksum(message):
    print("Checksum is: \n"+ str(sum(message)) + "\n")

def main():
    infile = GetFilepath("\Qustion_3\checksum.txt")
    message_in_bytes = GetMessage(infile)
    print("PlainText Message :\n " + str(message_in_bytes.decode("utf-8")))
    Checksum(message_in_bytes)
    #Better way to do it using SHA
    ShaHash(message_in_bytes)
     
    #for i in range(0, len(message_in_bytes)):    
    #    print(message_in_bytes[i]),    

    print("Totally different message:\n")
    # Cracking The checksum Method 
    infile = GetFilepath("\Qustion_3\checksumCrack.txt")
    message_in_bytes = GetMessage(infile)
    print("PlainText Message :\n " + str(message_in_bytes.decode("utf-8")))
    Checksum(message_in_bytes)
    #Better way to do it using SHA
    ShaHash(message_in_bytes)



  
if __name__ == "__main__":
    main()