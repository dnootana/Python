#!/usr/bin/env python3.8

def areAnagram(str1,str2):
	if len(str1) != len(str2):
		return False
	else:
		max = 256
		count1 = [0]*max
		count2 = [0]*max

		for i in range(len(str1)):
			count1[ord(str1[i])] += 1
			count2[ord(str2[i])] += 1

		for i in range(max):
			if count1[i] != count2[i]:
				return False
		return True

def areAnagram1(str1,str2):
	if len(str1) != len(str2):
		return False
	else:
		max = 256
		count = [0]*max

		for i in range(len(str1)):
			count[ord(str1[i])] -= 1
			count[ord(str2[i])] += 1

		# for i in range(max):
		# 	if count[i] != 0:
		# 		return False
		# return True
		return all(c == 0 for c in count)


String1 = 'adbb'
String2 = 'abbc'
result = areAnagram1(String1,String2)
print(result)