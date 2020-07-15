# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.
import math
def largestperfectsquare(n):
	# your code goes here
	a=n
	flag = 0
	for i in range(int(math.sqrt(a) + 1),0,-1):
		res = i*i
		if flag == 1:
			break
		else:
			if res < n:
				if int(round(res)) == res:
					flag = 1
					return res
				
			