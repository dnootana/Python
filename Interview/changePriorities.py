#!/usr/bin/env python3.8

def changePriority(P_list):
	"""
		1 ≤ n ≤ 100
		1 ≤ priorities[n] ≤ 99 - Positive Priorities
		100 ≤ priorities[n] - Negative Priorities
		minimize the value of your priority, so that the value of maximum priority is reduced
	"""
	print("Priority List", P_list)
	P_sorted = sorted(P_list)
	P_dict = {}
	p_count = 0
	n_count = 0
	inc = +1
	for i in range(len(P_sorted)):
		if P_sorted[i] <= 99:
			if P_sorted[i] not in P_dict:
				p_count += 1
				P_dict[P_sorted[i]] = p_count
		else:
			if i == 0:
				n_count = 0
				inc = -1
			if n_count == 0 and inc == +1 :
				n_count = -len(P_list[i:])-1
			if P_sorted[i] not in P_dict:
				n_count = n_count + inc
				P_dict[P_sorted[i]] = n_count
	for i in range(len(P_list)):
		P_list[i] = P_dict[P_list[i]]
	print("Minimized priority List", P_list)


# P_list = [825, 221, 489, 300, 221, 113]
# P_list = [1, 201, 4, 8, 4, 105]
P_list = list(map(int, input("enter priority list").split(" ")))
changePriority(P_list)