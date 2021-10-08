#!/usr/bin/env python3.8

def string_compression(string):
	new_string = ""
	length = len(string)
	i = 0
	
	while i<length:
		count = 1
		char = string[i]
		i += 1
		while i<length and string[i]==char:
			count += 1
			i += 1
		new_string += char+str(count)
	return new_string

def string_compression1(string):
	new_string = ""
	length = len(string)
	char = string[0]
	i = 1
	count = 1
	while i<length:
		if char == string[i]:
			count += 1
		else:
			new_string += char+str(count)
			count = 1
			char = string[i]
		i += 1
	new_string += char+str(count)

	return new_string

print(string_compression('AAABCCDDDDD'))
print(string_compression1('AAABCCDDDDD'))