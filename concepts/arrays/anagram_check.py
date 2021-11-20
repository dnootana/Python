#!/usr/bin/env python3.8

def check_anagram(S1, S2):
	S1 = S1.replace(' ', '').lower()
	S2 = S2.replace(' ', '').lower()
	return sorted(S1) == sorted(S2)

def check_anagram2(S1, S2):
	S1 = S1.replace(' ', '').lower()
	S2 = S2.replace(' ', '').lower()

	if len(S1) != len(S2):
		return False

	count = {}
	for char in S1:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1

	for char in S2:
		if char in count:
			count[char] -= 1
		else:
			count[char] = -1

	for i in count:
		if count[i] != 0:
			return False

	return True


print(check_anagram2('dog','god'))

print(check_anagram2('clint eastwood','old west action'))

print(check_anagram2('dd','aa'))
