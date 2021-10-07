#!/usr/bin/env python3.8

class Stack(object):
	def __init__(self):
		self.items = []

	def isempty(self):
		return len(self.items) == []

	def size(self):
		return len(self.items)

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

s = Stack()
for i in range(5):
    s.push(i)
    
for i in range(5):
    print(s.pop())