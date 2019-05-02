# -*- coding: utf-8 -*-
"""
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the 
dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195

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
        mh[words[1]] = mh.get(words[1], 0) + 1 # get method???

bnam = None
bnum = None
for k, v in mh.items():   # mh.item??? why can't mh???
    if bnam is None or bnum < v:
        bnam = k
        bnum = v
        
print(bnam, bnum)