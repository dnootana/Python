#!/usr/bin/env python3.8

def uni_char(string):
	return len(string) == len(set(string))

def uni_char1(string):
	letters = set()

	for char in string:
		if char in letters:
			return False
		else:
			letters.add(char)
	return True

def uni_char2(string):
	letters = {}

	for char in string:
		if char in letters:
			return False
		else:
			letters[char] = True
	return True

print(uni_char1('abcdaefg'))