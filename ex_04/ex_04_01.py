# -*- coding: utf-8 -*-
"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
and create a function called computepay which takes two parameters
(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

"""

def computepay(hour, rate):
    if type(hour) is str or type(rate) is str or hour < 0 or rate < 0:
        print('Invalid Input')
        quit()
    if hour > 40:
        payroll = 40 * rate + (hour - 40) * rate * 1.5
    else:
        payroll = hour * rate
    print('Payment:', payroll)
