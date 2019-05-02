# -*- coding: utf-8 -*-
"""
Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
    
X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.

"""
import re

filename = input('Enter a file name: ') # mbox.txt / mbox-short.txt
filetype = input('Enter the file type: ')
file = filename + '.' + filetype
if file == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
try:
    text = open(file)
    count = 0
    for line in text:
        if re.search('^Subject:', line): 
            ##??? why word[0] == 'Subject:' doesn't work
            count = count + 1
    print('There were {} subject lines in mbox.txt'.format(count))
except:
    print('Python can not open the file', filename)
