# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	p = 1
	x = 0
	if n == 1:
		return 0

	while p!=n:
		x = x + 1
		res = x * x
		y = str(x)
		res = str(res)
		a = len(y)
		b = len(res)
		c = b - a
		if res[c:] == y:
			p = p + 1

	return x