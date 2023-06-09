#!/usr/bin/python3

from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    """Perform a magic calculation."""
    if a < b:
        c = a
        for i in range(4, 6):
            c = add(c, i)
        return add(c, b)
    else:
        return sub(a, b)
