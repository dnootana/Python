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

locations,count = isPermutationString('cbabadcbbabbcbabaabccbabc','abbc')
print(locations)
print(count)