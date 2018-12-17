"""
Given an unknown amount of variables find all the variables that are
in the first variable (a list) and delete them. return the new list
"""
from random import randrange

def destroy(search, *args):
    print(f'\nSearch in here {search}\n\nDestroy these: {args}\n')
    for target in args:
        if target in search:
            search = [x for x in search if x != target]
    print('Results after' ,search)

# Tests
search = [randrange(1, 10) for x in range(10)]
destroy(search, 1,4,6,7,8,3)
"""
# Each one will be random but Results will always be right

Search in here [2, 9, 5, 4, 2, 1, 6, 2, 1, 2]

Destroy these: (1, 4, 6, 7, 8, 3)

Results after [2, 9, 5, 2, 2, 2]
"""
