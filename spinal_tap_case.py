"""
Return a Spinal-Tap-Case string in all lowercase. this-is-a-spinal-tap
"""

import re

s = 'This_Is-A SpinalTap'

def spinal_tap(string):
    for letter in string:
        if letter.isupper():
            print(letter)

spinal_tap(s)
