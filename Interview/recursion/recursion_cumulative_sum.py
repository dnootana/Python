#!/usr/bin/env python3.8

def rec_sum(num):
	if num == 1:
		return 1
	return num + rec_sum(num-1)

print(rec_sum(9))