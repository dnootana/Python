#!/usr/bin/python3.8

def substring_index(Str, word):
	S = len(Str)
	w = len(word)
	index = []
	for i in range(S-w+1):
		j = 0
		while j<w:
			if (Str[i+j]!=word[j]):
				break
			#print(Str[i+j],' ',word[j],' ',i,' ',j)
			j +=1
		if(j==w):
			index.append(i)
	return index

Str = input('Enter string : ')
word = input('Enter word : ')
index = substring_index(Str, word)

if (len(index)==0):
	print('Word doesn\'t exist')
else: 
	print('index is : ',', '.join(map(str,index)))