# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 12:57:55 2016
@author: lruhlen
"""

"""
PROBLEM 4:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import numpy as np
DEFAULT_LOWER_VAL = 100
DEFAULT_UPPER_VAL = 999

def is_number_palindrome(x):
    if str(abs(x)) == str(abs(x))[::-1]:
        print "FOUND A PALINDROME!"
        print x
        return True
    else:
        return False


def make_diag_elements(row_vals, col_vals):
    return "placeholder for now"


## Tests
def make_printable_matrix(min_val=0, max_val=0):
    vec = np.arange(min_val, max_val)
    matr = np.triu(np.outer(vec, vec.T))
    return matr

min_val = 8
max_val = 20
print make_printable_matrix(min_val=min_val, max_val=max_val)
