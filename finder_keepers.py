"""
Given a test as a second argument return the first item from a list
, first argument, that passes it.
"""
def test(n):
	if n > 0:
		return True


def pass_test(list, func):
	for item in list:
		if func(item):
			print(item)
l = [0, -1, 1]

pass_test(l,test)
# Tests
"""
>>> foo(list, test())
True 6
"""