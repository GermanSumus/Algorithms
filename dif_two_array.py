"""
Return the diffrence between two arrays. foo([1,2], [2,3]) returns 
[1,3].
"""
def diff_arrays(a, b):
	temp = []
	for item in a:
		if item not in b:
			temp.append(item)

	for item in b:
		if item not in a:
			temp.append(item)
	print(temp)	

# Tests

a = [1,2]
b = [2,3]

diff_arrays(a,b)