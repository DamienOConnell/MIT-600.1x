#!/usr/bin/env python3


y = float(input("enter an integer to find the square root of? "))
guess = y / 2.0  # our starting point

epsilon = 0.01  # how close an acceptable answer should be
numGuesses = 0

while abs(guess * guess - y) >= epsilon:
    print("I guess ", str(guess))
    numGuesses += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))

print("I guess ", str(guess), " this took ", str(numGuesses), " guesses.")
