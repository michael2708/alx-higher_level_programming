#!/usr/bin/python3
'''
0-add_integer.py has two argumenst a and b'
which must be integers or floats,
otherwise raise a TypeError.
otherwise returns sum of a and b as integers 
'''

def add_integer(a, b=98):
    '''
    Returns the addition of a and b as integers
    '''
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
