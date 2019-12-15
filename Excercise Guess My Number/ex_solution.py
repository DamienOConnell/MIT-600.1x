#!/usr/bin/env python3

# Exercise 2 submitted solution
low = 0
high = 100
guess = (high + low) // 2

print("Please think of a number between 0 and 100!")


while high != low:
    question = "Is your secret number " + str(guess) + "?"
    print(question)
    response = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to "
        "indicate the guess is too low. Enter 'c' to indicate I guessed "
        "correctly. "
    )

    if response == "l":
        low = guess
        guess = (high + low) // 2
    elif response == "h":
        high = guess
        guess = (high + low) // 2
    elif (response == "c") or (high == low):
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")

