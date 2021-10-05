#!/usr/bin/env python3.8

count = 0
def permutation1(string):
	permutation(string,"")

def permutation(string,prefix):
	print(string)
	global count
	if len(string)==0:
		count += 1
		#print(prefix)
		pass
	else:
		for i in range(len(string)):
			count += 1
			rem = string[0:i]+string[i+1:]
			permutation(rem,prefix+string[i])

permutation1("ABCDE")
print(count)