#!/usr/bin/env python3.8
"""
Given a list of integers, find the largest product you could make from 3 integers in the list
"""
def largestProduct(A):
	high = max(A[0], A[1])
	low = min(A[0], A[1])
	prod2min = low*high
	prod2max = low*high

	prod3max = A[0]*A[1]*A[2]

	for val in A[2:]:
		prod3max = max(prod3max, prod2min*val, prod2max*val)

		prod2min = min(prod2min, low*val, high*val)
		prod2max = max(prod2max, low*val, high*val)

		low = min(low, val)
		high = max(high, val)
	return prod3max

A_list = [99, -82, 82, 40, 75, -24, 39, -82, 5, 30, -25, -94, 93, -23, 48, 50, 49, -81, 41, 63]
max_prod = largestProduct(A_list)
print(max_prod)


print(solution(A_list))