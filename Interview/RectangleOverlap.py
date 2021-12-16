#!/usr/bin/env python3.8
"""
Given two rectangles, determine if they overlap. The rectangles are defined as a Dictionary, for example:
r1 = {
    
         # x and y coordinates of the bottom-left corner of the rectangle
         'x': 2 , 'y': 4,
         
         # Width and Height of rectangle
         'w':5,'h':12}
"""

import copy

def overlap(coord1, dim1, coord2, dim2):
	greater = max(coord1, coord2)

	smaller = min(coord1+dim1, coord2+dim2)
	if greater > smaller:
		return None, None
	return greater, smaller - greater

def rectOverlap(R_1, R_2):
	x_overlap, x_dim = overlap(R_1['x'], R_1['w'], R_2['x'], R_2['w'])
	y_overlap, y_dim = overlap(R_1['y'], R_1['h'], R_2['y'], R_2['h'])

	if not y_dim or not x_dim:
		if x_overlap and y_overlap:
			if x_dim or y_dim:
				print('side overlap at',x_overlap,x_dim,y_overlap,y_dim)
			else:
				print("point overlap at",x_overlap,y_overlap)
		else:
			print("no overlap")
		return

	print(x_overlap, x_dim, y_overlap, y_dim)



r1 = {'x': 2, 'y': 4, 'w':5, 'h':12}
r2 = {'x': 1, 'y': 5, 'w':7, 'h':14}
rectOverlap(r1, r2)

r1 = {'x': 5, 'y': 5, 'w':5, 'h':5}
r2 = {'x': 1, 'y': 5, 'w':4, 'h':14}
rectOverlap(r1, r2)

r1 = {'x': 5, 'y': 4, 'w':5, 'h':5}
r2 = {'x': 1, 'y': 1, 'w':4, 'h':3}
rectOverlap(r1, r2)

r1 = {'x': 5, 'y': 4, 'w':5, 'h':5}
r2 = {'x': 1, 'y': 1, 'w':4, 'h':2}
rectOverlap(r1, r2)