#!/usr/bin/env python3

# example of square root using bisection search

x = 27
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 3 - x) >= epsilon:
    print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    if ans ** 3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to cube root of " + str(x))
