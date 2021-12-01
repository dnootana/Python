#!/usr/bin/env python3.8

import random
import copy

def quick_sort_inc(arr, start, end):
	"""
		
	"""
	if start < end:
		q = partition(arr, start, end)
		quick_sort_inc(arr, start, q-1)
		quick_sort_inc(arr, q+1, end)
	return arr

def partition(arr, start, end):
	x = arr[end]
	i = start -1
	print(arr)
	for j in range(start, end):
		if arr[j] >= x:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[end] = arr[end], arr[i+1]
	print(arr)
	return i+1

arr = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(arr)
arr.reverse()
array = quick_sort_inc(copy.deepcopy(arr), 0, len(arr)-1)
print(array)