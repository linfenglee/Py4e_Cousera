# -*- coding: utf-8 -*-
"""
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.

"""

import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ') # http://data.pr4e.org/romeo.txt
fhand = urllib.request.urlopen(url, context=ctx).read()
# Why here we need to transfer bytes format to Unicode format???
if type(fhand) is bytes:
    fhand = str(fhand, encoding = 'utf8')
    
count = 0
for line in fhand:
    for c in line:
        if count < 3000:
            print(c, end = '')
        count = count + 1

print('\n\nThere are {} characters in this documet.'.format(count))
# There are 8864 characters in this documet
# Means it ignores the header!