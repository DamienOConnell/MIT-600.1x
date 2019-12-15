#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:20:57 2019

@author: damien
"""


def print_without_vowels(s):
    """
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    """
    newstr = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in s:
        if char not in vowels:
            newstr += char
    print(newstr)
