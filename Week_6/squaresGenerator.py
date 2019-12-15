#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#
#
def square_numbers(nums):
    # standard function that changes the list entries to their squares:
    result = []
    for i in nums:
        result.append(i * i)
    return result


def square_generator(nums):
    # convert the function above to generator version
    for i in nums:
        yield (i * i)


# initialize the list values
my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)

# reset the list values
my_nums = square_generator([1, 2, 3, 4, 5])
# now we iterate for the result:
for num in my_nums:
    print(num)

