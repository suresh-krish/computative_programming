# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	a = (x1-x2)**2 +(y1-y2)**2
	a = math.sqrt(a)
	b = (x1-x3)**2 + (y1-y3)**2
	b = math.sqrt(b)
	c = (x2-x3)**2 + (y2-y3)**2
	c = math.sqrt(c)
	s = (a + b + c) / 2
	area = s*(s-a)*(s-b)*(s-c)
	area = math.sqrt(area)
	return area
