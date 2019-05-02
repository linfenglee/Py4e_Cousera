# -*- coding: utf-8 -*-
"""
Exercise 5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.

Formula: Fahrenheit temperature = 32F + 1.8 * Celsius temperature

"""

ct = input('Please enter Celsius temperature: ')
try:
    ctem = float(ct)
except:
    print('Invalid Input')
    
ftem = 32 + 1.8 * ctem

print('Fahrenheit temperature:', round(ftem, 1))



