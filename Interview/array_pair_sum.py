#!/usr/bin/env python3.8

def pair_sum(arr, k):
	if len(arr)<2:
		return

	# set tracking
	seen = set()
	output = set()

	for num in arr:
		target = k - num
		if target not in seen:
			seen.add(num)
		else:
			output.add( ( min(num, target), max(num, target) ) )

	print("\n".join(map(str,output)))


pair_sum([1,3,2,2],4)