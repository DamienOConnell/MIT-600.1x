#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def myLog(x, b):
    """
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    """
    power = 0
    wip = b
    while wip <= x:
        power += 1
        wip = wip * b
    return power


print("return 2")
print(myLog(15, 3))
print("return 4")
print(myLog(16, 2))
