#!/usr/bin/env python3

# -*- coding: utf-8 -*-

numFibCalls = 0


def fib(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib(n - 1, d) + fib(n - 2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}

# print("fib(1) is: ", fib(1, d))
# print("fib(2) is: ", fib(2, d))
# print("fib(3) is: ", fib(3, d))
# print("fib(34) is: ", fib(34, d))
print("fib(34) is: ", fib(34, d))
print("fib(999) is: ", fib(999, d))


print("fib() was called: ", str(numFibCalls), " times.")
