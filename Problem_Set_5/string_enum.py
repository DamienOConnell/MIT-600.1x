#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
import string

#         A = 65
#         Z = 90
#         a = 97
#         z = 122

# ORD() IS THE REVERSE OF CHR()


def alphaDict(offset: int):

    alphabet = {
        letter: (ord(letter) + offset)
        for value, letter in enumerate(string.ascii_lowercase)
    }

    # scores = sorted(
    #     index * alphabet[letter.lower()] for index, letter in enumerate(word)
    # )
    return alphabet
    # return scores


OFFSET = 2

lowerCaseLetters = list(string.ascii_lowercase)
lowerCaseCaesar = lowerCaseLetters[:]

# fix up the lower case caesar ordering
for i in range(OFFSET):
    next = lowerCaseCaesar.pop()
    lowerCaseCaesar.insert(0, next)


upperCaseLetters = list(string.ascii_uppercase)
upperCaseCaesar = upperCaseLetters[:]

# fix up the lower case caesar ordering
for i in range(OFFSET):
    next = upperCaseCaesar.pop()
    upperCaseCaesar.insert(0, next)

alphaList = []
alphaCaesar = []

alphaList += lowerCaseLetters
alphaList += upperCaseLetters

alphaCaesar += lowerCaseCaesar
alphaCaesar += upperCaseCaesar

print("DEBUG ALPHABET - ORIGINAL")
print(alphaList)

print("DEBUG ALPHABET - CAESAR")
print(alphaCaesar)

caesarDict = {}
caesarDict = {letter: value for letter, value in zip(alphaList, alphaCaesar)}

print("DEBUG: ALPHABET MAPPING MY LETTER TO ITS CAESAR CIPHER")
print(caesarDict)

# caesarDict = {letter: value for letter, value in zip(lowerCaseLetters, lowerCaseCaesar)}

# print(caesarDict)
