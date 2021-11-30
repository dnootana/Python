#!/usr/bin/env python3.8

import copy
import random

def selection_sort_dec(array):
	"""
		it looks for largest value for each pass, after completing the pass, it places it in the proper position
		it has O(n2) time complexity
		larger numbers are sorted first
	"""
	for i in range(len(array)):
		# print(array)
		large = i
		for j in range(i+1,len(array)):
			if array[large] < array[j]:
				large = j
		array[i], array[large] = array[large], array[i]
	return array

def selection_sort_dec1(array):
	"""
		it looks for smallest value for each pass, after completing the pass, it places it in the proper position
		it has O(n2) time complexity
		smaller numbers are sorted first
	"""
	for i in range(len(array)-1,-1,-1):
		small = i
		for j in range(0,i):
			if array[small] > array[j]:
				small = j
		array[i], array[small] = array[small], array[i]
	return array

arr = [1,2,3,4,5,6,7,8,9]
random.shuffle(arr)
array = selection_sort_dec(copy.deepcopy(arr))
print(array)
random.shuffle(arr)
array = selection_sort_dec1(copy.deepcopy(arr))
print(array)