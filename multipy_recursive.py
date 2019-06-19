#!/usr/bin/env python3


def rec_multiply(x, y):
    if y > 1:
        return x + rec_multiply(x, y - 1)
    else:
        return x


x = 65999
y = 999

print("The result is: ", rec_multiply(x, y))
