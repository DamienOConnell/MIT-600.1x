#!/usr/bin/env python3

from pprint import pprint


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


songWords = {}
with open("she-loves-you.txt", mode="r", encoding="utf-8") as file:

    song = file.read()

    for word in song.split():

        word = word.lower().strip(",")
        if word in songWords:
            songWords[word] += 1
        else:
            songWords[word] = 1

# pprint(songWords)
# sort the resulting dict
sorted_d = sorted(songWords.items(), key=lambda x: x[1], reverse=True)

pprint(sorted_d)
print("-" * 80)

topWord, topFreq = most_common_words(songWords)
print("Commonest word is: ", topWord, "Top frequency is: ", topFreq)
print("-" * 80)
print()
