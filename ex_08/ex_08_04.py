# -*- coding: utf-8 -*-
"""
Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
Write a program to open the file romeo.txt and read it line by line. For
each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word
is not in the list, add it to the list. When the program completes, sort
and print the resulting words in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

"""

fn = input('Enter the file name: ')
ft = input('Enter the file type: ')
file = fn + '.' + ft
try:
    text = open(file)
except:
    print('Python cannot open the file:', fn)
    quit()
ms = list()
for line in text:
    words = line.split()
    for word in words:
        if word not in ms:
            ms.append(word)
print(sorted(ms)) # why ms.sort() doesn't work?
    