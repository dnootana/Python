#!/usr/bin/python3.8

number = 10
def fib_gen(up_to):
	"""
		fibonacci series upto number 50 (i.e. <=50)
	"""
	a,b=0,1
	while a<up_to:
		yield a
		a,b=b,a+b

fib_num = []
for num in fib_gen(number):
	fib_num.append(num)
print('Fibonacci series upto 50 are : ',', '.join(list(map(str,fib_num))))

def fib_gen1():
	"""
		fibonacci series upto 50 numbers
	"""
	a,b=0,1
	while 1:
		yield a
		a,b=b,a+b

fib_num1 = []
x = fib_gen1()
for num in range(number):
	fib_num1.append(x.__next__())
print('Fibonacci series of 50 numbers are : ',', '.join(list(map(str,fib_num1))))