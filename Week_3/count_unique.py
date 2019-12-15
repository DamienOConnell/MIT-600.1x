#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def count_unique(a: str, b: str) -> int:
    newstr = ""
    for word in a, b:
        for char in word:
            if char not in newstr:
                newstr += char
    return len(newstr)


# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"
print("should be 5:\t", count_unique("apple", "play"))
print("should be 7:\t", count_unique("sore", "zebra"))
print("should be 5:\t", count_unique("a", "soup"))
