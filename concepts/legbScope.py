#!/usr/bin/python3.8
#LEBG- Local, Enclosing, Global, Built-in
x = "Global x"

def outer():
#    global x
    x = "Local x"
    def inner():
        nonlocal x   #cant use global variables as nonlocal in nested function
        x = "Nonlocal x"
        print(x)
    print(x)
    inner()
    print(x)
    
print(x)
outer()
print(x)