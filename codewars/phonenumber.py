#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:13:13 2021

@author: dnootana
"""
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}".format(*n)

def create_phone_number1(n):
    return '('+''.join(map(str,n[:3]))+') '+''.join(map(str,n[3:6]))+'-'+''.join(map(str,n[6:]))

def create_phone_number2(n):
    f = ''.join(str(i) for i in n[:3])
    m = ''.join(str(i) for i in n[3:6])
    l = ''.join(str(i) for i in n[6:])
    return '('+f+') '+m+'-'+l

def create_phone_number3(n):
    n = ''.join(str(i) for i in n)
    return f'({n[:3]}) {n[3:6]}-{n[6:]}'

def create_phone_number4(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

def create_phone_number5(n):
    return "(%i%i%i) %i%i%i-%i%i%i" % tuple(n)

create_phone_number6 = lambda n: "({}{}{}) {}{}{}-{}{}{}".format(*n)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(create_phone_number(A))
print(create_phone_number1(A))
print(create_phone_number2(A))
print(create_phone_number3(A))
print(create_phone_number4(A))
print(create_phone_number5(A))
print(create_phone_number6(A))