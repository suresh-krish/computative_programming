"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    i = (low + high) // 2
    l = len(input_array) - 1
    j = 0
    while True:
        if value == input_array[i]:
            return i
        elif value > input_array[i]:
            low = i
            i = (low + high) // 2

        elif value < input_array[i]:
            high = i
            i = (low + high) // 2
        if low == high - 1:
            break

    return -1
        
            
