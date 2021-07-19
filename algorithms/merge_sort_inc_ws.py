#!/usr/bin/python3.8

def mergeSort(arr,l,r):
	if l<r:
		m = (l+r)//2
		mergeSort(arr,l,m)
		mergeSort(arr,m+1,r)
		print(arr)
		merge(arr,l,m,r)

def merge(arr,l,m,r):
	nL = m-l+1
	nR = r-m
	L = [0]*(nL)
	R = [0]*(nR)
	for i in range(nL):
		L[i]=arr[l+i]
	for j in range(nR):
		R[j]=arr[m+1+j]
	i=0
	j=0
	for k in range(l,r+1):
		if i<nL and (j>=nR or L[i]<=R[j]):
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1

#A = [int(x) for i in input("Enter Elements : ").split()]
A = [9,8,7,6,5,4,3,2,1,0]
mergeSort(A,0,len(A)-1)
print(A)