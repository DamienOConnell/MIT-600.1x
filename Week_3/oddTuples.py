#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def oddTuples(aTup):

    newList = []
    i = 0
    for entry in aTup:
        i += 1
        if i % 2 == 1:
            newList.append(entry)
    return tuple((newList))


tTup = ("I", "am", "a", "test", "tuple")
print("tuple - tTup - BEFORE:\t", tTup)
print("tuple - tTup - AFTER:\t", oddTuples(tTup))
print(type(oddTuples(tTup)))
