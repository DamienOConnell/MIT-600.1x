#!/usr/bin/env python3

number = int(input("supply a value: "))
guess = 0

for guess in range(abs(number) + 1):
    if guess ** 3 >= abs(number):
        break

if guess ** 3 != abs(number):
    print(f"{number} is not in fact a cube root")
else:
    if number < 0:
        guess = -guess
    print(f"The cube root of {number} is {guess}")
