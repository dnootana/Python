#!/usr/bin/env python3.8

class Queue2Stacks(object):
	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self,item):
		self.instack.append(item)

	def dequeue(self):
		if not self.outstack:
			while len(self.instack):
				self.outstack.append(self.instack.pop())
		return self.outstack.pop()

def main():
	q = Queue2Stacks()

	for i in range(5):
		q.enqueue(i)

	for i in range(5):
		print(q.dequeue())

if __name__ == "__main__":
	main()
