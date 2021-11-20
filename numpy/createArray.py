#!/bin/usr/env python3.8

import numpy as np

# 0-dimensional array
arr = np.array(34)
print(arr.ndim,"-d array : ",arr, "with shape", arr.shape)

# 1-dimensional array
arr1 = np.array([0,1,2,3,4,5])
print(arr1.ndim,"-d array : ",arr1, "with shape", arr1.shape)

# 2-dimensional array
arr2 = np.array([[0,1,2], [3,4,5]])
print(arr2.ndim,"-d array : ",arr2, "with shape", arr2.shape)

# 3-dimensional array
arr3 = np.array([[[0,1], [2,3]], [[4,5],[6,7]]])
print(arr3.ndim,"-d array : ",arr3, "with shape", arr3.shape)

# assign dimension while creating array
arrn = np.array([1,2,3,4,5], ndmin=5)
print(arrn.ndim,"-d array : ", arrn, "with shape", arrn.shape)

print(arr1, "=>", arr1[0:3])
print(arr2, "=>", arr2[0:2,2])
print(arr3, "=>", arr3[0:1,1])
print(arrn, "=>", arrn[0,0,0,0,1])

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

print(arr.dtype)

arrs = np.array(['apple', 'ball', 'cat', 'dog'])
print(arrs.dtype)


# create array with defined datatype
arrd = np.array([1, 2, 3, 4], dtype = 'i4')
print(arrd.dtype)

# if a value cannot be converted
#arre = np.array(['a',1,2,3], dtype='i')


# to convert an existing array make a copy of the array using astype() and pass the type
arrc = arr1.astype('U')
print(arrc.dtype, arrc)


arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()
view = arr.view()

print(arr, copy, view)

arr[0] = 0
print('arr = ', arr, 'copy = ', copy, 'view = ', view)

copy[1] = 0
print('arr = ', arr, 'copy = ', copy, 'view = ', view)

view[2] = 0
print('arr = ', arr, 'copy = ', copy, 'view = ', view)

print(copy.base)
print(view.base)

print("ndarray reshape")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr2 = arr.reshape(3,3)
print(arr2, arr)
arr = arr2.reshape(9)
print(arr)
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
arr2 = arr.reshape(2,2,2)
print(arr2)
arr = arr2.reshape(8)
print(arr.base)

# reshape with unknown dimension
print("reshape with unknown direction with -1")
arr = arr2.reshape(2,-1)
print(arr)


print("flattening the array")
arr = arr2.reshape(-1)
print(arr)

print("iterating 2-d array")

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
for i in arr:
	for j in i:
		print(j)

print("iterating using iter:")
for i in np.nditer(arr):
	print(i)

print("iterating with different datatype: ")
for i in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
	print(i)

print("iterating with different step size : ")
print(arr)
for i in np.nditer(arr[::2,::2]):
	print(i)

print("enumerated iteration ")
for idi, i in np.ndenumerate(arr[::2,::2]):
	print(idi, i)

print("ndarry concatenation : ")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

arr3 = np.concatenate((arr1, arr2))
arr4 = np.stack((arr1, arr2))
print("array 1 = ", arr1)
print("array 2 = ", arr2)
print("array 3 = ", arr3)
print("array 4 = ", arr4)


print("ndarry concatenation 2-d : (default axis 0)")
arr1 = np.array([[1, 2, 3], [4, 5, 0]])
arr2 = np.array([[6, 7, 8], [9, 10, 0]])

arr3 = np.concatenate((arr1, arr2))
arr4 = np.stack((arr1, arr2))
print("array 1 = ", arr1)
print("array 2 = ", arr2)
print("array 3 = ", arr3)
print("array 4 = ", arr4)

print("with axis 1: ")

arr3 = np.concatenate((arr1, arr2), axis=1)
arr4 = np.stack((arr1, arr2), axis=1)
print("array 1 = ", arr1)
print("array 2 = ", arr2)
print("array 3 = ", arr3)
print("array 4 = ", arr4)


print("ndarry concatenation 3-d : (default axis 0)")
arr1 = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
arr2 = np.array([[[5, 5, 5], [6, 6, 6]], [[7, 7, 7], [8, 8, 8]]])

arr3 = np.concatenate((arr1, arr2))
arr4 = np.stack((arr1, arr2))
print("array 1 = ", arr1)
print("array 2 = ", arr2)
print("array 3 = ", arr3)
print("array 4 = ", arr4)

print("with axis : 1")

arr3 = np.concatenate((arr1, arr2), axis=1)
arr4 = np.stack((arr1, arr2), axis=1)
print("array 1 = ", arr1)
print("array 2 = ", arr2)
print("array 3 = ", arr3)
print("array 4 = ", arr4)

print("with axis : 2")

arr3 = np.concatenate((arr1, arr2), axis=2)
arr4 = np.stack((arr1, arr2), axis=2)
print("array 1 = ", arr1)
print("array 2 = ", arr2)
print("array 3 = ", arr3)
print("array 4 = ", arr4)


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.hstack((arr1,arr2))
arr4 = np.vstack((arr1,arr2))
arr5 = np.dstack((arr1,arr2))
print("arr1 :", arr1)
print("arr2 :", arr2)
print("hstack :",arr3)
print("vstack :",arr4)
print("dstack :",arr5)


print("array split : ")
arr = np.array([1,2,3,4,5,6])
arr2 = np.array_split(arr, 3)
print(arr2)
arr2 = np.split(arr, 3)
print(arr2)

arr2 = np.array_split(arr, 4)
print(arr2)
#arr2 = np.split(arr, 4)   #produces an error as length is low
print(arr2)

arr2 = np.array_split(arr, 7)
print(arr2)


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr2 = np.array_split(arr, 3)
print(arr2)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr2 = np.array_split(arr, 3)
print(arr2)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr2 = np.array_split(arr, 3, axis= 1)
print(arr2)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr3 = np.hsplit(arr,3)
arr4 = np.vsplit(arr,3)
print("arr1 :", arr)
print("hsplit :",arr3)
print("vsplit :",arr4)
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]])
arr5 = np.dsplit(arr,1)
print("dsplit :",arr5)


print("array search : ")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

print("search for even numbers : ")
x = np.where(arr%2 == 0)
print(x)


print("returns index where the specified value would be inserted : (assumes arr to be sorted)")
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

print("search from right to return the right most match to insert in right most position")
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

print("search multiple values")
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

print("array sorting : ")

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array([[3, 2, 5, 1],[0,7,4,3]])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))


print("array filtering")
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)


print("filter array creation")
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


arr = np.array([0,1,2,3,4])
print(arr[[True,False,True,False,True]])