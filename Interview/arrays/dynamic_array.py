#!/usr/bin/env python3.8

import ctypes
import sys

class DynamicArray(object):
	def __init__(self):
		self.n = 0
		self.capacity = 1
		self.A = self.make_array(self.capacity)

	def __len__(self):
		return self.n

	def __getitem__(self,k):
		if not 0 <= k < self.n:
			return IndexError("k is out of bound")
		return self.A[k]

	def append(self, elem):
		if self.n == self.capacity:
			self._resize(2*self.capacity)
		self.A[self.n] = elem
		self.n += 1

	def _resize(self, new_cap):
		B = self.make_array(new_cap)
		for k in range(self.n):
			B[k] = self.A[k]
		self.A = B
		self.capacity = new_cap

	def make_array(self, new_cap):
		return (new_cap * ctypes.py_object)()

	def getsize(self):
		return ctypes.sizeof(self.A)

arr = DynamicArray()
n = 100
for x in range(n):
	arr.append(x)
	a = len(arr)
	b = sys.getsizeof(arr)
	c = arr.getsize()
	print("len = {} getsizeof = {} sizeof = {}".format(a,b,c))
print(arr[1])