#!/usr/bin/env python3.8

"""
Given a list of integers, write a function that will return a list, in which for each index the element will be the product of all the integers except for the element at that index

For example, an input of [1,2,3,4] would return [24,12,8,6] by performing [2×3×4,1×3×4,1×2×4,1×2×3]

"""

import copy

def resultList(O_list):
	"""
	time complexity : O(n)
	"""
	prod = 1
	for i in O_list:
		prod *= i
	for i in range(len(O_list)):
		O_list[i] = prod // O_list[i]
	print(O_list)

def resultList1(O_list):
	"""
	time complexity : O(n2)
	"""
	A_list = [1]*len(O_list)
	for i in range(len(O_list)):
		for j in range(len(O_list)):
			if i!=j:
				A_list[i] *= O_list[j]
	print(A_list)

def resultList2(O_list):
	"""
	time complexity : O(n)
	"""
	A_list = [None]*len(O_list)
	i = 0
	product =1
	while i < len(O_list):
		A_list[i] = product
		product *= O_list[i]
		i += 1
	product = 1
	i = len(O_list) - 1
	while i>=0:
		A_list[i] *= product

		product *= O_list[i]
		i -= 1 
	print(A_list)

A = [1, 2, 3, 4]
resultList(copy.deepcopy(A))
resultList1(copy.deepcopy(A))
resultList2(copy.deepcopy(A))