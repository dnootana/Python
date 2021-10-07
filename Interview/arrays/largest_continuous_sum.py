#!/usr/bin/env python3.8

def largest_sum(arr):
	all_sums = []
	sum1 = arr[0]
	for num in arr[1:]:
		if sum1 < 0:
			sum1 = 0
		sum1 += num
		all_sums.append(sum1)

	return max(all_sums)

def largest_sum1(arr):
	maxsum = 0
	cursum = arr[0]
	indexs = (0, 0)
	for num in arr[1:]:
		cursum = max(cursum+num, num)
		maxsum = max(cursum, maxsum)

	return maxsum

arr = [[1,2,-1,3,4,10,10,-10,-1],[-1,1],[1,2,-1,3,4,-1]]
for inp in arr:
	print(largest_sum1(inp))