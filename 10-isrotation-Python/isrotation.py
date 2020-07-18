# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	x,y = str(x),str(y)
	if len(x) == len(y):
		res = x
		for i in range(0,len(x) + 1):
			res = x[i:] + x[0:i]
			if res == y:
				return True
			elif x[::-1] == y:
				return True
	return False