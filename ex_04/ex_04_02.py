# -*- coding: utf-8 -*-
"""
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
 < 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.
"""

def computegrade(score):
    try:
        if score < 0:
            print('Bad Score')
        elif score < 0.6:
            print('F')
        elif score < 0.7:
            print('D')
        elif score < 0.8:
            print('C')
        elif score < 0.9:
            print('B')
        elif score <= 1.0:
            print('A')
        else:
            print('Bad Score')
    except:
        print('Bad Score')