#!/usr/bin/env python3.8

def binary_search(arr, key):
	"""
		binary seach using iterative method
	"""
	first = 0
	last = len(arr)-1
	found = False

	while first <= last and not found:
		mid = (first + last) // 2
		if arr[mid] == key:
			found = True
		else:
			if arr[mid] > key :
				last = mid -1
			else:
				first = mid + 1
	return found

def binary_search1(arr, key):
	"""
		binary search using recursive method
	"""
	if len(arr) > 0:
		mid = len(arr)//2
		if key == arr[mid]:
			return True
		else:
			if arr[mid] > key:
				return binary_search1(arr[0:mid], key)
			else:
				return binary_search1(arr[mid+1:], key)
	else:
		return False

arr = [1,2,3,4,5,6,7,8,9,10,13,15,17,19]
for i in range(20):
	status = binary_search(arr, i)
	status1 = binary_search1(arr, i)
	print(int(status==status1), status, status1)
