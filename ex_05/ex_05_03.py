# -*- coding: utf-8 -*-
"""
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.

"""

ma = None
mi = None

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try:
        inp = float(inp)
    except:
        print("Invalid Input")
        continue
    if ma is None:
        ma = inp
    elif ma < inp:
        ma = inp  
    if mi is None:
        mi = inp
    elif mi > inp:
        mi = inp
print("Maximum Number:", ma, "Minimum Number:", mi)