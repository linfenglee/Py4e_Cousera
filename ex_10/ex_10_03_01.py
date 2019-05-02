# -*- coding: utf-8 -*-
"""
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.

"""

import re
# let's take romeo-full.txt as example.
fn = input('Enter the file name: ')
ft = input('Enter the file type: ')
file = fn + '.' + ft
try:
    text = open(file)
except:
    print('Python cannot open the file:', fn)

dic = dict()   
for line in text:
    lin = line.rstrip()
    mlis = re.findall('\s([A-Za-z]+).', lin) # how to explain this???
    for word in mlis:
        dic[word] = dic.get(word, 0) + 1

lis = sorted([(v,k) for k,v in dic.items()], reverse = True)

n = input('Please enter a number: ')
try:
    num = int(n)
except:
    print('Invalid Input')
    
for a, b in lis[:num]:
    print(b,a)