#!/usr/bin/python3.8
import math
def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    nL = m - l + 1
    nR = r - m
    L = [0] * (nL + 1)
    R = [0] * (nR + 1)
    for i in range(0, nL):
        L[i] = arr[l + i]
    for j in range(0, nR):
        R[j] = arr[m + 1 + j]
    L[nL] = math.inf
    R[nR] = math.inf
    i = 0
    j = 0
    for k in range(l, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
A = [2, 3, 5, 1, 5, 9, 7, 2, 8]

mergeSort(A, 0, len(A) - 1)

print(A)
