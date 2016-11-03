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
        print x
        return True
    else:
        return False


def diag_vals(lower_val=DEFAULT_LOWER_VAL,
              upper_val=DEFAULT_UPPER_VAL,
              row_shift=0,
              col_shift=0):
    x = upper_val - col_shift
    y = upper_val - row_shift
    while (x >= lower_val) and (x >= lower_val):
        yield x, y, x*y
        x -= 1
        y -= 1

def find_largest_diag_palindrome(lower_val=DEFAULT_LOWER_VAL,
                                 upper_val=DEFAULT_UPPER_VAL,
                                 row_shift=0,
                                 col_shift=0):
    diag_val_gen = diag_vals(lower_val=lower_val,
                             upper_val=upper_val,
                             row_shift=row_shift,
                             col_shift=col_shift)
    x = next(diag_val_gen)

    while (not(is_number_palindrome(x[-1]))
        and x[1] <= upper_val
        and x[0] >= lower_val):
        x = next(diag_val_gen)

    print "FOUND A PALINDROME! ", x
    return x


def search_for_palindromes(lower_val=DEFAULT_LOWER_VAL,
                           upper_val=DEFAULT_UPPER_VAL):
    row_shift = 0
    col_shift = 0


    while lower_val < upper_val:
        try:
            N = find_largest_diag_palindrome(lower_val=lower_val,
                                             upper_val=upper_val,
                                             row_shift=row_shift,
                                             col_shift=col_shift)
            lower_val += 1
        except StopIteration:
            print "Nothing on this diagonal..."

        row_shift -= 1
        lower_val = N[1]
        print N

    return N


## Tests
print search_for_palindromes(lower_val=14, upper_val=24)

print search_for_palindromes(lower_val=10, upper_val=99)

