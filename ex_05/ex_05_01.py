# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:58:34 2019

@author: Administrator
"""

count = 0
total = 0

while True:
    inp = input("Enter a number: ")
    try:
        inp = float(inp)
        count = count + 1
        total = total + inp
    except:
        if inp == "done":
            break
        print("Invalid Input")
        
print("Total:", total, "Count:", count, "Average:", total/count)
    