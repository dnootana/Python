#!/usr/bin/env python3.8

"""
Given an array of integers we need to move all the zeroes to the end and maintain the order of rest of the elements.
"""

import copy

class Numbers:
	def moveZero1(self, numbers):
		"""
			used pop and append
			time complexity is O(Nk)=>O(N2) as pop has TC O(k) (because of shift operation)

		"""
		num_length = len(numbers)
		i = 0
		while i < num_length:
			if numbers[i] == 0:
				x = numbers.pop(i)
				numbers.append(x)
				num_length -= 1
			else:
				i += 1
		return numbers

	def moveZero2(self, numbers):
		"""
			Copy non-zero element to left, mark everything else zero
			time complexity is O(N)
		"""
		count = 0
		for i in range(len(numbers)):
			if numbers[i] != 0:
				numbers[count] = numbers[i]
				count += 1
		for i in range(count,len(numbers)):
			numbers[i] = 0
		return numbers

	def moveZero3(self, numbers):
		"""
			using single for loop
			time complexity is O(N)
		"""
		count = 0
		for i in range(len(numbers)):
			if numbers[i] != 0:
				numbers[count], numbers[i] = numbers[i], numbers[count]
				count += 1
		return numbers

nums = [2,3,1,6,0,4,0,40,2,4,6,0,1,00,4,55,76,0,40,5]
N = Numbers()
nums1 = N.moveZero1(copy.deepcopy(nums))
print(nums1)
nums2 = N.moveZero2(copy.deepcopy(nums))
print(nums2)
nums3 = N.moveZero3(copy.deepcopy(nums))
print(nums3)