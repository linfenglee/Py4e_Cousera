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

fn = input('Enter a file name: ')
try:
    text = open(fn)
except:
    print('Python cannot open the file:', fn)

dic = dict()   
for line in text:
    words = line.rstrip().split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1

lis = sorted([(v,k) for k,v in dic.items()], reverse = True)

n = input('Please enter a number: ')
try:
    num = int(n)
except:
    print('Invalid Input')
    
for a, b in lis[:num]:
    print(b,a)