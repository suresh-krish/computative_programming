# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(a):
	for i in range(2,a//2):
		if a % i == 0:
			return 0

	return a



def nthcircularprime(n):
	p = 1
	x = 3
	if n == 1 or n == 2:
		return n + 1

	while p != n:
		x = x + 1
		num = x
		l = isprime(num)
		if l != 0:
			s = str(l)
			s = s[::-1]

		q = isprime(int(s))
		if q != 0:
			p = p + 1

	return x

	