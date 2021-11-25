#!/usr/bin/env python3.8

"""
given a number N generate N no of fibonacci numbers
"""
from memoize import memoize

number = 25
fib_list = [None] * (number)

def fibonacci(num):
	"""
		fibonacci series using iteration
	"""
	a, b = 0, 1
	for i in range(num-1):
		fib_list[i], fib_list[i+1] = a, b
		a, b = b, a+b
	return a

fibonacci(number)
print("fibonacci series using iteration : ", fib_list)

fib_list = [None] * (number)

def fibonacci_a(num):
	fib_list[0:2] = [0,1]
	for i in range(2,num):
		fib_list[i] = fib_list[i-2] + fib_list[i-1]

fibonacci_a(number)
print("fibonacci series using iteration : ", fib_list)

fib_list = [None] * (number)

def fibonacci1(num):
	"""
		fibonacci series using recursion
	"""
	global fib_list
	if fib_list[num] is None:
		if num == 0 or num == 1:
			fib_list[num] = num
		else:
			fib_list[num] = fibonacci1(num-1) + fibonacci1(num-2)
	return fib_list[num]

fibonacci1(number-1)
print("fibonacci series using recursion : ",fib_list)

fib_list = [None] * (number)

def fibonacci2(num):
	"""
		fibonacci series using recursion with memoization
	"""
	global fib_list
	def fib(N):
		if N==0 or N==1:
			return N
		else:
			return fib(N-1) + fib(N-2)

	fib = memoize(fib)
	for i in range(num):
		fib_list[i] = fib(i)

fibonacci2(number)
print("fibonacci series using recursion with memoization : ", fib_list)