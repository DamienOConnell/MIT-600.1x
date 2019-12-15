#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:57:15 2019

@author: damien
"""

for n in range(5):
    print(n)

mysum = 0

for i in range(5,11,2):
    print("i is: " + str(i))
    mysum += i**9
    
print("mysum = ", mysum)

for i in range(5,99,2):
    print("i is: " + str(i))
    mysum += i**9
    if i == 27:
        print("Breaking .....")
        break
    
print("mysum = ", mysum)
