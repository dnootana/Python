#!/usr/bin/env python3.8
"""

"""
import random

def dice7():
	return random.randint(1, 7)

def dice7to5():
	roll = 7

	while roll > 5:
		roll = dice7()
		print("dice7 produced a roll of ", roll)

	print(roll)

# dice7to5()

