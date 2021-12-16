#!/usr/bin/env python3.8

"""
reduce() works by calling the function we passed for the first two items in the sequence. 
The result returned by the function is used in another call to function alongside with the next (third in this case), element.

This process repeats until we've gone through all the elements in the sequence.

The optional argument initial is used, when present, at the beginning of this "loop" with the first element in the first call to function. 
In a way, the initial element is the 0th element, before the first one, when provided.
"""

from functools import reduce

def add3(a, b, c=0):
	return a+b+c

print(reduce(add3, [1,2,3,4,5,6,7,8,9], 10))