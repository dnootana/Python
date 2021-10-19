#!/usr/bin/python3.8
N = input('Enter numbers to sort : ')
A = N.split()
for i in range(1,len(A)):
	key = A[i]
	j = i - 1
	while (j>=0 and A[j]<key):
		A[j+1] = A[j]
		j-=1
	A[j+1] = key
print(A)