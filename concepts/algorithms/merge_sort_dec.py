#!/usr/bin/python3.8
import math

def mergeSort(Arr,l,r):
	if l<r:
		m = (l+r)//2
		mergeSort(Arr,l,m)
		mergeSort(Arr,m+1,r)
		merge(Arr,l,m,r)

def merge(Arr,l,m,r):
	nL = m-l+1
	nR = r-m
	L = [0]*(nL+1)
	R = [0]*(nR+1)
	for i in range(nL):
		L[i] = Arr[l+i]
	for j in range(nR):
		R[j] = Arr[m+1+j]
	L[nL] = -math.inf
	R[nR] = -math.inf
	i = 0
	j = 0
	for k in range(l,r+1):
		if L[i]>=R[j]:
			Arr[k]=L[i]
			i+=1

		else:
			Arr[k]=R[j]
			j+=1

#A = [int(x) for x in input("Enter the Elements : ").split()]
A = list(map(int,input("Enter the Elements : ").split()))
print(A)
#A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mergeSort(A, 0, len(A)-1)
print(A)