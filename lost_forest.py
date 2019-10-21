#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-

"""
Created on Mon Jun 10 13:11:46 2019

@author: damien
"""


def choice(msg: str, choices: tuple) -> str:
    response = ""
    while response not in choices:
        response = input(msg)
        print(f"selection was: {response}")
    return response


print("Entering the Lost Forest")

n = ""
while n != "right":
    n = choice("Yo is in de los fores' bro, lef or ri?", ("left", "right"))

print("you escaped the lost forest")
