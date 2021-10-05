#!/usr/bin/env python3.8

n = 1000
def sol_equation(n):
	for a in range(n):
		for b in range(n):
			for c in range(n):
				for d in range(n):
					if a**3 + b**3 == c**3 + d**3 :
						print("a={},b={},c={},d={}".format(a,b,c,d))

def sol_equation1(n):
	for a in range(n):
		for b in range(n):
			for c in range(n):
				d = pow(a**3 + b**3 + c**3 , 1/3)
				if a**3 + b**3 == c**3 + d**3 :
					print("a={},b={},c={},d={}".format(a,b,c,d))

def sol_equation2(n):
	map1 = {}
	for a in range(n):
		for b in range(n):
			result = a**3 + b**3
			if result in map1:
				map1[result].append((a,b))
			else:
				map1[result] = [(a,b)]
	for a in range(n):
		for b in range(n):
			result = a**3 + b**3
			sol_list = map1.get(result)
			for s in sol_list:
				print("a={0},b={1},c={2[0]},d={2[1]}".format(a,b,s))

def sol_equation3(n):
	map1 = {}
	for a in range(n):
		for b in range(n):
			result = a**3 + b**3
			if result in map1:
				map1[result].append((a,b))
			else:
				map1[result] = [(a,b)]
	for result in map1.values():
		for r in result:
			for r1 in result:
				print("a={0[0]},b={0[1]},c={1[0]},d={1[1]}".format(r,r1)) 

sol_equation3(n)