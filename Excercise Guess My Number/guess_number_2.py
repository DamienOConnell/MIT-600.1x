#!/usr/bin/env python3

initial_question = "Please think of a number between 0 and 100!"
is_it = "Is your secret number "
instructions = (
    "Enter 'h' to indicate the guess is too high. Enter 'l' to "
    "indicate the guess is too low. Enter 'c' to indicate I guessed "
    "correctly. "
)
guessed_it = "Game over. Your secret number was: "


numGuesses = 0
secret = 99

low = 0
high = 100
guess = (high + low) // 2

while guess != secret:
    print("low = " + str(low) + " high = " + str(high) + " guess = " + str(guess))
    numGuesses += 1
    if guess < secret:
        low = guess
    else:
        high = guess
    guess = (high + low) // 2

print("numGuesses was " + str(numGuesses))
print( guessed_it  + str(guess))

