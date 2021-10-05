#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:34:29 2021

@author: dnootana
"""

def iq_test1(numbers):
    nums = list(map(int,numbers.split()))
    num_type = {'even':[],'odd':[]}
    for i in range(len(nums)):
        if nums[i]%2==0:
            num_type["even"].append(i)
        else:
            num_type["odd"].append(i)
        if i>1:
            if len(num_type['even'])==1:
                return num_type['even'][0]+1
            if len(num_type['odd'])==1:
                return num_type['odd'][0]+1
            
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
            
print(iq_test("2 4 7 8 10")) # => 3  Third number is odd, while the rest of the numbers are even

print(iq_test("1 2 1 1")) # => 2 Second number is even, while the rest of the numbers are odd