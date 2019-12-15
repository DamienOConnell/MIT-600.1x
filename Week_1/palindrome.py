#!/usr/bin/env python3


def isPalindrome(word):

    """ First
          - remove whitespace from word
          - make word lowercase
    """
    word = word.strip().lower()

    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        if isPalindrome(word[1:-1]):
            return True
    return False


def main():

    print(isPalindrome(""), " expect - True")
    print(isPalindrome("aA"), " expect -True")
    print(isPalindrome("G   lEne lg"), " expect - True")
    print(isPalindrome("aEcba"), " expect - False")
    print(isPalindrome("abcdbba"), " expect - False")


if __name__ == "__main__":
    main()
