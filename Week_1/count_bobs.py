#!/usr/bin/env python3

# count 'bob' strings in string s

s = 'bobsillybobob'

count = 0
for i in range(len(s) - 2):
    if s[i:i+3] == 'bob':
        count += 1

print ("Number of times bob occurs is: " + str(count))
