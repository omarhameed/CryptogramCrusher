# Packages To install
pip install pandas
pip install matplotlib
pip install sklearn

# Program Description
In this program a message is read from `SecureMessage.txt` as a string and encrypted using the AES-128 method. It follows the following steps:

## GetMessage()
1) This function reads a plain English message from the input file and returns the message as a string in byte format. The message is returned in bytes, because the encryption function AES.encrypt() must have the parameter type in bytes.
The message is then padded using pad(message) in order to make the message have a size of 16 bytes. This is because AES uses 128 bit-block size data.

2) The `Encrypt message` function then takes an argument, padded message as bytes. An AES is then created and used to call the function `encrypt`, which returns an AES-128 encrypted message. This message is returned as a string type, which will then be reversed in the decryption process.

## SaveEncrypt function
This function takes in two arguments, the encrypted message and the directory to store the encrypted message in. If the directory inputted does not exist, then the program terminates. 

# Decryption
The `receive.py` program reads an encrypted message stored in `AES-128.dat` and then decrypts the message and unpads the added values. It then saves it as "`DecryptedMessage.txt`".

The `GetMessage` function reads the message as a string, which is then converted to bytes in order to be the correct format for the `Decrypt` function. The base64 data is decoded using the `b64decode` function and the output is decrypted using the `AES.decrypt` function. The decrypted output is unpadded from the added values, the total block size of the string is `BLOCK_SIZE = 16 Bytes`. The function then returns a string value.

`SaveDecrypt()` writes the output value to a text file `DecryptedMessage.txt`.

# Additional Information
Both programs above, `receive.py` and `send.py`, contain the function `GetFilePath` which is only used as a sanity check. It looks for the argument file name in all the sub-directories in case the order of the files is altered after installation.