"""
Return a given string in title case.
"""
def title_case(string):
	words = string.split(' ')
	str = ''
	for word in words:
		new_word = word[0].upper() + word[1:]
		str += (new_word + ' ')

	print(str)



# Test
title_case('I\'m a sentence')