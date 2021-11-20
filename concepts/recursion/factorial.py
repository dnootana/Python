#!/usr/bin/env python3.8

"""
given a number N generate factorial of N
"""
from memoize import memoize

def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num-1)

factorial = memoize(factorial)
print(factorial(44))
print(factorial(44))