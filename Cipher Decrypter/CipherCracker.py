#!/usr/bin/env python

""" 

This program compares two text files, one has been encrypted with a Caesar cipher and the other is a random english Article taken online 
The Most Boring Thing Ever Written (https://www.brade.zone/2008/09/13/boring/). 


Using Bar plots and the pandas doorframe the most common letter from both articles was calculated and they were aligned together; 
in order to calculate the shift of the alphabet used.

File Output:
    
    -> Csv files ordered by how often a specific letter is used 
    letter_frequency_cipher_text.csv
    letter_frequency_Most_Boring_Thing.csv

    -> Bar plots for how often letters were used 
    letter_frequency_cipher_text.png
    letter_frequency_Most_Boring_Thing.png

    -> Output of decrypted message 
    DecryptedCipher.txt


 """


__author__ = "Omar Hameed"
__version__ = "1.0.1"
__maintainer__ = "Omar Hameed"
__email__ = "omarg@dal.ca"


# =============================  Question 1 (6 points) =============================
# Question 1a (3 points)
# Generate a letter frequency chart for this passage.

# Question 1b (2 points)
# Compare the letter frequency of this passage to standard english. Suggest the “shift”.

# Question 1c (1 point)
# Decrypt the message.



from asyncio.windows_events import NULL
from collections import Counter
from contextlib import nullcontext
#import pdb; pdb.set_trace()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import collections
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_iris
import os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# shift + alt 


import os

def search_file(filename):
    if filename in os.listdir():
        return os.path.abspath(filename)
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        if filename in filenames:
            return os.path.abspath(os.path.join(dirpath, filename))

       
    print("Error: File Not Foud")
    exit()


  
def LoadDataBuffer(FileName):
    Text = open(FileName, "r")
    # Count the number of hashable objects and set zip object to store all letters with their frequency 
    data = Text.read()
    Text.close()
    return data
    

def SortData(data):


    collections.Counter(data)
    zip(*collections.Counter(data).items())
    a, b = zip(*collections.Counter(data).items())
  
    # Sort List By frequency Size
    zipped_lists = zip(b, a)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    list1, list2 = [ list(tuple) for tuple in  tuples]

    # Remove Space from txt 
    space_index = list2.index(" ")
    # list1: is the frequency list
    list1.pop(space_index)
    list2.pop(space_index)
    return list1,list2
 

def CreateDF(FileName, list1,list2):
    # Create Data-frame for each file
    list_of_tuples = list(zip(list1,list2))
    # Converting lists of tuples into
    # pandas Data-frame.
    filename_replace_ext = FileName.with_suffix('.csv')
    df = pd.DataFrame(list_of_tuples, columns = ['Frequency', 'Letter'],)
    #sort dataframe
    sorted_df = df.sort_values(by='Frequency', ascending=False)
    # reset_index to get back a default index
    sorted_df = sorted_df.reset_index(drop=True)

    most_used_letter = sorted_df.at[0,'Letter']
    return most_used_letter 


def PlotBarGraph(FileName,list1,list2 ):
   
    # Plot bar-chart 
    plt.bar(list2,list1, width= 0.4, color='blue', align = 'center', edgecolor = 'red', ecolor = 'yellow')
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d times'))
    filename_replace_ext = FileName.with_suffix('.png')
    plt.savefig('letter_frequency_' + str(filename_replace_ext))
    plt.ylabel('Frequency')
    plt.xlabel('Letter')
    # Clear plot for next graph and delete data frame 
    plt.clf()
   
   
  
def CrackCipher(cipher_text, most_used_english_letter, most_used_cipher_letter):
   
  
    key = ord(most_used_cipher_letter) - ord(most_used_english_letter)
    # The Decryption Function

    index = 0
    decrypted = ""

    for character  in cipher_text:
        index += 1

        if character.isupper(): 

            c_index = ord(character) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            # ADD character to string of characters 
            decrypted += c_og

        elif character.islower(): 

            c_index = ord(character) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif character.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(character) - key) % 10

            decrypted += str(c_og)
        
        elif character == '€' or character =='”':
            # if its emdash used convert to --
            emDash = "-"
            decrypted += emDash
#

        else:
            
            # if its neither alphabetical nor a number
            decrypted += character
    

    if os.path.isfile('filename.txt'):
        # Remove any old files used 
        os.remove("DecryptedCipher.txt")
        #open text file
        text_file = open("DecryptedCipher.txt", "w")
        #write string to file
        text_file.write(str(decrypted))
        #close file
        text_file.close()
    else:
        #open text file
        text_file = open("DecryptedCipher.txt", "w")
        #write string to file
        text_file.write(str(decrypted))
        #close file
        text_file.close()





def main():
    
    english_file_path = search_file('Most_Boring_Thing.txt')     
    english_filename =   english_file_path
    cipher_file_path = search_file('Most_Boring_Thing.txt')     
    cipher_filename = cipher_file_path
    
    # Get Data  & sort in order from biggest to smallest
    english_data = LoadDataBuffer(english_filename)
    cipher_data = LoadDataBuffer(cipher_filename)
    e_frequency,e_letter = SortData(english_data)
    c_frequency,c_letter = SortData(cipher_data)

    # Represent Data on a csv file a bar graph
    PlotBarGraph(english_filename, e_frequency,e_letter)
    PlotBarGraph(cipher_filename, c_frequency,c_letter)
    e_most_used_letter = CreateDF(english_filename, e_frequency,e_letter)
    c_most_used_letter = CreateDF(cipher_filename, c_frequency,c_letter)

    # Crack Cipher
    CrackCipher(cipher_data, e_most_used_letter, c_most_used_letter)

   

if __name__ == "__main__":
    main()
