#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:06:14 2021

@author: dnootana
"""
import math
def divisors1(integer):
    div_low = [i for i in range(2,int(math.sqrt(integer)) + 1) if integer%i==0]
    divs = div_low + [integer//i for i in div_low[::-1] if i!=integer//i]
    if not divs:
        return "{} is prime".format(integer)
    return divs

def divisors(integer):
    divs = [i for i in range(2,integer) if integer%i==0]
    if not divs:
        return "{} is prime".format(integer)
    return divs

def divisors2(integer):
    divs_lo = []
    divs_hi = []
    for i in range(2, int(math.sqrt(integer)) + 1):
        if integer % i == 0:
            divs_lo.append(i)
            if i != integer / i:
                divs_hi.append(int(integer/i))
    if not divs_lo:
        return '{} is prime'.format(integer)
    divs_hi.reverse()
    return divs_lo + divs_hi

print(divisors(12)) #should return [2,3,4,6]
print(divisors(25)) #should return [5]
print(divisors(13)) #should return "13 is prime"
print(divisors(5000000))