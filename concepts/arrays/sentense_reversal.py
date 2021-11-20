#!/usr/bin/env python3.8

def sentense_reverse(sentense):
	return ' '.join(reversed(sentense.split()))

def sentense_reverse1(sentense):
	return ' '.join(sentense.split()[::-1])

def sentense_reverse2(sentense):
	reverse_sentense = ""
	length = len(sentense)
	i = 0
	while i<length:
		if sentense[i] != " ":
			word_start = i
			while i < length and sentense[i] != " ":
				i += 1

			word_end = i
			if i != length:
				reverse_sentense = " " + reverse_sentense
			reverse_sentense = sentense[word_start:word_end] + reverse_sentense
		else:
			i += 1
	return reverse_sentense

print(sentense_reverse('   Hello John    how are you   '))
print(sentense_reverse1('   Hello John    how are you   '))
print(sentense_reverse2('   Hello John    how are you   '))