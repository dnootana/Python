#!/usr/bin/env python3.8

from math import factorial

def listPosition(word):
    def getAnagrams(string):
        anagram_list = []
        def anagrams(str,prefix):
            if len(str) == 0:
                anagram_list.append(prefix)
            else:
                for i in range(len(str)):
                    rem = str[0:i]+str[i+1:]
                    anagrams(rem,prefix+str[i])
        anagrams(string,"")
        print(sorted(list(set(anagram_list))))
        return anagram_list

    return sorted(list(set(getAnagrams(word)))).index(word)+1

def listPosition1(word):
	def getdict(word):
		char_dict = {}
		for char in word:
			char_dict[char] = char_dict.get(char,0) +1
		return char_dict

	position = 0
	for i in range(len(word)):
		numerator = factorial(len(word)-i-1)
		sortedword = sorted(list(set(word[i:])))
		unique_word = set(word[i:])
		for sortpos in range(sortedword.index(word[i])):
			dict_word = word[i:]
			dict_word = dict_word.replace(sortedword[sortpos],'',1)
			char_dict = getdict(dict_word)
			denominator = 1
			for key in char_dict.keys():
				denominator *= factorial(char_dict[key])
			position += numerator // (denominator)
	return position + 1


def listPosition2(word):
    """Return the anagram list position of the word"""
    count = 0
    while len(word) > 1:
        first = word[0]
        uniques = set(word)
        possibilities = factorial(len(word))
        for letter in uniques:
            possibilities /= factorial(word.count(letter))
        for letter in uniques:
            if letter < first:
                count += possibilities / len(word) * word.count(letter)
        word = word[1:]
    return count + 1

#     "BOOKKEEPER"
Str = "BOOKKEEPER"
print(listPosition(Str))
print(listPosition1(Str))
print(listPosition2(Str))

for i in ['AABB', 'ABAB', 'ABBA', 'BAAB', 'BABA', 'BBAA']:
	print(i,listPosition1(i))

