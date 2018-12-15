"""
# 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def same_rvs(integer):

    string = str(integer)
    m_list = list(string)
    m_list.reverse()
    to_string = ''

    for char in m_list:
        to_string += char

    test_me = int(to_string)

    return test_me == integer


def palindrome_max(digit_size=3):

    p_max = 0
    f_1 = 0
    f_2 = 0
    size = int('9' * digit_size) + 1
    temp = digit_size-1
    start = int('1' + '0' * temp)
    for x in range(start, size):
        for y in range(start, size):
            i = x * y
            if same_rvs(i):
                if p_max <= i:
                    p_max = i
                    f_1 = x
                    f_2 = y
    print(p_max, '=', f_1, 'x', f_2)






# Test
palindrome_max(2)
"""
>>> foo(2)
9009
"""
