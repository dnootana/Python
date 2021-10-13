#!/usr/bin/env python3.8

"""
given a string return list of all the possible permutations of the string and count of possible permutations
"""

count = 0
list = []

def permutation(string,prefix):
	global count
	if len(string)==0:
		count += 1
		list.append(prefix)
	else:
		for i in range(len(string)):
			permutation(string[0:i]+string[i+1:], prefix+string[i])

def permutation1(string):
	out = []
	if len(string) == 1:
		out = [string]
	else:
		for i, char in enumerate(string):
			for perm in permutation1(string[:i]+string[i+1:]):
				out += [char + perm]
	return out

string = "ABC"
permutation(string, "")
print(list, count)
list = permutation1(string)
print(list, len(list))