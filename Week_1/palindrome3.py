#!/usr/bin/env python3


def isPalindrome(word):

    """ First
        - remove whitespace from word
        - make word lowercase
    """

    def chkPal(word: str):
        if len(word) <= 1:
            return True

        return word[0] == word[-1] and chkPal(word[1:-1])

    return chkPal(word.strip().lower())


def main():

    print(isPalindrome(""), " expect - True")
    print(isPalindrome("aA"), " expect -True")
    print(isPalindrome("G   lEne lg"), " expect - True")
    print(isPalindrome("aEcba"), " expect - False")
    print(isPalindrome("abcdbba"), " expect - False")
    print(isPalindrome("Able was I ere I saw Elba"), " expect - True")


if __name__ == "__main__":
    main()
