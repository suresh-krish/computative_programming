# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	hi = a[0]
	sm = a[0]
	if len(a) == 0:
		return -1
	else:
		for i in range(0,len(a)):
			if hi < a[i]:
				hi = a[i]
			elif sm > a[i]:
				sm = a[i]
		return hi - sm
