# -*- coding: utf-8 -*-
"""
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the number 
of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
Sample Line:
    
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
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

md = dict()   
for line in text:
    words = line.rstrip().split()
    if len(words) > 2 and words[0] == 'From':
        md[words[1]] = md.get(words[1], 0) + 1

# List Comprehension!!!
ml = sorted([(v,k) for k,v in md.items()], reverse = True)

n = input('Please enter a number: ')
try:
    num = int(n)
except:
    print('Invalid Input')
    
for a, b in ml[:num]:
    print(b,a)
        
        