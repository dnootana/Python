#!/usr/bin/env python3.8

"""
given a string return the reverse of the string
"""

import sys
sys.path.append('../')
from stackQueueDeque.stack import Stack

def string_reverse(string):
	reverse = ""
	for i in range(len(string), 0, -1):
		reverse += string[i-1]
	return reverse

def string_reverse1(string):
	reverse = ""
	for s in string:
		reverse = s + reverse
	return reverse

def string_reverse2(string):
	if string == '':
		return string
	return string_reverse1(string[1:]) + string[0]

#stack
def string_reverse3(string):
	stack = Stack()
	n = ''
	for s in string:
		stack.push(s)
	while stack.size:
		n += stack.pop()
	return n

string = "abcdefghijklmnopqrstuvwxyz"
print(string_reverse(string))
print(string_reverse1(string))
print(string_reverse2(string))
print(string_reverse3(string))