#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def score(word, f):
    import string

    alphabet = {
        letter: value + 1 for value, letter in enumerate(string.ascii_lowercase)
    }

    scores = sorted(
        index * alphabet[letter.lower()] for index, letter in enumerate(word)
    )

    # create tuple containing the top and second top scores
    first = (scores.pop(), scores.pop())
    return f(first)


print("the scores for the letters in 'adD' are 1*0, 4*1, andG 4*2")
print(score("aD", sum), " should be 4")
print(score("adD", sum), " should be 12")
print(score("adD", max), " should be 8")
print(score("adD", min), " should be 4")
print(score("zzz", sum), " should be 78")
