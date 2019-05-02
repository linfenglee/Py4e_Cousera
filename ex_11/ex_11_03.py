# -*- coding: utf-8 -*-
"""
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
"""

import re

fn = input('Enter a file name: ')
try:
    text = open(fn)
except:
    print('Python cannot open the file:', fn)
    quit()

lis = list()
for line in text:
    lin = line.rstrip()
    mlis = re.findall('[0-9]+', line)
    lis = lis + mlis

total = 0
for i in lis:
    total = total + int(i)

print('Num:', len(lis))    
print('Sum:', total)

    