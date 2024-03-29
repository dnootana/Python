#!/usr/bin/env python3.8

class Sentence:
	def __init__(self,sentence):
		self.sentence = sentence
		self.index = 0
		self.words = self.sentence.split()

	def __iter__(self):
		return self

	def __next__(self):
		if self.index>=len(self.words):
			raise StopIteration
		index = self.index
		self.index += 1
		return self.words[index]

def sentence(sentence):
	for word in sentence.split():
		yield word

my_sentence = sentence("This is a test")

for word in my_sentence:
	print(word)

class_sentense = Sentence("This is a test")
for word in class_sentense:
	print(word)