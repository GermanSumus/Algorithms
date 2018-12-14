'''
# 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
from random import random as rdm
'''

def mutiples_of(integer):
    divisibles = []
    for _ in range(1, integer):
        if not _ % 3:
            divisibles.append(_)
        elif not _ % 5:
            divisibles.append(_)
    print(sum(divisibles))


# Tests

mutiples_of(10)
'''
# [3, 5, 6, 9] =
>>> 23
'''
mutiples_of(100)
