# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math




def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = (x1-x2)**2 + (y1-y2)**2
	b = (x1 - x3) ** 2 + (y1 - y2)**2
	c = (x2 - x3)**2 + (y2-y3)**2
	
	if a > b:
		if c > a:
			if c >= a + b:
				return True
			return False
		else :
			if a >= c + b:
				return True
			return False
	else :
		if c > b:
			if c >= a + b:
				return True
			return False
		else :
			if b >= c + a:
				return True
			return False

		
	
