#!/usr/bin/env python3.8

"""
Given a string, write a function that uses recursion to reverse it.
"""

def rev_string(strg):
	if len(strg) <= 1:
		return strg
	return rev_string(strg[1:]) + strg[0]

def rev_string1(strg):
	return strg[::-1]

def rev_string2(strg):
	s_list = list(strg)
	for i in range(len(s_list)//2):
		s_list[i], s_list[-i-1] = s_list[-i-1], s_list[i]
	return "".join(s_list)

def rev_string3(strg):
	stack = []
	for s in strg:
		stack.append(s)
	rev_s = ""
	while len(stack):
		rev_s += stack.pop()
	return rev_s

def rev_string4(strg):
	return "".join(reversed(strg))

string = "abcdefghijklmnopqrstuvwxyz"
rev_string = rev_string(string[:])
print(rev_string)

rev_string = rev_string1(string[:])
print(rev_string)

rev_string = rev_string2(string[:])
print(rev_string)

rev_string = rev_string3(string[:])
print(rev_string)

rev_string = rev_string4(string[:])
print(rev_string)