#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#


def is_list_permutation(L1, L2):
    """
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    """

    list_items = {}

    if len(L1) != len(L2):
        return False

    if len(L1) == 0:
        return (None, None, None)

    for item in L1:
        if item not in L2:  # lists don't contain the same items
            return False

        # add to the list_items tracking dictionary:
        elif list_items.get(item):
            list_items[item] += 1
        else:
            list_items[item] = 1
        L2.remove(item)

    # find key with biggest value in the dictionary
    for thing in list_items:
        if list_items[thing] == max(list_items.values()):
            return (thing, max(list_items.values()), type(thing))


def main():

    L1 = ["a", "a", "b"]
    L2 = ["a", "b"]
    print("is_list_permutation should return: False")
    print(is_list_permutation(L1, L2))

    L1 = [1, "b", 1, "c", "c", 1]
    L2 = ["c", 1, "b", 1, 1, "c"]
    print("is_list_permutation should return: (1, 3, <class 'int'>)")
    print(is_list_permutation(L1, L2))

    # because the integer 1 occurs the most, 3 times, and the type of 1 is an integer
    # (note that the third element in the tuple is not a string).
    print("problem areas " + "=" * 55)

    print("\nShould return: (None, None, None)")
    print(is_list_permutation([], []))

    print("\nShould return:  False")
    print(is_list_permutation([1, 2, 1], [2, 1, 2]))

    print("\n Should return: ('a', 2, <class 'str'>)")
    print(is_list_permutation(["1", "2", "a", "a"], ["2", "a", "1", "a"]))

    print("\nShould return: ('5', 2, <class 'str'>)")
    print(is_list_permutation([3, "5", "5", 7, 1, 2], [1, 2, "5", 7, 3, "5"]))

    print("\nShould return:  False")
    print(
        is_list_permutation(
            [0, 4, 8, 3, 0, 2, 2, 1, 4, 7, 8, 3, 7, 0, 0],
            [3, 4, 0, 3, 8, 0, 2, 0, 7, 2, 0, 3, 7, 2, 1],
        )
    )


if __name__ == "__main__":
    main()
