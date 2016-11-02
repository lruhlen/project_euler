# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 23:15:38 2016

@author: lruhlen

Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# Code
import numpy as np
def get_next_prime():
    list_of_primes = [2]

    while True:
        current_max_prime = max(list_of_primes)
        yield current_max_prime
        
        candidate = current_max_prime + 1
        while 0 in [candidate%n for n in list_of_primes]:
            candidate +=1
        list_of_primes.append(candidate)
        

def get_prime_factor_ceiling(n):
    return int(np.sqrt(n))
    
    
def factor(n):
    print "Factoring: ", n
    ceiling = get_prime_factor_ceiling(n)
    print "factor ceiling =", ceiling
    prime_faucet = get_next_prime()
    this_factor = next(prime_faucet)
    max_factor = this_factor
    
    while this_factor <= ceiling:
        if n % this_factor == 0:
            print "current max_factor =", this_factor
            max_factor = factor(n/this_factor)
        else:
            this_factor = next(prime_faucet)
            
    return max_factor
    


# Tests
#prime_faucet = get_next_prime()
#for x in xrange(10):
#    print next(prime_faucet)


assert get_prime_factor_ceiling(26) == 5, "get_prime_factor_ceiling \
returned incorrect answer"

print factor(13195)
assert factor(13195)== 29, "factor(13195) failed to return 29"

#print factor(600851475143)