#!/usr/bin/env python3.8

class Queue(object):
	def __init__(self):
		self.items = []

	def isempty(self):
		return len(self.items) == []

	def size(self):
		return len(self.items)

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

q = Queue()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())