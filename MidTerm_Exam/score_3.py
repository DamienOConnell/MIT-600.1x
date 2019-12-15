#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def score(word, f):
    def letter_score(letter, position):
        letter_value = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,
            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,
            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26,
        }
        return letter_value[letter.lower()] * position

    scores = []
    for i in range(len(word)):
        scores.append(letter_score(word[i], i))

    scores.sort()
    highest = []
    highest.append(scores.pop())
    highest.append(scores.pop())
    return f(highest)


print("the scores for the letters in 'adD' are 1*0, 4*1, andG 4*2")
print(score("aD", sum), " should be 4")
print(score("adD", sum), " should be 12")
print(score("adD", max), " should be 8")
print(score("adD", min), " should be 4")
print(score("aDdfz", sum), " should be 122")
