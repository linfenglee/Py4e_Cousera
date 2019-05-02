# -*- coding: utf-8 -*-
"""
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

"""

hour = input("Enter Hours: ")
#try:
#    hour = float(hour)
#except:
#    print("Error, please enter into a number.")
rate = input("Enter Rate: ")
#try:
#    rate = float(rate)
#except:
#    print("Error, please enter into a number.")
#    quit()

if float(hour) > 40:
    payroll = 40 * float(rate) + (float(hour) - 40) * 1.5 * float(rate)
else:
    payroll = float(hour) * float(rate)
    
print("Pay:", round(payroll, 2))

