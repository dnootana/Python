#!/usr/bin/env python3.8

import copy
import random

def bubbleSort_decr(array):
	"""
		It repeatedly swaps adjacent elements that are out of order
		it has O(n2) time complexity
		smaller numbers are sorted first
	"""
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] < array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array

def bubbleSort_decr1(array):
	"""
		It repeatedly swaps adjacent elements that are out of order
		it has O(n2) time complexity
		larger numbers are sorted first
	"""
	for i in range(len(array)):
		for j in range(len(array)-1,i,-1):
			if array[j-1] < array[j]:
				array[j], array[j-1] = array[j-1], array[j]
	return array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(arr)
array = bubbleSort_decr(copy.deepcopy(arr))
print(array)
random.shuffle(arr)
array = bubbleSort_decr1(copy.deepcopy(arr))
print(array)