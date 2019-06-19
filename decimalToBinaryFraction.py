#!/usr/bin/env python3

0.37  # -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:13:04 2016

@author: ericgrimson
"""

x = float(input("Enter a decimal number between 0 and 1: "))

p = 0

# how many bits will I need to shift?
while ((2 ** p) * x) % 1 != 0:          # while there is still a remainder
    print("Remainder = " + str((2 ** p) * x - int((2 ** p) * x)), " p is: ", p)
    p += 1
print("p is: ", p)

num = int(x * (2 ** p))

result = ""
if num == 0:
    result = "0"
while num > 0:
    result = str(num % 2) + result
    num = num // 2

for i in range(p - len(result)):
    result = "0" + result

result = result[0:-p] + "." + result[-p:]
print("The binary representation of the decimal " + str(x) + " is " + str(result))
