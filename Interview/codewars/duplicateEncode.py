#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:59:07 2021

@author: dnootana
"""
import collections
def duplicate_encode1(word):
    encode_word = ""
    word = word.lower()
    for i in word:
        if word.count(i)>1:
            encode_word += ")"
        else:
            encode_word += "("
    return encode_word

def duplicate_encode2(word):
    word = word.lower()
    counter = collections.Counter(word)
    print(counter)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)

def duplicate_encode3(word):
    new_string = ''
    word = word.lower()
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string

def duplicate_encode(word):
    table = {}
    for c in word.lower():
        table[c] = ')' if c in table else '('
    return word.lower().translate(str.maketrans(table))


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))