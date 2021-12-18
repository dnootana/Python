#!/usr/bin/env python3.8
from functools import reduce

def coinChange(m, c):
	prod = reduce(lambda x, y: x+y, c)
	rem = m / prod
	print(rem)

money = 100
change = [1, 2, 3]
coinChange(money, change)