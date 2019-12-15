#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
import string

#         A = 65
#         Z = 90
#         a = 97
#         z = 122

# ORD() IS THE REVERSE OF CHR()


def build_shift_dict(shift: int):
    """ return a dictionary that maps all upper and lower alphabet letters
    mapped to their Caesar cipher, shift by 'shift' characters
    """

    lowerCaseLetters = list(string.ascii_lowercase)
    lowerCaseCaesar = lowerCaseLetters[:]

    upperCaseLetters = list(string.ascii_uppercase)
    upperCaseCaesar = upperCaseLetters[:]

    # shift lower case for Caesar ordering
    for i in range(shift):
        next = lowerCaseCaesar.pop()
        lowerCaseCaesar.insert(0, next)

    # shift upper case for Caesar ordering
    for i in range(shift):
        next = upperCaseCaesar.pop()
        upperCaseCaesar.insert(0, next)

    alphaList = lowerCaseLetters + upperCaseLetters
    alphaCaesar = lowerCaseCaesar + upperCaseCaesar

    caesarDict = {letter: value for letter, value in zip(alphaList, alphaCaesar)}

    return caesarDict


print(build_shift_dict(2))
print("-" * 80)
print(build_shift_dict(24))
print("-" * 80)
print(build_shift_dict(26))
print("-" * 80)
print(build_shift_dict(53))
print("-" * 80)
