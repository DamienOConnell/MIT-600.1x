#!/usr/bin/env python3


def rec_multiply(x, y):
    sum = 0
    while y > 0:
        sum += x
        y -= 1
    return sum


x = 13
y = 13

print("The result is: ", rec_multiply(x, y))
