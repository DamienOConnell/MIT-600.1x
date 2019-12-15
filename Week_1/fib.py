#!/usr/bin/env python3


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(str(fib(1)))
print(str(fib(2)))
print(str(fib(3)))
print(str(fib(4)))
print(str(fib(5)))
print(str(fib(6)))
print(str(fib(7)))
print(str(fib(100)))
