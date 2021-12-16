#!/usr/bin/env python3.8

def checkUnique(String):
	"""
		Time Complexity : O(n2)
	"""
	for i in range(len(String)):
		if String[i] in String[:i]+String[i+1:]:
			return False
	return True

def checkUnique1(String):
	"""
		Time Complexity : O(n) = O(c) = O(1) as we know loop cannot go beyond 128 or 256
	"""
	if len(String)>128: #total ascii characters is 128, can use 256 for extended ascii
		return False

	Str_dict = {}
	for char in String:
		if char in Str_dict:
			return False
		else:
			Str_dict[char] = True
	return True

def checkUnique2(String):
	"""
		Time Complexity : O(n)
	"""
	if len(String)>128: #total ascii characters is 128, can use 256 for extended ascii
		return False

	checker = 0
	for i in range(len(String)):
		val = ord(String[i])
		print(checker, val, 1<<val)
		if ((checker & (1<<val)) > 0):
			return False
		checker = checker|(1<<val)
	return True

def checkUnique3(String):
	"""
		Time Complexity : O(n2)
	"""
	for i in range(len(String)):
		for j in range(len(String)):
			if i!=j and String[i]==String[j]:
				return False
	return True

def checkUnique4(String):
	"""
		Time Complexity : O(nlogn + n-1) = O(nlogn)
	"""
	SortedString = sorted(String)
	for i in range(len(String)-1):
		if SortedString[i] == SortedString[i+1]:
			return False
	return True


All = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
Str = " a bs"
print(checkUnique3(Str))