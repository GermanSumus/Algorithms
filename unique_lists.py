"""
Write a function that takes two or more arrays and returns a new array of
unique values in the order of the original provided arrays.

In other words, all values present from all arrays should be included in their
original order, but with no duplicates in the final array.

The unique numbers should be sorted by their original order, but the final
array should not be sorted in numerical order.
"""

def unique_list(a_list, b_list):
    for num in a_list:
        if num in b_list:
            b_list.remove(num)
            
    concat = a_list + b_list
    print(concat)

unique_list([1,2,3], [1,2,3,4,5])
unique_list([1,1,7,5], [3,9,4,5])




