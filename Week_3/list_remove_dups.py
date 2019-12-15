#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def remove_dup1(V1, L2):
    # use L1copy to iterate over L1, without issues when L1 elemenmts removed
    L1copy = L1[:]
    for e in L1copy:
        if e in L2:
            L1.remove(e)
    return L1


def remove_dup2(V1, L2):
    # iterate a copy [:] of L1 without the intermediate variable
    for e in L1[:]:
        if e in L2:
            L1.remove(e)
    return L1


def remove_dup2(V1, L2):
    for e in L1[:]:
        if e in L2:
            L1.remove(e)
    return L1


L1 = [1, 2, 5, 6, 7]
L2 = [0, 2, 8, 6, 9]

print("Remove remove 2 and 6, from L1 only?")
print("L1 before is: ", L1)
remove_dup1(L1, L2)
print("L1 after is: ", L1)

print("." * 80)


L1 = [1, 2, 5, 6, 7]
L2 = [0, 2, 8, 6, 9]

print("Remove remove 2 and 6, from L1 only?")
print("L1 before is: ", L1)
remove_dup2(L1, L2)
print("L1 after is: ", L1)

print("." * 80)
