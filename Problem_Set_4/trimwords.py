#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-

MODULUS = 25  # fraction of original words that will be retained


def main():
    count = 0
    lw = open("littlewords.txt", "w")
    with open("words.txt", "r") as fd:
        for line in fd:
            count += 1
            print(line)
            if count % MODULUS == 0:
                lw.write(line)
    lw.close()


if __name__ == "__main__":
    main()
