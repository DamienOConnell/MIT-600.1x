#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def sumDigits(N):

    """
    recursive Python function, return the sum of its digits.
    """

    if N >= 10:
        return N % 10 + sumDigits(N // 10)
    else:
        return N % 10


print(sumDigits(1))
print(sumDigits(11))
print(sumDigits(126))
print(sumDigits(0))
