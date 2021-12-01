#!/usr/bin/python3.8

def merge_sort_inc(arr, start, end):
	"""
		Merge Sort is a Divide and Conquer algorithm
		It is a recursive algorithm which continually splits a list in half until the list is empty or has one item and then recursively merges them sorting simultaneously
		it has O(n(log n)) time complexity
	"""
	if start < end:
		mid = (start + end) // 2
		merge_sort_inc(arr, start, mid)
		merge_sort_inc(arr, mid+1, end)
		merge(arr, start, mid, end)
	return arr

def merge(arr, start, mid, end):
	nL = mid - start + 1
	nR = end - mid
	L = nL * [0]
	R = nR * [0]
	for i in range(nL):
		L[i] = arr[start+i]
	for j in range(nR):
		R[j] = arr[mid+1+j]
	i=0
	j=0
	for k in range(start, end+1):
		if i<nL and (j>=nR or L[i]<=R[j]):
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1

#A = [int(x) for i in input("Enter Elements : ").split()]
A = [9,8,7,6,5,4,3,2,1,0]
merge_sort_inc(A,0,len(A)-1)
print(A)