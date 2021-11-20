#!/usr/bin/env python3.8

from numpy import random

a = random.randint(100)
print(a)

a = random.rand()
print(a)

a = random.randint(100, size=(5))
print(a)


a = random.randint(100, size=(3, 5))
print(a)

a = random.rand(5)
print(a)

a = random.rand(5,3)
print(a)

a = random.choice([1,2,3,4,5])
print(a)

a = random.choice(["dfasdf", "dsfas", "sdfsdf", "asdfasd"])
print(a)

a = random.choice([1,2,3,4,5], size=(2,2))
print(a)