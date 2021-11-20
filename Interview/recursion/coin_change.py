#!/usr/bin/env python3.8

"""
Given a target amount n and a list (array) of distinct coin values, 
what's the fewest coins needed to make the change amount.

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1

5 + 1+1+1+1+1

5+5

10

With 1 coin being the minimum amount.
"""
from memoize import memoize

# list_c = []
# def rec_coin(N, C): # not true for all cases
# 	if N == 0 :
# 		return
# 	while len(C):
# 		Cmax = max(C)
# 		if N >= Cmax:
# 			list_c.append(Cmax)
# 			rec_coin(N-Cmax, C)
# 			break
# 		else:
# 			C.remove(Cmax)

def rec_coin1(N, C):
	min_coins = N
	if N in coins:
		return 1
	else:
		for value in [c for c in coins if c<=N]:
			num_coins = rec_coin1(N-value, coins) + 1
			min_coins = min(num_coins, min_coins)
	return min_coins


# def min_coin(change, lst):
#     if change <= 0 : return(0)
#     while change < max(lst):
#         lst.pop()
#     coins = change // max(lst)
#     change %= max(lst)
#     lst.pop()
#     return coins + min_coin(change,lst)


Amount = 5
coins = [1,5,10,25,50,100]
min_coins = rec_coin1(Amount, coins)
print(min_coins,"coins are required to make",Amount,"using ",list_c)

