# -*- coding: utf-8 -*-
"""
Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:
    
"""
import re

fn = input('Enter a file name: ')
try:
    text = open(fn)
except:
    print('Python cannot open the file:', fn)
# regular expression: '^Author', '^X-', 'java$': 4218??? 
reg = input('Enter a regular expression: ')

count = 0
for line in text:
    lin = line.rstrip()
    if re.search(reg, lin):
        count = count + 1

# Learn Format
print('{} had {} lines that matched {}'.format(fn, count, reg))
    