#!/usr/bin/python3.8

import copy
import random

def insertion_sort_dec(A):
	"""
		insertion sort always maintains a sorted sublist 
		it has O(n2) time complexity
		sorted sublist is in the lower positions of the list
	"""
	for i in range(1,len(A)):
		key = A[i]
		j = i - 1
		while j >= 0 and A[j] < key:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key
	return A

def insertion_sort_dec1(A):
	"""
		insertion sort always maintains a sorted sublist 
		it has O(n2) time complexity
		sorted sublist is in the higher positions of the list
	"""
	for i in range(len(A)-2, -1, -1):
		key = A[i]
		j = i + 1
		while j < len(A) and A[j] > key:
			A[j-1] = A[j]
			j += 1
		A[j-1] = key
	return A

# N = input('enter numbers : ')
# A = N.split()
# print(A)

arr = [9,8,7,6,5,4,3,2,1]
random.shuffle(arr)
array = insertion_sort_dec(copy.deepcopy(arr))
print(array)
random.shuffle(arr)
array = insertion_sort_dec1(copy.deepcopy(arr))
print(array)