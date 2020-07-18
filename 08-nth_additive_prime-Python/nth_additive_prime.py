# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
import math

def is_prime(p):
	flag = 0
	for i in range(2,p):
		if p%i == 0:
			flag = 1
	return flag


def fun_nth_additive_prime(n):
	a = 0
	p = 3
	if n == 0:
		return 2

	while a < n:
		k = is_prime(p)
		if k == 0:
			ch = str(p)
			sum = 0
			for j in ch:
				sum = sum + int(j)
			d = is_prime(sum)
			if d == 0:
				a = a + 1
			p = p + 1
		else:
			p = p + 1
	return p - 1
