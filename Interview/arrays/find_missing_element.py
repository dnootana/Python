#!/usr/bin/env python3.8

def missing_element(arr1, arr2):
	arr1.sort()
	arr2.sort()

	for num1, num2 in zip(arr1, arr2):
		if num1 != num2:
			return num1

	return -1

def missing_element1(arr1, arr2):
	count = {}
	output = []
	for i in arr1:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1

	for i in arr2:
		if i in count:
			count[i] -= 1
		else:
			count[i] = -1

	for k in count:
		if count[k] > 0:
			output.append(k)

	return output

import collections
def missing_element2(arr1, arr2):
	count = collections.defaultdict(int)
	output = []
	for i in arr2:
			count[i] += 1

	for i in arr1:
		if count[i] == 0:
			output.append(i)
		else:
			count[i] -= 1

	return output

def missing_element3(arr1, arr2):
	return sum(arr1) - sum(arr2)

def missing_element4(arr1, arr2):
	result = 0

	for num in arr1+arr2:
		result ^= num

	return result

arr1 = [5,5,7,7]
arr2 = [5,7,7]

print(missing_element4(arr1,arr2))

print( ord("A")^ord("A"))