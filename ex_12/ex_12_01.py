# -*- coding: utf-8 -*-
"""
Exercise 1: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.

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
    
    while True:
        data = mysock.recv(512) # What is 512 used for???
        if len(data) < 1:
            break
        print(data.decode().rstrip(), end='') 
        # Is it necessary to add data.decode().rstrip() here    
except:
    print('Invalid Input')

mysock.close()