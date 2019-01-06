"""
Find the missing letter in the passed letter range and return it.

If all letters are present in the range, return undefined.
"""

def missing_letter(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = list(string)
    s.sort()
    s = ''.join(s)
    x = alpha.find(s[0])
    while alpha[x] in s:
        x += 1
    print(f'{string} is missing the letter "{alpha[x]}"')


missing_letter('badcfehgj')

