#!/usr/bin/env python3.8

def rec_int(num):
	if num % 10 == num:
		return num
	return num % 10 + rec_int(num / 10)

print(rec_int(123456789))