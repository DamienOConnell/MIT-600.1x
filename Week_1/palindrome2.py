#!/usr/bin/env python3


def isPalindrome(word):

    """
    First - remove whitespace, make word lowercase
    """

    def toChars(s):
        chars = "abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        for c in s:
            if c in chars:
                s += c
        return s

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(toChars(s[1:-2]))

    return isPal(toChars(word))


def main():

    print(isPalindrome(""), " expect - True")
    print(isPalindrome("aA"), " expect -True")
    print(isPalindrome("G   lEne lg"), " expect - True")
    print(isPalindrome("aEcba"), " expect - False")
    print(isPalindrome("abcdbba"), " expect - False")


if __name__ == "__main__":
    main()
