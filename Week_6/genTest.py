#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:10:30 2019

@author: damien
"""

def genTest():
    yield 1
    yield 2

foo = genTest()
foo.netxt()