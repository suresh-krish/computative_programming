"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def sortin(array,low,high):
	i = -1
	j = high
	while low < j:
		if array[low] < array[j]:
			i = i + 1
			b = array[low]
			array[low] = array[i]
			array[i] = b
			low = low + 1
		else:
			low = low + 1

	b = array[low]
	array[low] = array[j]
	array[j] = b
	return array,low + 1,high




def quicksort(array):
	low = 0
	high = len(array) - 1
	# pivot = high
	while low < high:
	    array,low,high = sortin(array,low,high)

	return array



