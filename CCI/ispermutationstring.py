#!/usr/bin/env python3.8

def isPermutationString(Str,Substr):
	count = 0
	location = []
	for i in range(len(Str)-len(Substr)+1):
		copySubstr = [c for c in Substr]
		for j in range(len(Substr)):
			if Str[i+j] in copySubstr:
				copySubstr.remove(Str[i+j])
				if len(copySubstr)==0:
					location.append(i)
					count += 1
			else:
				break
	return location,count

def isPermutationString1(Str,Substr):
	count = 0
	location = []
	sorted_substr = sorted(Substr)
	for i in range(len(Str)-len(Substr)+1):
		if sorted(Str[i:i+len(Substr)]) == sorted_substr:
			location.append(i)
			count += 1
	return location,count

def isPermutationString2(Str,Substr):
	count = 0
	location = []
	max = 256

	for num in range(len(Str)-len(Substr)+1):
		hcount = [0]*max
		compStr = Str[num:num+len(Substr)]
		for i in range(len(Str)):
			hcount[compStr[i]] += 1
			hcount[Substr[i]] -= 1

		if all(val==0 for val in hcount):
			location.append(i)
			count += 1
	return location,count

mainString = 'cbabadcbbabbcbabaabccbabc'
subString = 'abbc'
locations,count = isPermutationString(mainString,subString)
print(locations)
print(count)
locations,count = isPermutationString1(mainString,subString)
print(locations)
print(count)

locations,count = isPermutationString1(mainString,subString)
print(locations)
print(count)