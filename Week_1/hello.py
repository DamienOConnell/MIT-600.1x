# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

ans = 0
x = int(input('what number to check? '))
while ans**3 < abs(x):
    ans+=1


if ans**3 == abs(x):
    if x < 0:
        ans = -ans
    print(f'x: {x} does indeed have a cube root and it is {ans}')
else:
    print(f'x: {x} does not have a cube root')
        