#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:10:27 2021

@author: dnootana
"""

import ctypes

a = [1,2,3]
a_id = id(a)
memVal = ctypes.cast(a_id,ctypes.py_object).value
print(a_id,id(a[0]),memVal)