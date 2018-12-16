"""
return the sum of all numbers in a given range. foo(1, 4) will add all
the numbers beteen 1 and 4.(1,2,3,4 = 10). The smallest numbers will
not always be first. foo(4,1) should return the same.
"""
def sum_between(a, b):
	if b < a:
		small = b
		big = a
	else:
		small = a
		big = b

	sum = 0
	for i in range(small, big + 1):
		sum += i

	print(sum)

# Tests
sum_between(1,4)
sum_between(4,1)