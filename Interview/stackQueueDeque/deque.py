#!/usr/bin/env python3.8

class Deque:
	def __init__(self):
		self.items = []
		self.size = 0

	def isEmpty(self):
		return self.size == 0

	def size(self):
		return self.size

	def addFront(self,item):
		self.items.append(item)
		self.size += 1

	def addRear(self):
		self.items.insert(0,item)
		self.size += 1

	def deleteFront(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		self.size -= 1
		return self.items.pop()

	def deleteRear(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		self.size -= 1
		return self.items.pop(0)

d = Deque()

for i in range(5):
    d.addFront(i)
    
for i in range(5):
    print(d.deleteFront())