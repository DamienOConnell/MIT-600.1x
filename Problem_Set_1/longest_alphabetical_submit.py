#!/usr/bin/env python3

print("answer should be begg")
s = "azcbobobegghakl"


def longest(s):
    substring = s[0]
    for i in range(len(s) - 1):
        if s[i] <= s[i + 1]:
            substring += s[i + 1]
        else:
            return substring
    return substring


last_ix = len(s) - 1
longest_so_far = ""
for i in range(last_ix):
    if len(longest(s[i:])) > len(longest_so_far):
        longest_so_far = longest(s[i:])


print("Longest substring in alphabetical order is: " + longest_so_far)
