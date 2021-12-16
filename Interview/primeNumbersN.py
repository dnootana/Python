#!/usr/bin/env python3.8

"""
prime numbers below N
"""

def primes(N):
	"""
	create a list of N numbers 
	starting from p = 2 to p <= sqrt(N) 
	mark multiples of p from p*p to N+1

	"""
	primes = [True] * (N+1)
	primes[0], primes[1] = False, False
	p = 2
	while p * p <= N: # we stop when p*p > N as no number above p we have multiple under N
		if primes[p] is True:
			for i in range(p*p, N+1, p): # we start from p*p as previous multiples are already marked by earlier p
				primes[i] = False
		p += 1
	print([i for i in range(N+1) if primes[i]])

primes(15)