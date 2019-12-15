#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#


def dict_interdiff(d1, d2, f):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    difference{} -
      (a) every key-value pair in d1 whose key appears only in d1 and not in d2
      (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
    """
    intersect = {}
    difference = {}
    for item in d1:
        if item in d2:
            intersect[item] = f(d1[item], d2[item])
        else:
            # it's not there, add it to the difference dict
            difference[item] = d1[item]

    for item in d2:
        if item not in d1:
            difference[item] = d2[item]

    return (intersect, difference)


def main():

    print("\n\n--- Example 1: ---------------------")

    def f(a, b):
        return a + b

    d1 = {1: 30, 2: 20, 3: 30, 5: 80}
    d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}
    print("Should return:")
    print("({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})")
    print(dict_interdiff(d1, d2, f))

    print("\n\n--- Example 2: ---------------------")

    def f(a, b):
        return a > b

    d1 = {1: 30, 2: 20, 3: 30}
    d2 = {1: 40, 2: 50, 3: 60}
    print("Should return:")
    print("({1: False, 2: False, 3: False}, {})")
    print(dict_interdiff(d1, d2, f))


if __name__ == "__main__":
    main()
