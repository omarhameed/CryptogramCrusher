# Libraries to Download:
- pip install pycrypto
- pip install aes-pkcs5

## CreateDF
The `CreateDF` function is used to produce a data frame using the pandas library 
and sorts their values in ascending order. This function’s purpose is to analyze 
the frequency of letters in the text data. The result of the sorting is saved to a 
CSV file for further analysis. The function returns the most used letter in the data.

## PlotBarGraph
The `PlotBarGraph` function uses the `matplotlib.pyplot` library to create a bar 
graph of the letter frequency analysis. This function allows for a visual representation 
of the data. The `plt.clf` function is also used to clear any plotted data once it has 
been saved, avoiding overlapping results on subsequent runs of the function. 

## Main Function
The main function calls both `CreateDF` and `PlotBarGraph` functions twice, once for 
the cipher text and once for a plain English text article. The purpose is to compare 
the letter frequency in both texts. The most used letter in both functions is then 
cross-referenced using the `CrackCipher` function. This function sets the decryption 
key equal to the difference between the Unicode values of the most used cipher letter 
and the most used English letter. 

The decryption process happens by iterating through each letter in the cipher text with 
a for loop and a series of if statements. The five possibilities considered are: capital 
letter, lower letter, digit, em dash, or other characters. If the letter is a lower or 
capital letter, its position is calculated relative to the letter A or a, and then the 
character is shifted to the left by the key positions to get its original position. The 
resulting character is then added to the decrypted text string. If the character is a 
number, its value is shifted. If the character is an em dash (a double dash --), it may 
be represented as €” in Python, and an if statement with € or ” is used to convert it 
to a dash (-). Any other characters are simply added to the decrypted text string.


## Sample output:


![Plain English letter frequncy graph](https://github.com/omarhameed/EncryptionMethods/blob/main/Cipher%20Decrypter/SampleOutput/Picture1.png?raw=true)
![Plain English letter frequncy table](https://github.com/omarhameed/EncryptionMethods/blob/main/Cipher%20Decrypter/SampleOutput/Picture2.png)


![Cipher letter frequncy graph](https://github.com/omarhameed/EncryptionMethods/blob/main/Cipher%20Decrypter/SampleOutput/Picture3.png)
![Cipher letter frequncy table](https://github.com/omarhameed/EncryptionMethods/blob/main/Cipher%20Decrypter/SampleOutput/Picture4.png)
