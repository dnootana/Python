#!/var/bin/env python3.8


"""
You've been given a list of historical stock prices for a single day for Amazon stock. The index of the list represents the timestamp, 
so the element at index of 0 is the initial price of the stock, the element at index 1 is the next recorded price of the stock for that day, etc. 
Your task is to write a function that will return the maximum profit possible from the purchase and sale of a single share of Amazon stock on that day. 
Keep in mind to try to make this as efficient as possible.

For example, if you were given the list of stock prices:

prices = [12,11,15,3,10]

Then your function would return the maximum possible profit, which would be 7 (buying at 3 and selling at 10).

"""
def maxprofit(P):
	"""
	Brute Force solution
	time complexity : O(n2)
	"""
	min_s = 0
	max_s = 0
	for i in range(len(P)):
		min_i = P[i]
		max_i = 0
		for j in range(i+1,len(P)):
			if P[j] >= min_i:
				max_i = P[j]
			if max_i-min_i > max_s-min_s:
				min_s = min_i
				max_s = max_i
	print(min_s, max_s, "-", max_s-min_s)

def maxprofit1(P):
	"""
	time complexity : O(n)
	"""
	if len(P) < 2:
		raise Exception("Need at least 2 stock prices")
	min_s = P[0]
	max_p = P[1] - P[0]

	for price in P[1:]:
		comp_profit = price - min_s
		max_p = max(max_p, comp_profit)
		min_s = min(min_s, price)
		print(min_s, price, max_p)
	print(max_p)


prices = [12,11,15,3,10]
prices = [10,12,14,12,13,11,8,7,6,13,23,45,11,10]
prices = [4, 14, 3, 7]
# prices = [30,22,21,5]
# maxprofit(prices)
maxprofit1(prices)