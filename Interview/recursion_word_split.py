#!/usr/bin/env python3.8
word_list = []

def word_split(sentense, list_of_words):
	global word_list
	if sentense == "":
		return 
	for words in list_of_words:
		if sentense.startswith(words):
			word_list.append(words)
			list_of_words.remove(words)
			word_split(sentense[len(words):], list_of_words)
			break

word_split('themanran',['the','ran','man'])
print(word_list)
word_list = []
word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
print(word_list)