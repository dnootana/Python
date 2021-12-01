#!/usr/bin/env python3.8

class MaxHeap:
	def __init__(self):
		self.HeapList = [0]
		self.currentSize = 0

	def insert(self, k):
		self.HeapList.append(k)
		self.currentSize += 1
		self.percUp(self.currentSize)

	def percUp(self, i):
		while i // 2 > 0:
			if self.HeapList[i // 2] < self.HeapList[i]:
				self.HeapList[i // 2], self.HeapList[i] = self.HeapList[i], self.HeapList[i // 2]
			i = i // 2

	def delMax(self):
		retrival = self.HeapList[1]
		self.HeapList[1] = self.HeapList[self.currentSize]
		self.HeapList.pop()
		self.currentSize -= 1
		self.percDown(1)
		return retrival

	def percDown(self, i):
		while i * 2 <= self.currentSize:
			mc = self.maxChild(i)
			print("Min :",mc)
			if self.HeapList[mc] > self.HeapList[i]:
				self.HeapList[mc], self.HeapList[i] = self.HeapList[i], self.HeapList[mc]
			i = i * 2

	def maxChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.HeapList[i * 2] > self.HeapList[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.HeapList = [0] + alist[:]
		self.currentSize = len(alist)
		while i > 0:
			self.percDown(i)
			i = i -1


list_given = [1, 2, 3, 4, 5, 6, 7, 8]
Heap = MaxHeap()
Heap.buildHeap(list_given)
print("0 ",list_given)
print("Heap from the list : ")
print(Heap.HeapList)

print("\nBuilding a Heap :")
my_heap = MaxHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)
print(my_heap.HeapList)
print(my_heap.delMax())
print(my_heap.HeapList)