#!/usr/bin/env python3.8

def add(x, y):
	""" add function """
	return x + y

def subtract(x, y):
	""" subtract function """
	return x - y

def multiply(x, y):
	""" multiply function """
	return x * y

def divide(x, y):
	""" divide function """
	if y == 0:
		raise ValueError("can't divide by zero!")
	return x / y