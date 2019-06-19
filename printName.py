#!/usr/bin/env python3


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName, firstName)
    else:
        print(firstName, lastName)


printName("eric", "grimson", False)
printName("eric", "grimson", True)
printName("eric", "grimson", reverse=False)
printName(firstName="eric", lastName="grimson", reverse=True)
printName(lastName="grimson", firstName="eric", reverse=False)
printName("eric", lastName="grimson", reverse=True)
# this one doesnt' work, positional follows keyword argument:
# printName(firstName="eric", "grimson", reverse=True)
