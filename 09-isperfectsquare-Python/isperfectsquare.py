# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math

def isperfectsquare(n):
	# your code goes here
	try:
		n = int(n)
		if n > 0:
			a = math.sqrt(n)
			if type(a) != float:
				return True
			else :
			    return False
		else:
		    return False

	except :
		return False
	
