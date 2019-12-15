#!/usr/bin/env python3


s = input("give me a string? ")

vowels = ["a", "e", "i", "o", "u"]
count = 0
for char in s:
    if char in vowels:
        count += 1

print("Number of vowels: " + str(count))
