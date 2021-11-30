#!/usr/bin/env python3.8

import random
import copy

def bubbleSort_inc(array):
	"""
		It repeatedly swaps adjacent elements that are out of order
		it has O(n2) time complexity
		larger numbers are sorted first
	"""
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array

def bubbleSort_inc1(array):
	"""
		It repeatedly swaps adjacent elements that are out of order
		it has O(n2) time complexity
		smaller numbers are sorted first
	"""
	for i in range(len(array)):
		for j in range(len(array)-1,i,-1):
			if array[j-1] > array[j]:
				array[j], array[j-1] = array[j-1], array[j]
	return array

arr = [9,8,7,6,5,4,3,2,1]
random.shuffle(arr)
array = bubbleSort_inc(copy.deepcopy(arr))
print(array)
random.shuffle(arr)
array = bubbleSort_inc1(copy.deepcopy(arr))
print(array)