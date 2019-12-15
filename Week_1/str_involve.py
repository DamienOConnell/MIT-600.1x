#!/usr/bin/env python3

# 1 "string involved:"
varA = 4
varB = "adieu"

# 2 "string involved"
varA = hola, varB = hola


if (type(varA) == str) or (type(varB) == str):
    print("string involved")
elif (type(varA) == int) and (type(varB) == int):
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")

