# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
	if bound1 > bound2:
		a = bound2
		b = bound1
	else :
		b = bound2
		a = bound1

	if x >= a and x <= b:
		return x
	elif x < a:
		return a
	else :
		return b
