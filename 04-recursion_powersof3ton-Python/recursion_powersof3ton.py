# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 


def recursive(a,b,c):
	if b > a:
		return c
	if (11623452267%b == 0):
		l.append(num)
	return recursive(a,b+1,c)

def recursion_powersof3ton(n):
	if n < 1:
		return None
	elif n == 1:
		return [1]
	else:
		return recursive(n,1,[])
