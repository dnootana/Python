#!/usr/bin/python3.8
N = input('Enter numbers : ')
S = input('Enter search number : ')
A = N.split()
i= 'NIL'
for j in range(len(A)):
	if S==A[j]:
		i=j
		break
print('Position is '+i, ' in ',A)