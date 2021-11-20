#!/usr/bin/env python3.8

class MyRange():
	def __init__(self, start, end, step):
		self.value = start
		self.end = end
		self.step = step

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current_value = self.value
		self.value += self.step
		return current_value

my_range = MyRange(0,6,2)
# print(my_range)
# rang = range(0,6,2)
# print(rang)
# print(dir(my_range))
for i in my_range:
	print(i)

