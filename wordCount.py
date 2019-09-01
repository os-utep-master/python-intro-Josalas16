# CS 4375: Theory of Operating Systems
# Author: Jaime O. Salas
# Description:

# Helps match or finds strings (Regular Expression)
import re 
# Interaction with the file system
import os
# Constants functions and methods
import sys


# Input and output Files
fileInput = sys.argv[1]
fileOutput= sys.argv[2]




# Dictionary for all words
wordfileDict = {}

# Opening a file
with open(fileInput, "r") as wordFile:
    for line in wordFile:
        #removes newlines
       
        line = line.lower()
        
        #words = line.split()
        words = re.findall(r'\b[a-z]{1,15}\b' , line)
    
        for word in words:
            if word in wordfileDict:
                wordfileDict[word] += 1
            else:
                wordfileDict[word] = 1
                
finalsorted = sorted(wordfileDict.keys())
#sortedFileWords = sorted(wordfileDict)
with open(fileOutput, 'w') as f:
    for key in list(finalsorted):
        f.writelines("%s %s\n" %((key, str(wordfileDict[key]))))