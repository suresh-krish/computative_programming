# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	a = (b2 - b1) 
	if a == 0:
		return None
	elif m1-m2 ==0 :
		return None
	else:
	    a1 = a/ (m1 - m2)
	b = (b1*m2 - b2*m1) / (m1 - m2)
	if a1 > 0 and b > 0:
		return a1
	return None