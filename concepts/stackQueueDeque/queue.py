#!/usr/bin/env python3.8

class Queue(object):
	def __init__(self):
		self.items = []
		self.size = 0

	def isEmpty(self):
		return self.size == 0

	def size(self):
		return self.size

	def enqueue(self,item):
		self.items.insert(0,item)
		self.size += 1

	def dequeue(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		self.size -= 1
		return self.items.pop()

def main():
	q = Queue()

	for i in range(5):
		q.enqueue(i)

	for i in range(5):
		print(q.dequeue())

if __name__ == "__main__":
	main()
