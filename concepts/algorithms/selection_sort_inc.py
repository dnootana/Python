#!/usr/bin/python3.8
N = input('Enter array elements : ')
A = N.split()
for i in range(len(A)-1):
	small = i
	for j in range(i+1,len(A)):
		if(A[small]>A[j]):
			small = j
	temp = A[i]
	A[i] = A[small]
	A[small] = temp
print(A)