#!/usr/bin/env python3.8

"""
given a number N generate N no of fibonnaci numbers
"""
from memoize import memoize

def fibonnaci(num):
	global fib_list
	if fib_list[num] is not None:
		return fib_list[num]
	elif num == 0 or num == 1:
		fib_list[num] = num
		return num
	else:
		fib_list[num] = fibonnaci(num-1) + fibonnaci(num-2)
		return fib_list[num]

# iteration
def fibonnaci1(num):
	a, b = 0, 1
	for i in range(num):
		fib_list[i], fib_list[i+1] = a, b
		a, b = b, a+b
	return a

#
def fibonnaci2(num):
	global fib_list
	def fib(N):
		if N==0 or N==1:
			return N
		else:
			return fib(N-1) + fib(N-2)

	fib = memoize(fib)
	for i in range(num+1):
		fib_list[i] = fib(i)




number = 25
fib_list = [None] * (number+1)
# fibonnaci(number)
# print(fib_list)

# fib_list = [None] * (number+1)
# fibonnaci1(number)
# print(fib_list)

fib_list = [None] * (number+1)
fibonnaci2(number)
print(fib_list)