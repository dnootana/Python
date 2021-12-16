#!/usr/bin/env python3.8

"""
Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function. 
For example, squareroot of a number between [9, 15] should return 3, and [16, 24] should be 4.
"""

def sqrt(num1):
	i = 1
	while True:
		if num1 < i*i:
			print(i-1)
			return
		elif num1 == i*i:
			print(i)
			return
		i += 1


def sqrt1(num1):
	if num1 < 0:
		raise ValueError("Number should be greater than 0")
	elif num1==1:
		return 1

	low = 0
	high = 1 + num1//2

	while low+1 < high:
		mid = low + (high-low)//2
		print(low, high, mid)
		sq = mid**2
		if sq==num1:
			return mid
		elif sq < num1:
			low = mid
		else:
			high = mid
	return low

# sqrt(15)
print(sqrt1(15))