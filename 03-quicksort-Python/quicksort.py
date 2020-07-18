"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(arr,low,high): 
	i = ( low-1 )
	pivot = arr[high]

	for j in range(low , high): 


		if arr[j] <= pivot: 
		
	
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 


def quickSorting(arr,low,high): 
	if low < high: 
		pi = partition(arr,low,high)
		quickSorting(arr, low, pi-1) 
		quickSorting(arr, pi+1, high) 



def quicksort(array):
	low = 0
	high = len(array) - 1
	# pivot = high
	quickSorting(array,low,high)

	return array



