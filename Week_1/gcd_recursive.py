#!/usr/bin/env python3


def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

    If b = 0, then the answer is a

    Otherwise, gcd(a, b) is the same as gcd(b, a % b)
    """

    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


if __name__ == "__main__":

    print(str(gcdRecur(2, 12)), " should be: 2")
    print(str(gcdRecur(6, 12)), " should be: 6")
    print(str(gcdRecur(9, 12)), " should be: 3")
    print(str(gcdRecur(17, 12)), " should be: 1")
