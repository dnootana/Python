#!/usr/bin/env python3.8

import random

def bogoSort(L):
	while not is_sorted(L):
		random.shuffle(L)
		
L = [5,7,2,6,8,3,1,9,4,0]
bogoSort(L)
print(L)