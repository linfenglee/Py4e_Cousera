# -*- coding: utf-8 -*-
"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
    
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input

"""

hour = input("Enter Hours: ")
try:
    h = float(hour)
except:
    print("Error, please enter into a number.")
    quit() # why blow up???
    
rate = input("Enter Rate: ")
try:
    r = float(rate)
except:
    print("Error, please enter into a number.")
    quit()
    
if h > 40:
    payroll = 40 * r + (h - 40) * 1.5 * r
else:
    payroll = h * r
    
print("Pay:", payroll)