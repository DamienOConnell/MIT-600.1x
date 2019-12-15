#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-

"""
Explanation:
In the best case scenario, L is an empty list.
Thus we execute only the first two assignment statements, then the return statement.
Therefore in the best case we execute 3 steps
Note that since the list is empty, no assignments are performed in the for x in L lines.
In the worst case scenario, L is a list with its elements sorted in increasing order (eg, [1, 3, 5, 7, ...])
In this case we execute the first two assignment statements (2 steps)
Next we execute the first loop n times.
This first loop has three steps (one for the assignment of x each time through the loop, as well as two for the += operation), adding 3*n steps.
Finally we execute the second loop n times
The first time we execute this loop, we perform 3 steps - one for the assignment of x; then we run the check if highestFound == None, and finding it to be True, we execute the assignment highestFound = x.
The next (n-1) times we execute this loop, we perform 4 steps: one for the assignment of x, then we run the check if highestFound == None, and finding it to be False, we run the check elif x > highestFound
Since this is always True (the list is sorted in increasing order), we execute the assignment highestFound = x
Therefore in the second loop we execute 3 + (n-1)*4 = 3 + 4*n - 4 = 4*n - 1 steps.
Finally we execute the return statement, which is one more step.
Pulling this all together, we can see that in the worst case we execute 2 + 3*n + 4*n - 1 + 1= 7*n + 2 steps.
"""


def program3(L):
    totalSum = 0  # 1
    highestFound = None  # 1
    for x in L:  # n
        totalSum += x  # n

    for x in L:  # n
        if highestFound == None:  #   1
            highestFound = x  #
        elif x > highestFound:  #
            highestFound = x  #

    return (totalSum, highestFound)  #
