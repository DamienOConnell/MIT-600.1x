#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def dict_invert(d):
    newdict = {}
    for key in d.keys():
        # this value has been seen before
        if d[key] in newdict:
            newdict[d[key]].append(key)
            newdict[d[key]].sort()
        else:
            newdict[d[key]] = []
            newdict[d[key]].append(key)
    return newdict


d = {1: 10, 2: 20, 3: 30}
print(dict_invert(d))
print("{10: [1], 20: [2], 30: [3]}   -- should be ")
print("-" * 80)


d = {1: 10, 2: 20, 3: 30, 4: 30}
print(dict_invert(d))
print("{10: [1], 20: [2], 30: [3, 4]} --- should be")
print("-" * 80)

d = {4: True, 2: True, 0: True}
print(dict_invert(d))
print("{True: [0, 2, 4]} -- should be")
print("-" * 80)
