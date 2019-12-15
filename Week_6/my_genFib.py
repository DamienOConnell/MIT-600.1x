#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#


def genFib():
    fibn_1 = 1   # fib(n-1)
    fibn_2 = 2   # fib(n-2)

    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next          # generator yields for base case
        fibn_2 = fibn_1
        fibn+1 = next

