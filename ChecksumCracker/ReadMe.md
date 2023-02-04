## The Checksum Calculation 

The message is first read in as a byte array and the sum function is used to calculate the total sum of the values in the byte array. 

## Checksum Vulnerabilities

The checksum function sums all the ASCII values of the string message and outputs a unique number. However, this number can be vulnerable as different patterns of malicious letters can output the same checksum and have the same amount of characters. 

## The Power of Hashing Algorithms 

SHA hashing algorithms offer a solution to the vulnerabilities of checksum calculations. The SHA hash outputs a hash of fixed size that is unique to any file or string, regardless of its size or content. 