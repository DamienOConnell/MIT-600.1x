#!/usr/bin/env python3


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def main():
    print("factorial 1 is ", str(factorial(1)))
    print("factorial 2 is ", str(factorial(2)))
    print("factorial 3 is ", str(factorial(3)))
    print("factorial 4 is ", str(factorial(4)))
    print("factorial 5 is ", str(factorial(5)))
    print("factorial 600 is ", str(factorial(600)))


if __name__ == "__main__":
    main()
