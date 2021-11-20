#!/usr/bin/env python3.8

def balance_check(string):
	if len(string)%2 != 0:
		return False

	opening = set('([{')
	matches = set( [('(', ')'), ('[', ']'), ('{', '}')] )

	stack = []
	for c in string:
		if c in opening:
			stack.append(c)
		else:
			if len(stack)>0:
				item = stack.pop()
				if (item, c) not in matches:
					return False
	return True

all_case = ['[](){([[[]]])}','']
for case in all_case:
	print(balance_check(case))