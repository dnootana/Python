#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:45:23 2021

@author: dnootana
"""

def printer_error1(s):
    p_correct = "abcdefghijklm"
    t_count = len(s)
    e_count = 0
    for i in s:
        if i not in p_correct:
            e_count += 1
    return "{}/{}".format(e_count,t_count)

def printer_error2(s):
    return "{}/{}".format(sum(i>'m' for i in s),len(s))

from re import sub
def printer_error3(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

def printer_error4(s):
    return "%s/%s" % (len(s.translate(str.maketrans('','','abcdefghijklm'))), len(s))

def printer_error(s):
    import re
    return str(len(re.findall('[n-z]', s))) + "/" + str(len(s))

print(printer_error("aaabbbbhaijjjm")) # => "0/14"
print(printer_error("aaaxbbbbyyhwawiwjjjwwm")) #=> "8/22"