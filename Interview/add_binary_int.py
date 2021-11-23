#!/usr/bin/python3.8
A = input('Enter binary number 1 : ')
B = input('Enter binary number 2 : ')
m = max(len(A),len(B))
#A = A.rjust(m,'0') 
A = A.zfill(m)
#B = B.rjust(m,'0') 
B = B.zfill(m)
C = ''
carry = 0
for i in range(m-1,-1,-1):
	s = int(A[i])+int(B[i])+int(carry)
	C = str(s % 2) + C
	carry = s//2
C = str(carry)+C
print(C)