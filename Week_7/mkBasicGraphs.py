#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):

    mySamples.append(i)
    myLinear.append(i * 1.3)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.3 ** i)

# first graph trial
#


plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)
