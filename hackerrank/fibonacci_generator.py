#!/usr/bin/python3.8
def fib_gen(up_to):
	a,b=0,1
	while a<up_to:
		yield a
		a,b=b,a+b

fib_num = []
for num in fib_gen(50):
	fib_num.append(num)
print('Fibonacci series upto 50 are : ',', '.join(list(map(str,fib_num))))

def fib_gen1():
	a,b=0,1
	while 1:
		yield a
		a,b=b,a+b

fib_num1 = []
x = fib_gen1()
for num in range(50):
	fib_num1.append(x.__next__())
print('Fibonacci series upto 50 are : ',', '.join(list(map(str,fib_num1))))