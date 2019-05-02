# -*- coding: utf-8 -*-
"""
Exercise 4: Assume that we execute the following assignment statements:
    
width = 17
height = 12.0

For each of the following expressions, write the value of the expression and the
type (of the value of the expression).

1. width//2
2. width/2.0
3. height/3
4. 1 + 2 * 5

Use the Python interpreter to check your answers.

"""

width = 17
height = 12.0

a = width//2
b = width/2.0
c = height/3
d = 1 + 2 * 5

for i in [a,b,c,d]:
    print('Value:', i, 'Type:', type(i)) 
    # how to add a, b, c, d into the print function
    
    