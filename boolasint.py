#! /usr/bin/env python3
"""True and False can be used as integer values
True -> 1
False -> 0
"""
a = input("Enter your number here") 
print(isinstance(a, int) + (a <= 10))
print(["is odd", "is even"][a % 2 == 0])
