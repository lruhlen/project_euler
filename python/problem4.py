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
        return True
    else:
        return False

def make_initial_matrix(min_val=DEFAULT_LOWER_VAL, max_val=DEFAULT_UPPER_VAL):
    vec = np.arange(min_val, max_val+1)
    mat = np.triu(np.outer(vec, vec.T))
    return vec, mat

def get_diag_elements(mat, k=0):
    return np.diagonal(mat, k)


def get_palindrome_indices(vec):
    tmp= map(is_number_palindrome, vec)
    if any(tmp):
        return np.max(np.where(map(is_number_palindrome, vec)))
    return np.array([])



def truncate_matrix(vec, mat, new_min_val=0):
    vec = np.delete(vec, range(new_min_val), 0)
    mat = np.delete(np.delete(mat, range(new_min_val), 0),
                    range(new_min_val), 1)
    return vec, mat


def main(min_val=DEFAULT_LOWER_VAL, max_val=DEFAULT_UPPER_VAL):
    largest_palin = 0
    k = 0
    vec, mat = make_initial_matrix(min_val=min_val, max_val=max_val)
    max_k = len(vec)
    print mat
    counter = 0

    while k <= max_k and counter < 10:
#        print "\n\n LOOP NUMBER ", counter
        counter += 1
#        print "vec length = ", len(vec)
        x = get_diag_elements(mat, k)
#        print "diagonal elements = ", x
        if not x.size:
            break

        new_min = get_palindrome_indices(x)

#       print "new_min = ", new_min, new_min.size
#        print "max_k = ", max_k

        if (new_min.size > 0) and new_min < max_k:
            largest_palin = x[new_min]
            vec, mat = truncate_matrix(vec, mat, new_min)
            max_k = len(vec)
            k += 1
        else:
            break

    if largest_palin == 0:
        return "No palindromes found"
    else:
        return vec[0], largest_palin/vec[0], largest_palin






## Tests
print main(min_val=9, max_val=20)
#def make_printable_matrix(min_val=0, max_val=0):
#    vec = np.arange(min_val, max_val)
#    matr = np.triu(np.outer(vec, vec.T))
#    return matr
#
#min_val = 8
#max_val = 20
#print make_printable_matrix(min_val=min_val, max_val=max_val)
#
#idx, test_matrix = make_initial_matrix(min_val=8, max_val=20)