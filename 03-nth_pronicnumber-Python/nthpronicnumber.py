# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	x = 0
	y=1
	p = 0
	if n == 0:
		return 0

	while p!=n:
		x = x + 1
		y = y + 1
		res = x * y
		p = p + 1

	return res

	
