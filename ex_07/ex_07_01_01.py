# -*- coding: utf-8 -*-
"""
Exercise 1: Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will
look as follows:
    
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500

You can download the file from www.py4e.com/code3/mbox-short.txt

"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ')
try:
    text = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(text, 'txt.parser')
    for line in text:
        line = line.rstrip().upper()
        print(line)
except:
    print('Python can not open the URL:', url)
