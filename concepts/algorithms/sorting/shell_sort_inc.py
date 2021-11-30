#!/usr/bin/env python3.8

import random
import copy

def shell_sort_inc(arr):
	"""
		The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared. 
		By starting with far apart elements, it can move some out-of-place elements into position faster than a simple nearest neighbor exchange
	"""
	sublist_len = len(arr) // 2
	while sublist_len > 0:
		for start in range(sublist_len):
			gap_insertion_sort(arr, start, sublist_len)
		sublist_len //= 2
	return arr

def gap_insertion_sort(arr, start, gap):
	for i in range(start + gap, len(arr), gap):
		currentValue = arr[i]
		position = i - gap
		while (position>=0 and arr[position] > currentValue):
			arr[position+gap] = arr[position]
			position -= gap
		arr[position + gap] = currentValue

arr = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(arr)
arr.reverse()
print(len(arr))
array = shell_sort_inc(copy.deepcopy(arr))
print(array)