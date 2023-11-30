#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        return add(add(a, b), add(4, 5))
    else:
        return sub(a, b)
