#!/usr/bin/env python3.8

"""
decorators examples

A decorator in Python is a function that takes another function as its argument, and returns yet another function . Decorators can be extremely useful as they allow the extension of 
an existing function, without any modification to the original function source code
"""


""" example 1 """
def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print("wrapper_function executed this before {}".format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

""" without decorator """
def display():
	print("display function ran")

display = decorator_function(display)
display()

""" using decorator """
@decorator_function
def display():
	print("display function ran")

display()

@decorator_function
def display_info(name, age):
	print("display_info ran with arguments {} and {}".format(name, age))

display_info("Nootana", 26)
""" example 2 """
print("\nclass decorator\n")
class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print("call method executed this before {}".format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)

@decorator_class
def display_info(name, age):
	print("display_info ran with arguments {} and {}".format(name, age))

display_info("Nootana", 26)

""" example 3 """
print("\nexample 3\n")
def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)

	return wrapper

@my_logger
def display_info(name, age):
	print("display_info ran with arguments {} and {}".format(name, age))

display_info("Manu", 26)

""" example 4 """
print("\nexample 4\n")
import time
def my_timer(orig_func):

	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in: {} sec'.format(orig_func.__name__, t2))
		return result

	return wrapper

@my_timer
def display_info(name, age):
	time.sleep(1)
	print("display_info ran with arguments {} and {}".format(name, age))

display_info("Manu", 26)


""" example 5 """

print("\nexample 5\n")
from functools import wraps
def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)

	return wrapper

import time
def my_timer(orig_func):

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in: {} sec'.format(orig_func.__name__, t2))
		return result

	return wrapper


@my_timer
@my_logger
def display_info(name, age):
	time.sleep(1)
	print("display_info ran with arguments {} and {}".format(name, age))

display_info("shourya", 26)

""" example 6 -----decorator to accept arguments"""
print("\nexample 6\n")
def prefix_decorator(prefix):
	def decorator_function(original_function):
		def wrapper_function(*args, **kwargs):
			print(prefix, "wrapper_function executed this before {}".format(original_function.__name__))
			result = original_function(*args, **kwargs)
			print(prefix, "wrapper_function executed this after {}".format(original_function.__name__))
			return result
		return wrapper_function
	return decorator_function

@prefix_decorator('TESTING:')
def display_info(name, age):
	print("display_info ran with arguments {} and {}".format(name, age))

display_info("Nootana", 26)