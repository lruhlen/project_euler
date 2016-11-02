## Problem 2
fib_prev=1
fib_current=2
max_val = 4e6
even_fibs_sum = 0

while fib_current <= max_val:
    if fib_current % 2 == 0:
        even_fibs_sum += fib_current
    fib_next = fib_prev + fib_current
    fib_prev = fib_current
    fib_current = fib_next
    
print even_fibs_sum