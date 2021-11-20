#!/usr/bin/env python3.8

class Stack(object):
	def __init__(self):
		self.items = []
		self.size = 0

	def size(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def push(self,item):
		self.items.append(item)
		self.size += 1

	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		self.size -= 1
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

def main():
	s = Stack()
	for i in range(5):
		s.push(i)

	for i in range(5):
		print(s.pop())

if __name__ == "__main__":
	main()
