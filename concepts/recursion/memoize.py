#!/usr/bin/env python3.8

"""
create a memoize class
"""

class memoize:
	def __init__(self, f):
		self.f = f
		self.mem = {}

	def __call__(self, *args):
		if args in self.mem:
			return self.mem[args]
		else:
			self.mem[args] = self.f(*args)
			return self.mem[args]