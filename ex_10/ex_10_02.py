# -*- coding: utf-8 -*-
"""
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""

fn = input('Enter the file name: ')
ft = input('Enter the file type: ')
file = fn + '.' + ft
try:
    text = open(file)
except:
    print('Python cannot open the file:', fn)

dic = dict()   
for line in text:
    words = line.rstrip().split()
    if len(words) > 6 and words[0] == 'From':
        word = words[5].split(':')
        dic[word[0]] = dic.get(word[0], 0) + 1

# List Comprehension
lis = sorted([(v,k) for k,v in dic.items()], reverse = True)

print('Time Freq')
for a, b in lis[:]:
    print(b, a)
    
    
    
        