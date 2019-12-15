#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def lessThan4(aList):
    """
    aList: a list of strings
    """
    bList = []
    for word in aList:
        if len(word) < 4:
            bList.append(word)
    return bList


aList = ["apple", "cat", "dog", "banana"]
print(lessThan4(aList))
