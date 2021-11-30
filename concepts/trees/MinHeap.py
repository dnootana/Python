#!/usr/bin/env python3.8

class MinHeap:
	def __init__(self):
		self.HeapList = [0]
		self.currentSize = 0

	def percUp(self, i):
		while i // 2 > 0:
			if self.HeapList[i // 2] > self.HeapList[i]:
				self.HeapList[i // 2], self.HeapList[i] = self.HeapList[i], self.HeapList[i // 2]
			i = i // 2

	def insert(self, k):
		self.HeapList.append(k)
		self.currentSize+1
		self.percUp(self.currentSize)

	def delMin(self):
		retrival = self.HeapList[1]
		self.HeapList[1] = self.HeapList[self.currentSize]
		self.HeapList.pop()
		self.currentSize -= 1
		self.percDown(1)
		return retrival

	def percDown(self, i):
		while i * 2 <= self.currentSize:
			mc = self.minChild(i)
			if self.HeapList[mc] < self.HeapList[i]:
				self.HeapList[i], self.HeapList[mc] = self.HeapList[mc], self.HeapList[i]
			i = mc

	def minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.HeapList[i * 2] < self.HeapList[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.HeapList = [0] + alist[:]
		self.currentSize = len(alist)
		while i > 0:
			self.percDown(i)
			i = i - 1

list_given = [6, 10, 34, 23, 12, 3, 5, 2, 9, 5, 3, 2, 9]
Heap = MinHeap()
Heap.buildHeap(list_given)
print("0 ",list_given)
print("Heap from the list : ")
print(Heap.HeapList)

print("\nBuilding a Heap :")
my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)
print(my_heap.HeapList)
print(my_heap.delMin())
print(my_heap.HeapList)