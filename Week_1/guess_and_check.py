#!/usr/bin/env python3

number = int(input("supply a value: "))
myguess = 0

while myguess ** 3 < abs(number):
    myguess += 1

if myguess ** 3 != number:
    print(f"{number} is not in fact a cube root")
else:
    print(f"The cube root of {number} is {myguess}")

