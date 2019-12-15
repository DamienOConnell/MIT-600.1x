#!/usr/bin/env python3

import sys
number = int(input("supply a value: "))
guess = 0

for guess in range(number + 1):
    if guess ** 3 == number:
        print(f"The cube root of {number} is {guess}")
        sys.exit()
print(f"{number} is not in fact a cube root")

# while myguess ** 3 < abs(number):
#     myguess += 1

# if myguess ** 3 != number:
#     print(f"{number} is not in fact a cube root")
# else:
#     print(f"The cube root of {number} is {myguess}")
