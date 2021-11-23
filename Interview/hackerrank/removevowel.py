#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:33:31 2021

@author: dnootana
"""

def disemvowel(string_):
    return string_.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('A','').replace('E','').replace('I','').replace('O','').replace('U','')

def disemvowel1(s):
    return s.translate(s.maketrans(dict.fromkeys("aeiouAEIOU")))

def disemvowel2(s):
    return s.translate(None, "aeiouAEIOU")

def disemvowel3(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def disemvowel4(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

import re
def disemvowel5(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

def disemvowel6(string):
    return re.sub(r"[aeiouAEIOU]", "", string)

S = "This website is for losers LOL!"
print(disemvowel(S))
print(disemvowel1(S))
# python2 print(disemvowel2(S))
print(disemvowel3(S))
print(disemvowel4(S))
print(disemvowel5(S))
print(disemvowel6(S))