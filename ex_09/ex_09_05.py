# -*- coding: utf-8 -*-
"""
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

"""

fn = input('Enter the file name: ')
ft = input('Enter the file type: ')
file = fn + '.' + ft
try:
    text = open(file)
except:
    print('Python cannot open the file:', fn)
    
mh = dict()
for line in text:
    words = line.rstrip().split()
    if len(words) > 2 and words[0] == 'From':
        mw = words[1].split('@')
        mh[mw[1]] = mh.get(mw[1], 0) + 1 # get method???

print(mh)