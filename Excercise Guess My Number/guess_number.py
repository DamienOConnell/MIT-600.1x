#!/usr/bin/env python3

initial_question = "Please think of a number between 0 and 100!"
is_it = "Is your secret number "
instructions = (
    "Enter 'h' to indicate the guess is too high. Enter 'l' to "
    "indicate the guess is too low. Enter 'c' to indicate I guessed "
    "correctly. "
)
guessed_it = "Game over. Your secret number was: "


# guess = 50
# print(initial_question)
# print(is_it + str(guess) + "?")
# found = false
# while not found:
#     response = input(instructions)
#     if response == "c":
#         print(guessed_it + str(guess))
#     elif response == "l":
#         guess = guess_again(guess
numGuesses = 0
secret = 30

low = 0
high = 100
guess = (high + low) // 2


while guess != secret:
    print("low = " + str(low) + " high = " + str(high) + " guess = " + str(guess))
    # numGuesses += 1
    if guess < secret:
        low = guess
    else:
        high = guess
    guess = (high + low) // 2.0


print("numGuesses was " + str(numGuesses))
