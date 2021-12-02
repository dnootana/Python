#!/usr/bin/env python3.8

"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
1) Only one disk can be moved at a time. 
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. 
3) No disk may be placed on top of a smaller disk.
"""

def TOH(n, A, B, C):
	if n>0:
		TOH(n-1, A, C, B)
		print("move 1 disc from",A,"to",C)
		TOH(n-1, B, A, C)

TOH(3, 1, 2, 3)