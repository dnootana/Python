#!/usr/bin/env python3.8

fib_dict = {}
def fib(num):
	"""
		using recursion with memoization
	"""
	if num not in fib_dict:
		if num < 2:
			fib_dict[num] =  num
		else:
			fib_dict[num] = fib(num - 1) + fib(num - 2)
	return fib_dict[num]
	
def fib1(num):
	"""
		using generator
	"""
	a, b = 0, 1
	for i in range(num+1):
		yield a
		a, b = b, a+b

# generator using decorator
class Memoize:
	def __init__(self, fn):
		self.memo = {}
		self.fn = fn

	def __call__(self, arg):
		if arg not in self.memo:
			self.memo[arg] = self.fn(arg)
		return self.memo[arg]

@Memoize
def fib2(num):
	if num == 0:
		return num
	elif num == 1:
		return num
	else:
		return fib2(num-1) + fib2(num-2)

N = 35
fibN = fib(N)
print(N,"th fibonacci number is ", fibN)
print(fib_dict)
for i in fib1(N):
	print(i,end=", ")
print("")

print(fib2(N))