#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    answer = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            answer += letter
        else:
            answer += "_"
    return answer


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    unused = ""
    for letter in alphabet:
        if letter not in lettersGuessed:
            unused += letter
    return unused


secretWord = "apple"
lettersGuessed = ["e", "i", "k", "p", "r", "s"]
print(isWordGuessed(secretWord, lettersGuessed), " should return False")
print(getGuessedWord(secretWord, lettersGuessed), " should return False")

lettersGuessed = ["e", "l", "p", "a"]
print(isWordGuessed(secretWord, lettersGuessed), " should return True")
print(getGuessedWord(secretWord, lettersGuessed), " should return True")


lettersGuessed = ["e", "i", "k", "p", "r", "s"]
print("should return: abcdfghjlmnoqtuvwxyz")
print(getAvailableLetters(lettersGuessed))
