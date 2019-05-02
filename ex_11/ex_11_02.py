# -*- coding: utf-8 -*-
"""
Exercise 2: Write a program to look for lines of the form:
    
New Revision: 39772

Extract the number from each of the lines using a regular expression 
and the findall() method. Compute the average of the numbers and
print out the average.

"""

import re

fn = input('Enter a file name: ')
try:
    text = open(fn)
except:
    print('Python cannot open the file:', fn)

lis = list()
for line in text:
    lin = line.rstrip()
    mlis = re.findall('New Revision: ([0-9]+)', lin)
    for n in mlis:
        num = int(n)
        lis.append(num)

print('Average:', round(sum(lis)/len(lis),2))