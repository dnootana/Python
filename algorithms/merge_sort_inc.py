#!/usr/bin/python3.8
import math
def mergesort(arr, l, r):
	if l<r:
		m = (l + r)//2
		mergesort(arr, l, m)
		mergesort(arr, m+1, r)
		merge(arr, l, m, r)

def merge(arr, l, m, r):
	nL = m - l + 1
	nR = r - m
	L = [0]*(nL+1)
	R = [0]*(nR+1)
	for i in range(nL):
		L[i] = arr[l + i]
	for j in range(nR):
		R[j] = arr[ m+1+j ]
	L[nL] = math.inf
	R[nR] = math.inf

	i=0
	j=0
	for k in range(l,r+1):
		if L[i]<=R[j]:
			arr[k]=L[i]
			i+=1

		else:
			arr[k]=R[j]
			j+=1

#A = [int(x) for x in input("Enter the Elements : ").split()]
A = list(map(int,input("Enter the Elements : ").split()))
#A = [9,8,7,6,5,4,3,2,1]
mergesort(A, 0, len(A)-1)
print(A)