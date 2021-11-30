#!/usr/bin/python3.8

import random

def selection_sort_inc(A):
	"""
		it looks for smallest value for each pass, after completing the pass, it places it in the proper position
		it has O(n2) time complexity
		smaller numbers are sorted first
	"""
	for i in range(len(A)-1):
		small = i
		for j in range(i+1,len(A)):
			if(A[small] > A[j]):
				small = j
		A[i], A[small] = A[small], A[i]
	return A

def selection_sort_inc1(A):
	"""
		it looks for largest value for each pass, after completing the pass, it places it in the proper position
		it has O(n2) time complexity
		larger numbers are sorted first
	"""
	for i in range(len(A)-1,-1,-1):
		large = i
		for j in range(0,i):
			if(A[large] < A[j]):
				large = j
		A[i], A[large] = A[large], A[i]
	return A


# N = input('Enter array elements : ')
# A = list(map(int, N.split()))
# print(A)
A = [9,8,7,6,5,4,3,2,1]
random.shuffle(A)
Array = selection_sort_inc(A)
print(Array)
random.shuffle(A)
Array = selection_sort_inc1(A)
print(Array)