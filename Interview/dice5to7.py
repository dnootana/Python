#!/usr/bin/env python3.8

"""
Given a dice which rolls from 1 to 5, simulate a uniform 7 sided dice!
"""

import random

def dice5():
	return random.randint(1, 5)

def dice5to7():
	while True:
		roll1 = dice5()
		roll2 = dice5()

		num = (roll1-1)*5 + (roll2)
		if num > 21:
			continue
		print(num % 7 + 1)
		return

dice5to7()

# for i in range(1, 6):
# 	for j in range(1, 6):
# 		num = (i-1)*5 + (j)
# 		if num > 21:
# 			continue
# 		print(i, j, num, num % 7 + 1)