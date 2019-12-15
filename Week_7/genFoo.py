#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#
# A simple generator that returns two values
#


def genFoo():
    yield 1
    yield 2


>>> foo = genFoo.genFoo()

>>> foo.__next__()
    1

>>> foo.__next__()
    2

>>> foo.__next__()
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-6-5d994c17f9ca> in <module>
