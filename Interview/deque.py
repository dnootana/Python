#!/usr/bin/env python3.8

class Deque:
	def __init__(self):
		self.items = []

	def isempty(self):
		return len(self.items) == []

	def size(self):
		return len(self.items)

	def addFront(self,item):
		self.items.append(item)

	def addRear(self):
		self.items.insert(0,item)

	def deleteFront(self):
		return self.items.pop()

	def deleteRear(self):
		return self.items.pop(0)

d = Deque()

for i in range(5):
    d.addFront(i)
    
for i in range(5):
    print(d.deleteFront())