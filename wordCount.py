# CS 4375: Theory of Operating Systems
# Author: Jaime O. Salas
# Description: Intorduction to basic features and tools for python.

# Helps match or finds strings (Regular Expression)
import re 
# Interaction with the file system
import os
# Constants functions and methods
import sys


# Input and output Files
# fileInput is for reading
# fileOutput is the file to write to
fileInput = sys.argv[1]
fileOutput= sys.argv[2]




# Dictionary for all words
wordfileDict = {}

# Opening a file
# Source: https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
with open(fileInput, "r") as wordFile:
    for line in wordFile:
        #removes newlines
       
        line = line.lower()
        
        # source: https://www.guru99.com/python-regular-expressions-complete-tutorial.html
        # eliminates Chars
        words = re.findall(r'\b[a-z]{1,15}\b' , line)
    
        # if the word is not already in the dictionary it gets added
        # else it is counted if it exists in the Dict
        for word in words:
            if word in wordfileDict:
                wordfileDict[word] += 1
            else:
                wordfileDict[word] = 1
                
# Sorts all keys in the wordFileDict 
finalsorted = sorted(wordfileDict.keys())

# Write a sequence of strings to the file
# Source: https://www.tutorialspoint.com/python/file_writelines.htm
with open(fileOutput, 'w') as f:
    for key in list(finalsorted):
        f.writelines("%s %s\n" %((key, str(wordfileDict[key]))))