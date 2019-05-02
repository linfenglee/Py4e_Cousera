# -*- coding: utf-8 -*-
"""
Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
of the number of characters at the end of the document.

"""

import socket
#import re

myurl = input('Please enter the URL: ')
# http://data.pr4e.org/romeo.txt
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # What's the meaning???
    mysock.connect((myurl.split('/')[2], 80))
    myu = 'GET' + ' ' + myurl + ' ' + 'HTTP/1.0\r\n\r\n' # What's the meaning???
    cmd = myu.encode()
    mysock.send(cmd)
        
    count = 0
    while True:
        data = mysock.recv(1)
        # the number in the parenthesis indicates the character this recv will read
        if len(data) < 1:
            break
        if count < 3000:
            print(data.decode(), end='')
        count = count + 1
        # count the entire document and the number of characters.
except:
    print('Invalid Input')
    
print('\n\nThere are {} characters in this document.'.format(count))
# There are 9236 characters in this document.
# Please compare the result with ex_12_03
mysock.close()