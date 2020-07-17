# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	if len(a) == 0:
		return None
	elif len(a)%2 != 0:
		l = len(a)//2
		return a[l]
	else:
		l = len(a)//2
		return (a[l-1] + a[l]) / 2