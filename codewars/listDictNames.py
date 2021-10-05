#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 12:27:24 2021

@author: dnootana
"""

def namelist1(names):
    str_name = ""
    for i in range(len(names)):
        str_name += names[i]["name"]
        if i<len(names)-2:
            str_name += ", "
        elif i!=len(names)-1:
            str_name += " & "
    return str_name

def namelist2(names):
    if len(names)==0:
        return ''
    elif len(names)==1:
        return names[0]['name']
    else:
        return "{} & {}".format(', '.join(name['name'] for name in names[:-1]),names[-1]['name'])

def namelist3(names):
    names = [ hash["name"] for hash in names ]
    output = names[:-2]
    output.append(" & ".join(names[-2:]))
    return ", ".join(output)

namelist=lambda names:' & '.join(', '.join(d['name']for d in names).rsplit(', ',1))


print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
# returns 'Bart, Lisa & Maggie'
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
# returns 'Bart & Lisa'
print(namelist([ {'name': 'Bart'} ]))
# returns 'Bart'
print(namelist([]))
# returns ''