## Problem 1
max_val = 1000
total = 0

for num in xrange(max_val):
    if ((num%3) == 0 ) or ((num%5) == 0):
        total += num
    
print total