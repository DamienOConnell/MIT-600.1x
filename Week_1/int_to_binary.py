#!/usr/bin/env python3

entered = int(input("enter a number to convert to binary:  "))
num = entered

if num < 0:
    isNeg = True
else:
    isNeg = False

num = abs(num)
result = ""

if num == 0:
    result = 0
while num > 0:
    result = str(num % 2) + result
    num = num // 2
    print("num so far: ", result, " num is now ", num)

if isNeg:
   result = '-' + result
print("Integer: ", entered, " yields binary: ", result)
