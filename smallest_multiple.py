""" 
# 5
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20?
"""
import fractions

def smallest_multiple(n):
	smallest_num = 1
	for i in range(1, n + 1):
		smallest_num = (smallest_num * i)/ fractions.gcd(smallest_num,i)
	print(smallest_num)

# Tests
smallest_multiple(20)
"""
>>> foo(10)
2520
"""
