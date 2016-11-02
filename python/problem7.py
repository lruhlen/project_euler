## Problem 7
def find_next_prime(primes_list):
    number = primes_list[-1] + 1
    while not is_number_prime(number, primes_list):
        number += 1
    
    return number
    

def is_number_prime(number, primes_list):
    if 0 in [number%prime for prime in primes_list]:
        return False
    else:
        return True

primes_list = [2]
stop_num = 10001

while len(primes_list) < stop_num:
    next_prime = find_next_prime(primes_list)
    primes_list.append(next_prime)
    

primes_list[-10:]